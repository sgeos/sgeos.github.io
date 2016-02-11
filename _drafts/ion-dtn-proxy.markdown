---
layout: post
title:  "ION-DTN Proxy"
date:   2016-02-10 09:33:35 +0900
categories: freebsd ion dtn
---
The goal is to serve a web page using an architecture like this.
{% highlight txt %}
client ⇄(tcp/ip)⇄ reverse proxy ⇄(ltp/bp)⇄ proxy ⇄(tcp/ip)⇄ server
{% endhighlight %}

In this post, a symbolic notation will be used to describe network connections at a single point in time.
The software nodes in the above diagram will be represented by lowercase greek letters.
{% highlight txt %}
α ⇄ β ⇄ γ ⇄ δ
{% endhighlight %}

| Notation         | Meaning                                             |
|:----------------:|:--------------------------------------------------- |
| α                | client software                                     |
| β                | clientside reverse proxy                            |
| γ                | serverside forward proxy                            |
| δ                | server software                                     |
|                  |                                                     |

The connections will be represented by a pair of greek letters.
The first letter is the source, the second letter is the destination.
The following are unidirectional connections.

| Notation         | Meaning                                             |
|:----------------:|:--------------------------------------------------- |
| αβ               | client to reverseproxy connection                   |
| βγ               | reverse to forward proxy connection                 |
| γδ               | forward proxy to server connection                  |
| αδ               | client-server request path                          |
| δα               | client-server response path                         |
|                  |                                                     |

A bidirectional request-response path is written with three letters.
The first letter is the request sender.
The second letter is the inflection point- the request recipient and response sender.
The third letter is the response recipient.
The first and third letter are the same when describing a normal request-response path.
They can differ when leaving off part of the path in one direction.

| Notation         | Meaning                                                            |
|:----------------:|:------------------------------------------------------------------ |
| αδα              | client-server request-response path                                |
| βγβ              | proxy request-response path                                        |
| γδα              | path from foward proxy to server and back to client                |
|                  |                                                                    |

Intermediate hops can be represented with a subscript.
If the request and response take the same N hop path βγ<sub>i</sub> and γβ<sub>N-i</sub> are the same machine.
The request and response need not take the same path.
The number of hops need not be the same in both directions.

| Notation         | Meaning                                                            |
|:----------------:|:------------------------------------------------------------------ |
| βγ<sub>0</sub>   | zeroth hop from β to γ, i.e. β                                     |
| βγ<sub>1</sub>   | first hop from β to γ                                              |
| βγ<sub>N</sub>   | n-th hop from β to γ, i.e. γ for N hops                            |
| γβ<sub>0</sub>   | zeroth hop from γ to β, i.e. γ                                     |
| γβ<sub>N-1</sub> | one hop from β coming from γ, for N hops                           |
| γβ<sub>N</sub>   | at β coming from γ for N hops, N implies the same return path      |
| γβ<sub>M-3</sub> | three hops from β coming from γ, M implies a different return path |
|                  |                                                                    |

Hardware and the application execution environment follow the same conventions, but use uppercase notation.

{% highlight txt %}
Α ⇄ Β ⇄ Γ ⇄ Δ
{% endhighlight %}

For example, Α is my MacBook, α is Safari, Δ is a virtual machine running on Α and δ is a webserver.
ΑΒ<sub>1</sub> is my wireless router and ΑΒ is simply a WiFi connection.
ΒΑ<sub>1</sub> and ΑΒ<sub>1</sub> happen to be the same device.
If αβ<sub>1</sub> fails, my firewall is misconfigured.
If ΑΒ<sub>1</sub> fails, one of my kids pulled the plug on the router.

Where the OS and firmware fall is context specific.
If you are building a router, a firmware bug would be an αβ<sub>1</sub> failure.
If you are simply using a router, a firmware bug is an ΑΒ<sub>1</sub> failure.

## Software Versions
{% highlight sh %}
$ date
February 10, 2016 at 09:33:35 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ionadmin
: v
ION OPEN SOURCE 3.4.0
{% endhighlight %}

