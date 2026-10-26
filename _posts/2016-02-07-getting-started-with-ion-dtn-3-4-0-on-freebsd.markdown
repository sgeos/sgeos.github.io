---
layout: post
comments: true
title:  "Getting Started with ION-DTN 3.4.0 on FreeBSD"
date: 2016-02-07 18:34:50 +0000
categories: freebsd ion dtn
---

<!-- A12 -->
<script>console.log("A12");</script>

I was reading Wikipedia articles about things like the [interplanetary internet][wikipedia_interplanetary],
[InterPlaNet][wikipedia_ipn] and [delay-tolerant networking][wikipedia_dtn].
After writing a [post on serving web content with tor][freebsd_tor], I wanted to try to serve a web page over ION-DTN.
This post covers installing [ION-DTN][ion_dtn] 3.4.0 on FreeBSD.

After the installation instructions, there are a few usage examples, including a very crude scripted web server.
The original goal was to take an outside web request, send it over ION-DTN to a server on the other side and return the response.
That example deserves a separate post.

Special thanks to Scott C Burleigh for helping me work through some setup problems.

The following are follow ups to this post:

- [ION DTN as a Service on FreeBSD](https://sgeos.github.io/freebsd/ion/dtn/2016/02/15/ion-dtn-as-a-service-on-freebsd.html)
- [Almost Serving a Web Page with ION-DTN bpchat](https://sgeos.github.io/freebsd/ion/dtn/2016/02/12/almost-serving-a-web-page-with-ion-dtn-bpchat.html)
- [Serving a Web Page with ION-DTN bpsendfile and bprecvfile](https://sgeos.github.io/freebsd/ion/dtn/2016/02/17/serving-a-web-page-with-ion-dtn-bpsendfile-and-bprecvfile.html)

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
See the chapter in the [FreeBSD Handbook][freebsd_sysctl] for more information.
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

# System Wide Install

A system wide installation needs to be performed by root.
I also run the build as root because I ultimately
want root to be the owner of the installed files.
Note that by default the man pages are installed in the wrong place on FreeBSD.

{% highlight sh %}
su
./configure --mandir=/usr/local/man
gmake clean
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

# Single User Install

A single user install can be performed by passing the --prefix flag to **configure**.

{% highlight sh %}
./configure --prefix="$HOME/ion" --mandir="$HOME/ion/man"
gmake clean
gmake
(cd tests/; ./runtests sbsp/)
gmake install
{% endhighlight %}

Appended **ion/bin** to **PATH**.
If **ion/bin** is in **$PATH** then **manpath** will look for manpages in **ion/man**.

**~/.profile**
{% highlight sh %}
export "PATH=$HOME/ion/bin:$PATH"
{% endhighlight %}

The ion library path could be added to **LD_LIBRARY_PATH**, but running **ldconfig**
requires root privileges, so this does not make sense for a single user install.
See [this link][freebsd_ld_library_path] for details.

# Documentation

Serve **tutorial.html** and [open](http://localhost:8080/) it in your favorite browser.
Read through the tutorial.
{% highlight sh %}
FILE="tutorial.html"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
{% endhighlight %}

Also look at **ION Deployment Guide.pdf** and **ION.pdf**.
Note the **AMS programmer's guide v2.2.pdf** and the Windows related PDFs.
On a system wide install, there are a bunch of useful resources in **/usr/local/share/ion/**.
Finally, **man ion**.
{% highlight sh %}
FILE="ION Deployment Guide.pdf"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
FILE="ION.pdf"; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <"$FILE")\r\n\r\n"; cat "$FILE"; } | nc -N -l 0.0.0.0 8080
ls /usr/local/share/ion/
man ion
{% endhighlight %}

# Starting ION

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
ionscript -i host1.ionrc -s host1.ionsecrc -l host1.ltprc -b host1.bprc -p host1.ipnrc -O host1.rc
{% endhighlight %}

Start ION with either of the following commands.
{% highlight sh %}
ionstart -I host1.rc
ionstart -i host1.ionrc -s host1.ionsecrc -l host1.ltprc -b host1.bprc -p host1.ipnrc
{% endhighlight %}

ION can be stopped with the following command.
{% highlight sh %}
ionstop
{% endhighlight %}

## Examples

The following examples can be used to get started.

# Hello World

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

# Chat

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

# Echo Loop

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

# Scripted Request-Response: Serving a Web Page Over BP

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

If **ionstart** or **ionstop** hangs, run **killm** directly and restart ion.
{% highlight sh %}
killm
ionstart -I host1.rc
{% endhighlight %}

## write failed, filesystem is full

Congratulations!
**ion.log** probably ate up all of your disk space.
Delete it.
{% highlight sh %}
rm ion.log
{% endhighlight %}

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- "FreeBSD Handbook, Tuning with sysctl(8)." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/configtuning-sysctl.html][freebsd_sysctl]
- "FreeBSD, man manpath." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/cgi/man.cgi?query=manpath&apropos=0&sektion=0&manpath=FreeBSD+8.0-RELEASE&format=html][freebsd_man_manpath]
- "FreeBSD, man pages not installed correctly on FreeBSD." n.d. github.com. Accessed October 25, 2026. [https://github.com/thoughtbot/rcm/issues/131][freebsd_bad_man]
- ION-DTN, Web Archive. 2004. "DTN Train - Berkeley Open House." *October* 15. [https://web.archive.org/web/20070217092916/http://www.melissaho.com/research/dtn/demo/index.php][ion_dtn_train]
- "ION-DTN, GitHub ION 2.2.1." n.d. github.com. Accessed October 25, 2026. [https://github.com/b/ION][ion_dtn_github221]
- "ION-DTN, Interplanetary Overlay Network (ION) Design and Operation V1.12 PDF." n.d. github.com. Accessed October 25, 2026. [https://github.com/b/ION/blob/master/ION.pdf][ion_dtn_github221_pdf]
- "ION-DTN, Man bptrace." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bptrace][ion_dtn_man_bptrace]
- "Man Bp (3): Bundle Protocol Communications Library." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bp/3][ion_dtn_man_bp]
- "Man Bpchat (1): Bundle Protocol Chat Test Program." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bpchat][ion_dtn_man_bpchat]
- "Man Bprecvfile (1): Bundle Protocol (BP) File Reception Utility." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bprecvfile][ion_dtn_man_bprecvfile]
- "Man Bpsendfile (1): Bundle Protocol (BP) File Transmission Utility." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bpsendfile][ion_dtn_man_bpsendfile]
- "Man Bpsink (1): Bundle Protocol Reception Test Program." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bpsink][ion_dtn_man_bpsink]
- "Man Bpsource (1): Bundle Protocol Transmission Test Shell." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/bpsource][ion_dtn_man_bpsource]
- "Man Ion (3): Interplanetary Overlay Network Common Definitions and Functions." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/ion/3][ion_dtn_man_ion]
- "Man Ionsecadmin (1): ION Security Policy Administration Interface." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/ionsecadmin][ion_dtn_man_ionsecadmin]
- "Man Ionsecrc (5): ION Security Policy Management Commands File." n.d. manpages.org. Accessed October 25, 2026. [http://manpages.org/ionsecrc/5][ion_dtn_man_ionsecrc]

### General Sources

- "Bash: Awk/Sed: How to Do a Recursive Find/replace of a String?" n.d.-a. Accessed October 25, 2026. [http://stackoverflow.com/questions/1583219/awk-sed-how-to-do-a-recursive-find-replace-of-a-string][unix_sed_all]
- "Bash: Pipe Multiple Commands to a Single Command with No EOF Signal Wait." n.d.-b. Accessed October 25, 2026. [http://stackoverflow.com/questions/13195285/pipe-multiple-commands-to-a-single-command-with-no-eof-signal-wait][unix_pipe_multiple]
- "FreeBSD Forums, sed not working with -i?" n.d. Accessed October 25, 2026. [https://forums.freebsd.org/threads/sed-not-working-with-i.12235/][freebsd_sed]
- "FreeBSD, freebsd server limits question." n.d. Accessed October 25, 2026. [https://lists.freebsd.org/pipermail/freebsd-questions/2012-January/236726.html][freebsd_limits]
- "FreeBSD, LD\_LIBRARY\_PATH." n.d. Accessed October 25, 2026. [https://lists.freebsd.org/pipermail/freebsd-questions/2007-March/146062.html][freebsd_ld_library_path]
- "FreeBSD, On FreeBSD, what is the best practice for adding to manpath?" n.d. Accessed October 25, 2026. [https://www.reddit.com/r/freebsd/comments/3zxa3j/on\_freebsd\_what\_is\_the\_best\_practice\_for\_adding/][freebsd_manpath]
- "FreeBSD, sysctl options loader.conf or sysctl.conf." n.d. Accessed October 25, 2026. [https://lists.freebsd.org/pipermail/freebsd-questions/2005-August/095010.html][freebsd_sysctl_options]
- "How Do I Download from SourceForge with Wget?" n.d. Accessed October 25, 2026. [http://unix.stackexchange.com/questions/86971/how-do-i-download-from-sourceforge-with-wget][unix_download_sourceforge]
- "How to Replace a Path with Another Path in Sed?" n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/12061410/how-to-replace-a-path-with-another-path-in-sed][unix_sed]
- "ION-DTN, dtn-interest Mailing List Archives." n.d. Accessed October 25, 2026. [https://mailarchive.ietf.org/arch/search/?email\_list=dtn-interest][ion_dtn_interest]
- "ION-DTN, Introduction to DTN." n.d. Accessed October 25, 2026. [http://dtnsetup.com][ion_dtn_intro]
- "ION-DTN, ion and dtn2 interoperability configuration." n.d. Accessed October 25, 2026. [https://sites.google.com/site/dtnresgroup/home/dtn-bone/use-cases/ion-and-dtn2-interoperability][ion_dtn_config]
- "ION-DTN, NASA Astronaut Email - MS-RPC Over HTTP - ION-DTN Module Architecture." n.d. Accessed October 25, 2026. [https://www.topcoder.com/challenge-details/30043039/?type=develop][ion_dtn_nasa_email]
- "ION-DTN, Re: (dtn-interest) DTN2 manual or tutorials?" n.d. Accessed October 25, 2026. [http://www.ietf.org/mail-archive/web/dtn-interest/current/msg03336.html][ion_dtn_interest_manuals]
- "ION-DTN, RFC 5050 Bundle Protocol Specification." n.d. Accessed October 25, 2026. [https://tools.ietf.org/html/rfc5050][ion_dtn_rfc5050]
- "ION-DTN, SourceForge, ION-DTN." n.d. Accessed October 25, 2026. [http://sourceforge.net/projects/ion-dtn/][ion_dtn]
- "ION-DTN, SourceForge, Support." n.d. Accessed October 25, 2026. [http://sourceforge.net/p/ion-dtn/mailman/ion-dtn-support/][ion_dtn_support]
- "ION-DTN: Browse Files at SourceForge.net." n.d. Accessed October 25, 2026. [http://sourceforge.net/projects/ion-dtn/files/?source=navbar][ion_dtn_download]
- "Is There a Standard Command-Line Tool for Unix for Piping to a Socket?" n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/576750/is-there-a-standard-command-line-tool-for-unix-for-piping-to-a-socket][unix_pipe]
- "Make: Installing Glib in Non-Standard Prefix Fails." n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/10279829/installing-glib-in-non-standard-prefix-fails][unix_libtool_clean]
- "Shell Script: Empty the Contents of a File." n.d. Accessed October 25, 2026. [http://unix.stackexchange.com/questions/88808/empty-the-contents-of-a-file][unix_empty_file]
- "TCP Proxy with Netcat." n.d. Accessed October 25, 2026. [http://www.noah.org/wiki/TCP\_proxy\_with\_netcat][unix_tcp_proxy]
- "UNIX, Extract tar.gz File." n.d. Accessed October 25, 2026. [http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/][unix_tar_gz]
- "UNIX, Netcat without -e? No Problem!" n.d. Accessed October 25, 2026. [https://pen-testing.sans.org/blog/2013/05/06/netcat-without-e-no-problem][unix_netcat_no_e]
- "Using Netcat to Build a Simple TCP Proxy in Linux: Notes: Tweakblogs: Tweakers." n.d. Accessed October 25, 2026. [http://notes.tweakblogs.net/blog/7955/using-netcat-to-build-a-simple-tcp-proxy-in-linux.html][unix_netcat_tcp_proxy]
- "What, at the Bare Minimum, Is Required for an HTTP Request?" n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/6686261/what-at-the-bare-minimum-is-required-for-an-http-request][unix_minimum_http]

### Tertiary Sources

- "Delay-Tolerant Networking." 2026. Wikipedia. Last modified July 29, at 06:08 (UTC). [https://en.wikipedia.org/w/index.php?title=Delay-tolerant\_networking&oldid=1366639475][wikipedia_dtn]
- "InterPlaNet." 2025. Wikipedia. Last modified August 26, at 14:22 (UTC). [https://en.wikipedia.org/w/index.php?title=InterPlaNet&oldid=1307933632][wikipedia_ipn]
- "Interplanetary Internet." 2026. Wikipedia. Last modified March 8, at 20:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Interplanetary\_Internet&oldid=1342407596][wikipedia_interplanetary]

### Related Posts

- Sechter, Brendan. 2016. "Single File Elixir Programs." *Brendan A R Sechter's Development Blog*, January 12. [https://sgeos.github.io/elixir/erlang/2016/01/12/single-file-elixir-programs.html][unix_single_elixir]
- Sechter, Brendan. 2016. "Getting Started With tor Hidden Services on FreeBSD." *Brendan A R Sechter's Development Blog*, February 6. [https://sgeos.github.io/tor/freebsd/nc/curl/2016/02/06/getting-started-with-tor-hidden-services-on-freebsd.html][freebsd_tor]
- Sechter, Brendan. 2016. "Single Line Web Server With nc on FreeBSD." *Brendan A R Sechter's Development Blog*, February 9. [https://sgeos.github.io/freebsd/nc/2016/02/09/single-line-web-server-with-nc-on-freebsd.html][freebsd_singlefile_nc]

[freebsd_bad_man]: https://github.com/thoughtbot/rcm/issues/131
[freebsd_ld_library_path]: https://lists.freebsd.org/pipermail/freebsd-questions/2007-March/146062.html
[freebsd_limits]: https://lists.freebsd.org/pipermail/freebsd-questions/2012-January/236726.html
[freebsd_man_manpath]: https://www.freebsd.org/cgi/man.cgi?query=manpath&apropos=0&sektion=0&manpath=FreeBSD+8.0-RELEASE&format=html
[freebsd_manpath]: https://www.reddit.com/r/freebsd/comments/3zxa3j/on_freebsd_what_is_the_best_practice_for_adding/
[freebsd_sed]: https://forums.freebsd.org/threads/sed-not-working-with-i.12235/
[freebsd_singlefile_nc]: {% post_url 2016-02-09-single-line-web-server-with-nc-on-freebsd %}
[freebsd_sysctl]: https://www.freebsd.org/doc/handbook/configtuning-sysctl.html
[freebsd_sysctl_options]: https://lists.freebsd.org/pipermail/freebsd-questions/2005-August/095010.html
[freebsd_tor]: {% post_url 2016-02-06-getting-started-with-tor-hidden-services-on-freebsd %}
[ion_dtn]: http://sourceforge.net/projects/ion-dtn/
[ion_dtn_config]: https://sites.google.com/site/dtnresgroup/home/dtn-bone/use-cases/ion-and-dtn2-interoperability
[ion_dtn_download]: http://sourceforge.net/projects/ion-dtn/files/?source=navbar
[ion_dtn_github221]: https://github.com/b/ION
[ion_dtn_github221_pdf]: https://github.com/b/ION/blob/master/ION.pdf
[ion_dtn_interest]: https://mailarchive.ietf.org/arch/search/?email_list=dtn-interest
[ion_dtn_interest_manuals]: http://www.ietf.org/mail-archive/web/dtn-interest/current/msg03336.html
[ion_dtn_intro]: http://dtnsetup.com
[ion_dtn_man_bp]: http://manpages.org/bp/3
[ion_dtn_man_bpchat]: http://manpages.org/bpchat
[ion_dtn_man_bprecvfile]: http://manpages.org/bprecvfile
[ion_dtn_man_bpsendfile]: http://manpages.org/bpsendfile
[ion_dtn_man_bpsink]: http://manpages.org/bpsink
[ion_dtn_man_bpsource]: http://manpages.org/bpsource
[ion_dtn_man_bptrace]: http://manpages.org/bptrace
[ion_dtn_man_ion]: http://manpages.org/ion/3
[ion_dtn_man_ionsecadmin]: http://manpages.org/ionsecadmin
[ion_dtn_man_ionsecrc]: http://manpages.org/ionsecrc/5
[ion_dtn_nasa_email]: https://www.topcoder.com/challenge-details/30043039/?type=develop
[ion_dtn_rfc5050]: https://tools.ietf.org/html/rfc5050
[ion_dtn_support]: http://sourceforge.net/p/ion-dtn/mailman/ion-dtn-support/
[ion_dtn_train]: https://web.archive.org/web/20070217092916/http://www.melissaho.com/research/dtn/demo/index.php
[unix_download_sourceforge]: http://unix.stackexchange.com/questions/86971/how-do-i-download-from-sourceforge-with-wget
[unix_empty_file]: http://unix.stackexchange.com/questions/88808/empty-the-contents-of-a-file
[unix_libtool_clean]: http://stackoverflow.com/questions/10279829/installing-glib-in-non-standard-prefix-fails
[unix_minimum_http]: http://stackoverflow.com/questions/6686261/what-at-the-bare-minimum-is-required-for-an-http-request
[unix_netcat_no_e]: https://pen-testing.sans.org/blog/2013/05/06/netcat-without-e-no-problem
[unix_netcat_tcp_proxy]: http://notes.tweakblogs.net/blog/7955/using-netcat-to-build-a-simple-tcp-proxy-in-linux.html
[unix_pipe]: http://stackoverflow.com/questions/576750/is-there-a-standard-command-line-tool-for-unix-for-piping-to-a-socket
[unix_pipe_multiple]: http://stackoverflow.com/questions/13195285/pipe-multiple-commands-to-a-single-command-with-no-eof-signal-wait
[unix_sed]: http://stackoverflow.com/questions/12061410/how-to-replace-a-path-with-another-path-in-sed
[unix_sed_all]: http://stackoverflow.com/questions/1583219/awk-sed-how-to-do-a-recursive-find-replace-of-a-string
[unix_single_elixir]: {% post_url 2016-01-12-single-file-elixir-programs %}
[unix_tar_gz]: http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/
[unix_tcp_proxy]: http://www.noah.org/wiki/TCP_proxy_with_netcat
[wikipedia_dtn]: https://en.wikipedia.org/w/index.php?title=Delay-tolerant_networking&oldid=1366639475
[wikipedia_interplanetary]: https://en.wikipedia.org/w/index.php?title=Interplanetary_Internet&oldid=1342407596
[wikipedia_ipn]: https://en.wikipedia.org/w/index.php?title=InterPlaNet&oldid=1307933632
