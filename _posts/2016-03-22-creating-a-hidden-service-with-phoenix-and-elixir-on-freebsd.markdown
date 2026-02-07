---
layout: post
comments: true
title:  "Creating a Hidden Service with Phoenix and Elixir on FreeBSD"
date:   2016-03-22 06:45:48 +0000
categories: tor freebsd nc curl
---

<!-- A30 -->

This post is a synthesis of a couple of prior posts.

- [Phoenix as a Service on FreeBSD][freebsd-phoenix]
- [Getting Started With tor Hidden Services on FreeBSD][freebsd-tor]

It covers configuration and deployment of simple Phoenix application as a [tor][tor] hidden service.
Important topics like Phoenix auth, and properly securing a hidden service are not covered.

**security/tor** needs to be installed.

{% highlight sh %}
portmaster security/tor
{% endhighlight %}

Phoenix, Elixir and PostgreSQL also need to [be installed][freebsd-phoenix-install].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-22 06:45:48 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ tor --version
Tor version 0.2.7.6.
$ curl --version
curl 7.47.0 (amd64-portbld-freebsd11.0) libcurl/7.47.0 OpenSSL/1.0.2e zlib/1.2.8
Protocols: dict file ftp ftps gopher http https imap imaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp 
Features: AsynchDNS IPv6 Largefile GSS-API Kerberos SPNEGO NTLM NTLM_WB SSL libz TLS-SRP UnixSockets 
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

The sample project will be a simple memo JSON API service.
A real service will almost certainly need some sort of authentication,
but that is not covered in this post.

{% highlight sh %}
mix phoenix.gen.json Memo memos title:string body:string
{% endhighlight %}

Revise the **web/router.ex** file.
The “/api” scope needs to be uncommented and the “/memos” route needs to be added.

**web/router.ex**
{% highlight elixir %}
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

Configure the app to only serve localhost (127.0.0.1) in **config/prod.exs**.
Also make sure server is set to true and a dynamic port configuration is used.

**config/prod.exs** partial listing
{% highlight elixir %}
config :phoenix_service, PhoenixService.Endpoint,
  http: [port: {:system, "PORT"}, ip: {127,0,0,1}], # serve localhost with dynamic port
  url: [host: "example.com", port: 80],
  cache_static_manifest: "priv/static/manifest.json", # added comma
  server: true # this line is new
{% endhighlight %}

Optionally, configure the IP address and add a dynamic port configuration
with a default value to **config/dev.exs**.
The above dynamic port solution is suitable for releases.
The interpreted solution below is suitable for development.

**config/dev.exs** partial listing
{% highlight elixir %}
  # http: [port: 4000], # old line 10
  http: [port: System.get_env("PORT") || Application.get_env(:phoenix_service, :port) || 4000, ip: {127,0,0,1}],
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
A [prior post][phoenix-json] covers a shell script for conveniently interacting with this sample app.

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
curl http://localhost:7777/api/memos
{% endhighlight %}

Exit the console with ^C.

Consider [configuring the Phoenix app as a service][freebsd-phoenix]
to get it to start automatically when the machine boots.

## Serving a Hidden Service

Content needs to be served to a port on localhost.
This post will use port 8080.

{% highlight sh %}
RELX_REPLACE_OS_VARS=true PORT=8080 rel/phoenix_service/bin/phoenix_service start
{% endhighlight %}

Read the [tor configuration instructions][tor-config].
Open **/usr/local/etc/tor/torrc** (see [torrc instructions][tor-torrc]).
Add the following lines to the section titled
"This section is just for location-hidden services".

**/usr/local/etc/tor/torrc** partial listing
{% highlight sh %}
HiddenServiceDir /usr/home/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8080
{% endhighlight %}

Enable **tor** in **/etc/rc.conf**

**/etc/rc.conf** partial listing
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

Test your hidden service with **curl** by supplying the tor proxy with the -x option.
The -v flag gives verbose output.

{% highlight sh %}
# POST new
curl -v -x socks5h://127.0.0.1:9050 -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://$(cat /usr/home/tor/hidden_service/hostname)/api/memos
# GET id 1
curl -v -x socks5h://127.0.0.1:9050 -H 'Content-Type: application/json' http://$(cat /usr/home/tor/hidden_service/hostname)/api/memos/1
{% endhighlight %}

You can also test your hidden service with [Tor2web][tor-tor2web].
For example, if your hidden service has a hostname of ABCDEFGHIJKLMNOP.onion,
go to https://ABCDEFGHIJKLMNOP.onion.to to view it in a web browser.