## Instructions

My hardware setup is as follows.  This is not a very elaborate setup.

{% highlight txt %}
Α ⇄ Β ⇄ Γ ⇄ Δ
Α: OSX Macbook Pro
Β, Γ, Δ: FreeBSD VirtualBoxVM running on Α
ΑΒΑ: WiFi, VM uses bridged adapter
ΒΔΒ: virtualized connections (probably)
{% endhighlight %}

For this exercise, **host1.bprc** will need to define two endpoints if everything is running on one machine.
You might want a couple of extra endpoints to run hello world or transfer tests.

{% highlight sh %}
1
a scheme ipn 'ipnfw' 'ipnadminep'
a endpoint ipn:1.0 q
a endpoint ipn:1.1 q
a endpoint ipn:1.2 q
a endpoint ipn:1.3 q
a endpoint ipn:1.4 q
a protocol ltp 1400 100
a induct ltp 1 ltpcli
a outduct ltp 1 ltpclo
s
{% endhighlight %}

Make sure to (re)start ion.

{% highlight sh %}
ionscript -i host1.ionrc -p host1.ipnrc -l host1.ltprc -b host1.bprc -O host1.rc -s host1.ionsecrc
ionstop
ionstart -I host1.rc
{% endhighlight %}

Using the following commands to change the title of your terminals may make it easier to follow along.
{% highlight sh %}
# ionadmin terminal
(TITLE="ionadmin"; printf "\033]0;${TITLE}\007")

# α terminal
(TITLE="α"; printf "\033]0;${TITLE}\007")

# β terminal
(TITLE="β"; printf "\033]0;${TITLE}\007")

# γ terminal
(TITLE="γ"; printf "\033]0;${TITLE}\007")

# δ terminal
(TITLE="δ"; printf "\033]0;${TITLE}\007")
{% endhighlight %}

# δ Web Server

Set up a webserver that serves on 127.0.0.1:8080.
The following single file JSON/HTTP date server can be used.
It is a crude implementation that is probably less robust than ideal.

**date_server.sh**
{% highlight sh %}
#/bin/sh

HOST=127.0.0.1
PORT=8080
CONTENT_TYPE=application/json

