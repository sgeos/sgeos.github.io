---
layout: post
comments: true
title:  "Serving a Web Page with ION-DTN bpsendfile and bprecvfile"
date:   2016-02-18 07:12:10 +0900
categories: freebsd ion dtn
---
This post is a follow up to [Almost Serving a Web Page with ION-DTN bpchat][ion-almost].
The **bpchat** proxies were rewritten with **bpsendfile** and **bprecvfile**.
This strategy will only work for protocols with a request response exchange.

This post covers a proxy model for serving HTTP over ION-DTN.
The scripts are an imperfect proof of concept.
The proxies were only designed with GET requests in mind.
Other HTTP verbs may work, but POST and PUT will almost certainly fail.

The proxy scripts have a mechanism to simulate transmission delay.

## Software Versions
{% highlight sh %}
$ date
February 18, 2016 at 07:12:10 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ionadmin
: v
ION OPEN SOURCE 3.4.0
{% endhighlight %}

## Instructions

The proxy model looks like this.
See the [previous post][ion-almost] for a description of the symbolic notation used.

{% highlight sh %}
α ⇄ β ⇄ γ ⇄ δ
α:   web browser
β:   reverse proxy
γ:   forward proxy
δ:   web server
αδ:  HTTP request
δα:  HTTP response
αβα: browser ⇄ proxy (nc tcp/ip)
βγβ: proxy ⇄ proxy (bpsendfile/bprecvfile bp/ltp)
γδγ: proxy ⇄ server (nc tcp/ip)
{% endhighlight %}

# Simulated Transmission Delay

Both proxies rely on the same script to simulate transmission delay.
This script encapsulates delay functionality and defines delay time in one place.
The delay time is one way trip time in seconds.
Set delay to 0 to disable simulated delay.

**delay.sh**
{% highlight sh %}
#!/bin/sh

DELAY=15

timer_display ()
{
  DISPLAY_D=$(($1/86400))
  DISPLAY_H=$((($1%86400)/3600))
  DISPLAY_M=$((($1%3600)/60))
  DISPLAY_S=$(($1%60))
  printf "%02dd %02dh %02dm %02ds" $DISPLAY_D $DISPLAY_H $DISPLAY_M $DISPLAY_S
}

delay_display ()
{
  DISPLAY_TIMER=$1
  DISPLAY_TOKEN=$2
  echo -n ' '
  while expr 0 '<' "${DISPLAY_TIMER}" >/dev/null
  do
    DISPLAY_TIMER=$(expr "${DISPLAY_TIMER}" '-' 1)
    sleep 1
    echo -n "${DISPLAY_TOKEN}"
  done
  echo ''
}

delay ()
{
  DELAY_TIMER="${DELAY}"
  DELAY_TOKEN=$1
  DELAY_TOKEN=${DELAY_TOKEN:='.'}
  while expr 0 '<' "${DELAY_TIMER}" >/dev/null
  do
    timer_display "${DELAY_TIMER}"
    if expr 60 '<' "${DELAY_TIMER}" >/dev/null
    then
      DELAY_TIMER=$(expr "${DELAY_TIMER}" '-' 60)
      delay_display 60 "${DELAY_TOKEN}"
    elif expr 10 '<' "${DELAY_TIMER}" >/dev/null
    then
      DELAY_TIMER=$(expr "${DELAY_TIMER}" '-' 10)
      delay_display 10 "${DELAY_TOKEN}"
    else
      DELAY_TIMER=$(expr "${DELAY_TIMER}" '-' 1)
      delay_display 1 "${DELAY_TOKEN}"
    fi
  done
}
{% endhighlight %}

The following script can be used to test the delay simulation.

**test_delay.sh**
{% highlight sh %}
#!/bin/sh

. delay.sh

echo "[ SEND ]"
delay ">"
echo "[ RECEIVE ]"
delay "<"
{% endhighlight %}