The author of this post could not get Tor2web **curl** commands to work with a Phoenix app.
Something like the following commands should theoretically work.
Note that Tor2web blocks the curl user agent, so the user agent is set to test instead.

{% highlight sh %}
# POST new
curl -v -A test -x socks5h://127.0.0.1:9050 -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://$(cat /usr/home/tor/hidden_service/hostname).to/api/memos
# GET id 1
curl -v -A test -x socks5h://127.0.0.1:9050 -H 'Content-Type: application/json' http://$(cat /usr/home/tor/hidden_service/hostname).to/api/memos/1
{% endhighlight %}

To disable **tor** when you no longer need to use it, stop it with the **service** command.
{% highlight sh %}
service tor stop
{% endhighlight %}

Then disable it in **/etc/rc.conf**.
{% highlight sh %}
tor_enable="NO"
{% endhighlight %}

## A Sample Shell Script for Working With Hidden Phoenix JSON APIs

This is a modified version of the script covered in
[Phoenix, A Shell Script for Working with Phoenix JSON APIs][phoenix-json].
See that post for a description of the script.

Support for flags has been added.
The flags default to using the tor proxy.
The default host has been changed to automatically
pull in the hidden service hostname.

**tor_memo_api.sh**
{% highlight sh %}
#!/bin/sh

reset() {
  HOST=http://$(cat /usr/home/tor/hidden_service/hostname)
  SCOPE=api
  ROUTE=memos
  METHOD="GET"
  FLAGS="-x socks5h://127.0.0.1:9050"
  HEADERS="Content-Type: application/json"
  ID=""
  TITLE=""
  BODY=""
}

usage() {
  reset
  echo "Usage:  ${0} [options]"
  echo "Options:"
  echo "  -o HOST : set URL host, defaults to \"${HOST}\""
  echo "  -s SCOPE : set URL scope, defaults to \"${SCOPE}\""
  echo "  -r ROUTE : set URL route, defaults to \"${ROUTE}\""
  echo "  -X METHOD : set HTTP method, defaults to \"${METHOD}\""
  echo "  -f FLAGS : set flags passed to curl, defaults to \"${FLAGS}\""
  echo "  -H HEADERS : set HTTP headers, defaults to \"${HEADERS}\""
  echo "  -i ID : set memo id, defaults to \"${ID}\""
  echo "  -t TITLE : set memo title, defaults to \"${TITLE}\""
  echo "  -b BODY : set memo body, defaults to \"${BODY}\""
  echo "  -h : display this help"
  echo "Examples:"
  echo "  ${0} -X GET"
  echo "  ${0} -X GET -i 7"
  echo "  ${0} -X POST -t \"Memo Title\" -b \"Memo body here.\""
  echo "  ${0} -X PATCH -t \"Patched title.\" -i 7"
  echo "  ${0} -X PATCH -b \"Patched body.\" -i 7"
  echo "  ${0} -X PUT -t \"New Title\" -b \"New body.\" -i 7"
  echo "  ${0} -X DELETE -i 7"
  exit ${1}
}

reset
while getopts "o:s:r:X:f:H:i:t:b:h" opt
do
  case "${opt}" in
    o) HOST="${OPTARG}" ;;
    s) SCOPE="${OPTARG}" ;;
    r) ROUTE="${OPTARG}" ;;
    X) METHOD="${OPTARG}" ;;
    f) FLAGS="${OPTARG}" ;;
    H) HEADERS="${OPTARG}" ;;
    i) ID="${OPTARG}" ;;
    t) TITLE="${OPTARG}" ;;
    b) BODY="${OPTARG}" ;;
    h) usage 1 ;;
    \?) usage 2 ;;
  esac
done
shift $(expr ${OPTIND} - 1)

