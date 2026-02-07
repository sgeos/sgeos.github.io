---
layout: post
comments: true
title:  "Multiplayer Elixir"
date:   2016-01-10 00:10:02 +0900
categories: elixir erlang
---

<!-- A5 -->

I wanted to write a multinode elixir example for multiple people on the same network.  A toy direct messaging app that can be run from iex is created in this post.  Any number of people can participate, but this post is largely written as if there are only two participants.

## Software Versions
{% highlight sh %}
$ date
January 10, 2016 at 12:10:02 AM JST
$ # computer a
$ uname -a
FreeBSD mirage.sennue.com 11.0-CURRENT FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [async-threads:10] [hipe] [kernel-poll:false]
Elixir 1.2.0
$ # computer b
$ uname -a
Darwin siderite.attlocal.net 15.2.0 Darwin Kernel Version 15.2.0: Fri Nov 13 19:56:56 PST 2015; root:xnu-3248.20.55~2/RELEASE_X86_64 x86_64
$ $ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false]
Elixir 1.2.0
{% endhighlight %}

## Instructions
First, start a new project and create a directory for the messenger module.
{% highlight sh %}
mix new --sup multiplayer
cd multiplayer
mkdir lib/multiplayer
{% endhighlight %}

Next, we need some code to run on the nodes.  Add the following to **lib/multiplayer/messenger.ex**.
{% highlight elixir %}
defmodule Multiplayer.Messenger do
  use GenServer

  # Client API

  def start_link() do
    {:ok, pid} = GenServer.start_link(__MODULE__, :ok, [])
    :global.register_name(node_name, pid)
    {:ok, pid}
  end

  def message(server, contents) when is_atom(server) do
    server
    |> :global.whereis_name
    |> message(contents)
  end

  def message(server, contents) when is_pid(server) do
    GenServer.cast(server, {:message,
      "#{node_name |> to_string |> String.upcase}: #{contents}"})
  end

  # Server Callbacks

  def init(:ok) do
    {:ok, nil}
  end

  def handle_cast({:message, contents}, state) do
    IO.puts contents
    {:noreply, state}
  end

  # Utility Functions

  def node_name do
    Node.self
    |> to_string
    |> String.split("@")
    |> List.first
    |> String.to_atom
  end
end
{% endhighlight %}

Nodes have a name in the form :name@host.  The node_name function discards the @host portion and returns :name.  This :name atom is passed to :global.register_name so any node on the network can look up any other messenger without having to know the host or IP address.  This is not a production ready solution, but it is good enough for this example.

The message function can send a message by messenger pid or node :name.  The uppercase node name is prepended to the message on the sending node.  IO.puts runs in the receiving node and prints the message in iex.  Messages are send and forget, so handle_cast is used.  This GenServer has no state.

Next, set up supervision in **lib/multiplayer.ex**.
{% highlight elixir %}
defmodule Multiplayer do
  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    children = [
      worker(Multiplayer.Messenger, []),
    ]

    opts = [strategy: :one_for_one, name: Multiplayer.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
{% endhighlight %}

Start the project in iex on two different machines on the same network.  Make sure the node names are different.  Also, make sure to append a routable host or IP address to the node name.
{% highlight sh %}
# machine a
iex --name alpha@192.168.1.166 --cookie double_chocolate -S mix

# machine b
iex --name beta@192.168.1.70 --cookie double_chocolate -S mix
{% endhighlight %}

Connect one of the nodes to the other.  This will connect both nodes to one another.  If there are more than two nodes, the remaining nodes can connect to any of the already connected nodes.  Each node only needs to connect once.
{% highlight elixir %}
# all except machine a
Node.connect :"alpha@192.168.1.166"
{% endhighlight %}

Send messages back and forth by calling Multiplayer.Messenger.message :name, "message"
{% highlight elixir %}
# machine a
Multiplayer.Messenger.message :beta, "hi"

# machine b
Multiplayer.Messenger.message :alpha, "Hello."
{% endhighlight %}

Messages are not broadcast to all participants.  Each message is only sent to the specified party.  Output will look something like this.
{% highlight elixir %}
# machine a
BETA: Hello.

# machine b
ALPHA: hi
{% endhighlight %}

## References:
- [StackOverflow: How to connect two Elixir nodes via local network?][stackoverflow-elixir-nodes]
- [Programming Elixir 1.2][elixir-book]
- [Elixir GenServer][elixir-genserver]

[stackoverflow-elixir-nodes]: http://stackoverflow.com/questions/17351882/how-to-connect-two-elixir-nodes-via-local-network
[elixir-book]:                https://pragprog.com/book/elixir12/programming-elixir-1-2
[elixir-genserver]:           http://elixir-lang.org/docs/v1.2/elixir/GenServer.html

