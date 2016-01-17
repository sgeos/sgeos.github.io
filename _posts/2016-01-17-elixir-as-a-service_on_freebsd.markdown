---
layout: post
title:  "Elixir as a Service on FreeBSD"
date:   2016-01-17 07:36:31 +0900
categories: elixir erlang
---
Ease of deployment is one of the things I seriously consider when evaluating technology solutions.
In this post, a modified version of the Elixir [getting started echo server][elixir-gen-tcp] will be installed as a
FreeBSD service.  There are three goals.

- The app needs to be able to be rebuilt and the service restarted to reflect changes on a development machine.  
- The service needs to automatically start when the machine is booted.
- The service sould work like any other service.
{% highlight sh %}
service elixir_echo start
service elixir_echo stop
service elixir_echo restart
service elixir_echo status
{% endhighlight %}

The steps are a little involved, but ultimately straightforward.

## Software Versions
{% highlight sh %}
$ date
January 17, 2016 at 07:37:31 PM JST
$ uname -a
FreeBSD mirage.sennue.com 11.0-CURRENT FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [async-threads:10] [hipe] [kernel-poll:false]
Elixir 1.2.0
{% endhighlight %}

## Instructions
elixir needs to be installed.  The tooling to install dependencies for elixir apps comes with the port.
{% highlight sh %}
sudo portmaster lang/elixir
{% endhighlight %}

First, start a new project for the echo service.
{% highlight sh %}
mix new --sup elixir_echo
cd elixir_echo
{% endhighlight %}

