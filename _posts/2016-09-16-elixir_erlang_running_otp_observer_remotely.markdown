---
layout: post
mathjax: false
comments: true
title:  "Elixir/Erlang, Running OTP Observer Remotely"
date:   2016-09-16 14:17:43 +0000
categories: elixir erlang observer
---
This post covers running the OTP's observer on a node running on a remote machine.
It is a step-by-step of [this gist][observer-remote].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-09-16 14:17:43 +0000

# localhost
$ uname -vm
Darwin Kernel Version 15.6.0: Mon Aug 29 20:21:34 PDT 2016; root:xnu-3248.60.11~1/RELEASE_X86_64 x86_64
$ mix hex.info
Hex:    0.13.0
Elixir: 1.3.2
OTP:    19.0
* snip *

# remotehost
$ uname -vm
FreeBSD 12.0-CURRENT #0 r304324: Thu Aug 18 13:27:23 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ mix hex.info
Hex:    0.13.0
Elixir: 1.3.2
OTP:    19.0.7
* snip *
{% endhighlight %}

## Instructions

On the remote host, start a node with known name and cookie values.
**iex** or **erl** will be used for this example.

**sh** remotehost
{% highlight sh %}
IF=em0
HOST=$(ifconfig ${IF} | grep 'inet ' | cut -d ' ' -f 2)
NAME="wild_exhibisionist@${HOST}"
COOKIE="banana_chocolate_chip_nut_butter"
printf "NAME='${NAME}'\nCOOKIE='${COOKIE}'\n"
iex --name "${NAME}" --cookie "${COOKIE}"
# OR
erl -name "${NAME}" -setcookie "${COOKIE}"
{% endhighlight %}

From the localhost, **ssh** into the remote host and run **epmd**.

**sh** localhost
{% highlight sh %}
# use your own remote host
REMOTE_HOST=192.168.1.14
ssh "${REMOTE_HOST}" "epmd -names"
{% endhighlight %}

With the previously started node running, the output should look something like this.

**sh** localhost
{% highlight sh %}
epmd: up and running on port 4369 with data:
name wild_exhibisionist at port 48341
{% endhighlight %}

Note the ports that **empd** and the node you want to debug are using.
Reconnect to the remote host with these ports forwarded.

**sh** localhost
{% highlight sh %}
# below NODE_PORT setting assumes there is only one node running
EPMD_PORT=$(ssh "${REMOTE_HOST}" "epmd -names" | grep epmd | sed 's/[^0-9]//g')
NODE_PORT=$(ssh "${REMOTE_HOST}" "epmd -names" | grep name | sed 's/[^0-9]//g')
printf "REMOTE_HOST='${REMOTE_HOST}'\nEPMD_PORT='${EPMD_PORT}'\nNODE_PORT='${NODE_PORT}'\n"
ssh -L "${EPMD_PORT}:${REMOTE_HOST}:${EPMD_PORT}" -L "${NODE_PORT}:${REMOTE_HOST}:${NODE_PORT}" "${REMOTE_HOST}"
{% endhighlight %}

Start a hidden node running the observer app.

**sh** localhost
{% highlight sh %}
# both interfaces probably need to be on the same network
IF=en0
HOST=$(ifconfig ${IF} | grep 'inet ' | cut -d ' ' -f 2)
NAME="observer@${HOST}"
# use the same cookie value
COOKIE="banana_chocolate_chip_nut_butter"
printf "NAME='${NAME}'\nCOOKIE='${COOKIE}'\n"
iex --name "${NAME}" --cookie "${COOKIE}" --hidden -e ":observer.start"
# OR
erl -name "${NAME}" -setcookie "${COOKIE}" -hidden -run observer
{% endhighlight %}

In *observer*, go to *Nodes* -> *Connect Node* and enter the name of the remote node.

If you are having trouble connecting, try to manually connect
the nodes from the **iex** or **erl** prompt.
If the nodes do not connect manually, solve that problem.
After the nodes have been manually connected, go to *Nodes* -> *Connect Node* and
enter the name of the remote node in *observer*.

**iex** localhost
{% highlight elixir %}
Node.connect :"wild_exhibisionist@192.168.1.14"
{% endhighlight %}

**iex** remotehost
{% highlight elixir %}
Node.connect :"observer@192.168.1.2"
{% endhighlight %}

**erl** localhost
{% highlight erlang %}
net_kernel:connect('wild_exhibisionist@192.168.1.14').
{% endhighlight %}

**erl** remotehost
{% highlight erlang %}
net_kernel:connect('observer@192.168.1.2').
{% endhighlight %}

Use the following to get a remote shell.

**sh** localhost
{% highlight sh %}
REMOTE_NODE="wild_exhibisionist@192.168.1.14"
iex --name "${NAME}" --cookie "${COOKIE}" --remsh "${REMOTE_NODE}"
# OR
erl -name "${NAME}" -setcookie "${COOKIE}" -remsh "${REMOTE_NODE}"
{% endhighlight %}

Note that **:runtime_tools** must be in the applications list to observe an app released with *exrm*.

**mix.exs** partial listing
{% highlight elixir %}
  def application do
    [mod: {MyApp, []},
     applications: [:runtime_tools]] # add to this list
  end
{% endhighlight %}

## References:

- [Erlang, Using OTP's observer (appmon replacement) remotely][observer-remote]
- [Erlang, epmd][erlang-epmd]
- [Erlang, Install erlang with wxwidgets (macports)][observer-macports]
- [Erlang R16 64Bit on OS X 10.9 with wxWidgets][erlang-wxwidget]
- [Erlang, Fixing erlang 15B Observer (from macports); fails to run][erlang-15b-observer]
- [Erlang, Connecting Erlang nodes when an internal and external IP address are at play][erlang-connect]
- [Elixir, iex Command Line Options List][elixir-iex-arg]
- [Elixir, Observer is not available][elixir-no-observer]
- [Elixir, Multiplayer Elixir][elixir-multiplayer]
- [UNIX, SSH tunneling error: “channel 1: open failed: administratively prohibited: open failed”][unix-ssh-fail]

[observer-remote]: https://gist.github.com/pnc/9e957e17d4f9c6c81294
[erlang-epmd]: http://erlang.org/doc/man/epmd.html
[observer-macports]: http://jjw.in/server/install-erlang-with-wxwidgets-macports
[erlang-wxwidget]: http://smyck.net/2014/02/28/erlang-r16-64bit-on-os-x-10-9-with-wxwidgets/
[erlang-15b-observer]: http://ebanshi.cc/questions/1453208/fixing-erlang-15b-observer-from-macports-fails-to-run
[elixir-iex-arg]: https://github.com/elixir-lang/elixir/blob/master/bin/iex
[elixir-no-observer]: http://stackoverflow.com/questions/32449234/observer-is-not-available-elixir
[elixir-multiplayer]: https://sgeos.github.io/elixir/erlang/2016/01/09/multiplayer-elixir.html
[erlang-connect]: http://stackoverflow.com/questions/26474591/connecting-erlang-nodes-when-an-internal-and-external-ip-address-are-at-play
[unix-ssh-fail]: http://unix.stackexchange.com/questions/14160/ssh-tunneling-error-channel-1-open-failed-administratively-prohibited-open

