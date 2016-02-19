---
layout: post
comments: true
title:  "Getting PID by Name on FreeBSD"
date:   2016-02-19 07:57:31 +0900
categories: freebsd
---
This post covers getting the PID of a process by name with and without the **sysutils/psmisc** port.

## Software Versions

{% highlight sh %}
$ date
February 19, 2016 at 07:57:31 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions

The easy way is to install the **sysutils/psmisc** port and use the **pidof** command.

{% highlight sh %}
portmaster sysutils/psmisc
PROCESS_NAME="sshd"
pidof "${PROCESS_NAME}"
{% endhighlight %}

The following can be used to get the information on all of the processes matching a name.

{% highlight sh %}
PROCESS_NAME="sshd" ; ps -aux | grep "${PROCESS_NAME}" | grep -v "grep"
{% endhighlight %}

The following can be used to get the PIDs of all processes matching a name.

{% highlight sh %}
PROCESS_NAME="sshd" ; ps -ax | grep "${PROCESS_NAME}" | grep -v "grep" | awk '{ print $1 }'
{% endhighlight %}

Something like the following can be used for control flow in a shell script.
The -qs flags suppress grep output.

{% highlight sh %}
#!/bin/sh

PROCESS_NAME="sshd"
if ps -ax | grep "${PROCESS_NAME}" | grep -qsv "grep"
then
  echo "${PROCESS_NAME} is running."
else
  echo "${PROCESS_NAME} is not running."
fi
{% endhighlight %}

## References:
- [FreeBSD, man pidof][freebsd-man-pidof]
- [FreeBSD, Fresh Ports sysutils/psmisc][freebsd-psmisc]
- [UNIX, How to terminate process by name in UNIX][unix-terminate]
- [sgeos.github.io Post History][blog-history]

[freebsd-man-pidof]: https://www.freebsd.org/cgi/man.cgi?query=pidof&manpath=SuSE+Linux/i386+11.3
[freebsd-psmisc]: https://www.freshports.org/sysutils/psmisc
[unix-terminate]: http://notetodogself.blogspot.com/2006/07/how-to-terminate-process-by-name-in.html
[blog-history]: https://github.com/sgeos/sgeos.github.io/commit/5c4dcf97faced6fefe5e29e4a8c95ed94ce599ef