Next, add a modified version of the [echo server][elixir-gen-tcp] from the Elixir getting started section.
This version loads the port from environment variables or the app configuration environment.
The default fallback is port 4040.  It also gracefully handles closed sockets.
The code goes in **lib/echo_elixir.ex**.
{% highlight elixir %}
defmodule ElixirEcho do
  use Application
  require Logger

  @default_port 4040

  @doc false
  def start(_type, _args) do
    import Supervisor.Spec

    port = "PORT" |> get_env(@default_port) |> to_integer(@default_port)

    children = [
      supervisor(Task.Supervisor, [[name: ElixirEcho.TaskSupervisor]]),
      worker(Task, [ElixirEcho, :accept, [port]])
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

  defp write_line(:closed, _socket), do: :closed
  defp write_line(line, socket) do
    :gen_tcp.send(socket, line)
    Logger.info "Echo: #{line |> String.strip}"
    :ok
  end

  # Utility Functions

  def get_env(name, default) do
    case (
      System.get_env(name) ||
      Application.get_env(:elixir_echo, name |> String.downcase |> String.to_atom)
    ) |> to_string
    do
      "" -> default |> to_string
      result -> result
    end
  end

  def to_integer(x, _default) when is_integer(x), do: x
  def to_integer(x, default) when is_binary(x) do
    case x |> Integer.parse do
      {result, _} -> result
      :error -> default
    end
  end
  def to_integer(_, default), do: default
end
{% endhighlight %}

Add the [elixir release manager (exrm)][elixir-exrm] to **mix.exs** as a project dependency.
{% highlight elixir %}
  defp deps do
    [{:exrm, "~> 1.0.0-rc7"}]
  end
{% endhighlight %}

Install exrm and build a release.  This will create the **rel/** directory.
{% highlight sh %}
mix deps.get
mix deps.compile
mix release
{% endhighlight %}

The rc script will use environment variable knobs to configure the app.
Note that the **RELX_REPLACE_OS_VARS=true** environment variable needs to be defined to use environment variables for dynamic configuration.

The **vm.args** file is primarily used to configure the erlang VM.
It can also be used to define application configure parameters.
Application configuration parameters defined in this file can be passed into the program as atoms or integers.
Add the following to **rel/vm.args**.
{% highlight sh %}
## Name of the node
-name ${NODE_NAME}

## Cookie for distributed erlang
-setcookie ${COOKIE}

## App Settings
-elixir_echo port ${PORT}
{% endhighlight %}

Alternatively, **sys.config** can be used to pass in application configuration parameters.
In this file, application configuration parameters defined with environment variables must be strings.
Pass the port setting in as above or add the following to **rel/sys.config**.
The app module was written to work with either solution.
Adding both files will not break anything.
{% highlight erlang %}
[
  {elixir_echo, [
    {port, "${PORT}"}
  ]}
].
{% endhighlight %}

Build a release with the configuration files and do the initial install.
{% highlight sh %}
mix release
su
sh
PROJECT=elixir_echo
INSTALL_DIR=/usr/local/opt
VERSION=$(cat rel/${PROJECT}/releases/start_erl.data | cut -d' ' -f2)
INSTALL_TAR=`pwd`/rel/$PROJECT/releases/$VERSION/$PROJECT.tar.gz
mkdir -p $INSTALL_DIR/$PROJECT
(cd $INSTALL_DIR/$PROJECT; \
tar -xf $INSTALL_TAR)
pw adduser $PROJECT -d $INSTALL_DIR/$PROJECT -s /usr/sbin/nologin -c "$PROJECT system service user"
chown -R $PROJECT:$PROJECT $INSTALL_DIR/$PROJECT
{% endhighlight %}

An rc script defines the the service.
**elixir_echo_run()** is called from the other functions.
It configures and calls the release.
**HOME** is set to the installation directory to force the erlang cookie file to be written there regardless of **elixir_echo_user** setting.
**elixir_echo_status()** echoes a user friendly message if the release can be pinged.
Add **shutdown** to the keyword list if the service needs to gracefull shutdown when the machine restarts.
The rest is standard rc configuration.
Add the rc script to **/usr/local/etc/rc.d/elixir_echo**
{% highlight sh %}
#!/bin/sh
#
# PROVIDE: elixir_echo
# REQUIRE: networking
# KEYWORD:
 
. /etc/rc.subr
 
name="elixir_echo"
rcvar="${name}_enable"
install_dir="/usr/local/opt/${name}"
version=$(cat ${install_dir}/releases/start_erl.data | cut -d' ' -f2)
command="${install_dir}/bin/${name}"
 
start_cmd="${name}_start"
stop_cmd="${name}_stop"
status_cmd="${name}_status"

load_rc_config $name
: ${elixir_echo_enable:="no"}
: ${elixir_echo_port:="4040"}
: ${elixir_echo_user:=${name}}
: ${elixir_echo_node_name:="${name}@127.0.0.1"}
: ${elixir_echo_cookie:="${name}"}
: ${elixir_echo_config_dir:="${install_dir}/releases/${version}/${name} start"}

elixir_echo_run()
{
  RELX_REPLACE_OS_VARS=true \
  HOME="${install_dir}" \
  RELEASE_CONFIG_DIR="${elixir_echo_config}" \
  NODE_NAME="${elixir_echo_node_name}" \
  COOKIE="${elixir_echo_cookie}" \
  PORT="${elixir_echo_port}" \
  su -m "$elixir_echo_user" -c "$command $1"
}

elixir_echo_start()
{
  elixir_echo_run start
}

elixir_echo_stop()
{
  elixir_echo_run stop
}

elixir_echo_status()
{
  ping_result=`elixir_echo_run ping`
  echo "${ping_result}"
  case "${ping_result}" in
    *pong*)
      echo "${name} is running."
      ;;
  esac
}

load_rc_config $name
run_rc_command "$1"
{% endhighlight %}

Enable and configure the service in **/etc/rc.conf**
{% highlight sh %}
elixir_echo_enable="YES"
elixir_echo_port=8255
elixir_echo_node_name="parrot"
elixir_echo_cookie="cracker"
{% endhighlight %}

The service can now be started.  If the service is enabled, it will automatically start when the machine boots.
{% highlight sh %}
service elixir_echo start
telnet 127.0.0.1 8255 # make sure it works
{% endhighlight %}

### Optional: Adding a Release to the Systemwide Path

Adding a release to the systemwide path is not necessary, but it can be convenient.
The pass through script can be pointed at the development install instead of the service install if you want to build with exrm **mix release --dev**.

Create a directory for the convenience pass through script.
{% highlight sh %}
mkdir -p $INSTALL_DIR/bin
{% endhighlight %}

