---
layout: post
mathjax: false
comments: true
title: "Getting Started with Claude Code Over SSH"
date: 2026-02-26 00:01:00 +0000
categories: ai ai-tools ssh development
---

<!-- Axxx -->

[Claude Code][claude_setup] is Anthropic's agentic command line tool
for software development.
It runs in the terminal, navigates repositories,
generates and modifies code, executes builds and tests,
and manages git workflows through natural language commands.
Companion posts cover
[installation and usage on macOS][related_post_claude_code],
[installation on FreeBSD][related_post_claude_code_freebsd],
and [installation on OpenBSD][related_post_claude_code_openbsd].

Not every machine that a developer needs to work on
can or should run Claude Code.
Production servers, embedded systems, legacy machines,
and platforms without Node.js support
are all cases where local installation is impractical or inadvisable.
SSH provides an alternative.
A developer can run Claude Code on a local workstation
and use SSH to execute commands, transfer files,
and manage remote targets.
The local machine provides the intelligence
and the remote machine provides the environment.

This post covers four topics.
First, it introduces SSH fundamentals
for readers who are unfamiliar with or rusty regarding the protocol.
Second, it walks through key-based authentication setup
and SSH client configuration.
Third, it covers SSH agent forwarding,
which allows Claude Code to perform Git operations
and other key-authenticated tasks on remote machines.
Fourth, it demonstrates how Claude Code's Bash tool
can execute commands on remote machines over SSH
and how scp handles file transfer.

Claude Code Desktop also provides
a [native SSH connection feature][claude_desktop]
that offers a more integrated remote development experience.
That feature requires Claude Code to be installed on the remote machine
and is covered briefly in a later section.
The primary focus of this article is the Bash tool approach,
which requires nothing on the remote machine
beyond a standard SSH server.

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

# OpenSSH
$ ssh -V
```

## SSH Background

This section provides a brief introduction to SSH
for readers who are unfamiliar with or rusty regarding the protocol.
Readers who are comfortable with SSH key pairs,
SSH agent, and SSH client configuration
may skip ahead to the Instructions section.

### What SSH Is

SSH stands for Secure Shell.
It is a protocol for encrypted communication between two machines.
An SSH client on the local machine
connects to an SSH server on the remote machine.
The connection is encrypted and authenticated.
It can carry terminal sessions, file transfers,
and port-forwarded traffic.

[OpenSSH][ref_openssh] is the reference implementation of the SSH protocol.
It ships with macOS, Linux, and most BSD variants.
On Windows, OpenSSH is available as an optional feature
or through the Windows Subsystem for Linux.
The commands in this article assume OpenSSH.

### Authentication

SSH supports two primary authentication methods.
Password authentication requires typing a password
at each connection.
Public key authentication uses a cryptographic key pair.
The private key stays on the local machine.
The public key is copied to the remote machine.
When the client connects,
the server challenges the client to prove possession of the private key
without transmitting it.

Claude Code's Bash tool does not support interactive password prompts.
A command that requires typing a password will hang
until the Bash tool timeout expires.
Key-based authentication is therefore required
for this workflow.

The SSH agent is a program that caches decrypted private keys in memory.
When a private key is protected by a passphrase,
the agent allows the passphrase to be entered once
rather than at every connection.
Claude Code's Bash tool inherits the agent socket
from the shell environment,
so keys loaded into the agent are available
to SSH commands that Claude Code executes.

### SSH Configuration

The SSH client reads its configuration
from the file `~/.ssh/config`.
This file defines host aliases, default usernames,
identity files, and connection options.
A configured host alias allows the command
`ssh myserver` to replace a longer invocation
such as `ssh -i ~/.ssh/mykey -p 2222 deploy@192.168.1.100`.

Host aliases are useful for Claude Code
because shorter commands reduce the chance
of errors in Bash tool invocations.
The configuration file also ensures that
connection parameters are consistent
across every SSH command that Claude Code executes.

## Instructions

### Prerequisites

This workflow requires the following.

Claude Code must be installed and authenticated on the local machine.
The [companion post][related_post_claude_code] covers installation on macOS.
The [FreeBSD][related_post_claude_code_freebsd]
and [OpenBSD][related_post_claude_code_openbsd] companion posts
cover installation on those platforms.

An SSH client must be available on the local machine.
OpenSSH ships with macOS, Linux, and most BSD variants.
Verify that the `ssh` command is available.

```sh
$ ssh -V
```

An SSH server must be running on the remote machine.
Most Unix-like systems ship with OpenSSH server
or make it available as a package.
Verify that the server is running on the remote machine.

```sh
$ ssh user@remote "echo SSH server is running"
```

Replace `user` with the remote username
and `remote` with the remote hostname or IP address.
If this command fails,
consult the remote system's documentation
for enabling the SSH server.

### Key Generation

Generate an Ed25519 SSH key pair.
Ed25519 is a modern elliptic curve algorithm
that produces short keys with strong security properties.

```sh
$ ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -C "user@local"
```

The `-t` flag specifies the key type.
The `-f` flag specifies the output file.
The `-C` flag adds a comment to the public key
for identification purposes.

The command will prompt for a passphrase.
A passphrase adds a layer of protection to the private key.
If the key file is compromised,
the passphrase prevents immediate use.
The passphrase is optional but recommended.
The SSH agent described below
handles passphrase re-entry.

The command produces two files.
The private key is saved to `~/.ssh/id_ed25519`.
The public key is saved to `~/.ssh/id_ed25519.pub`.
The private key file must have permissions set to 600.
The `~/.ssh` directory must have permissions set to 700.

```sh
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/id_ed25519
```

See the [ssh-keygen manual][ref_ssh_keygen] for additional options.

### Copying the Public Key

The public key must be appended to the
`~/.ssh/authorized_keys` file on the remote machine.
The `ssh-copy-id` utility automates this process.

```sh
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote
```

This command will prompt for the remote password one time.
After the public key is copied,
subsequent connections will use key-based authentication.

If `ssh-copy-id` is not available,
copy the public key manually.

```sh
$ cat ~/.ssh/id_ed25519.pub | ssh user@remote "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

