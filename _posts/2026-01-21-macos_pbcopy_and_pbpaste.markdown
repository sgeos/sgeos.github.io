---
layout: post
mathjax: false
comments: true
title:  "pbcopy and pbpaste for macOS"
date:   2026-01-21 09:34:50 +0000
categories: [macos, terminal, unix]
---
If you spend any amount of time in the macOS Terminal, chances are you have
copied and pasted text between the command line and graphical apps more times
than you can count. macOS provides two small but powerful utilities, `pbcopy`
and `pbpaste`, that make pasteboard access a first-class citizen of the Unix
pipeline.

This post explores what they are, how they work, and how to use them
effectively in everyday workflows.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-21 09:34:50 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# pbcopy and pbpaste are built in utilities
# see OS version info for utility version
```

## What Are pbcopy and pbpaste?

- **`pbcopy`** reads from **standard input** and writes the data to the macOS
system pasteboard.
- **`pbpaste`** reads data **from the system pasteboard** and writes it to
standard output.

They act as a bridge between the Unix `stdin`/`stdout` and the macOS
pasteboard.

- These utilities work with UTF-8 text by default.
- They can also handle some non-text formats (RTF, HTML) depending on how
they are used, but they are most reliable for plain text.
- They integrate directly with the macOS pasteboard, so anything copied in
Finder, Safari, etc., is accessible via pbpaste.

## pbcopy Basic Usage

Anything sent to `pbcopy` via a pipe ends up on the general pasteboard,
ready to paste into another app.

```sh
# Copy the contents of a file to the clipboard
pbcopy < file.txt

