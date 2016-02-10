---
layout: post
title:  "Getting Started with ION-DTN 3.4.0 on FreeBSD"
date:   2016-02-08 03:34:50 +0900
categories: freebsd ion dtn
---
I was reading Wikipedia articles about things like the [interplanetary internet][wikipedia-interplanetary],
[InterPlaNet][wikipedia-ipn] and [delay-tolerant networking][wikipedia-dtn].
After writing a [post on serving web content with tor][freebsd-tor], I wanted to try to serve a web page over ION-DTN.
This post covers installing [ION-DTN][ion-dtn] 3.4.0 on FreeBSD.

After the installation instructions, there are a few usage examples, including a very crude scripted web server.
The original goal was to take an outside web request, send it over ION-DTN to a server on the other side and return the response.
That example deserves a separate post.

Special thanks to Scott C Burleigh for helping me work through some setup problems.

## Software Versions
{% highlight sh %}
$ date
February  8, 2016 at 03:34:50 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ionadmin
: v
ION OPEN SOURCE 3.4.0
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

The **sysctl_script.sh** script needs to be patched to build IOT-DTN run on FreeBSD.
A number of other files also need to be patched work properly.
These scripts appear to be written for Linux and use **#!/bin/bash** instad of **#!/usr/bin/env bash**.
{% highlight sh %}
sed -i '' 's:#!/bin/bash:#!/usr/bin/env bash:' sysctl_script.sh
find ./ -type f -print0 | xargs -0 sed -i '' 's:#!/bin/bash:#!/usr/bin/env bash:'
{% endhighlight %}

Some of the shared memory values suggested by **sysctl_script.sh** are too low on FreeBSD.
Copy the following lines into **/boot/loader.conf**.
These values are read only tunable and must be set before the
system enters multi-user mode.
{% highlight sh %}
kern.ipc.shmmni=192
kern.ipc.shmseg=128
kern.ipc.semmns=32000
kern.ipc.semmni=128
{% endhighlight %}

Copy the following lines into your choice of  **/boot/loader.conf** or **/etc/sysctl.conf**.
These values are tunable in multi-user mode.
See the chapter in the [FreeBSD Handbook][freebsd-sysctl] for more information.
{% highlight sh %}
kern.ipc.shmmax=536870912
kern.ipc.shmmin=1
kern.ipc.shmall=131072
net.inet.udp.maxdgram=32000
kern.ipc.shm_use_phys=0
kern.ipc.shm_allow_removed=0
{% endhighlight %}

Note that the above tunable values can be changed by root at runtime.
{% highlight sh %}
su
sysctl kern.ipc.shmmax=536870912
{% endhighlight %}

Reboot the system so the new shared memory values will take effect.
{% highlight sh %}
su
shutdown -r now
{% endhighlight %}

Read **README.txt**.
Optionally run **./config -h**.
When you know what you are doing, configure and build.
Note that by default the man pages are installed in the wrong place on FreeBSD.

The installation needs to be done by root.
I also run the build as root because I ultimately
want root to be the owner of the installed files.
{% highlight sh %}
su
./configure --mandir=/usr/local/man
gmake
{% endhighlight %}

Test the build.
**gmake test** should work, but it is configured to test the original Bundle Security Protocol.
The depreciated bsp tests are skipped, so running **gmake test** is pointless.
Instead, Run the following command.
It tests the new not yet standardized Streamlined Bundle Security Protocol.
{% highlight sh %}
(cd tests/; ./runtests sbsp/)
{% endhighlight %}

If the tests pass, perform a system wide install as root.
{% highlight sh %}
gmake install
ldconfig
{% endhighlight %}

