---
layout: post
title:  "Single Line Web Server With nc on FreeBSD"
date:   2016-02-07 02:27:30 +0900
categories: freebsd nc
---
I wrote a single file web server in my last post about [Getting Started With tor Hidden Services on FreeBSD][freebsd-tor].
I figured it might be useful to have a couple of variations of simple web servers in their own post.
This post covers single line and single file web servers with **nc** on FreeBSD.
Content served from a static file or a script is presented.

## Software Versions
{% highlight sh %}
$ date
February  7, 2016 at 02:27:30 AM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions
First, add the following to **index.html** so we have a file to serve.
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

The [netcat Wikipedia page][wikipedia-netcat] lists a one-line one-shot web server.
It has been adapted for FreeBSD below.
{% highlight sh %}
FILE=index.html; { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <$FILE)\r\n\r\n"; cat $FILE; } | nc -N -l 127.0.0.1 8080
{% endhighlight %}

The server body can be put in a loop to serve the file multiple times.
The host and port definitions have been moved to the beginning of the line in the version below.
{% highlight sh %}
FILE=index.html; HOST=127.0.0.1; PORT=8080; while true; do { printf "HTTP/1.0 200 OK\r\nContent-Length: $(wc -c <$FILE)\r\n\r\n"; cat $FILE; } | nc -N -l $HOST $PORT ; done
{% endhighlight %}

The above line is complicated enough that it might want live in a file, like **server.sh**.
A content type definition has been moved to the beginning of the file.
A body and response have been defined.
A couple of useful headers have been added.
Finally, the response number is echoed before each response.
{% highlight sh %}
#/bin/sh

HOST=127.0.0.1
PORT=8080
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
echo "$RESPONSE" | nc -N -l $HOST $PORT
done
{% endhighlight %}

Make the server script executable before running it.
{% highlight sh %}
chmod +x server.sh
./server.sh
{% endhighlight %}

By redefining the body clause, the script can serve dynamic content.
A simple JSON date server is listed below.
{% highlight sh %}
#/bin/sh

HOST=127.0.0.1
PORT=8080
CONTENT_TYPE=application/json

while true; do
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
echo "---$((X=X+1))---"
echo "$RESPONSE" | nc -N -l $HOST $PORT
done
{% endhighlight %}

A one line version of the JSON date server is listed below.
{% highlight sh %}
HOST=127.0.0.1; PORT=8080; CONTENT_TYPE=application/json; while true; do BODY=$(printf "{\r\n  \"Date\": \"$(date)\"\r\n}\r\n");RESPONSE=$(printf "HTTP/1.0 200 OK\r\nContent-Type: ${CONTENT_TYPE}\r\nContent-Length: $((${#BODY}+1))\r\nConnection: close\r\n\r\n${BODY}"); echo "---$((X=X+1))---"; echo "$RESPONSE" | nc -N -l $HOST $PORT; done
{% endhighlight %}

A one line version of the single file web server is listed below.
{% highlight sh %}
HOST=127.0.0.1; PORT=8080; FILE=index.html; CONTENT_TYPE=text/html; while true; do BODY=$(cat $FILE);RESPONSE=$(printf "HTTP/1.0 200 OK\r\nContent-Type: ${CONTENT_TYPE}\r\nContent-Length: $((${#BODY}+1))\r\nConnection: close\r\n\r\n${BODY}"); echo "---$((X=X+1))---"; echo "$RESPONSE" | nc -N -l $HOST $PORT; done
{% endhighlight %}

Either of the following lines can be used to test the server from the command line.
**date** is piped into **nc** so the client will send EOF to the server.
The server will also log something to the terminal this way.
{% highlight sh %}
curl -v 127.0.0.1:8080
# log request date on the server and send EOF
date | nc 127.0.0.1 8080
{% endhighlight %}

Note that these servers are not necessarily robust.
They may trip up clients that do not close the connection.

## References:
- [Bash, How to assign a heredoc value to a variable in Bash?][bash-heredoc]
- [Bash, The while loop][bash-while]
- [Bash, Length of string in bash][bash-string-length]
- [Bash, Command Substitution][bash-command-sub]
- [FreeBSD, Man nc][man-nc]
- [FreeBSD Forums, nc Server Not Disconnecting][freebsd-forum-nc]
- [FreeBSD, Getting Started With tor Hidden Services on FreeBSD][freebsd-tor]
- [HTML, Coding An HTML 5 Layout From Scratch][html-template]
- [HTML, The Complete List of MIME Types][html-mime-types]
- [HTML, W3C Markup Validation Service][html-validator]
- [UNIX, Simple command line http server][unix-single-line-server]
- [UNIX, One command line web server on port 80 using nc (netcat)][unix-one-command-server]
- [UNIX, Faking Services using Netcat (For Testing Nagios)][unix-faking-services]
- [Wikipedia, Netcat: Setting up a one-shot webserver on port 8080 to present the content of a file][wikipedia-netcat]

[html-template]:           https://www.smashingmagazine.com/2009/08/designing-a-html-5-layout-from-scratch/
[html-mime-types]:         http://www.sitepoint.com/web-foundations/mime-types-complete-list/
[html-validator]:          https://validator.w3.org
[man-nc]:                  https://www.freebsd.org/cgi/man.cgi?nc
[freebsd-forum-nc]:        https://forums.freebsd.org/threads/nc-server-not-disconnecting.55033/
[freebsd-tor]:             https://sgeos.github.io/tor/freebsd/nc/curl/2016/02/06/getting-started-with-tor-hidden-services-on-freebsd.html
[bash-heredoc]:            http://stackoverflow.com/questions/1167746/how-to-assign-a-heredoc-value-to-a-variable-in-bash
[bash-while]:              http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_02.html
[bash-string-length]:      http://stackoverflow.com/questions/17368067/length-of-string-in-bash
[bash-command-sub]:        http://www.tldp.org/LDP/abs/html/commandsub.html
[unix-faking-services]:    http://notes.rioastamal.net/2014/02/faking-services-using-netcat-for-nagios-testing.html
[unix-single-line-server]: http://unix.stackexchange.com/questions/32182/simple-command-line-http-server
[unix-one-command-server]: http://www.commandlinefu.com/commands/view/9164/one-command-line-web-server-on-port-80-using-nc-netcat
[wikipedia-netcat]:        https://en.wikipedia.org/wiki/Netcat#Setting_up_a_one-shot_webserver_on_port_8080_to_present_the_content_of_a_file

