---
layout: post
comments: true
title:  "Phoenix as a Service on FreeBSD"
date:   2016-03-21 15:48:51 +0000
categories: phoenix elixir erlang freebsd
---
In this post a Phoenix app will be installed as a service on FreeBSD.
The goals are the same as the [Elixir as a Service on FreeBSD post][elixir-service].

- The app needs to be able to be rebuilt and the service
  restarted to reflect changes on a development machine.  
- The service needs to automatically start when the machine is booted.
- The service sould work like any other service.

{% highlight sh %}
service phoenix_service start
service phoenix_service stop
service phoenix_service restart
service phoenix_service status
{% endhighlight %}

This post assumes Phoenix, Elixir and PostgreSQL are [already installed on FreeBSD][phoenix-install].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-21 15:48:51 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r296925: Wed Mar 16 20:53:04 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ mix hex.info
Hex:    0.11.3
Elixir: 1.2.3
OTP:    18.2.4
* snip *
$ mix phoenix.new -v
Phoenix v1.1.4
{% endhighlight %}

## Creating a Sample Project

Create a new Phoenix project.

{% highlight sh %}
mix phoenix.new phoenix_service --no-brunch
cd phoenix_service
mix ecto.create
{% endhighlight %}

This sample project needs to be simple.
Let's make a JSON memo service.

{% highlight sh %}
mix phoenix.gen.json Memo memos title:string body:string
{% endhighlight %}

Revise the **web/router.ex** file.
The "/api" scope needs to be uncommented and the "/memos" route needs to be added.

**web/router.ex file**
{% highlight elixer %}
defmodule PhoenixService.Router do
  use PhoenixService.Web, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", PhoenixService do
    pipe_through :browser # Use the default browser stack
  
    get "/", PageController, :index
  end

  scope "/api", PhoenixService do
    pipe_through :api

    resources "/memos", MemoController, except: [:new, :edit]
  end
end
{% endhighlight %}

Run the migration.

{% highlight sh %}
mix ecto.migrate
{% endhighlight %}

Set server to true in **config/prod.exs**.
Also make sure a dynamic port configuration is used.

**config/prod.exs** partial listing
{% highlight elixir %}
config :phoenix_service, PhoenixService.Endpoint,
  http: [port: {:system, "PORT"}], # dynamic port configuration
  url: [host: "example.com", port: 80],
  cache_static_manifest: "priv/static/manifest.json", # added comma
  server: true # this line is new
{% endhighlight %}

Optionally, add a dynamic port configuration with a default value to **config/dev.exs**.
The above build time solution is suitable for releases.
The interpreted solution below is suitable for development.

**config/dev.exs** partial listing
{% highlight elixir %}
  # http: [port: 4000], # old line 10
  http: [port: System.get_env("PORT") || Application.get_env(:phoenix_service, :port) || 4000],
{% endhighlight %}

Tests should pass

{% highlight sh %}
mix test
{% endhighlight %}

Start the server.

{% highlight sh %}
mix phoenix.server
{% endhighlight %}

POST and GET a memo to make sure the server works.
A [prior post][phoenix-script] covers a shell script for conveniently
interacting with this sample app.

{% highlight sh %}
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://localhost:4000/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos/1
{% endhighlight %}

## Generating a Release

Now that the Phoenix app is working, it is time to build a release.
Add the [elixir release manager (exrm)][elixir-exrm] to **mix.exs** as a project dependency.

**mix.exs** partial listing
{% highlight elixir %}
  defp deps do
    [{:phoenix, "~> 1.1.4"},
     {:postgrex, ">= 0.0.0"},
     {:phoenix_ecto, "~> 2.0"},
     {:phoenix_html, "~> 2.4"},
     {:phoenix_live_reload, "~> 1.0", only: :dev},
     {:gettext, "~> 0.9"},
     {:exrm, "~> 1.0.2"}, # this line is new
     {:cowboy, "~> 1.0"}]
  end
{% endhighlight %}

