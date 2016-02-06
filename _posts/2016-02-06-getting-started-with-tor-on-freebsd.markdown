---
layout: post
title:  "Getting Started With tor on FreeBSD"
date:   2016-02-06 14:45:48 +0900
categories: tor freebsd nc curl
---
At times I have wanted to demo the development version of a server that is
running on my FreeBSD virtual machine.
This is not a problem if the person I want to show it to is withing walking
distance.
The net being what it is, sometimes the other party is halfway around the world.

I figured [**tor**][tor] would be a neat way to demo a server running on
my laptop.
This post covers serving content via **tor** on a FreeBSD machine.
This does not cover securing a hidden service because it is non-trivial and
that is not my use case.

## Software Versions
{% highlight sh %}
$ date
February  6, 2016 at 08:59:26 AM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ tor --version
Tor version 0.2.7.6.
$ curl --version
curl 7.47.0 (amd64-portbld-freebsd11.0) libcurl/7.47.0 OpenSSL/1.0.2e zlib/1.2.8
Protocols: dict file ftp ftps gopher http https imap imaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp 
Features: AsynchDNS IPv6 Largefile GSS-API Kerberos SPNEGO NTLM NTLM_WB SSL libz TLS-SRP UnixSockets 
{% endhighlight %}

## Instructions
First, install **security/tor**.
Consider enabling **TOR2WEB** if your service does not really need to be hidden.
{% highlight sh %}
portmaster security/tor
{% endhighlight %}

Serve content to a port on localhost.
For example, add the following to **server.sh** for a simple date server
that serves content to port 8080.
This is not a robust server, but it is good enough for configuration testing.
{% highlight sh %}
#/bin/sh

HOST=127.0.0.1
PORT=8080

