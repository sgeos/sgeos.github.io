---
layout: post
mathjax: false
comments: true
title: "Getting Started with Claude Code on FreeBSD"
date: 2026-02-24 00:01:00 +0000
categories: ai ai-tools freebsd development
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

[Claude Code][claude_setup] is Anthropic's agentic command line tool
for software development.
It runs in the terminal, navigates repositories,
generates and modifies code, executes builds and tests,
and manages git workflows through natural language commands.
A companion post covers [installation and usage on macOS][related_post_claude_code].

FreeBSD is not an officially supported platform for Claude Code.
Anthropic's native installer targets macOS, Linux, and Windows.
A community-maintained FreeBSD port at [misc/claude-code][freebsd_freshports_claude_code]
provides a supported installation path through the ports tree and package system.
An alternative npm installation method provides access to the latest upstream version
at the cost of additional manual configuration.

This post covers three topics.
First, it documents installation via the FreeBSD ports tree, the package system, and npm.
Second, it addresses known compatibility issues
and the workarounds required for npm installations.
Third, it demonstrates Claude Code's agentic capabilities
with a post-installation exercise
that uses only the FreeBSD base system.

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

Three installation methods are available.
The FreeBSD port is the recommended approach
for users who prefer building from source.
The package system provides pre-built binaries from the same port.
The npm installation method provides access to the latest upstream version
but requires manual workarounds for FreeBSD compatibility.

### Installing from Ports

The [misc/claude-code][freebsd_freshports_claude_code] port
installs Claude Code with system ripgrep as a dependency,
addressing the bundled binary compatibility issue automatically.
The port uses npm during the build process
and installs the result as a system package.

Ensure the ports tree is available.
The [FreeBSD Handbook][freebsd_handbook_ports] covers ports tree setup
for users who have not yet configured it.

```sh
$ cd /usr/ports/misc/claude-code && sudo make install clean
```

The port depends on www/node24 and textproc/ripgrep at runtime.
Build dependencies include www/npm and textproc/jq.
These are installed automatically during the build.

The port version may lag behind the latest upstream release.
Check the [FreshPorts page][freebsd_freshports_claude_code]
for the current port version.

### Installing from Packages

The package system provides pre-built binaries from the same port.
This is faster than building from source
but the version may lag further behind on the quarterly package branch.

```sh
$ sudo pkg install claude-code
```

This pulls in the same runtime dependencies as the port.

### npm Installation

The npm installation method provides access to the latest upstream version.
This path is deprecated by Anthropic
and may be removed in a future release.
It requires manual workarounds for FreeBSD compatibility
that the port handles automatically.

Install the prerequisites.

```sh
$ sudo pkg install node22 npm-node22 textproc/ripgrep shells/bash devel/git
```

These prerequisites may also be built from ports.
Claude Code requires Node.js version 18 through 24.
Node.js version 25 and later removed the SlowBuffer API
that Claude Code depends on,
and will cause runtime errors.

Install Claude Code globally with npm.

```sh
$ npm install -g @anthropic-ai/claude-code
```

Do not use `sudo` with `npm install`.
If npm's global prefix requires elevated permissions,
configure a user-writable prefix instead.

```sh
$ npm config set prefix ~/.npm-global
$ export PATH="${HOME}/.npm-global/bin:${PATH}"
```

Add the `PATH` export to your shell profile to make it permanent.

### Shebang Fix