Install exrm and build a release.
This will create the **rel/** directory.

{% highlight sh %}
mix deps.get
mix deps.compile
MIX_ENV=prod mix ecto.create
MIX_ENV=prod mix ecto.migrate
MIX_ENV=prod mix compile
# brunch build --production # if using brunch
MIX_ENV=prod mix phoenix.digest
MIX_ENV=prod mix release
{% endhighlight %}

The rc script will use environment variable knobs to configure the app.
Note that the **RELX_REPLACE_OS_VARS=true** environment variable needs
to be defined to use environment variables for dynamic configuration.

The **vm.args** file is primarily used to configure the erlang VM.
It can also be used to define application configure parameters.
Application configuration parameters defined in this file can be
passed into the program as atoms or integers.
Note that the location of this file can be [configured][elixir-exrm-release-config]
with the **RELEASE_CONFIG_DIR** environment variable.
Add the following to **rel/vm.args**.

**rel/vm.args**
{% highlight sh %}
## Name of the node
-name ${NODE_NAME}

## Cookie for distributed erlang
-setcookie ${COOKIE}

## App Settings
-phoenix_service port ${PORT}
{% endhighlight %}

Alternatively, **sys.config** can be used to pass in
application configuration parameters.
In this file, application configuration parameters
defined with environment variables must be strings.
Pass the port setting in as above or add the following
to **rel/sys.config**.
The app module should work with either solution.
Adding both files will not break anything.
Note that **rel/sys.config** is written in Erlang.

**rel/sys.config**
{% highlight erlang %}
[
  {phoenix_service, [
    {port, "${PORT}"}
  ]}
].
{% endhighlight %}

Rebuild the release with the configuration files.

{% highlight sh %}
MIX_ENV=prod mix release
{% endhighlight %}

Start the release in the console.

{% highlight sh %}
RELX_REPLACE_OS_VARS=true PORT=7777 rel/phoenix_service/bin/phoenix_service console
{% endhighlight %}

Make sure the server responds.

{% highlight sh %}
curl 192.168.0.23:7777/api/memos
{% endhighlight %}

Exit the console with ^C.

## Installing the Release as a Service

Now that the release is working, it is time to set it up as a service.
Perform the initial install.

{% highlight sh %}
su
sh
PROJECT=phoenix_service
INSTALL_DIR=/usr/local/opt
VERSION=$(cat rel/${PROJECT}/releases/start_erl.data | cut -d' ' -f2)
INSTALL_TAR=`pwd`/rel/$PROJECT/releases/$VERSION/$PROJECT.tar.gz
mkdir -p $INSTALL_DIR/$PROJECT
(cd $INSTALL_DIR/$PROJECT; tar -xf $INSTALL_TAR)
pw adduser $PROJECT -d $INSTALL_DIR/$PROJECT -s /usr/sbin/nologin -c "$PROJECT system service user"
chown -R $PROJECT:$PROJECT $INSTALL_DIR/$PROJECT
{% endhighlight %}

An rc script defines the the service.

- **phoenix_service_run()** is called from the other functions.
  It configures and calls the release.
  **HOME** is set to the installation directory to force the
  erlang cookie file to be written there regardless of the
  **phoenix_service_user** setting.
- **phoenix_service_status()** echoes a user friendly
  message if the release can be pinged.
- **extra_commands** is used to add the **console** and
  **remote_console** commands.
  **console** is used to start a new service and attach a console to it.
  **remote_console()** is used to connect a console to the service
  if it is already running.
- Add **shutdown** to the keyword list if the service needs to
  gracefull shutdown when the machine restarts.
- The rest is standard rc configuration.

Add following to **/usr/local/etc/rc.d/phoenix_service**

**/usr/local/etc/rc.d/phoenix_service**
{% highlight sh %}
#!/bin/sh
#
# PROVIDE: phoenix_service
# REQUIRE: networking
# KEYWORD:
 
. /etc/rc.subr
 
name="phoenix_service"
rcvar="${name}_enable"
install_dir="/usr/local/opt/${name}"
version=$(cat ${install_dir}/releases/start_erl.data | cut -d' ' -f2)
command="${install_dir}/bin/${name}"
 
start_cmd="${name}_start"
stop_cmd="${name}_stop"
status_cmd="${name}_status"
console_cmd="${name}_console"
remote_console_cmd="${name}_remote_console"
extra_commands="console remote_console"

load_rc_config $name
: ${phoenix_service_enable:="no"}
: ${phoenix_service_port:="4000"}
: ${phoenix_service_user:=${name}}
: ${phoenix_service_node_name:="${name}@127.0.0.1"}
: ${phoenix_service_cookie:="${name}"}
: ${phoenix_service_config_dir:="${install_dir}/releases/${version}/${name} start"}