while true; do
echo "<<<$((X=X+1))<<<"
BODY=$(cat <<EOF
{
  "Date": "$(date)"
}
EOF
)
RESPONSE=$(cat <<EOF
HTTP/1.0 200 OK
Content-Type: ${CONTENT_TYPE}
Content-Length: $((${#BODY}+1))
Connection: close

${BODY}
EOF
)
echo "$RESPONSE" | nc -N -l $HOST $PORT
echo ">>>${X}>>>"
echo "$RESPONSE"
done
{% endhighlight %}

Run and test the server.
{% highlight sh %}
# δ terminal
chmod +x date_server.sh
./date_server.sh

# γ terminal
curl -v 127.0.0.1:8080
{% endhighlight %}

# βγβ Communication Problems

The problem with something like HTTP is that αδ basically needs to be held open until α gets a response.
The best case scenerio closes connections as the response travels back.
The upshot is that βγβ needs to be an open connection over bp.

{% highlight txt %}
α ⇄ β ⇄ γ ⇄ δ
αδ: request path
δα: response path
αδα: HTTP
βγβ: ltp/bp
{% endhighlight %}

A fifo can not be used to hold an open connection with **bpsendfile** and **bprecvfile**.
{% highlight sh %}
$ mkfifo fifo
$ echo "request text" >fifo & bpsendfile ipn:1.1 ipn:1.2 fifo
Stopping bpsendfile.
[1]   Broken pipe             echo request >fifo
$ tail -3 ion.log
[2016/02/11-07:51:20] at line 2107 of ici/library/ion.c, Assertion failed. (length > 0)
[2016/02/11-07:51:20] [?] No stack trace available on this platform.
[2016/02/11-07:51:20] at line 83 of bp/utils/bpsendfile.c, bpsendfile can't create ZCO.
{% endhighlight %}

**bpchat** can be used, by adding a mechanism to send EOF to γ when αβ is closed.
The basic mechanism looks like this.
{% highlight sh %}
# γ terminal
mkfifo fifo
bpchat ipn:1.2 ipn:1.1 <fifo | sed -u -n "/$(printf "\4")$/q; p" | tee fifo

# β terminal
bpchat ipn:1.1 ipn:1.2; printf "\4\n" | bpchat ipn:1.1 ipn:1.2
{% endhighlight %}

# γ Forward Proxy

The goal is to build this forward proxy.

{% highlight txt %}
β ⇄ γ ⇄ δ
β: reverse proxy
γ: forward proxy
δ: web server
βγβ: bpchat ltp/bp
γδγ: nc tcp/ip
{% endhighlight %}

The serverside proxy communicates over ltp/bp with **bpchat** and connects to the webserver with **nc**.

**forward_proxy.sh**
{% highlight sh %}
#/bin/sh

BP_SOURCE=ipn:1.2
BP_DESTINATION=ipn:1.1
NC_HOST=127.0.0.1
NC_PORT=8080

REQUEST=request.pipe
RESPONSE=response.pipe

EOT=$(printf "\4\4\4\4\4\4\4\4")

TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "$TMP_DIR"; exit' INT TERM QUIT EXIT
cd "$TMP_DIR"
mkfifo -m 600 "$RESPONSE" "$REQUEST"
pwd

while true; do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  bpchat "$BP_SOURCE" "$BP_DESTINATION" <"$RESPONSE" |
  sed -u -n "/${EOT}$/q; p" |
  tee "$REQUEST" | sed 's/^/< /' &
  nc -N "$NC_HOST" "$NC_PORT" <"$REQUEST" |
  tee "$RESPONSE" | sed 's/^/> /'
done
{% endhighlight %}

Run and test the forward proxy.

{% highlight sh %}
# γ terminal
chmod +x forward_proxy.sh
./forward_proxy.sh

# β terminal
bpchat ipn:1.1 ipn:1.2; { printf "\4\4\4\4\4\4\4\4\n"; sleep 2; } | bpchat ipn:1.1 ipn:1.2
{% endhighlight %}

# β Reverse Proxy

Setup.

{% highlight txt %}
α ⇄ β ⇄ γ ⇄ δ
α: web browser
β: 
γ: response proxy connect
δ:
αβα: complete request-response connection
αβ: client to proxy connection
βγ: request proxy connect
γβ: response proxy connect
αβα: complete request-response connection
{% endhighlight %}

Connections.

{% highlight txt %}
αβ: client to proxy connection
βγ: request proxy connect
γβ: response proxy connect
αβα: complete request-response connection
{% endhighlight %}

## References:
- [ION, Bundle Protocol][ion-bp]
- [ION, ion-dtn-support Mailing List Archives][ion-dtn-support]
- [ION, Getting Started with ION-DTN 3.4.0 on FreeBSD][ion-getting-started]
- [FreeBSD Handbook, Bridging][freebsd-bridging]
- [FreeBSD Single Line Web Server With nc on FreeBSD][freebsd-singleline]
- [UNIX, Netcat - network connections made easy][unix-netcat-easy]
- [UNIX, Using netcat to build a simple TCP proxy in Linux][unix-netcat-proxy]
- [UNIX, Bourne Shell Scripting/Debugging and signal handling][unix-sh]
- [UNIX, Sh - the Bourne Shell][unix-bourne-shell]
- [UNIX, How can I trap interrupts in my shell script?][unix-trap]
- [UNIX, in bash does control-c = SIGINT or SIGTERM?][unix-sigint]
- [UNIX, Sed and UTF-8 encoding][unix-sed-utf8]
- [UNIX, In Unix, how can I display the last lines of a file?][unix-last-lines]
- [UNIX, FIFO Operations][unix-fifo]
- [UNIX, Trouble with piping through sed][unix-sed-unbuffered]
- [UNIX, how can I get sed to quit after the first matching address range?][unix-sed-match-quit]
- [UNIX, Linux: Block until a string is matched in a file (“tail + grep with blocking”)][unix-match-block]
- [UNIX, sed Find and Replace ASCII Control Codes / Nonprintable Characters][unix-sed-control]
- [UNIX, change terminal title][unix-terminal-title]
- [UNIX, ASCII Table and Description][unix-ascii]
- [Networking, StackOverflow, what is the difference between proxy server and normal server?][networking-proxy1]
- [Networking, StackOverflow, Difference between proxy server and reverse proxy server][networking-proxy2]
- [Jekyll, Writing posts][jekyll-posts]
- [Jekyll, superscript in markdown (Github flavored)?][jekyll-subscript1]
- [Jekyll, Why there is no syntax for subscript and supscript?][jekyll-subscript2]
- [Wikipedia, UTF-8][wikipedia-utf8]
- [Wikipedia, Greek alphabet][wikipedia-greek]
- [Wikipedia, End-of-Transmission character][wikipedia-eot]
- [Wikipedia, Escape sequences in C][wikipedia-escape-c]

[ion-bp]: http://bundleprotocol.com
[ion-dtn-support]: https://sourceforge.net/p/ion-dtn/mailman/ion-dtn-support/
[ion-getting-started]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/07/getting-started-with-ion-dtn-3-4-0-on-freebsd.html
[freebsd-bridging]: https://www.freebsd.org/doc/handbook/network-bridging.html
[freebsd-singleline]: https://sgeos.github.io/freebsd/nc/2016/02/06/single-line-web-server-with-nc-on-freebsd.html
[unix-sh]: https://en.wikibooks.org/wiki/Bourne_Shell_Scripting/Debugging_and_signal_handling
[unix-bourne-shell]: http://www.grymoire.com/Unix/Sh.html
[unix-trap]: http://kb.mit.edu/confluence/pages/viewpage.action?pageId=3907156
[unix-sigint]: http://www.linuxquestions.org/questions/linux-general-1/in-bash-does-control-c-%3D-sigint-or-sigterm-443130/
[unix-netcat-easy]: http://www.stearns.org/doc/nc-intro.current.html
[unix-netcat-proxy]: http://notes.tweakblogs.net/blog/7955/using-netcat-to-build-a-simple-tcp-proxy-in-linux.html
[unix-sed-utf8]: http://stackoverflow.com/questions/27072558/sed-and-utf-8-encoding
[unix-last-lines]: https://kb.iu.edu/d/acrj
[unix-fifo]: http://www.tldp.org/LDP/lpg/node18.html
[unix-sed-unbuffered]: http://stackoverflow.com/questions/2427338/trouble-with-piping-through-sed
[unix-sed-match-quit]: http://stackoverflow.com/questions/20943025/how-can-i-get-sed-to-quit-after-the-first-matching-address-range
[unix-match-block]: http://stackoverflow.com/questions/6454915/linux-block-until-a-string-is-matched-in-a-file-tail-grep-with-blocking
[unix-sed-control]: http://www.cyberciti.biz/faq/unix-linux-sed-ascii-control-codes-nonprintable/
[unix-terminal-title]: http://unix.stackexchange.com/questions/11223/change-terminal-title
[unix-ascii]: http://www.asciitable.com
[networking-proxy1]: http://stackoverflow.com/questions/12702885/what-is-the-difference-between-proxy-server-and-normal-server
[networking-proxy2]: http://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server
[jekyll-posts]: http://jekyllrb.com/docs/posts/
[jekyll-subscript1]: http://stackoverflow.com/questions/15155778/superscript-in-markdown-github-flavored
[jekyll-subscript2]: http://talk.commonmark.org/t/why-there-is-no-syntax-for-subscript-and-supscript/586
[wikipedia-utf8]: https://en.wikipedia.org/wiki/UTF-8
[wikipedia-greek]: https://en.wikipedia.org/wiki/Greek_alphabet
[wikipedia-eot]: https://en.wikipedia.org/wiki/End-of-Transmission_character
[wikipedia-escape-c]: https://en.wikipedia.org/wiki/Escape_sequences_in_C

