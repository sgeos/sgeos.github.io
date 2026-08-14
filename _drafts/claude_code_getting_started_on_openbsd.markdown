---
layout: post
mathjax: false
comments: true
title: "Getting Started with Claude Code on OpenBSD"
date: 2026-08-14 00:01:00 +0000
categories: ai ai-tools openbsd development
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

[Claude Code][claude_setup] is Anthropic's agentic command line tool
for software development.
It runs in the terminal, navigates repositories,
generates and modifies code, executes builds and tests,
and manages git workflows through natural language commands.
Companion posts cover
[installation and usage on macOS][related_post_claude_code]
and [installation on FreeBSD][related_post_claude_code_freebsd].

OpenBSD is not an officially supported platform for Claude Code.
Anthropic's native installer targets macOS, Linux, and Windows.
Unlike FreeBSD, no community-maintained port or package exists for OpenBSD.
The only viable installation path is npm,
which Anthropic has deprecated in favor of native installers.

OpenBSD is by design hostile to software
that assumes a Linux environment.
The Linux binary compatibility layer
was [removed from OpenBSD in version 6.0][openbsd_linux_compat]
as a security improvement.
Claude Code is built on the [Bun runtime][bun_openbsd_issue],
which does not support any BSD variant.
The native installer will download an incompatible Linux binary
and must not be used on OpenBSD.

This post covers three topics.
First, it documents installation via npm
and the manual configuration required for OpenBSD compatibility.
Second, it addresses the ripgrep and bash requirements
that prevent Claude Code from functioning out of the box.
Third, it demonstrates Claude Code's agentic capabilities
with a post-installation exercise
that uses only the OpenBSD base system.

General Claude Code usage, features, and workflows
are covered in the [companion post][related_post_claude_code]
and the [official documentation][claude_docs].

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"

# OS and Version
$ uname -vm

# Claude Code
$ claude --version

# Node.js and npm
$ node --version
$ npm --version

# Ripgrep
$ rg --version

# Bash
$ bash --version | head -n 1

# Git
$ git --version
```

## Instructions

The npm installation method is the only viable path on OpenBSD.
No port or package exists.
The native installer and the `claude install` command
must not be used.
They download an incompatible Linux binary
and will [break an existing npm installation][github_24711].

### Prerequisites

Install the required packages.
OpenBSD uses `pkg_add` for package management
and `doas` for privilege elevation.

```sh
$ doas pkg_add node
$ doas pkg_add ripgrep
$ doas pkg_add bash
$ doas pkg_add git
```

Claude Code requires Node.js version 18 through 24.
Node.js version 25 and later removed the SlowBuffer API
that Claude Code depends on,
and will cause runtime errors.

OpenBSD defaults to ksh as its login shell.
Claude Code [requires bash][github_19264]
and will not function with POSIX-only shells.
A request to support ksh and other POSIX shells was closed upstream.

### Installation

Install Claude Code globally with npm.

```sh
$ npm install -g @anthropic-ai/claude-code
```

Do not use `doas` with `npm install`.
If npm's global prefix requires elevated permissions,
configure a user-writable prefix instead.

```sh
$ npm config set prefix ~/.npm-global
$ export PATH="${HOME}/.npm-global/bin:${PATH}"
```

Add the `PATH` export to your shell profile to make it permanent.
For ksh, add it to `~/.profile`.
For bash, add it to `~/.bash_profile` or `~/.bashrc`.

The npm installation path is deprecated by Anthropic
and may be removed in a future release.
It is the only option on OpenBSD
because the native installer does not support the platform.

> **Warning.**
> Do not run `claude install`
> or `curl -fsSL https://claude.ai/install.sh | bash`
> on OpenBSD.
> The installer does not detect OpenBSD
> and will download an incompatible Linux ELF binary.
> This [overwrites the working npm installation][github_24711]
> and renders Claude Code unusable
> until the npm package is reinstalled.

### Bash Configuration

OpenBSD installs bash at `/usr/local/bin/bash`
rather than `/bin/bash`.
Claude Code wrapper scripts use a `#!/bin/bash` shebang
that does not resolve on OpenBSD.

Create a symlink to make bash available at the expected path.

```sh
$ doas ln -s /usr/local/bin/bash /bin/bash
```

Verify that the symlink works.

