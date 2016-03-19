---
layout: post
comments: true
title:  "Phoenix as a Service on FreeBSD"
date:   2016-03-19 00:55:41 +0000
categories: phoenix elixir freebsd
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

This post assumes PostgreSQL is [already installed][postgresql-install].
If **portmaster** and **sudo** are not installed you are on your own for installation.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-19 00:55:41 +0000
$ mix hex.info
Hex:    0.11.3
Elixir: 1.2.3
OTP:    18.2.4
* snip *
$ mix phoenix.new -v
Phoenix v1.1.4
{% endhighlight %}

## Instructions

First, install Elixir and Phoenix.

{% highlight sh %}
sudo portmaster lang/elixir
mix local.hex
mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez
{% endhighlight %}

Optionally, install **npm** and **brunch**.

{% highlight sh %}
sudo portmaster www/node www/npm
sudo npm install -g brunch
{% endhighlight %}

# Creating a Sample Project

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

# Testing the Sample Project

Start the server.

{% highlight sh %}
mix phoenix.server
{% endhighlight %}

Create a script to POST and GET memos.
Yes, the payload quoting is insane.
Read a [Bourne Shell tutorial][sh-tutorial] if you need help figuring it out.

**memo_api.sh**
{% highlight sh %}
#!/bin/sh

HOST=http://localhost:4000
SCOPE=api
ROUTE=memos
HEADERS="Content-Type: application/json"

case "${1}" in
  get)
    curl -H "${HEADERS}" -X GET "${HOST}/${SCOPE}/${ROUTE}"
    ;;
  post)
    PAYLOAD='{"memo": {"title": "'"${2-"(no title)"}"'", "body": "'"${3-"(no body"}"'"}}'
    curl -H "${HEADERS}" -X POST -d "${PAYLOAD}" "${HOST}/${SCOPE}/${ROUTE}" 
    ;;
  *) #*
    echo "Usage:"
    echo "  ${0} get"''
    echo "  ${0} "'post "title" "body"'
    ;;
esac
echo ""
{% endhighlight %}

POST and GET a message with the above script.

{% highlight sh %}
chmod +x memo_api.sh
./memo_api.sh post "Memo Title" "This is the memo body."
./memo_api.sh get
{% endhighlight %}

# Generating a Release

Now that the Phoenix app is working, it is time to set it up as a service.

# Installing the Release as a Service

Install as a service.

## References:
- [Phoenix, Deployment][phoenix-deployment]
- [Phoenix, Building a JSON API With Phoenix][phoenix-json]
- [Phoenix, Building a versioned REST API with Phoenix Framework][phoenix-versioned-rest]
- [Elixir as a Service on FreeBSD][elixir-service]
- [PostgreSQL, Installing PostgreSQL on FreeBSD][postgresql-install]
- [Sh - the Bourne Shell][sh-tutorial]

[phoenix-deployment]: http://www.phoenixframework.org/docs/deployment
[phoenix-json]: http://learnwithjeff.com/blog/2015/10/03/building-a-json-api-with-phoenix/
[phoenix-versioned-rest]: https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html
[elixir-service]: https://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service_on_freebsd.html
[postgresql-install]: https://jasonk2600.wordpress.com/2010/01/11/installing-postgresql-on-freebsd/
[sh-tutorial]: http://www.grymoire.com/Unix/Sh.html