Verify that key-based authentication works.

```sh
$ ssh user@remote "echo connection successful"
```

If this command prints `connection successful`
without prompting for a password,
key-based authentication is configured correctly.

### SSH Agent

Start the SSH agent and add the private key.

```sh
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_ed25519
```

The first command starts the agent
and sets the `SSH_AUTH_SOCK` environment variable.
The second command loads the private key into the agent.
If the key has a passphrase,
`ssh-add` will prompt for it once.

On macOS, the following variant stores the passphrase
in the system Keychain
so that it persists across reboots.

```sh
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

The SSH agent is important for Claude Code
because the Bash tool starts new shell sessions
that inherit the agent socket.
Keys loaded into the agent are available
to every SSH command that Claude Code executes
for the duration of the agent session.

### Host Configuration

Create or edit the SSH client configuration file
at `~/.ssh/config`.
Add a host alias for the remote machine.

```
Host myserver
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    ServerAliveInterval 60
```

Replace `myserver` with a short alias of your choice.
Replace `192.168.1.100` with the remote hostname or IP address.
Replace `deploy` with the remote username.

The `IdentityFile` directive specifies which private key to use.
The `IdentitiesOnly yes` directive
prevents the client from trying every key loaded in the agent
and restricts authentication to the specified key.
The `ServerAliveInterval 60` directive
sends a keepalive packet every 60 seconds
to prevent idle connections from being dropped
by firewalls or network equipment.

With this configuration in place,
the command `ssh myserver` is equivalent
to `ssh -i ~/.ssh/id_ed25519 deploy@192.168.1.100`.

See the [ssh_config manual][ref_ssh_config]
for the full list of configuration directives.

### Verification

Verify that the SSH connection works
through the configured host alias
without a password prompt.

```sh
$ ssh myserver "hostname && uname -a"
```

If this command prints the remote hostname and system information
without prompting for a password,
the configuration is complete.

If the command prompts for a password,
check the following.
Verify that the private key file has 600 permissions.
Verify that the `~/.ssh/authorized_keys` file on the remote machine
contains the public key and has 600 permissions.
Verify that the remote SSH server has `PubkeyAuthentication yes`
in its `sshd_config` file.

### Remote Execution with Claude Code

Claude Code's Bash tool can execute SSH commands
to run programs on remote machines.
The following examples show common patterns.

Execute a single command on the remote machine.

```sh
$ ssh myserver "uname -a"
```

Execute multiple commands with a specific working directory.

```sh
$ ssh myserver "cd /home/deploy/project && make clean && make"
```

Transfer a file from the local machine to the remote machine.

```sh
$ scp localfile.c myserver:/home/deploy/project/
```

Transfer a file from the remote machine to the local machine.

```sh
$ scp myserver:/home/deploy/project/output.txt ./
```

Transfer a directory recursively.

```sh
$ scp -r ./src myserver:/home/deploy/project/
```

Each SSH invocation through the Bash tool
starts a fresh shell session on the remote machine.
Working directory changes, environment variable exports,
and shell aliases do not persist between Bash tool calls.
To execute multiple dependent commands,
chain them in a single SSH invocation with `&&`.

Claude Code's Read, Edit, Glob, and Grep tools
only operate on the local filesystem.
To read a remote file, use SSH.

```sh
$ ssh myserver "cat /etc/os-release"
```

To edit a remote file,
one approach is to transfer it locally with scp,
edit it with Claude Code's Edit tool,
and transfer it back.

### Timeout Configuration

Claude Code's Bash tool has a default timeout
of approximately two minutes.
Long-running remote operations
such as compilation, package installation, or database migrations
may exceed this limit.

Configure longer timeouts
in `~/.claude/settings.json`.

```json
{
  "env": {
    "BASH_DEFAULT_TIMEOUT_MS": "300000",
    "BASH_MAX_TIMEOUT_MS": "600000"
  }
}
```

The values are in milliseconds.
300000 is five minutes.
600000 is ten minutes.

Claude Code can also run long commands in the background
and check their output later.
This is useful for operations
that may take longer than the configured timeout.

## Agent Forwarding

The Instructions section above covers
connecting to a remote machine and executing commands.
In some cases, the remote machine needs to authenticate
to a third-party service using the developer's SSH keys.
The most common example is Git operations over SSH.
Without agent forwarding,
running `git clone git@github.com:org/repo.git`
on the remote machine would fail
because the remote machine does not have
the developer's GitHub SSH key.

Agent forwarding solves this problem
by allowing the remote machine
to use the developer's local [SSH agent][ref_ssh_agent]
for authentication
without copying private keys to the remote machine.

### How Agent Forwarding Works

The SSH agent on the local machine
holds decrypted private keys in memory.
When agent forwarding is enabled,
the SSH client creates a secure channel
between the remote machine and the local agent.
Programs on the remote machine can ask the local agent
to sign authentication challenges
without the private key ever leaving the local machine.

This is implemented through a temporary Unix domain socket
on the remote machine.
The SSH server sets the `SSH_AUTH_SOCK` environment variable
to point to this socket.
When a program on the remote machine
connects to the socket to request authentication,
the request is forwarded through the encrypted SSH connection
to the local agent.
The local agent performs the cryptographic operation
and returns the result.

### Enabling Agent Forwarding

Add the `ForwardAgent yes` directive
to the host entry in `~/.ssh/config`.

```
Host myserver
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    ServerAliveInterval 60
    ForwardAgent yes