**NODE_NAME** and **COOKIE** need default values because **vm.args** has no useful default fallbacks.
**PORT** has a fallback.
Add the script to **/usr/local/opt/bin/elixir_echo**
{% highlight sh %}
#!/bin/sh
SCRIPT=$(realpath $0)
BASENAME=$(basename $SCRIPT)
BASEDIR=$(dirname $SCRIPT)
COMMAND=$(realpath $BASEDIR/../$BASENAME/bin/$BASENAME)

: ${NODE_NAME:=${BASENAME}}
: ${COOKIE:=${BASENAME}}
NODE_NAME=$NODE_NAME COOKIE=$COOKIE RELX_REPLACE_OS_VARS=true $COMMAND "$@"
{% endhighlight %}

Make the script executable.
{% highlight sh %}
chmod +x $INSTALL_DIR/bin/$PROJECT
{% endhighlight %}

Add **/usr/local/opt/bin** to the global path in **/etc/profile** for **sh**.
{% highlight sh %}
PATH=/usr/local/opt/bin:$PATH
export PATH
{% endhighlight %}

Add **/usr/local/opt/bin** to the global path in **/etc/csh.cshrc** for **csh**.
Consider updating the root path in **/root/.cshrc**.
{% highlight csh %}
set path=(/usr/local/opt/bin $path)
{% endhighlight %}

Update the path in the current shell if necessary.
{% highlight sh %}
# sh bash
source /etc/csh.cshrc
# csh tcsh
. /etc/profile
{% endhighlight %}