FreeBSD installs bash at `/usr/local/bin/bash`
rather than `/bin/bash`.
Claude Code wrapper scripts may use a `#!/bin/bash` shebang
that does not resolve on FreeBSD.
This issue is documented in [GitHub issue #9117][github_9117].

The port installation may handle this automatically.
Verify by running `claude --version` after installation.
If the command fails with a "bad interpreter" error,
create a symlink.

```sh
$ sudo ln -s /usr/local/bin/bash /bin/bash
```

Alternatively, edit the wrapper script at `~/.claude/local/claude`
to use `#!/usr/bin/env bash` instead.

### Ripgrep Configuration

Claude Code bundles platform-specific ripgrep binaries
for macOS, Linux, and Windows.
No FreeBSD binary is included.
When Claude Code attempts to use the bundled ripgrep on FreeBSD,
the Grep tool fails silently and returns zero matches for all searches.
This issue is documented in [GitHub issues #13161][github_13161]
and [#21542][github_21542].

The port installation configures Claude Code
to use the system ripgrep automatically.
No additional configuration is required for port or package installations.

For npm installations,
configure Claude Code to use the system ripgrep
by adding the following to `~/.claude/settings.json`.

```json
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  }
}
```

Create the file if it does not exist.
This setting directs Claude Code to use the system `rg` binary
from textproc/ripgrep instead of the missing bundled binary.

An alternative workaround is to symlink the system ripgrep
into the vendor directory.

```sh
$ mkdir -p ~/.claude/local/node_modules/@anthropic-ai/claude-code/vendor/ripgrep/x64-freebsd
$ ln -s /usr/local/bin/rg ~/.claude/local/node_modules/@anthropic-ai/claude-code/vendor/ripgrep/x64-freebsd/rg
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
Create a small test file and ask Claude Code to find a string in it.

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
its agentic capabilities on FreeBSD.
The goal is to issue a single prompt
that triggers web research, code generation,
compilation, and execution
using only the FreeBSD base system.
No additional ports or packages are required.

FreeBSD ships with `cc` from LLVM, BSD `make`, and `libncursesw`
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
Research FreeBSD sysctl MIBs for hostname, CPU model, physical memory
size, load averages, and system uptime. Write a curses-based C program
that displays this information in a formatted dashboard layout. Use
only FreeBSD base system headers and libraries. Compile with cc and
link against -lncurses. Include a BSD Makefile. Build and run the
program to verify it compiles.
````

Claude Code will research FreeBSD sysctl interfaces and curses APIs,
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
displaying system information retrieved through FreeBSD sysctl calls.
Press `q` or `Ctrl+C` to exit the program.

This exercise verifies three agentic capabilities in a single prompt.
Claude Code performs web research to identify the correct sysctl MIBs,
generates C source code and a build file,
and uses the Bash tool to compile and test the result.

## Limitations

FreeBSD is not an officially supported platform for Claude Code.
The following limitations apply.

The Anthropic native installer does not support FreeBSD.
This is documented in [GitHub issue #22564][github_22564].

The FreeBSD port version may lag behind the latest upstream release.
As of December 2025, the port carries version 2.0.58
while the latest npm release is newer.

The npm installation path is deprecated by Anthropic
and may be removed in a future release.

Running Claude Code in a FreeBSD Linux emulator jail does not work.
This is documented in [GitHub issue #22694][github_22694].

Workarounds for npm installations may break on Claude Code updates.
The `USE_BUILTIN_RIPGREP` setting is more durable than the symlink approach,
but neither is guaranteed to survive major version changes.

Earlier versions of Claude Code exhibited bash command hanging on FreeBSD.
This was documented in [GitHub issue #10673][github_10673].
Users who encounter hanging commands should verify
that the shebang fix and ripgrep configuration are both in place.

## Conclusion

Claude Code can be installed on FreeBSD
through the community-maintained port, the package system, or npm.
The port and package installations handle ripgrep configuration automatically
and are the recommended approach.
The npm installation provides access to the latest version
but requires manual configuration of the `USE_BUILTIN_RIPGREP` setting
and possibly a shebang fix.

The setup is not officially supported by Anthropic.
Compatibility may change as Claude Code evolves.
The [FreshPorts page][freebsd_freshports_claude_code]
and the GitHub issues referenced below
are useful resources for tracking the current state of FreeBSD support.

## Future Reading

The [official Claude Code documentation][claude_docs]
covers features, workflows, and configuration in detail.
The [companion post][related_post_claude_code]
covers installation on macOS, basic usage controls,
the `CLAUDE.md` configuration file,
and a practical code generation example.

The following GitHub issues track FreeBSD support.
Subscribing to these issues provides notification
of upstream changes that may affect FreeBSD installations.

- [Issue #22564][github_22564] tracks native installer support for FreeBSD.
- [Issue #13161][github_13161] tracks the bundled ripgrep binary issue.
- [Issue #22694][github_22694] tracks Linux emulator jail compatibility.

## References

- [Claude, Official Documentation][claude_docs]
- [Claude, npm Package][claude_npm]
- [Claude, Setup Guide][claude_setup]
- [FreeBSD, FreshPorts misc/claude-code][freebsd_freshports_claude_code]
- [FreeBSD, Handbook Installing Applications: Packages and Ports][freebsd_handbook_ports]
- [GitHub, Bash Commands Hang on FreeBSD #10673][github_10673]
- [GitHub, Blessed Installation Path Rules Out FreeBSD #22564][github_22564]
- [GitHub, Linux Emulator Jail Failure #22694][github_22694]
- [GitHub, Missing FreeBSD Ripgrep Binary #21542][github_21542]
- [GitHub, Ripgrep Tool Constant Failure on FreeBSD #13161][github_13161]
- [GitHub, Shebang Incompatibility on FreeBSD #9117][github_9117]
- [Related Post, Getting Started with Claude Code][related_post_claude_code]

[claude_docs]: https://code.claude.com/docs/en/home
[claude_npm]: https://www.npmjs.com/package/@anthropic-ai/claude-code
[claude_setup]: https://code.claude.com/docs/en/setup
[freebsd_freshports_claude_code]: https://www.freshports.org/misc/claude-code
[freebsd_handbook_ports]: https://docs.freebsd.org/en/books/handbook/ports/
[github_10673]: https://github.com/anthropics/claude-code/issues/10673
[github_13161]: https://github.com/anthropics/claude-code/issues/13161
[github_21542]: https://github.com/anthropics/claude-code/issues/21542
[github_22564]: https://github.com/anthropics/claude-code/issues/22564
[github_22694]: https://github.com/anthropics/claude-code/issues/22694
[github_9117]: https://github.com/anthropics/claude-code/issues/9117
[related_post_claude_code]: {% post_url 2026-01-31-claude_code_getting_started %}