```

This extends the host configuration
from the Instructions section
by adding the `ForwardAgent yes` directive.

For one-off use without modifying the configuration file,
pass the `-A` flag to the `ssh` command.

```sh
$ ssh -A myserver "git clone git@github.com:org/repo.git"
```

The remote server must have
`AllowAgentForwarding yes` in its `sshd_config` file.
This is the default on most OpenSSH installations.

### Verifying Agent Forwarding

Verify that agent forwarding works
by listing the keys available on the remote machine.

```sh
$ ssh -A myserver "ssh-add -l"
```

If this command prints the fingerprints
of the keys loaded in the local agent,
agent forwarding is working correctly.
The output should match the output of `ssh-add -l`
run locally.

If the command prints
"Could not open a connection to your authentication agent,"
the forwarding is not configured correctly.
Check that `ForwardAgent yes` is set
in the host entry or that the `-A` flag was passed.
Verify that the local SSH agent has keys loaded
by running `ssh-add -l` on the local machine.
Verify that the remote server has
`AllowAgentForwarding yes` in its `sshd_config`.

### Use with Claude Code

When Claude Code executes an SSH command
with agent forwarding enabled,
the forwarded agent allows programs on the remote machine
to authenticate using the developer's local SSH keys.

The Bash tool inherits the `SSH_AUTH_SOCK` environment variable
from the shell environment.
When Claude Code runs `ssh -A myserver "git clone git@github.com:org/repo.git"`,
the SSH client connects to the local agent,
forwards the agent to the remote machine,
and the remote Git command authenticates with GitHub
using the developer's local key.

The following prompt demonstrates agent forwarding
in a Claude Code session.

````
Connect to myserver via SSH with agent forwarding enabled.
Clone the repository git@github.com:org/repo.git into
~/projects/ on the remote machine. List the contents of
the cloned repository.
````

Claude Code will execute `ssh -A myserver "git clone git@github.com:org/repo.git ~/projects/repo"`
followed by `ssh myserver "ls ~/projects/repo"`.
The `-A` flag enables agent forwarding
so that the remote Git command can authenticate with GitHub.

### Security Considerations

Agent forwarding introduces a security risk
that must be understood before enabling it.

Any user with root access on the remote host
can access the forwarded agent socket
and use it to authenticate to any system
that accepts the forwarded keys.
This means a compromised remote host
could impersonate the developer on GitHub,
other servers, or any service
that trusts the forwarded SSH key.

The risk is limited to the duration of the SSH session.
Once the connection is closed,
the forwarded socket is removed
and the remote host can no longer access the agent.

The following practices reduce the risk.

Do not enable `ForwardAgent yes` globally
with a `Host *` directive.
Scope agent forwarding to specific trusted hosts.
Only enable agent forwarding for hosts
that the developer fully trusts and controls.
Do not enable agent forwarding
when connecting to shared hosting environments,
public servers, or any machine
where other users have root access.

For untrusted intermediate hosts such as bastion or jump hosts,
use `ProxyJump` instead of agent forwarding.

### ProxyJump Alternative

When a developer needs to reach a target
through an intermediate host that is not fully trusted,
`ProxyJump` provides a safer alternative to agent forwarding.

```
Host internal-server
    HostName 10.0.0.50
    User deploy
    ProxyJump bastion.example.com