The following commands can be used to run the test delay script.

{% highlight sh %}
chmod +x delay.sh test_delay.sh
./test_delay.sh
{% endhighlight %}

# δ Web Server

Start a web server on 0.0.0.0:4000 or use the following single file JSON/HTTP date server.

**date_server.sh**
{% highlight sh %}
#!/bin/sh

HOST=0.0.0.0
PORT=4000

REQUEST=request
RESPONSE=response.pipe

TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "${TMP_DIR}"; exit' INT TERM QUIT EXIT
cd "${TMP_DIR}"
touch "${REQUEST}"
mkfifo -m 600 "${RESPONSE}"

echo "Path:   $(pwd)"
echo "Server: nc -N -l ${HOST} ${PORT}"

response()
{
CONTENT_TYPE=application/json
BODY=$(cat <<EOF
{
  "Date": "$(date)"
}
EOF
)
DOCUMENT=$(cat <<EOF
HTTP/1.0 200 OK
Content-Type: ${CONTENT_TYPE}
Content-Length: $((${#BODY}+1))
Connection: close

${BODY}
EOF
)
echo "${DOCUMENT}"
}

while true
do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  cat "${RESPONSE}" | nc -N -l "${HOST}" "${PORT}" |
  (
    echo -n "" >"${REQUEST}"
    while read LINE
    do
      echo "${LINE}" >>"${REQUEST}"
      LINE=$(echo "${LINE}" | tr -d '[\r\n]')
      if [ "x${LINE}" = "x" ]
      then
        cat "${REQUEST}" | sed -u 's/^/< /';
        response | tee "${RESPONSE}" | sed -u 's/^/> /';
        break
      fi
    done
  )
done
{% endhighlight %}

# γ Forward Proxy

The forward proxy looks like this.
Note that it patches the request header host field to match the host and port **nc** uses to connect.
The connection header is patched so that the browser will close the connection.
The scripts are not very smart.
They blindly hold ports open and expect files to be sent and received in the correct order.

**forward_proxy.sh**
{% highlight sh %}
#!/bin/sh

BP_SOURCE=ipn:1.2
BP_DESTINATION=ipn:1.1
BP_SERVICE=0.1
NC_HOST=127.0.0.1
NC_PORT=4000

BP_REQUEST=testfile1
NC_REQUEST=request.pipe
NC_RESPONSE=response.pipe
BP_RESPONSE=response

EOT=$(printf "\4\4\4\4\4\4\4\4")

. delay.sh
TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "${TMP_DIR}"; exit' INT TERM QUIT EXIT
cd "${TMP_DIR}"
touch "${BP_RESPONSE}" "${BP_REQUEST}" "${NC_RESPONSE}" "${NC_REQUEST}"
#mkfifo -m 600 "${NC_RESPONSE}" "${NC_REQUEST}"

echo "Path: $(pwd)"
echo "Request In:   bprecvfile ${BP_SOURCE} 1"
echo "Server I/O:   nc -N ${NC_HOST} ${NC_PORT}"
echo "Response Out: bpsendfile ${BP_SOURCE} ${BP_DESTINATION} ${BP_RESPONSE} ${BP_SERVICE}"

while true
do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  echo "[ RECEIVE FILE : ${BP_REQUEST} ]"
  delay "<"
  bprecvfile "${BP_SOURCE}" 1
  cat "${BP_REQUEST}" |
  sed -u "s/^Host:.*/Host: ${NC_HOST}:${NC_PORT}/I" | # HTML Request Patch
  sed -u "s/^Connection:.*/Connection: close/I" | # HTML Request Patch
  tee "${NC_REQUEST}" | sed 's/^/< /'
  cat "${NC_REQUEST}" |
  nc -N "${NC_HOST}" "${NC_PORT}" >"${NC_RESPONSE}"
  cat "${NC_RESPONSE}" |
  tee "${BP_RESPONSE}" | sed 's/^/> /'
  echo "[ SEND FILE : ${BP_RESPONSE} ]"
  delay ">"
  bpsendfile "${BP_SOURCE}" "${BP_DESTINATION}" "${BP_RESPONSE}" "${BP_SERVICE}"
done
{% endhighlight %}

# β Reverse Proxy

The following script can be used to test the forward proxy one request at a time.
This script simulates delay.

**single_request.sh**
{% highlight sh %}
#!/bin/sh

BP_SOURCE=ipn:1.1
BP_DESTINATION=ipn:1.2
BP_SERVICE=0.1
BP_REQUEST=request.txt
BP_RESPONSE=testfile1

. delay.sh
echo "bpsendfile ${BP_SOURCE} ${BP_DESTINATION} ${BP_REQUEST} ${BP_SERVICE}"
echo "bprecvfile ${BP_SOURCE} 1"
echo -n "" >"${BP_RESPONSE}"
echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
cat "${BP_REQUEST}" | sed -u 's/^/> /'
echo "[ SEND ]"
delay ">"
bpsendfile "${BP_SOURCE}" "${BP_DESTINATION}" "${BP_REQUEST}" "${BP_SERVICE}"
echo "[ RECEIVE ]"
delay "<"
bprecvfile "${BP_SOURCE}" 1
cat "${BP_RESPONSE}" | sed -u 's/^/< /'
{% endhighlight %}

This is the request file used by the single request script.
Note that the file needs to end with a double newline.

**request.txt**
{% highlight http %}
GET / HTTP/1.1
Host: 127.0.0.1:4000
User-Agent: test-agent
Accept: */*
Connection: close

{% endhighlight %}

Run the single request script in the current shell to display an increasing request number with each request.

{% highlight sh %}
chmod +x single_request.sh
. ./single_request.sh
{% endhighlight %}

The reverse proxy accepts external connections in a loop with **nc**.
Received requests are sent to the forward proxy before waiting for a response.
This response is returned to the client.
This script assumes the request ends when it receives a blank line.
This will not work for POST or PUT requests.

**reverse_proxy.sh**
{% highlight sh %}
#!/bin/sh

BP_SOURCE=ipn:1.1
BP_DESTINATION=ipn:1.2
BP_SERVICE=0.1
NC_HOST=0.0.0.0
NC_PORT=8080

#NC_REQUEST=request.pipe
BP_REQUEST=request
BP_RESPONSE=testfile1
NC_RESPONSE=response.pipe

EOT=$(printf "\4\4\4\4\4\4\4\4")

. delay.sh
TMP_DIR=$(mktemp -d /tmp/$(basename $0).XXXXXX) || exit 1
trap 'rm -rf "${TMP_DIR}"; exit' INT TERM QUIT EXIT
cd "${TMP_DIR}"
touch "${BP_RESPONSE}" "${BP_REQUEST}"
mkfifo -m 600 "${NC_RESPONSE}" #"${NC_REQUEST}"

echo "Path: $(pwd)"
echo "Client I/O: nc -N -l ${NC_HOST} ${NC_PORT}"
echo "Proxy Out:  bpsendfile ${BP_SOURCE} ${BP_DESTINATION} ${BP_REQUEST} ${BP_SERVICE}"
echo "Proxy In:   bprecvfile ${BP_SOURCE} 1"

while true
do
  echo "---$((REQUEST_NUMBER=REQUEST_NUMBER+1))---"
  cat "${NC_RESPONSE}" | nc -N -l "${NC_HOST}" "${NC_PORT}" |
  (
    echo -n "" >"${BP_REQUEST}"
    while read LINE
    do
      echo "${LINE}" >>"${BP_REQUEST}"
      LINE=$(echo "${LINE}" | tr -d '[\r\n]')
      if [ "x${LINE}" = "x" ]
      then
        cat "${BP_REQUEST}" | sed -u 's/^/> /';
        echo "[ SEND FILE : ${BP_REQUEST} ]"
        delay ">"
        bpsendfile "${BP_SOURCE}" "${BP_DESTINATION}" "${BP_REQUEST}" "${BP_SERVICE}"
        echo "[ RECEIVE FILE : ${BP_RESPONSE} ]"
        delay "<"
        bprecvfile "${BP_SOURCE}" 1
        cat "${BP_RESPONSE}" | tee "${NC_RESPONSE}" | sed -u 's/^/< /'
        break
      fi
    done
  )
done
{% endhighlight %}

# Starting the Proxy Scripts

The scripts need to be started in the correct order.

{% highlight sh %}
# δ terminal
(TITLE="δ"; printf "\033]0;${TITLE}\007")
# Start a webserver on 0.0.0.0:4000 or use the following.
chmod +x date_server.sh
./date_server.sh

# γ terminal
(TITLE="γ"; printf "\033]0;${TITLE}\007")
chmod +x forward_proxy.sh
./forward_proxy.sh

# β terminal
(TITLE="β"; printf "\033]0;${TITLE}\007")
# test with single request, proxy with reverse_proxy
chmod +x single_request.sh
./single_request.sh
chmod +x reverse_proxy.sh
./reverse_proxy.sh

# α terminal
(TITLE="α"; printf "\033]0;${TITLE}\007")
# Direct a web browser to ${CURL_HOST}:8080 or use the following.
CURL_HOST=192.168.0.23
curl -v ${CURL_HOST}:8080
{% endhighlight %}

# α Web Browser

These proxies should serve web pages over ION-DTN.
The browser can handle modest delays, but will time out eventually.
**curl** will happily wait for a long time unless the --connect-timeout or --max-time options are passed to it.

If pages stop loading, the following can be used to restart the proxies in the correct order.

{% highlight sh %}
# β terminal
# kill proxy
^C

# γ terminal
# kill and restart proxy
^C
./forward_proxy.sh

# β terminal
# restart proxy
./reverse_proxy.sh
{% endhighlight %}

If a hello world test fails, ION needs to be restarted.

{% highlight sh %}
# β terminal
# kill proxy
^C

# γ terminal
# kill proxy
^C

# ionadmin terminal
(TITLE="ionadmin"; printf "\033]0;${TITLE}\007")
# hello world fails
{ echo "Hello, World!"; sleep 2; } | bpchat ipn:1.1 ipn:1.1
# restart ion
ionstop
killm
ionstart -I host1.rc
{% endhighlight %}

## References:
- [ION-DTN, Almost Serving a Web Page with ION-DTN bpchat][ion-almost]
- [ION-DTN, Getting Started with ION-DTN 3.4.0 on FreeBSD][ion-started]
- [ION-DTN, ION DTN as a Service on FreeBSD][ion-service]
- [FreeBSD, A Better Scripted Netcat Server][freebsd-better-nc]
- [UNIX, How to silence output in a bash script?][unix-silent]
- [UNIX, Convert seconds to hours, minutes, seconds in BASH][unix-time]
- [UNIX, Sh - the Bourne Shell][unix-sh]

[ion-almost]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/12/almost-serving-a-web-page-with-ion-dtn-bpchat.html
[ion-started]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/07/getting-started-with-ion-dtn-3-4-0-on-freebsd.html
[ion-service]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/15/ion-dtn-as-a-service-on-freebsd.html
[freebsd-better-nc]: https://sgeos.github.io/freebsd/nc/2016/02/17/a-better-scripted-netcat-server.html
[unix-silent]: http://stackoverflow.com/questions/2292847/how-to-silence-output-in-a-bash-script
[unix-time]: http://stackoverflow.com/questions/12199631/convert-seconds-to-hours-minutes-seconds-in-bash
[unix-sh]: http://www.grymoire.com/Unix/Sh.html#uh-36