phoenix_service_run()
{
  RELX_REPLACE_OS_VARS=true \
  HOME="${install_dir}" \
  RELEASE_CONFIG_DIR="${phoenix_service_config}" \
  NODE_NAME="${phoenix_service_node_name}" \
  COOKIE="${phoenix_service_cookie}" \
  PORT="${phoenix_service_port}" \
  su -m "$phoenix_service_user" -c "$command $1"
}

phoenix_service_start()
{
  phoenix_service_run start
}

phoenix_service_stop()
{
  phoenix_service_run stop
}

phoenix_service_status()
{
  ping_result=`phoenix_service_run ping`
  echo "${ping_result}"
  case "${ping_result}" in
    *pong*)
      echo "${name} is running."
      ;;
  esac
}

phoenix_service_console()
{
  phoenix_service_run console
}

phoenix_service_remote_console()
{
  phoenix_service_run remote_console
}

load_rc_config $name
run_rc_command "$1"
{% endhighlight %}

Make **/usr/local/etc/rc.d/phoenix_service** read only and executable.

{% highlight sh %}
chmod 555 /usr/local/etc/rc.d/phoenix_service
{% endhighlight %}

Enable and configure the service in **/etc/rc.conf**.

**/etc/rc.conf** lines to add
{% highlight sh %}
phoenix_service_enable="YES"
phoenix_service_port=8248
phoenix_service_node_name="suzaku"
phoenix_service_cookie="cookie-of-the-southern-flame"
{% endhighlight %}

The service can now be started.  If the service is enabled, it will automatically start when the machine boots.
{% highlight sh %}
service phoenix_service start
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "Service Running", "body": "The Phoenix service is running on '"$(hostname)"'."}}' http://localhost:8248/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:8248/api/memos/1
{% endhighlight %}

### Optional: Adding a Release to the Systemwide Path

Adding a release to the systemwide path is not necessary, but it can be convenient.
Create a directory for the convenience pass through script.

{% highlight sh %}
mkdir -p $INSTALL_DIR/bin
{% endhighlight %}

**PORT**, **NODE_NAME** and **COOKIE** need default values because **vm.args** has no useful default fallbacks.
There is no good way to automatically select a port, so 8080 is a hard coded default.
Add the following script to **/usr/local/opt/bin/phoenix_service**.

**/usr/local/opt/bin/phoenix_service**
{% highlight sh %}
#!/bin/sh

SCRIPT=$(realpath $0)
BASENAME=$(basename $SCRIPT)
BASEDIR=$(dirname $SCRIPT)
COMMAND=$(realpath $BASEDIR/../$BASENAME/bin/$BASENAME)

: ${NODE_NAME:=${BASENAME}}
: ${COOKIE:=${BASENAME}}
: ${PORT:="8080"}

NODE_NAME=${NODE_NAME} \
COOKIE=${COOKIE} \
PORT=${PORT} \
RELX_REPLACE_OS_VARS=true \
$COMMAND "$@"
{% endhighlight %}

Make the script executable.

{% highlight sh %}
chmod +x $INSTALL_DIR/bin/$PROJECT
{% endhighlight %}

Add **/usr/local/opt/bin** to the global path in **/etc/profile** for **sh**,
and **/etc/csh.cshrc** for **csh**.
Consider updating the root path in **/root/.cshrc**.

**/usr/local/opt/bin** partial listing
{% highlight sh %}
PATH=/usr/local/opt/bin:$PATH
export PATH
{% endhighlight %}

**/etc/csh.cshrc** partial listing
{% highlight csh %}
set path=(/usr/local/opt/bin $path)
{% endhighlight %}

**/root/.cshrc** partial listing
{% highlight csh %}
set path = (/usr/local/opt/bin /sbin /bin /usr/sbin /usr/bin /usr/local/sbin /usr/local/bin $HOME/bin)
{% endhighlight %}

Update the path in the current shell if necessary.

{% highlight sh %}
# sh bash
source /etc/csh.cshrc
# csh tcsh
. /etc/profile
{% endhighlight %}

Fix permissions if you want to be able to run as any user.
This may have security implications.

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
# start service
NODE_NAME=rudra COOKIE=treasure PORT=5678 phoenix_service start
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "Service Running", "body": "The Phoenix service is running on '"$(hostname)"'."}}' http://localhost:5678/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:5678/api/memos/1
# stop service
NODE_NAME=rudra COOKIE=treasure phoenix_service stop
{% endhighlight %}