```

Or as a one-off command.

```sh
$ ssh -J bastion.example.com deploy@10.0.0.50
```

`ProxyJump` forwards the SSH connection
through the intermediate host
without giving the intermediate host access to the agent.
The intermediate host acts as a TCP tunnel only.
It cannot use the developer's keys
to authenticate to other systems.

`ProxyJump` requires OpenSSH 7.3 or later,
which was released in 2016.
Older systems that lack `ProxyJump` support
can use the equivalent `ProxyCommand` directive,
which provides the same functionality
with a more verbose syntax.

See the [ssh_config manual][ref_ssh_config]
for the full list of proxy and forwarding directives.

## Claude Code Desktop SSH

[Claude Code Desktop][claude_desktop] provides
a native SSH connection feature
that offers a more integrated remote development experience.
The developer adds an SSH connection
through the Desktop application's environment dropdown
and Claude Code runs directly on the remote machine
with full access to its filesystem and tools.

This approach requires Claude Code
to be installed on the remote machine.
For targets that can run Claude Code
but are inconvenient to access directly,
Desktop SSH may be the better option.
It provides the same tool access
as a local Claude Code session
without the limitations of the Bash tool SSH workflow
described in this article.

The [official Desktop documentation][claude_desktop]
covers SSH connection setup.
This feature is only available in the Desktop application
and is not available in the CLI.

## Hello World

With SSH configured and verified,
the following exercise demonstrates
Claude Code's ability to work on a remote machine
through the Bash tool SSH workflow.
The goal is to issue a single prompt
that triggers remote OS detection, code generation,
file transfer, compilation, and execution.

Create an empty local project directory and launch Claude Code.

```sh
$ mkdir ~/remote-demo && cd ~/remote-demo
$ claude
```

Paste the following prompt.
Replace `myserver` with the host alias
configured in the Host Configuration section.

````
Connect to myserver via SSH. Determine the operating system and
available C compiler. Create a directory called ~/sysinfo on the
remote machine. Write a C program that displays the hostname,
operating system, kernel version, CPU count, and total memory
using only POSIX and standard system interfaces. Transfer the
source file to the remote machine. Compile and run it remotely.
Report the output.
````

Claude Code will execute `ssh myserver "uname"` to detect the remote OS,
write a C source file locally using the Write tool,
transfer it with `scp`,
compile it with `ssh myserver "cc -o sysinfo sysinfo.c"`,
and run it with `ssh myserver "./sysinfo"`.

The exact output will vary by session and remote OS.
The program should compile and run
on any POSIX system with a C compiler.
Expect at minimum a `sysinfo.c` file in the local directory
and compiled output on the remote machine.

This exercise verifies four capabilities in a single prompt.
Claude Code executes SSH commands to detect the remote environment,
generates C source code suited to that environment,
transfers the file to the remote machine with scp,
and compiles and runs the program remotely.

## Limitations

The Bash tool SSH workflow has the following constraints.

Claude Code's Read, Edit, Glob, and Grep tools
only operate on the local filesystem.
Remote file operations require SSH commands or scp
through the Bash tool.

Each Bash tool invocation starts a new SSH session.
Working directory, environment variables,
and shell state do not persist between calls.
To execute multiple dependent commands,
chain them in a single SSH invocation with `&&`.

Claude Code's Bash tool does not support interactive prompts.
Password-based SSH authentication,
sudo password prompts,
and interactive confirmation dialogs
will hang until the timeout expires.
Key-based authentication is required.

The default Bash tool timeout is approximately two minutes.
Long-running remote operations
require timeout configuration or background execution.

SSH port forwarding, X11 forwarding, and tunneling
must be configured in `~/.ssh/config`
or passed as flags in each SSH invocation.
Claude Code does not manage SSH tunnels automatically.

Community-maintained MCP SSH servers
provide persistent connections
and higher-level abstractions for SSH operations.
These are beyond the scope of this article.
The Model Context Protocol is documented
in the [official Claude Code documentation][claude_docs].

## Conclusion

SSH provides a practical path
for using Claude Code with remote machines
that cannot or should not run Claude Code locally.
The workflow requires only a working SSH connection
with key-based authentication.
Claude Code's Bash tool handles remote command execution
and scp handles file transfer.

The main constraints
are the lack of persistent shell state between invocations
and the absence of interactive prompt support.
For developers who work across multiple machines or platforms,
SSH bridges the gap between Claude Code's local execution model
and the reality of distributed development environments.

For machines that can run Claude Code remotely,
the [Desktop SSH feature][claude_desktop]
provides a more integrated experience.

## Future Reading

The [official Claude Code documentation][claude_docs]
covers features, workflows, and configuration in detail.
The [companion post][related_post_claude_code]
covers installation on macOS, basic usage controls,
the `CLAUDE.md` configuration file,
and a practical code generation example.
The [FreeBSD companion][related_post_claude_code_freebsd]
and [OpenBSD companion][related_post_claude_code_openbsd]
cover installation on those platforms.

The [OpenSSH manual pages][ref_openssh]
provide comprehensive documentation
for ssh, scp, ssh-keygen, ssh-agent,
and the ssh_config configuration file.

The [Claude Code Desktop documentation][claude_desktop]
covers the native SSH connection feature
for integrated remote development.

## References

- [Claude, Desktop Application][claude_desktop]
- [Claude, Official Documentation][claude_docs]
- [Claude, Settings][claude_settings]
- [Claude, Setup Guide][claude_setup]
- [Reference, OpenSSH Manual Pages][ref_openssh]
- [Reference, OpenSSH ssh-agent Manual][ref_ssh_agent]
- [Reference, OpenSSH ssh_config Manual][ref_ssh_config]
- [Reference, OpenSSH ssh-keygen Manual][ref_ssh_keygen]
- [Related Post, Getting Started with Claude Code][related_post_claude_code]
- [Related Post, Getting Started with Claude Code on FreeBSD][related_post_claude_code_freebsd]
- [Related Post, Getting Started with Claude Code on OpenBSD][related_post_claude_code_openbsd]

[claude_desktop]: https://code.claude.com/docs/en/desktop
[claude_docs]: https://code.claude.com/docs/en/home
[claude_settings]: https://code.claude.com/docs/en/settings
[claude_setup]: https://code.claude.com/docs/en/setup
[ref_openssh]: https://www.openssh.com/manual.html
[ref_ssh_agent]: https://man.openbsd.org/ssh-agent
[ref_ssh_config]: https://man.openbsd.org/ssh_config
[ref_ssh_keygen]: https://man.openbsd.org/ssh-keygen
[related_post_claude_code]: {% post_url 2026-01-31-claude_code_getting_started %}
[related_post_claude_code_freebsd]: {% post_url 2026-02-24-claude_code_getting_started_on_freebsd %}
[related_post_claude_code_openbsd]: {% post_url 2026-02-25-claude_code_getting_started_on_openbsd %}