Serve **tutorial.html** and [open](http://localhost:8080/) it in your favorite browser.
Read through the tutorial.
{% highlight sh %}
FILE="tutorial.html"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
{% endhighlight %}

Also look at **ION Deployment Guide.pdf** and **ION.pdf**.
Note the **AMS programmer's guide v2.2.pdf** and the Windows related PDFs.
**man ion**.
{% highlight sh %}
FILE="ION Deployment Guide.pdf"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
FILE="ION.pdf"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
man ion
{% endhighlight %}

A number of configuration files are required to start ION.
Add the following lines to the specified files.
It is probably a good idea to move to a different directory first.

**host1.ionrc**
{% highlight sh %}
1 1 ''
s
a contact +1 +3600 1 1 100000
a range +1 +3600 1 1 1
m production 1000000
m consumption 1000000
{% endhighlight %}

**host1.ltprc**
{% highlight sh %}
1 32
a span 1 32 32 1400 10000 1 'udplso localhost:1113'
s 'udplsi localhost:1113'
{% endhighlight %}

**host1.bprc**
{% highlight sh %}
1
a scheme ipn 'ipnfw' 'ipnadminep'
a endpoint ipn:1.0 q
a endpoint ipn:1.1 q
a endpoint ipn:1.2 q
a protocol ltp 1400 100
a induct ltp 1 ltpcli
a outduct ltp 1 ltpclo
s
{% endhighlight %}

**host1.ipnrc**
{% highlight sh %}
a plan 1 ltp/1
{% endhighlight %}

**host1.ionsecrc** is not required, but it keeps "Can't find ION security database." from being logged in **ion.log**.
{% highlight sh %}
1
{% endhighlight %}

Create **host1.rc** with the following command.
{% highlight sh %}
ionscript -i host1.ionrc -p host1.ipnrc -l host1.ltprc -b host1.bprc -O host1.rc -s host1.ionsecrc
{% endhighlight %}

Start ION with either of the following commands.
{% highlight sh %}
ionstart -I host1.rc
ionstart -i host1.ionrc -l host1.ltprc -b host1.bprc -p host1.ipnrc -s host1.ionsecrc
{% endhighlight %}

ION can be stopped with the following command.
{% highlight sh %}
ionstop
{% endhighlight %}

## Hello World

Enter the follow lines into the terminal.
Hit ^C to exit **bpsink** after verifying the payload has been delivered.
{% highlight sh %}
echo "Hello, World!" | bpsource ipn:1.1
bpsink ipn:1.1
# ^C to exit bpsink
{% endhighlight %}

A slightly unreliable single line hello world example is below.
{% highlight sh %}
{ echo "Hello, World!"; sleep 1; } | bpchat ipn:1.1 ipn:1.1
{% endhighlight %}

## Chat

Use two terminals to enter the following commands.
Enter text and hit enter to transfer the line to the other terminal.
Hit ^C to exit.

{% highlight sh %}
# α terminal
bpchat ipn:1.1 ipn:1.2
# ^C to exit bpchat

# β terminal
bpchat ipn:1.2 ipn:1.1
# ^C to exit bpchat
{% endhighlight %}

## Echo

This modified chat example sets up an echo server.
The server echoes lines back to the client until it receives EOT on a single line.
EOT is piped into the connection after the client is closed with ^C.
The server closes automatically without any manual intervention.

{% highlight sh %}
# α terminal
mkfifo fifo
bpchat ipn:1.1 ipn:1.2 <fifo | sed -u -n "/^$(printf "\4")$/q; p" | tee fifo

# β terminal
bpchat ipn:1.2 ipn:1.1; printf "\4\n" | bpchat ipn:1.2 ipn:1.1
# ^C to exit bpchat
{% endhighlight %}

## Scripted Request-Response: Serving a Web Page Over BP

This is a crude example of using **bpsendfile** and **bprecvfile** to serve a web page over BP.
First, create **index.html**.
Alternatively, use **tutorial.html** or another file.
{% highlight html %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello World!</title>
  </head>
  <body>
    <p>Hello World!</p>
  </body>
</html>
{% endhighlight %}

Add the following to **server.sh**.
The request is written to **testfile1**.
It also moonlights as the file to be sent.
{% highlight sh %}
#/bin/sh

SOURCE=ipn:1.1
DESTINATION=ipn:1.2
SERVICE_CLASS=0.1
FILE=index.html
CONTENT_TYPE=text/html

while true; do
echo "<<<$((X=X+1))<<<"
bprecvfile $SOURCE 1
REQUEST=$(cat testfile1)
echo "$REQUEST"
# in a real server, do something with the request
echo ">>>${X}>>>"
BODY=$(cat $FILE)
RESPONSE=$(cat <<EOF
HTTP/1.0 200 OK
Content-Type: ${CONTENT_TYPE}
Content-Length: $((${#BODY}+1))
Connection: close

${BODY}
EOF
)
echo "$RESPONSE"
echo "$RESPONSE" > testfile1
bpsendfile $SOURCE $DESTINATION testfile1 $SERVICE_CLASS
done
{% endhighlight %}

Add the following to **request.sh**.
This script is much like **server.sh**, but without the loop.
{% highlight sh %}
#/bin/sh

SOURCE=ipn:1.2
DESTINATION=ipn:1.1
SERVICE_CLASS=0.1

echo "<<<$((X=X+1))<<<"
REQUEST=$(cat <<EOF
GET / HTTP/1.1
Host: www.host.com
Connection: close

EOF
)
echo "$REQUEST"
echo "$REQUEST" > testfile1
bpsendfile $SOURCE $DESTINATION testfile1 $SERVICE_CLASS
echo ">>>${X}>>>"
bprecvfile $SOURCE 1
RESPONSE=$(cat testfile1)
echo "$RESPONSE"
{% endhighlight %}

From different terminals, start the server and make a request.
Note that **request.sh** is run in the current shell so that the request number increases if the command is executed multiple times.
{% highlight sh %}
chmod +x server.sh request.sh

# α terminal
./server.sh

# β terminal
. ./request.sh
{% endhighlight %}

## Unresponsive ION

If ION becomes unresponsive, restart it.
This example abuses ION.
Enter the following in **badserver.sh**.

{% highlight sh %}
#/bin/sh

SOURCE=ipn:1.1
DESTINATION=ipn:1.2
FILE=index.html
CONTENT_TYPE=text/html

while true; do
BODY=$(cat $FILE)
RESPONSE=$(cat <<EOF
HTTP/1.0 200 OK
Content-Type: ${CONTENT_TYPE}
Content-Length: $((${#BODY}+1))
Connection: close

${BODY}
EOF
)
echo "---$((X=X+1))---"
echo "$RESPONSE" | bpchat $SOURCE $DESTINATION
done
{% endhighlight %}

Let **badserver.sh** run until the hello world example stops working.

{% highlight sh %}
# α terminal
chmod +x badserver.sh
./badserver.sh

# β terminal
echo "Hello, World!" | bpsource ipn:1.3
bpsink ipn:1.3
# ^C to exit bpsink
{% endhighlight %}

Receive the data sent from **badserver.sh**.
{% highlight sh %}
bpsink ipn:1.2
# ^C to exit bpsink
{% endhighlight %}

Hold ^C to kill the **badserver.sh** script.
Stopping ION may help **badserver.sh** die faster.
Restart ION and the hello world example should work agian.
{% highlight sh %}
ionstop
ionstart -I host1.rc
echo "Hello, World!" | bpsource ipn:1.3
bpsink ipn:1.3
# ^C to exit bpsink
{% endhighlight %}

## write failed, filesystem is full

Congratulations!
**ion.log** probably ate up all of your disk space.
Delete it.
{% highlight sh %}
rm ion.log
{% endhighlight %}

## References:
- [ION-DTN, SourceForge, ION-DTN][ion-dtn]
- [ION-DTN, SourceForge, Source Code Download][ion-dtn-download]
- [ION-DTN, SourceForge, Support][ion-dtn-support]
- [ION-DTN, Introduction to DTN][ion-dtn-intro]
- [ION-DTN, RFC 5050 Bundle Protocol Specification][ion-dtn-rfc5050]
- [ION-DTN, dtn-interest Mailing List Archives][ion-dtn-interest]
- [ION-DTN, Re: (dtn-interest) DTN2 manual or tutorials?][ion-dtn-interest-manuals]
- [ION-DTN, Web Archive, DTN Train - Berkeley Open House, October 15, 2004][ion-dtn-train]
- [ION-DTN, ion and dtn2 interoperability configuration][ion-dtn-config]
- [ION-DTN, NASA Astronaut Email - MS-RPC Over HTTP - ION-DTN Module Architecture][ion-dtn-nasa-email]
- [ION-DTN, GitHub ION 2.2.1][ion-dtn-github221]
- [ION-DTN, Interplanetary Overlay Network (ION) Design and Operation V1.12 PDF][ion-dtn-github221-pdf]
- [ION-DTN, Man ion][ion-dtn-man-ion]
- [ION-DTN, Man bp][ion-dtn-man-bp]
- [ION-DTN, Man bpsource][ion-dtn-man-bpsource]
- [ION-DTN, Man bpsink][ion-dtn-man-bpsink]
- [ION-DTN, Man bpchat][ion-dtn-man-bpchat]
- [ION-DTN, Man bpsendfile][ion-dtn-man-bpsendfile]
- [ION-DTN, Man bprecvfile][ion-dtn-man-bprecvfile]
- [ION-DTN, Man bptrace][ion-dtn-man-bptrace]
- [ION-DTN, Man ionsecadmin][ion-dtn-man-ionsecadmin]
- [ION-DTN, Man ionsecrc][ion-dtn-man-ionsecrc]
- [FreeBSD, freebsd server limits question][freebsd-limits]
- [FreeBSD, sysctl options loader.conf or sysctl.conf][freebsd-sysctl-options]
- [FreeBSD, man pages not installed correctly on FreeBSD][freebsd-bad-man]
- [FreeBSD Forums, sed not working with -i?][freebsd-sed]
- [FreeBSD Handbook, Tuning with sysctl(8)][freebsd-sysctl]
- [FreeBSD, Single Line Web Server With nc on FreeBSD][freebsd-singlefile-nc]
- [FreeBSD, Getting Started With tor Hidden Services on FreeBSD][freebsd-tor]
- [UNIX, How do I download from SourceForge with wget?][unix-download-sourceforge]
- [UNIX, Extract tar.gz File][unix-tar-gz]
- [UNIX, How to replace a path with another path in sed?][unix-sed]
- [UNIX, Awk/Sed: How to do a recursive find/replace of a string?][unix-sed-all]
- [UNIX, Is there a standard command-line tool for unix for piping to a socket?][unix-pipe]
- [UNIX, Empty the contents of a file][unix-empty-file]
- [UNIX, Single File Elixir Programs][unix-single-elixir]
- [UNIX, What, at the bare minimum, is required for an HTTP request?][unix-minimum-http]
- [UNIX, Pipe multiple commands to a single command with no EOF signal wait][unix-pipe-multiple]
- [UNIX, Netcat without -e? No Problem!][unix-netcat-no-e]
- [UNIX, Using netcat to build a simple TCP proxy in Linux][unix-netcat-tcp-proxy]
- [UNIX, TCP proxy with netcat][unix-tcp-proxy]
- [Wikipedia, Interplanetary Internet][wikipedia-interplanetary]
- [Wikipedia, InterPlaNet][wikipedia-ipn]
- [Wikipedia, Delay-tolerant networking][wikipedia-dtn]

[ion-dtn]: http://sourceforge.net/projects/ion-dtn/
[ion-dtn-download]: http://sourceforge.net/projects/ion-dtn/files/?source=navbar
[ion-dtn-support]: http://sourceforge.net/p/ion-dtn/mailman/ion-dtn-support/
[ion-dtn-intro]: http://dtnsetup.com
[ion-dtn-rfc5050]: https://tools.ietf.org/html/rfc5050
[ion-dtn-interest]: https://mailarchive.ietf.org/arch/search/?email_list=dtn-interest
[ion-dtn-interest-manuals]: http://www.ietf.org/mail-archive/web/dtn-interest/current/msg03336.html
[ion-dtn-train]: https://web.archive.org/web/20070217092916/http://www.melissaho.com/research/dtn/demo/index.php
[ion-dtn-config]: https://sites.google.com/site/dtnresgroup/home/dtn-bone/use-cases/ion-and-dtn2-interoperability
[ion-dtn-nasa-email]: https://www.topcoder.com/challenge-details/30043039/?type=develop
[ion-dtn-github221]: https://github.com/b/ION
[ion-dtn-github221-pdf]: https://github.com/b/ION/blob/master/ION.pdf
[ion-dtn-man-ion]: http://manpages.org/ion/3
[ion-dtn-man-bp]: http://manpages.org/bp/3
[ion-dtn-man-bpsource]: http://manpages.org/bpsource
[ion-dtn-man-bpsink]: http://manpages.org/bpsink
[ion-dtn-man-bpchat]: http://manpages.org/bpchat
[ion-dtn-man-bpsendfile]: http://manpages.org/bpsendfile
[ion-dtn-man-bprecvfile]: http://manpages.org/bprecvfile
[ion-dtn-man-bptrace]: http://manpages.org/bptrace
[ion-dtn-man-ionsecadmin]: http://manpages.org/ionsecadmin
[ion-dtn-man-ionsecrc]: http://manpages.org/ionsecrc/5
[unix-download-sourceforge]: http://unix.stackexchange.com/questions/86971/how-do-i-download-from-sourceforge-with-wget
[unix-tar-gz]: http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/
[unix-sed]: http://stackoverflow.com/questions/12061410/how-to-replace-a-path-with-another-path-in-sed
[unix-sed-all]: http://stackoverflow.com/questions/1583219/awk-sed-how-to-do-a-recursive-find-replace-of-a-string
[unix-pipe]: http://stackoverflow.com/questions/576750/is-there-a-standard-command-line-tool-for-unix-for-piping-to-a-socket
[unix-empty-file]: http://unix.stackexchange.com/questions/88808/empty-the-contents-of-a-file
[unix-minimum-http]: http://stackoverflow.com/questions/6686261/what-at-the-bare-minimum-is-required-for-an-http-request
[unix-pipe-multiple]: http://stackoverflow.com/questions/13195285/pipe-multiple-commands-to-a-single-command-with-no-eof-signal-wait
[unix-single-elixir]: https://sgeos.github.io/elixir/erlang/2016/01/08/single-file-elixir-programs.html
[unix-netcat-no-e]: https://pen-testing.sans.org/blog/2013/05/06/netcat-without-e-no-problem
[unix-netcat-tcp-proxy]: http://notes.tweakblogs.net/blog/7955/using-netcat-to-build-a-simple-tcp-proxy-in-linux.html
[unix-tcp-proxy]: http://www.noah.org/wiki/TCP_proxy_with_netcat
[freebsd-sysctl]: https://www.freebsd.org/doc/handbook/configtuning-sysctl.html
[freebsd-sysctl-options]: https://lists.freebsd.org/pipermail/freebsd-questions/2005-August/095010.html
[freebsd-limits]: https://lists.freebsd.org/pipermail/freebsd-questions/2012-January/236726.html
[freebsd-sed]: https://forums.freebsd.org/threads/sed-not-working-with-i.12235/
[freebsd-bad-man]: https://github.com/thoughtbot/rcm/issues/131
[freebsd-singlefile-nc]: https://sgeos.github.io/freebsd/nc/2016/02/06/single-line-web-server-with-nc-on-freebsd.html
[freebsd-tor]: https://sgeos.github.io/tor/freebsd/nc/curl/2016/02/06/getting-started-with-tor-hidden-services-on-freebsd.html
[wikipedia-interplanetary]: https://en.wikipedia.org/wiki/Interplanetary_Internet
[wikipedia-ipn]: https://en.wikipedia.org/wiki/InterPlaNet
[wikipedia-dtn]: https://en.wikipedia.org/wiki/Delay-tolerant_networking