case "${METHOD}" in
  GET)
    curl ${FLAGS} -H "${HEADERS}" -X ${METHOD} "${HOST}/${SCOPE}/${ROUTE}${ID:+"/${ID}"}"
    ;;
  POST)
    PAYLOAD='{"memo": {"title": "'"${TITLE:-(no title)}"'", "body": "'"${BODY:-(no body)}"'"}}'
    curl ${FLAGS} -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}" 
    ;;
  PUT)
    PAYLOAD='{"memo": {"title": "'"${TITLE:-(no title)}"'", "body": "'"${BODY:-(no body)}"'"}}'
    curl ${FLAGS} -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}" 
    ;;
  PATCH)
    # if defined replace individual fields with
    # JSON fragments followed by a comma and space
    TITLE=${TITLE:+"\"title\": \"${TITLE}\", "}
    BODY=${BODY:+"\"body\": \"${BODY}\", "}
    # strip trailing comma and space
    PAYLOAD="$(echo "${TITLE}${BODY}" | sed 's/, $//g')"
    # complete JSON payload
    PAYLOAD="{\"memo\": {${PAYLOAD}}}"
    curl ${FLAGS} -H "${HEADERS}" -X ${METHOD} -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}" 
    ;;
  DELETE)
    curl ${FLAGS} -H "${HEADERS}" -X ${METHOD} "${HOST}/${SCOPE}/${ROUTE}/${ID:?'No ID specified.'}"
    ;;
  *)
    usage 2
    ;;
esac
echo ""
{% endhighlight %}

As written, the above script can only be run as root or the tor
user because **/usr/home/tor** does not have global read permissions.
Changing the permissions is a bad idea.
Instead, hard code the default host if you want to
be able to use the script with unprivileged users.

**tor_memo_api.sh** partial listing
{% highlight sh %}
HOST="http://abcdefghijklmnop.onion"
{% endhighlight %}

The script can be used as follows.

{% highlight sh %}
chmod +x tor_memo_api.sh
./tor_memo_api.sh -X POST -t "Memo Title" -b "Memo body here."
./tor_memo_api.sh -X GET -i 1
./tor_memo_api.sh -X POST -t "Another Memo" -b "This memo's body."
./tor_memo_api.sh -X PATCH -t "Patched title." -i 2
./tor_memo_api.sh -X PATCH -b "Patched body." -i 1
./tor_memo_api.sh -X PUT -t "New Title" -b "New body." -i 2
./tor_memo_api.sh -X GET
./tor_memo_api.sh -X DELETE -i 1
{% endhighlight %}

## References:

- [Elixir Release Manager][elixir-exrm]
- [Elixir, exrm, Release Configuration][elixir-exrm-release-config]
- [Phoenix, A Shell Script for Working with Phoenix JSON APIs][phoenix-json]
- [Tor Project][tor]
- [Tor, Tor2web][tor-tor2web]
- [Tor, Configuring Hidden Services for Tor][tor-config]
- [Tor, Edit torrc][tor-torrc]
- [Tor, HTTP connection closed on: Excess found in a non pipelined read][tor-curl]
- [Tor, StackOverflow, curl an .onion url over an http proxy does not return expected source][tor-curl-onion]
- [FreeBSD, Man curl][man-curl]
- [FreeBSD, Phoenix as a Service on FreeBSD][freebsd-phoenix]
- [FreeBSD, Getting Started With tor Hidden Services on FreeBSD][freebsd-tor]
- [FreeBSD, Installing Phoenix, Elixir and PostgreSQL on FreeBSD][freebsd-phoenix-install]

[elixir-exrm]: https://github.com/bitwalker/exrm
[elixir-exrm-release-config]: https://exrm.readme.io/docs/release-configuration
[phoenix-json]: https://sgeos.github.io/phoenix/elixir/sh/2016/03/19/a-shell-script-for-working-with-phoenix-json-apis.html
[tor]:                     https://www.torproject.org/index.html.en
[tor-tor2web]:             https://tor2web.org
[tor-config]:              https://www.torproject.org/docs/tor-hidden-service.html.en
[tor-torrc]:               https://www.torproject.org/docs/faq.html.en#torrc
[tor-curl]:                https://github.com/curl/curl/issues/232
[tor-curl-onion]:          http://stackoverflow.com/questions/18146295/curl-an-onion-url-over-an-http-proxy-does-not-return-expected-source
[man-curl]:                https://www.freebsd.org/cgi/man.cgi?query=curl&manpath=SuSE+Linux/i386+11.3
[freebsd-phoenix]: https://sgeos.github.io/phoenix/elixir/erlang/freebsd/2016/03/21/phoenix-as-a-service-on-freebsd.html
[freebsd-tor]: https://sgeos.github.io/tor/freebsd/nc/curl/2016/02/06/getting-started-with-tor-hidden-services-on-freebsd.html
[freebsd-phoenix-install]: https://sgeos.github.io/phoenix/elixir/postgresql/freebsd/2016/03/19/installing-phoenix-elixir-and-postgresql-on-freebsd.html