```sh
$ /bin/bash --version | head -n 1
```

### Ripgrep Configuration

Claude Code bundles platform-specific ripgrep binaries
for macOS, Linux, and Windows.
No OpenBSD binary is included.
When Claude Code attempts to use the bundled ripgrep on OpenBSD,
the Grep tool fails silently and returns zero matches for all searches.
This issue is documented in [GitHub issue #19260][github_19260].

Configure Claude Code to use the system ripgrep
by adding the following to `~/.claude/settings.json`.

```json
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  }
}
```

Create the file and its parent directory if they do not exist.

```sh
$ mkdir -p ~/.claude
$ cat > ~/.claude/settings.json << 'EOF'
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  }
}
EOF
```

This setting directs Claude Code to use the system `rg` binary
from the ripgrep package instead of the missing bundled binary.
The [official troubleshooting guide][claude_troubleshooting]
documents this setting for platforms
where the bundled ripgrep does not function correctly.

An alternative workaround is to symlink the system ripgrep
into the vendor directory.

```sh
$ mkdir -p ~/.npm-global/lib/node_modules/@anthropic-ai/claude-code/vendor/ripgrep/x64-openbsd
$ ln -s /usr/local/bin/rg ~/.npm-global/lib/node_modules/@anthropic-ai/claude-code/vendor/ripgrep/x64-openbsd/rg
```

This symlink will break on every Claude Code update.
The `USE_BUILTIN_RIPGREP` setting is the preferred approach.

### Verification

Confirm that Claude Code launches and that the Grep tool functions correctly.

```sh
$ claude --version
```

Run Claude Code and complete the login process if this is the first launch.

```sh
$ claude
```

After authentication, test the Grep tool
by asking Claude Code to search for a known pattern in a test file.

```sh
$ echo "hello world" > /tmp/test_grep.txt
$ claude -p "Use the Grep tool to search for 'hello' in /tmp/test_grep.txt"
```

If the Grep tool returns zero matches despite the pattern being present,
the ripgrep configuration is not working correctly.
Revisit the Ripgrep Configuration section above.

## Hello World

With Claude Code installed and verified,
the following exercise demonstrates
its agentic capabilities on OpenBSD.
The goal is to issue a single prompt
that triggers web research, code generation,
compilation, and execution
using only the OpenBSD base system.
No additional packages are required.

OpenBSD ships with `cc`, BSD `make`, and `libcurses`
in the base system.
These are sufficient for building curses-based C programs
without installing anything beyond Claude Code itself.

Create an empty project directory and launch Claude Code.

```sh
$ mkdir ~/sysinfo && cd ~/sysinfo
$ claude
```

Paste the following prompt.

````
Research OpenBSD sysctl MIBs for hostname, CPU model, physical memory
size, load averages, and system uptime. Write a curses-based C program
that displays this information in a formatted dashboard layout. Use
only OpenBSD base system headers and libraries. Compile with cc and
link against -lcurses. Include a BSD Makefile. Build and run the
program to verify it compiles.
````

Claude Code will research OpenBSD sysctl interfaces and curses APIs,
generate source files, compile the program,
and iterate on any errors until the build succeeds.
The exact output will vary by session.
Expect at minimum a `main.c` file and a `Makefile`.

After Claude Code finishes,
the program can be built and run manually.

```sh
$ make
$ ./sysinfo
```

The result should be a terminal dashboard
displaying system information retrieved through OpenBSD sysctl calls.
Press `q` or `Ctrl+C` to exit the program.

This exercise verifies three agentic capabilities in a single prompt.
Claude Code performs web research to identify the correct sysctl MIBs,
generates C source code and a build file,
and uses the Bash tool to compile and test the result.

## Limitations

OpenBSD is not an officially supported platform for Claude Code.
The following limitations apply.
These are more extensive than those on
[FreeBSD][related_post_claude_code_freebsd]
due to the absence of a dedicated port.

No port or package exists for Claude Code on OpenBSD.
The npm installation path is the only option
and is deprecated upstream.
Anthropic may remove npm installation support in a future release,
which would leave OpenBSD without a viable installation method.

The Bun runtime does not support OpenBSD.
The native installer and the `claude install` command
must not be used.
Running `claude install` on OpenBSD
[downloads an incompatible Linux binary][github_24711]
and breaks the existing npm installation.
This is documented in [GitHub issue #24711][github_24711].

OpenBSD [removed its Linux binary compatibility layer][openbsd_linux_compat]
in version 6.0.
Linux binaries cannot be executed on modern OpenBSD,
which rules out any approach based on running Linux builds
of Claude Code or its dependencies.

Claude Code's sandboxing features
rely on Linux-specific kernel mechanisms such as namespaces.
These features will not function on OpenBSD.
Claude Code does not use OpenBSD's native
pledge or unveil security mechanisms.

Claude Code [requires bash][github_19264]
and will not function with ksh or other POSIX shells.
OpenBSD defaults to ksh,
so bash must be installed separately as a package.

Workarounds may break on Claude Code updates.
The `USE_BUILTIN_RIPGREP` setting is more durable than the symlink approach,
but neither is guaranteed to survive major version changes.

## Conclusion

Claude Code can be made functional on OpenBSD
through npm installation with system ripgrep and bash.
The setup requires manual configuration of the `USE_BUILTIN_RIPGREP` setting,
a bash symlink, and awareness of the critical warning
against running the native installer.

The setup is more fragile than on FreeBSD,
where a [community-maintained port][related_post_claude_code_freebsd]
handles these workarounds automatically.
On OpenBSD, every Claude Code update
requires verifying that the configuration remains intact.

The GitHub issues referenced below
are useful resources for tracking the current state of OpenBSD support.
The [Bun OpenBSD support request][bun_openbsd_issue]
is the upstream dependency
that would need to be resolved
for native installer support on OpenBSD.

## Future Reading

The [official Claude Code documentation][claude_docs]
covers features, workflows, and configuration in detail.
The [companion post][related_post_claude_code]
covers installation on macOS, basic usage controls,
the `CLAUDE.md` configuration file,
and a practical code generation example.
The [FreeBSD companion][related_post_claude_code_freebsd]
covers installation via ports and packages on FreeBSD.

The following GitHub issues track OpenBSD support.
Subscribing to these issues provides notification
of upstream changes that may affect OpenBSD installations.

- [Issue #19260][github_19260] tracks the bundled ripgrep binary issue on OpenBSD.
- [Issue #20202][github_20202] tracks maintaining npm installation for unsupported platforms.
- [Issue #24711][github_24711] documents the native installer breaking npm installations on OpenBSD.

## References

- [Claude, Official Documentation][claude_docs]
- [Claude, npm Package][claude_npm]
- [Claude, Setup Guide][claude_setup]
- [Claude, Troubleshooting: Search and Discovery Issues][claude_troubleshooting]
- [GitHub, Bun OpenBSD Support Request #4678][bun_openbsd_issue]
- [GitHub, Claude Install Breaks npm Installation on OpenBSD #24711][github_24711]
- [GitHub, Maintain npm Installation for OpenBSD #20202][github_20202]
- [GitHub, POSIX Shell Support Request #19264][github_19264]
- [GitHub, Ripgrep Fails on OpenBSD #19260][github_19260]
- [OpenBSD, Linux Compatibility Removal][openbsd_linux_compat]
- [Related Post, Getting Started with Claude Code][related_post_claude_code]
- [Related Post, Getting Started with Claude Code on FreeBSD][related_post_claude_code_freebsd]

[bun_openbsd_issue]: https://github.com/oven-sh/bun/issues/4678
[claude_docs]: https://code.claude.com/docs/en/home
[claude_npm]: https://www.npmjs.com/package/@anthropic-ai/claude-code
[claude_setup]: https://code.claude.com/docs/en/setup
[claude_troubleshooting]: https://code.claude.com/docs/en/troubleshooting
[github_19260]: https://github.com/anthropics/claude-code/issues/19260
[github_19264]: https://github.com/anthropics/claude-code/issues/19264
[github_20202]: https://github.com/anthropics/claude-code/issues/20202
[github_24711]: https://github.com/anthropics/claude-code/issues/24711
[openbsd_linux_compat]: https://www.infoworld.com/article/2246944/openbsd-60-tightens-security-by-losing-linux-compatibility.html
[related_post_claude_code]: {% post_url 2026-01-31-claude_code_getting_started %}
[related_post_claude_code_freebsd]: {% post_url 2026-08-13-claude_code_getting_started_on_freebsd %}