Fix permissions if you want to be able to run as any user.  This has security implications.
It may make more sense to point the script at the development release if it is being used as a development convenience.
{% highlight sh %}
chmod 755 $INSTALL_DIR/$PROJECT/bin/$PROJECT
chmod 755 $INSTALL_DIR/$PROJECT/bin/nodetool
chmod 755 $INSTALL_DIR/$PROJECT/releases/$VERSION/$PROJECT.sh
mkdir -p $INSTALL_DIR/$PROJECT/log
chmod 777 $INSTALL_DIR/$PROJECT/log
chmod 777 $INSTALL_DIR/$PROJECT/log/*.*
mkdir -p $INSTALL_DIR/$PROJECT/tmp/erl_pipes/$PROJECT
chmod 777 $INSTALL_DIR/$PROJECT/tmp/erl_pipes/$PROJECT
mkdir -p $INSTALL_DIR/$PROJECT/running-config/
chmod 777 $INSTALL_DIR/$PROJECT/running-config/
chmod 666 $INSTALL_DIR/$PROJECT/running-config/*.*
chown -R $PROJECT:$PROJECT $INSTALL_DIR/$PROJECT
{% endhighlight %}

The release can now be conveniently controlled.
{% highlight sh %}
NODE_NAME=canary COOKIE=sesame PORT=5678 elixir_echo start
telnet 127.0.0.1 5678 # make sure it works
{% endhighlight %}

### Setup Complete

Switch from root to a normal user.
{% highlight sh %}
exit # sh
exit # su
{% endhighlight %}

### Updating

Casual updates on a development machine can be performed as follows.
{% highlight sh %}
mix release
su
sh
PROJECT=elixir_echo
INSTALL_DIR=/usr/local/opt
VERSION=$(cat rel/${PROJECT}/releases/start_erl.data | cut -d' ' -f2)
INSTALL_TAR=`pwd`/rel/$PROJECT/releases/$VERSION/$PROJECT.tar.gz
(cd $INSTALL_DIR/$PROJECT; \
tar -xf $INSTALL_TAR)
chown -R $PROJECT:$PROJECT $INSTALL_DIR/$PROJECT
service $PROJECT restart
exit # sh
exit # su
{% endhighlight %}

### Troubleshooting

If configuration looks like it should be working, but nothing changes, try deleting the **running-config** directory.

### What Next?

Consider looking into [edeliver][elixir-edeliver] for deployment.
"edeliver is based on deliver and provides a bash script to build and deploy
Elixir and Erlang applications and perform hot-code upgrades."

## References:
- [Elixir, Task and gen_tcp][elixir-gen-tcp]
- [Elixir, System][elixir-system]
- [Elixir Release Manager][elixir-exrm]
- [Elixir exrm Release Configuration][elixir-exrm-config]
- [Elixir exrm Deployment][elixir-exrm-deploy]
- [Elixir, edeliver][elixir-edeliver]
- [Elixir, Programming Elixir 1.2][elixir-book]
- [FreeBSD Forums, /opt directory replacement][freebsd-opt]
- [FreeBSD Forums, Creating a System User (like www)][freebsd-system-user]
- [FreeBSD Forums, Configurable rc.d Script Template?][freebsd-rc-template]
- [FreeBSD, Practical rc.d scripting in BSD][freebsd-rc]
- [FreeBSD Man Pages, rc.subr(8)][freebsd-rc-subr]
- [FreeBSD Handbook, Shells][freebsd-shells]
- [FreeBSD, Run as different user under FreeBSD (closed)][freebsd-su]
- [UNIX, What is the difference between /opt and /usr/local?][unix-opt]
- [UNIX, How do I forward parameters to other command in bash script?][bash-arg]
- [UNIX, sh Scripting Cheat Sheet][sh-cheat-sheet]
- [UNIX, How can I make chown work recursively?][unix-chown]
- [UNIX, String contains in bash][unix-shell-contains]
- [UNIX, bash Using case statements][unix-shell-case]
- [UNIX, Creating System Users And Groups][unix-users]
- [Erlang, Distributed Erlang][erlang-distributed]
- [Erlang, Config][erlang-config]
- [Erlang, A little known fact about Erlang's sys.config][erlang-sys-config]
- [Erlang, rebar Releases][erlang-rebar-releases]

[elixir-gen-tcp]:        http://elixir-lang.org/getting-started/mix-otp/task-and-gen-tcp.html
[elixir-system]:         http://elixir-lang.org/docs/v1.0/elixir/System.html#get_env/1
[elixir-exrm]:           https://github.com/bitwalker/exrm
[elixir-exrm-config]:    https://exrm.readme.io/docs/release-configuration
[elixir-exrm-deploy]:    https://hexdocs.pm/exrm/extra-deployment.html
[elixir-edeliver]:       https://github.com/boldpoker/edeliver
[elixir-syslog]:         https://hex.pm/packages?search=syslog&sort=downloads
[elixir-book]:           https://pragprog.com/book/elixir12/programming-elixir-1-2
[freebsd-opt]:           https://forums.freebsd.org/threads/opt-directory-replacement.12614/
[freebsd-rc]:            https://www.freebsd.org/doc/en/articles/rc-scripting/index.html
[freebsd-rc-subr]:       https://www.freebsd.org/cgi/man.cgi?query=rc.subr&sektion=8
[freebsd-rc-template]:   https://forums.freebsd.org/threads/configurable-rc-d-script-template.53308/
[freebsd-shells]:        https://www.freebsd.org/doc/handbook/shells.html
[unix-opt]:              http://unix.stackexchange.com/questions/11544/what-is-the-difference-between-opt-and-usr-local
[unix-users]:            http://www.greenend.org.uk/rjk/tech/useradd.html
[bash-arg]:              http://stackoverflow.com/questions/1537673/how-do-i-forward-parameters-to-other-command-in-bash-script
[unix-shell-contains]:   http://stackoverflow.com/questions/229551/string-contains-in-bash/229585#229585
[unix-shell-case]:       http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html
[sh-cheat-sheet]:        https://www.joedog.org/articles-cheat-sheet/
[freebsd-system-user]:   https://forums.freebsd.org/threads/creating-a-system-user-like-www.2152/
[freebsd-su]:            http://stackoverflow.com/questions/285658/run-as-different-user-under-freebsd
[unix-chown]:            http://superuser.com/questions/260925/how-can-i-make-chown-work-recursively
[erlang-distributed]:    http://www.erlang.org/doc/reference_manual/distributed.html
[erlang-config]:         http://www.erlang.org/doc/man/config.html
[erlang-sys-config]:     http://aerosol.github.io/anxibits/little-known-fact-about-erlang-sys-config/
[erlang-rebar-releases]: https://www.rebar3.org/docs/releases

