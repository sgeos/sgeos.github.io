---
layout: post
title:  "Getting Started with ION-DTN on FreeBSD"
date:   2016-02-08 03:34:50 +0900
categories: template
---
Problem description here.

## Software Versions
{% highlight sh %}
$ date
February  8, 2016 at 03:34:50 PM JST
$ uname -vm
{% endhighlight %}

## Instructions
First, download and extract the source code.
{% highlight sh %}
wget 'http://downloads.sourceforge.net/project/ion-dtn/ion-3.4.0b.tar.gz'
tar -zxvf ion-3.4.0b.tar.gz
cd ion-open-source/
{% endhighlight %}

Note that ION-DTN requires **gmake** and **bash**.
**autotools** are not required but useful.
{% highlight sh %}
portmaster devel/gmake shells/bash devel/autotools
{% endhighlight %}

The **sysctl_script.sh** script needs to be patched to run on FreeBSD.
So do many other files.
{% highlight sh %}
sed -i '' 's:#!/usr/bin/env bash:#!/usr/bin/env bash:' sysctl_script.sh
find ./ -type f -print0 | xargs -0 sed -i '' 's:#!/usr/bin/env bash:#!/usr/bin/env bash:'
{% endhighlight %}

Read **README.txt**.
Optionally run **./config -h**.
When you know what you are doing, run configure.
{% highlight sh %}
./configure --mandir=/usr/local/man
{% endhighlight %}

If instructed to do so, copy only the specified sysctl config lines
from the following list into **/boot/loader.conf**.
These values are read only tunable and must be set before the
system enters multi-user mode.
{% highlight sh %}
kern.ipc.shmmni=32
kern.ipc.shmseg=32
kern.ipc.semmns=32000
kern.ipc.semmni=128
{% endhighlight %}

If instructed to do so, copy only the specified sysctl config lines
from the following list into
your choice of  **/boot/loader.conf** or **/etc/sysctl.conf**.
These values are tunable in multi-user mode.
See the chapter in the [FreeBSD Handbook][freebsd-sysctl] for more information.
{% highlight sh %}
kern.ipc.shmmax=10485760
kern.ipc.shmmin=1
kern.ipc.shmall=4096
net.inet.udp.maxdgram=32000
{% endhighlight %}

Reboot if any changes were made.
{% highlight sh %}
su
shutdown -r now
{% endhighlight %}

Test the build.
{% highlight sh %}
gmake test
{% endhighlight %}

If configure runs without giving instructions to make changes, build.
Install as root for a system wide install.
{% highlight sh %}
su
gmake
gmake install
ldconfig
{% endhighlight %}

Serve **tutorial.html** and [open](http://localhost:8080/) it in your favorite browser.
Read through the tutorial.
{% highlight sh %}
FILE=tutorial.html; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <$FILE)\r\n\r\n"; cat $FILE; } | nc -N -l 0.0.0.0 8080
{% endhighlight %}

## References:
- [FreeBSD, freebsd server limits question][freebsd-limits]
- [FreeBSD, sysctl options loader.conf or sysctl.conf][freebsd-sysctl-options]
- [FreeBSD, man pages not installed correctly on FreeBSD][freebsd-bad-man]
- [FreeBSD Forums, sed not working with -i?][freebsd-sed]
- [FreeBSD Handbook, Tuning with sysctl(8)][freebsd-sysctl]
- [UNIX, Extract tar.gz File][unix-tar-gz]
- [UNIX, How to replace a path with another path in sed?][unix-sed]
- [UNIX, Awk/Sed: How to do a recursive find/replace of a string?][unix-sed-all]

[unix-tar-gz]: http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/
[unix-sed]: http://stackoverflow.com/questions/12061410/how-to-replace-a-path-with-another-path-in-sed
[unix-sed-all]: http://stackoverflow.com/questions/1583219/awk-sed-how-to-do-a-recursive-find-replace-of-a-string
[freebsd-sysctl]: https://www.freebsd.org/doc/handbook/configtuning-sysctl.html
[freebsd-sysctl-options]: https://lists.freebsd.org/pipermail/freebsd-questions/2005-August/095010.html
[freebsd-limits]: https://lists.freebsd.org/pipermail/freebsd-questions/2012-January/236726.html
[freebsd-sed]: https://forums.freebsd.org/threads/sed-not-working-with-i.12235/
[freebsd-bad-man]: https://github.com/thoughtbot/rcm/issues/131

