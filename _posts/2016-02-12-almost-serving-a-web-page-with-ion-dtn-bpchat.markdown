---
layout: post
title:  "Almost Serving a Web Page with ION-DTN bpchat"
date:   2016-02-12 09:41:21 +0900
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

Unidirectional communication is represented by a pair of nodes.
The first node is the source, the second node is the destination.

| Notation         | Meaning                                             |
|:----------------:|:--------------------------------------------------- |
| αβ               | client to reverse proxy connection                  |
| βγ               | reverse proxy to forward proxy connection           |
| γδ               | forward proxy to server connection                  |
| αδ               | client-server request path                          |
| δα               | client-server response path                         |
|                  |                                                     |

Bidirectional communication is represented by a group of three nodes.
Relevant communication starts at the first node,
passes through or to the second node and ultimately comes back to the third node.
The first and third letter are the same when describing normal bidirectional communication.
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
| βγ<sub>N</sub>   | N-th hop from β to γ, i.e. γ for N hops                            |
| γβ<sub>0</sub>   | zeroth hop from γ to β, i.e. γ                                     |
| γβ<sub>N-1</sub> | one hop from β coming from γ, for N hops                           |
| γβ<sub>N</sub>   | at β coming from γ for N hops, N implies the same return path      |
| γβ<sub>M-3</sub> | three hops from β coming from γ, M implies a different return path |
|                  |                                                                    |

Hardware and the application execution environment follow the same conventions, but use uppercase notation.

{% highlight txt %}
Α ⇄ Β ⇄ Γ ⇄ Δ
{% endhighlight %}

For example, Α is my MacBook, α is Safari, Δ is a virtual machine running on Α, and δ is a web server.
ΑΒ<sub>1</sub> is my wireless router and ΑΒ is simply a WiFi connection.
ΒΑ<sub>1</sub> and ΑΒ<sub>1</sub> happen to be the same device.
If αβ<sub>1</sub> fails, my firewall is misconfigured.
If ΑΒ<sub>1</sub> fails, one of my kids pulled the plug on the router.

Where the OS and firmware fall is context specific.
If building a router, a firmware bug would be an αβ<sub>1</sub> failure.
If simply using a router, a firmware bug is an ΑΒ<sub>1</sub> failure.

## Software Versions
{% highlight sh %}
$ date
February 12, 2016 at 09:41:21 AM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ionadmin
: v
ION OPEN SOURCE 3.4.0
{% endhighlight %}

## Instructions

My unelaborate hardware setup is as follows.
ΑΒ<sub>1</sub> is a WiFi router.

{% highlight txt %}
Α ⇄ Β ⇄ Γ ⇄ Δ
Α: OSX MacBook Pro
Β, Γ, Δ: FreeBSD VirtualBoxVM running on Α
ΑΒΑ: WiFi, VM uses bridged adapter
ΒΔΒ: virtualized connections (probably)
{% endhighlight %}

For this exercise, **host1.bprc** will need to define two endpoints if everything is running on one machine.
It may be useful to have a couple of extra endpoints for testing.

{% highlight sh %}
1
a scheme ipn 'ipnfw' 'ipnadminep'
a endpoint ipn:1.0 q
a endpoint ipn:1.1 q
a endpoint ipn:1.2 q
#a endpoint ipn:1.3 q
#a endpoint ipn:1.4 q
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

Named terminals may make it easier to follow along.
The following commands can be used to rename terminals.

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

Set up a webserver that serves on 127.0.0.1:4000.
If a web server is not handy, the following single file JSON/HTTP date server can be used.
It is a crude implementation that is probably less robust than ideal.

**date_server.sh**
{% highlight sh %}
#/bin/sh

NC_HOST=127.0.0.1
NC_PORT=4000

echo "I/O: nc -N -l $NC_HOST $NC_PORT"

while true; do
echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
CONTENT_TYPE=application/json
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
echo "$RESPONSE" | nc -N -l "$NC_HOST" "$NC_PORT" | sed 's/^/< /'
echo "$RESPONSE" | sed 's/^/> /'
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
The upshot is that βγβ needs to be an open connection over **bp**.

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
The proxy closes **bp** when eight EOT characters are found at the end of a line.
This was chosen because I am fairly certain it is a unicode safe solution.

The forward proxy also changes the host and connection request headers so
that the browser and web server will play better with the proxy setup.
This fix is HTTP specific and can be removed for other protocols.

**forward_proxy.sh**
{% highlight sh %}
#!/bin/sh

BP_SOURCE=ipn:1.2
BP_DESTINATION=ipn:1.1
NC_HOST=127.0.0.1
NC_PORT=4000

REQUEST=request.pipe
RESPONSE=response.pipe

EOT=$(printf "\4\4\4\4\4\4\4\4")

TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "$TMP_DIR"; exit' INT TERM QUIT EXIT
cd "$TMP_DIR"
mkfifo -m 600 "$RESPONSE" "$REQUEST"