Setup complete.  Switch from root to a normal user.

{% highlight sh %}
exit # sh
exit # su
{% endhighlight %}

### Updating

Casual updates on a development machine can be performed as follows.

{% highlight sh %}
# brunch build --production # if using brunch
MIX_ENV=prod mix phoenix.digest # if static assets could have changed
MIX_ENV=prod mix release
su
sh
PROJECT=phoenix_service
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

Note that the path permissions will need to be fixed again if
you added the release to the systemwide path and want to be able
to run it as any user.

### Troubleshooting

Make sure to set server to true in **config/prod.exs**.
If the server is mysteriously not working, start the release
with console to see error messages.

### What Next?

Consider looking into [edeliver][elixir-edeliver] for deployment.
"edeliver is based on deliver and provides a bash script to build and deploy
Elixir and Erlang applications and perform hot-code upgrades."

## References:
- [Phoenix, Deployment][phoenix-deployment]
- [Phoenix, Building a JSON API With Phoenix][phoenix-json]
- [Phoenix, Building a versioned REST API with Phoenix Framework][phoenix-versioned-rest]
- [Phoenix, Default (4000) port busy][phoenix-default-port]
- [Phoenix, Start Phoenix app with cowboy server on different port][phoenix-custom-port]
- [Phoenix, does not evaluate Env config overrides at runtime][phoenix-runtime-env]
- [Phoenix, Installing Phoenix, Elixir and PostgreSQL on FreeBSD][phoenix-install]
- [Phoenix, A Shell Script for Working with Phoenix JSON APIs][phoenix-script]
- [Elixir Release Manager][elixir-exrm]
- [Elixir, exrm, Release Configuration][elixir-exrm-release-config]
- [Elixir, exrm, Where should I place app.conf and vm.args][elixir-exrm-vm-args]
- [Elixir, exrm, Packages on Hex][elixir-exrm-hex]
- [Elixir, edeliver][elixir-edeliver]
- [Elixir, Mix.Config][elixir-mix-config]
- [Elixir as a Service on FreeBSD][elixir-service]
- [Ruby, adamkittelson's Cap File][ruby-adamkittelson-cap]
- [PostgreSQL, Installing PostgreSQL on FreeBSD][postgresql-install]
- [Sh - the Bourne Shell][sh-tutorial]
- [FreeBSD, KDE4 localization][freebsd-locale]
- [ION DTN as a Service on FreeBSD][freebsd-ion]

[phoenix-deployment]: http://www.phoenixframework.org/docs/deployment
[phoenix-json]: http://learnwithjeff.com/blog/2015/10/03/building-a-json-api-with-phoenix/
[phoenix-versioned-rest]: https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html
[phoenix-default-port]: https://github.com/phoenixframework/phoenix/issues/962
[phoenix-custom-port]: http://stackoverflow.com/questions/30540466/start-phoenix-app-with-cowboy-server-on-different-port
[phoenix-runtime-env]: https://github.com/phoenixframework/phoenix/issues/354
[phoenix-install]: https://sgeos.github.io/phoenix/elixir/postgresql/freebsd/2016/03/19/installing-phoenix-elixir-and-postgresql-on-freebsd.html
[phoenix-script]: https://sgeos.github.io/phoenix/elixir/sh/2016/03/19/a-shell-script-for-working-with-phoenix-json-apis.html
[elixir-exrm]: https://github.com/bitwalker/exrm
[elixir-exrm-release-config]: https://exrm.readme.io/docs/release-configuration
[elixir-exrm-vm-args]: https://github.com/bitwalker/exrm/issues/42
[elixir-exrm-hex]: https://hex.pm/packages?search=exrm
[ruby-adamkittelson-cap]: https://github.com/adamkittelson/apathy-drive-ex/blob/master/config/deploy.rb
[elixir-edeliver]: https://github.com/boldpoker/edeliver
[elixir-mix-config]: http://elixir-lang.org/docs/stable/mix/Mix.Config.html
[elixir-service]: https://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service_on_freebsd.html
[postgresql-install]: https://jasonk2600.wordpress.com/2010/01/11/installing-postgresql-on-freebsd/
[sh-tutorial]: http://www.grymoire.com/Unix/Sh.html
[freebsd-locale]: https://forums.freebsd.org/threads/9120/
[freebsd-ion]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/15/ion-dtn-as-a-service-on-freebsd.html