# Copy the contents of all files of a particular type to the clipboard
cat directory/*.txt | pbcopy

# Copy a list of files to the clipboard
ls | pbcopy
```

## pbpaste Basic Usage

`pbpaste` prints whatever is currently on the clipboard.

```sh
# print pasteboard to terminal
pbpaste

# Save pasteboard to a file
pbpaste > file.txt

# Append pasteboard contents to the end of a file
pbpaste >> file.txt
```

## Pasteboard Modification in Place

You can pipe pasteboard content through a command and back to the pasteboard
to modify the contents without creating a file.  The general pattern is
`pbpaste | command_a | command_b | pbcopy`.  Note that `tee /dev/tty` can be
used to print the contents of the pasteboard while piping to the next command.
It is useful if you want to print the initial or final pasteboard contents,
but it can be used at any step.

```sh
# Replace pasteboard CSV commas with tabs
pbpaste | sed "s/,/\t/g" | pbcopy

# Split pasteboard contents into lines no longer than 78 characters
# Print final pasteboard contents
pbpaste | fmt -p -w 78 | tee /dev/tty | pbcopy

# Replace pasteboard contents with a base64 encoded version
pbpaste | base64 | pbcopy
```

## Command Line Options

`pbcopy` and `pbpaste` have a command line option `-pboard` to specify the
`general`, `ruler`, `find`, or `font` pasteboard. `general` is the default.

- The General pasteboard stores text.
- The Ruler pasteboard stores paragraph-level layout and ruler settings, not
text.
- The Find pasteboard stores the current search string used by “Find”
operations (⌘F, Find Next, Find Previous) across applications.
- The Font pasteboard stores font and text-style information, not plain text.

```sh
# Write pasteboard font to file
pbpaste -pboard font > font.bin

# Restore pasteboard font from file
pbcopy -pboard font < font.bin
```

`pbpaste` has a `-Prefer` option to specify whether the utility should first
attempt to paste `txt`, `rtf`, or `ps`.

```sh
# Attempt to paste rtf into a file
pbpaste -Prefer rtf > file.rtf
```

## Locale Awareness

They are locale aware and use the C locale if no locale is specified.

```sh
# Force locale to UTF-8 and paste to terminal
LANG=en_US.UTF-8 pbpaste

# Force locale to UTF-8 and copy file to pasteboard
LANG=en_US.UTF-8 pbcopy < file.txt

# Multi-line example
LANG=en_US.UTF-8
pbcopy < file.txt
pbpaste
```

---

## Equivalent Utilities

The macOS pasteboard utilities are not unique in concept, but their exact
behavior is platform-specific. Other operating systems provide similar
command-line access to the system clipboard, often with different abstractions
and limitations.

### Linux

Linux does not have a single, universal clipboard API. Clipboard utilities
depend on the windowing system in use.

#### X11 (Xorg)

The most common tools are:

- **`xclip`**
- **`xsel`**

These tools interact with X11 selections, most notably:
- `CLIPBOARD` (what users expect as “the clipboard”)
- `PRIMARY` (middle-click paste)

Examples using `xclip`:

```sh
# Copy stdin to the clipboard
echo "hello" | xclip -selection clipboard

# Paste clipboard to stdout
xclip -selection clipboard -o
```

With `xsel`:

```sh
# Copy
echo "hello" | xsel --clipboard --input

# Paste
xsel --clipboard --output
```

Notes:
- These tools require an active X11 session.
- Clipboard ownership is process-based.  When the owning process exits,
clipboard contents may be lost unless a clipboard manager is running.

#### Wayland

Wayland uses a different protocol. Common tools include:

- **`wl-copy`**
- **`wl-paste`** (from `wl-clipboard`)

```sh
# Copy
echo "hello" | wl-copy

# Paste
wl-paste
```

Notes:
- Wayland typically enforces stricter clipboard security.
- Clipboard access may be limited or denied in some sandboxed environments.

---

### FreeBSD

FreeBSD itself does not define a clipboard mechanism. Clipboard utilities
depend on the desktop environment.

Common options mirror Linux:

- **`xclip` / `xsel`** (X11)
- **`wl-copy` / `wl-paste`** (Wayland)

Example:

```sh
pkg install xclip
echo "hello" | xclip -selection clipboard
```

On FreeBSD servers without a GUI, clipboard access is usually unavailable by
design.

---

### Windows

Windows provides clipboard access via several command-line tools.

#### `clip` (Command Prompt and PowerShell)

Windows includes a built-in utility:

```cmd
echo hello | clip
```

This copies text to the Windows clipboard.

However, `clip` is **write-only**. It cannot read from the clipboard.
This mirrors `pbcopy` without an equivalent of `pbpaste`.
Users often use `powershell -command "Get-Clipboard"` as a workaround.

#### PowerShell

PowerShell provides full read/write access:

```powershell
# Copy
"hello" | Set-Clipboard

# Paste
Get-Clipboard
```

Notes:
- PowerShell clipboard commands support text and richer data types.
- Available on modern Windows systems by default.

---

### Cross-Platform Abstractions

Some tools and environments attempt to smooth over platform differences:

- **Neovim / Vim**: `"+y` and `"+p` abstract clipboard access
- **tmux**: Can integrate with system clipboards using platform-specific
helpers
- **Python / Node.js libraries**: Often wrap OS-specific clipboard APIs

Despite these efforts, clipboard semantics remain fundamentally OS-dependent.

### Summary Table

| Platform | Copy | Paste | Notes |
|--------|------|-------|-------|
| macOS | `pbcopy` | `pbpaste` | Unified pasteboard model |
| Linux (X11) | `xclip`, `xsel` | `xclip`, `xsel` | Multiple selections |
| Linux (Wayland) | `wl-copy` | `wl-paste` | Stricter security |
| FreeBSD | `xclip`, `wl-copy` | `xclip`, `wl-paste` | Depends on GUI |
| Windows (cmd) | `clip` | — | Write-only |
| Windows (PowerShell) | `Set-Clipboard` | `Get-Clipboard` | Full access |

---

## References:

- [Man Page, pbcopy][man_pbcopy]
- [Man Page, pbpaste][man_pbpaste]

[man_pbcopy]: https://ss64.com/mac/pbcopy.html
[man_pbpaste]: https://ss64.com/mac/pbpaste.html