while true; do
BODY=$(cat <<EOF
{
  "Date": "$(date)"
}
EOF
)
RESPONSE=$(cat <<EOF
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: $((${#BODY}+1))
Connection: close

${BODY}
EOF
)
echo "---$((X=X+1))---"
echo "$RESPONSE" | nc -N -l $HOST $PORT
done
{% endhighlight %}

If using the above, make the server script executable and run it.
{% highlight sh %}
chmod +x server.sh
./server.sh
{% endhighlight %}

Read the [tor configuration instructions][tor-config].
Open **/usr/local/etc/tor/torrc** (see [torrc instructions][tor-torrc]).
Add the following lines to the section titled
**This section is just for location-hidden services**
{% highlight sh %}
HiddenServiceDir /usr/home/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8080
{% endhighlight %}

The following commands can be used to test the above server.
{% highlight sh %}
curl -v 127.0.0.1:8080
# log request date on the server and send EOF
date | nc 127.0.0.1 8080
{% endhighlight %}

Enable **tor** in **/etc/rc.conf**
{% highlight sh %}
tor_enable="YES"
{% endhighlight %}

Start **tor**.
{% highlight sh %}
service tor start
{% endhighlight %}

Get the hostname for your hidden service with the following command.
Do not share the **private_key**, found in the same directory.
{% highlight sh %}
cat /usr/home/tor/hidden_service/hostname
{% endhighlight %}

The following command can be used to test the above **nc** server by supplying the tor proxy with -x and proxy protocol with -X.
The -w 1 specifies a timeout.
This is necessary because the **nc** server does not close the connection.
The -v flag gives verbose output.
{% highlight sh %}
nc -w 1 -v -X5 -x localhost:9050 "$(cat /usr/home/tor/hidden_service/hostname)" 80
{% endhighlight %}

Test your hidden service with **curl** by supplying the tor proxy with the -x option.
{% highlight sh %}
curl -x socks5h://127.0.0.1:9050 -v "http://$(cat /usr/home/tor/hidden_service/hostname)/"
{% endhighlight %}

You alo can test your hidden service with [Tor2web][tor-tor2web].
For example, if your hidden service has a hostname of ABCDEFGHIJKLMNOP.onion,
go to https://ABCDEFGHIJKLMNOP.onion.to to view it in a web browser.
The **nc** server listed above might be a little flakey because it expects the client to close the connection..
You may need to restart the script if the server stops responding.

Test the hidden service with Tor2web from the command line with the following command.
Note that Tor2web blocks the curl user agent, so the user agent is set to test instead.
{% highlight sh %}
curl -A test "https://$(cat /usr/home/tor/hidden_service/hostname).to"
{% endhighlight %}

To disable **tor** when you no longer need to use it, stop it with the **service** command.
{% highlight sh %}
service tor stop
{% endhighlight %}

Then disable it in **/etc/rc.conf**.
{% highlight sh %}
tor_enable="NO"
{% endhighlight %}

## References:
- [Tor Project][tor]
- [Tor, Tor2web][tor-tor2web]
- [Tor, Configuring Hidden Services for Tor][tor-config]
- [Tor, Edit torrc][tor-torrc]
- [Tor, HTTP connection closed on: Excess found in a non pipelined read][tor-curl]
- [Tor, StackOverflow, curl an .onion url over an http proxy does not return expected source][tor-curl-onion]
- [Tor, Using nc and ncat with tor without torify/torsocks][tor-nc]
- [FreeBSD, Man nc][man-nc]
- [FreeBSD, Man curl][man-curl]
- [Bash, How to assign a heredoc value to a variable in Bash?][bash-heredoc]
- [Bash, The while loop][bash-while]
- [Bash, Length of string in bash][bash-string-length]
- [Bash, Command Substitution][bash-command-sub]
- [FreeBSD Forums, nc Server Not Disconnecting][freebsd-forum-nc]
- [UNIX, Simple command line http server][unix-single-line-server]
- [UNIX, One command line web server on port 80 using nc (netcat)][unix-one-command-server]
- [UNIX, Faking Services using Netcat (For Testing Nagios)][unix-faking-services]
- [Wikipedia, Netcat][wikipedia-netcat]

[tor]:                     https://www.torproject.org/index.html.en
[tor-tor2web]:             https://tor2web.org
[tor-config]:              https://www.torproject.org/docs/tor-hidden-service.html.en
[tor-torrc]:               https://www.torproject.org/docs/faq.html.en#torrc
[tor-curl]:                https://github.com/curl/curl/issues/232
[tor-curl-onion]:          http://stackoverflow.com/questions/18146295/curl-an-onion-url-over-an-http-proxy-does-not-return-expected-source
[tor-nc]:                  http://vicendominguez.blogspot.com/2014/08/using-nc-and-ncat-with-tor-without.html
[man-nc]:                  https://www.freebsd.org/cgi/man.cgi?nc
[man-curl]:                https://www.freebsd.org/cgi/man.cgi?query=curl&manpath=SuSE+Linux/i386+11.3
[bash-heredoc]:            http://stackoverflow.com/questions/1167746/how-to-assign-a-heredoc-value-to-a-variable-in-bash
[bash-while]:              http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_02.html
[bash-string-length]:      http://stackoverflow.com/questions/17368067/length-of-string-in-bash
[bash-command-sub]:        http://www.tldp.org/LDP/abs/html/commandsub.html
[freebsd-forum-nc]:        https://forums.freebsd.org/threads/nc-server-not-disconnecting.55033/
[unix-faking-services]:    http://notes.rioastamal.net/2014/02/faking-services-using-netcat-for-nagios-testing.html
[unix-single-line-server]: http://unix.stackexchange.com/questions/32182/simple-command-line-http-server
[unix-one-command-server]: http://www.commandlinefu.com/commands/view/9164/one-command-line-web-server-on-port-80-using-nc-netcat
[wikipedia-netcat]:        https://en.wikipedia.org/wiki/Netcat#Setting_up_a_one-shot_webserver_on_port_8080_to_present_the_content_of_a_file

