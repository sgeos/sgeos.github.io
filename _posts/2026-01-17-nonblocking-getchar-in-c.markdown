---
layout: post
mathjax: false
comments: true
title: "Nonblocking getchar() in C"
date: 2026-01-17 23:51:32 +0000
categories: [unix, c]
---

<!-- A69 -->

Getting characters one at a time with `getchar()` is useful. 
Sometimes a program needs to do other things while waiting for input. 
Sometimes blocking is problematic.

This post covers nonblocking `getchar()`. 
The problem consists of three parts.

- **Unbuffered `getchar()`.** By default, `getchar()` buffers until input followed by a newline is available.
- **Nonblocking `getchar()`.** By default, `getchar()` blocks until input is available.
- **Sleeping when input is not available.** There is no need to run the CPU full throttle.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-17 23:51:32 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

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

# C Compiler Version
$ clang --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin23.6.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

## Instructions

To achieve non-blocking input, we must interact with the Unix terminal interface `termios` and file control `fcntl`. 

### 1. Disable Canonical Mode
Input is usually processed line-by-line (canonical mode). We clear the `ICANON` and `ECHO` flags to allow `getchar()` to read keys immediately without a newline.

### 2. Set O_NONBLOCK
By setting the `O_NONBLOCK` flag on `stdin`, `getchar()` returns `EOF` immediately if no key is in the buffer, rather than hanging the thread.

### 3. Safety First: Signal Handling
Because we are modifying the terminal state, a crash or a `Ctrl+C` interrupt could leave your shell "broken" (no echo, no newlines). We use `sigaction` to catch interrupts and restore the original state before exiting.

## The Implementation

**`main.c`**
```c
#include <fcntl.h>
#include <signal.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <time.h>
#include <unistd.h>

// Original state restoration variables
struct termios original_termios;
int original_fcntl_flags;

void async_print(const char *format, ...) {
    char message_buffer[128];
    va_list args;
    
    va_start(args, format);
    int length = vsnprintf(message_buffer, sizeof(message_buffer), format, args);
    va_end(args);

    if (length > 0) {
        // Use write() to bypass stdio buffering
        write(STDOUT_FILENO, message_buffer, (size_t)length);
    }
}

void restore_terminal_settings(void) {
    tcsetattr(STDIN_FILENO, TCSANOW, &original_termios);
    fcntl(STDIN_FILENO, F_SETFL, original_fcntl_flags);
}

void handle_termination_signal(int signal_number) {
    // Cleanup and exit
    restore_terminal_settings();
    async_print("\nInterrupted by signal %d. Terminal settings restored.\n", signal_number);
    exit(0);
}

int main(void) {
    struct termios modified_termios;
    struct timespec sleep_duration = {0, 100000000L}; // 100ms
    int input_char;

    // Set up signal handling for safe exit (Ctrl+C)
    struct sigaction signal_action;
    signal_action.sa_handler = handle_termination_signal;
    sigemptyset(&signal_action.sa_mask);
    signal_action.sa_flags = 0;
    sigaction(SIGINT, &signal_action, NULL);

    // Save current terminal settings and file flags
    tcgetattr(STDIN_FILENO, &original_termios);
    original_fcntl_flags = fcntl(STDIN_FILENO, F_GETFL, 0);

    // Modify terminal: Disable canonical mode (line buffering) and echo
    modified_termios = original_termios;
    modified_termios.c_lflag &= (tcflag_t)~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &modified_termios);

    // Modify file descriptor: Set stdin to non-blocking mode
    fcntl(STDIN_FILENO, F_SETFL, original_fcntl_flags | O_NONBLOCK);

    async_print("Non-blocking loop started. Press 'q' to quit or Ctrl+C to interrupt.\n");

    while (1) {
        input_char = getchar();

        if (input_char != EOF) {
            async_print("\nYou pressed: %c", input_char);
            if (input_char == 'q') {
                break;
            }
            async_print("\n");
        } else {
            // No input currently available: visually indicate activity and sleep
            async_print(".");
            nanosleep(&sleep_duration, NULL); 
        }
    }

    // Cleanup and exit
    restore_terminal_settings();
    async_print("\nNormal exit. Terminal settings restored.\n");
    return 0;
}
```

## Compilation and Output

To compile and run:

```sh
BIN="getchar_nonblocking"
clang -O3 main.c -o "${BIN}"
"./${BIN}"
```

**Expected Output:**
You will see a sequence of dots appearing every 100ms. If you press a key, it is captured immediately without hitting Enter.

```text
Non-blocking loop started. Press 'q' to quit or Ctrl+C to interrupt.
.......
You pressed: a
.....
You pressed: s
....
You pressed: d
.....
You pressed: f
....
You pressed: q
Normal exit. Terminal settings restored.
```

If you terminate with `Ctrl+C`, the signal handler triggers, ensuring your terminal doesn't stay in a bugged, non-echoing state.

## References:
- [UNIX, How do you do non-blocking console I/O on Linux in C?][unix-nonblock]
- [UNIX, C: Question about getchar()][unix-getchar-q]
- [UNIX, non blocking input from keyboard][unix-rpi]
- [UNIX, Linux time.h][unix-time]

[unix-nonblock]: http://stackoverflow.com/questions/717572/how-do-you-do-non-blocking-console-i-o-on-linux-in-c
[unix-rpi]: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=23495
[unix-getchar-q]: http://ubuntuforums.org/showthread.php?t=1396108
[unix-time]: http://linux.die.net/include/sys/time.h

