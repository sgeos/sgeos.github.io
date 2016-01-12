---
layout: post
title:  "Elixir as a Service on FreeBSD"
date:   2016-01-10 00:10:02 +0900
categories: elixir erlang
---
One of the things I really like about golang is deployment.  Golang is statically linked so deployment is a breeze.
It is really easy to create a project in golang that can be started and stopped as a standard FreeBSD service.
I wanted to see how hard it is to do the same thing with elixir.  In this post, a modified version of the Elixir
[getting started echo server][elixir-gen-tcp] will be installed as a service.  This service can be started, stopped
and restarted.  Specifically it can be rebuilt and restarted to reflect changes on a development machine.

## Software Versions
{% highlight sh %}
$ date
January 12, 2016 at 12:40:14 PM JST
$ uname -a
FreeBSD mirage.sennue.com 11.0-CURRENT FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [async-threads:10] [hipe] [kernel-poll:false]
Elixir 1.2.0
{% endhighlight %}

## Instructions
First, start a new project for the echo service.
{% highlight sh %}
mix new --sup elixir_echo
cd elixir_echo
{% endhighlight %}

Next, add a modified version of the [echo server][elixir-gen-tcp] from the Elixir getting started section.  The code goes in **lib/echo_elixir.ex**.
{% highlight elixir %}
defmodule ElixirEcho do
  use Application
  require Logger

  @port 4040

  @doc false
  def start(_type, _args) do
    import Supervisor.Spec

    children = [
      supervisor(Task.Supervisor, [[name: ElixirEcho.TaskSupervisor]]),
      worker(Task, [ElixirEcho, :accept, [@port]])
    ]

    opts = [strategy: :one_for_one, name: ElixirEcho.Supervisor]
    Supervisor.start_link(children, opts)
  end

  @doc """
  Starts accepting connections on the given `port`.
  """
  def accept(port) do
    {:ok, socket} = :gen_tcp.listen(port,
                      [:binary, packet: :line, active: false, reuseaddr: true])
    Logger.info "Accepting connections on port #{port}"
    loop_acceptor(socket)
  end

  defp loop_acceptor(socket) do
    {:ok, client} = :gen_tcp.accept(socket)
    {:ok, pid} = Task.Supervisor.start_child(ElixirEcho.TaskSupervisor, fn -> serve(client) end)
    :ok = :gen_tcp.controlling_process(client, pid)
    Logger.info "Opened connection"
    loop_acceptor(socket)
  end

  defp serve(socket) do
    status = socket
    |> read_line()
    |> write_line(socket)

    case status do
      :ok ->
        serve(socket)
      :closed ->
        Logger.info "Closed connection"
        :gen_tcp.close(socket)
        :ok
    end
  end

  defp read_line(socket) do
    case :gen_tcp.recv(socket, 0) do
      {:ok, data} ->
        data
      {:error, :closed} ->
        :closed
    end
  end

  defp write_line(:closed, socket), do: :closed
  defp write_line(line, socket) do
    :gen_tcp.send(socket, line)
    Logger.info "Echo: #{line |> String.strip}"
    :ok
  end
end
{% endhighlight %}

Added [exrm][elixir-exrm] to **mix.exs** as a project dependency.
{% highlight elixir %}
  defp deps do
    [{:exrm, "~> 1.0.0-rc7"}]
  end
{% endhighlight %}

Get and compile the dependencies.  Build and create a symlink to the release.
{% highlight sh %}
mix deps.get
mix deps.compile
mix release
su
sh
PROJECT=elixir_echo
VERSION=0.0.1
INSTALL_DIR=/usr/local/opt/bin
mkdir -p $INSTALL_DIR/$PROJECT
cp rel/$PROJECT/releases/$VERSION/$PROJECT.tar.gz $INSTALL_DIR
cd $INSTALL_DIR/$PROJECT
tar -xf ../$PROJECT.tar.gz
exit # sh
exit # su
{% endhighlight %}

edeliver has a [bash][man-bash] dependency.  I'm not happy about that, but there are more obtrusive dependencies.
Not happy about the [bash][man-bash] dependency.
{% highlight sh %}
portmaster bash
{% endhighlight %}

Add syslog.
{% highlight elixir %}
{% endhighlight %}

Restart.
{% highlight sh %}
{% endhighlight %}

/etc/rc.conf
elixir_echo_enable="YES"
service elixir_echo start

csh tcsh
/etc/csh.cshrc
set path=(/usr/local/opt/bin $path)
source /etc/csh.cshrc

sh bash
/etc/profile
PATH=/usr/local/opt/bin:$PATH
export PATH
. /etc/profile


## References:
- [Elixir, Task and gen_tcp][elixir-gen-tcp]
- [Elixir Release Manager][elixir-exrm]
- [Programming Elixir 1.2][elixir-book]
- [FreeBSD Forums, /opt directory replacement][freebsd-opt]
- [FreeBSD Forums, Configurable rc.d Script Template?][freebsd-rc-template]
- [FreeBSD, Practical rc.d scripting in BSD][freebsd-rc]
- [FreeBSD Man Pages, rc.subr(8)][freebsd-rc-subr]
- [FreeBSD Handbook, Shells][freebsd-shells]
- [UNIX, What is the difference between /opt and /usr/local?][unix-opt]

[elixir-gen-tcp]:      http://elixir-lang.org/getting-started/mix-otp/task-and-gen-tcp.html
[elixir-exrm]:         https://github.com/bitwalker/exrm
[elixir-edeliver]:     https://github.com/boldpoker/edeliver
[elixir-book]:         https://pragprog.com/book/elixir12/programming-elixir-1-2
[man-bash]:            https://www.freebsd.org/cgi/man.cgi?query=bash&sektion=1&apropos=0&manpath=Red+Hat+Linux%2Fi386+9
[freebsd-opt]:         https://forums.freebsd.org/threads/opt-directory-replacement.12614/
[freebsd-rc]:          https://www.freebsd.org/doc/en/articles/rc-scripting/index.html
[freebsd-rc-subr]:     https://www.freebsd.org/cgi/man.cgi?query=rc.subr&sektion=8
[freebsd-rc-template]: https://forums.freebsd.org/threads/configurable-rc-d-script-template.53308/
[freebsd-shells]:      https://www.freebsd.org/doc/handbook/shells.html
[unix-opt]:            http://unix.stackexchange.com/questions/11544/what-is-the-difference-between-opt-and-usr-local