echo "Path: $(pwd)"
echo "In:   bpchat $BP_SOURCE $BP_DESTINATION"
echo "Out:  nc -N $NC_HOST $NC_PORT"

while true; do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  bpchat "$BP_SOURCE" "$BP_DESTINATION" <"$RESPONSE" |
  sed -u -n "/${EOT}$/q; p" |
  sed -u "s/^Host:.*/Host: ${NC_HOST}:${NC_PORT}/I" | # HTML Request Patch
  sed -u "s/^Connection:.*/Connection: close/I" | # HTML Request Patch
  tee "$REQUEST" | sed 's/^/< /' &
  nc -N "$NC_HOST" "$NC_PORT" <"$REQUEST" |
  tee "$RESPONSE" | sed 's/^/> /'
done
{% endhighlight %}

Create **request.txt** for testing.
Note that a double newline is required at the end of this file.

{% highlight html %}
GET / HTTP/1.1
Host: 127.0.0.1:4000
User-Agent: test-agent
Accept: */*
Connection: close
{% endhighlight %}

Run and test the forward proxy.
**date_server.sh** will probably send multiple responses.
A real web server plays better with the proxy setup.

{% highlight sh %}
# γ terminal
chmod +x forward_proxy.sh
./forward_proxy.sh

# β terminal
{ printf "$(cat request.txt)\4\4\4\4\4\4\4\4\n"; sleep 10; } |
bpchat ipn:1.1 ipn:1.2
{% endhighlight %}

# β Reverse Proxy

**The reverse proxy described in this section crashes bp when the second request begins.**
The reverse proxy is the last piece of the puzzle.

{% highlight txt %}
α ⇄ β ⇄ γ ⇄ δ
α: web browser
β: reverse proxy
γ: forward proxy
δ: web server
αβα: nc tcp/ip
βγβ: bpchat ltp/bp
γδγ: nc tcp/ip
{% endhighlight %}

The reverse proxy is a mirror of the forward proxy.
**nc** listens for connections and sends data through **bpchat**.
The host is 0.0.0.0 because the reverse proxy serves the outside world.
Note that the forward and reverse proxies need to use different ports if they are actually running on the same machine.

The reverse proxy does not need to modify the request or response stream.
Modifications are handled by the forward proxy.

**reverse_proxy.sh**
{% highlight sh %}
#/bin/sh

BP_SOURCE=ipn:1.1
BP_DESTINATION=ipn:1.2
NC_HOST=0.0.0.0
NC_PORT=8080

REQUEST=request.pipe
RESPONSE=response.pipe

EOT=$(printf "\4\4\4\4\4\4\4\4")

TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "$TMP_DIR"; exit' INT TERM QUIT EXIT
cd "$TMP_DIR"
mkfifo -m 600 "$RESPONSE" "$REQUEST"

echo "Path: $(pwd)"
echo "In:   nc -N -l $NC_HOST $NC_PORT"
echo "Out:  bpchat $BP_SOURCE $BP_DESTINATION"

while true; do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  { nc -N -l "$NC_HOST" "$NC_PORT" <"$RESPONSE"; printf "${EOT}\n"; } |
  tee "$REQUEST" | sed "s/^/< /; s/${EOT}/[EOT]/" &
  bpchat "$BP_SOURCE" "$BP_DESTINATION" <"$REQUEST" |
  tee "$RESPONSE" | sed 's/^/> /'
done
{% endhighlight %}

Test from the terminal.

{% highlight sh %}
# β terminal
chmod +x reverse_proxy.sh
./reverse_proxy.sh

# α terminal
CURL_HOST=192.168.0.23
curl -v ${CURL_HOST}:8080
{% endhighlight %}

# α Web Browser

Finally, test from a web browser.
Hopefully everything works.

**date_server.sh** does not overload bp and plays well with a standard browser.
It is more of a hack than a real web server so multiple responses are sent through the proxy layer.
A web browser will ignore the extra data.

In theory using should work better than **date_server.sh**.
The HTML document is served without issue.
**Due to a bug in reverse_proxy.sh the second request, a CSS file in my case, will cause bp to hang.**
This exercise has been posted as is for now because reproducable crashes are valuable.

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
- [UNIX, Can sed remove 'double' newline characters?][unix-sed-newline]
- [UNIX, Case-insensitive search & replace with sed][unix-sed-case-insensitive]
- [UNIX, How to replace whole line with sed?][unix-sed-whole-line]
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
[unix-sed-newline]: http://unix.stackexchange.com/questions/76061/can-sed-remove-double-newline-characters
[unix-sed-case-insensitive]: http://stackoverflow.com/questions/4412945/case-insensitive-search-replace-with-sed
[unix-sed-whole-line]: http://stackoverflow.com/questions/8822097/how-to-replace-whole-line-with-sed
[unix-case-insensitive]: http://stackoverflow.com/questions/4412945/case-insensitive-search-replace-with-sed
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

