---
layout: post
comments: true
title:  "Nonblocking getchar() in C"
date:   2016-01-01 00:00:00 +0000
categories: unix c
---
Getting characters one at a time with **getchar()** is useful.
Sometimes a program needs to do other things while waiting for input.
Sometimes blocking is problematic.

This post covers nonblocking **getchar()**.
The problem consists of three parts.

- Unbuffered **getchar()**.  By default, **getchar()** buffers until input followed by a newline is available.
- Nonblocking **getchar()**.  By default, **getchar()** blocks until input is available.
- Sleeping when input is not available.  There is no need to run the CPU full throttle.

This post covers the fix for the above problems.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
$ uname -vm
{% endhighlight %}

## Instructions

Instructions for solution here.

{% highlight sh %}
echo "Code here."
{% endhighlight %}

## References:
- [UNIX, How do you do non-blocking console I/O on Linux in C?][unix-nonblock]
- [UNIX, C: Question about getchar()][unix-getchar-q]
- [UNIX, non blocking input from keyboard][unix-rpi]
- [UNIX, Linux time.h][unix-time]

[unix-nonblock]: http://stackoverflow.com/questions/717572/how-do-you-do-non-blocking-console-i-o-on-linux-in-c
[unix-rpi]: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=23495
[unix-getchar-q]: http://ubuntuforums.org/showthread.php?t=1396108
[unix-time]: http://linux.die.net/include/sys/time.h

