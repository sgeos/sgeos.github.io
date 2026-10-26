---
layout: post
comments: true
title:  "Installing Phoenix, Elixir and PostgreSQL on FreeBSD"
date: 2016-03-20 07:35:02 +0000
categories: phoenix elixir postgresql freebsd
---

<!-- A28 -->
<script>console.log("A28");</script>

This post covers installing Phoenix, Elixir and PostgreSQL on a clean installation of FreeBSD.
The post assumes FreeBSD is installed and you have created an unprivileged user.
FreeBSD installation instructions can be found [here][freebsd_install].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-19 07:35:02 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r296925: Wed Mar 16 20:53:04 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ psql --version
psql (PostgreSQL) 9.4.6
$ mix hex.info
Hex:    0.11.3
Elixir: 1.2.3
OTP:    18.2.4
* snip *
$ mix phoenix.new -v
Phoenix v1.1.4
{% endhighlight %}

## Bootstrapping the system

Login as root and install **portmaster**.
If you are using packages instead of ports, you will need to
install packages instead of using **portmaster**.

{% highlight sh %}
portsnap fetch extract
(cd /usr/ports/ports-mgmt/portmaster && make config-recursive && make config-recursive && make install clean)
portmaster security/sudo
{% endhighlight %}

The following utilities may also be useful.
Note that **ftp/curl** is used at the end of the post.

{% highlight sh %}
portmaster ports-mgmt/portupgrade devel/git shells/bash editors/vim ftp/curl ftp/wget
{% endhighlight %}

## Installing PostgreSQL

Install **databases/postgresql94-server** as root.
If you would rather install a different version, do that instead.

{% highlight sh %}
portmaster databases/postgresql94-server
{% endhighlight %}

Initialize the database.

{% highlight sh %}
service postgresql initdb
{% endhighlight %}

If you want to enable remote connections,
add the following line to **/usr/local/pgsql/data/postgresql.conf**.

{% highlight sh %}
listen_addresses = '*'
{% endhighlight %}

If you want to change the port PostgreSQL listens on,
add the following line to **/usr/local/pgsql/data/postgresql.conf**.
Replace 5432 with the port you want to use.

{% highlight sh %}
port = 5432                            # (change requires restart)
{% endhighlight %}

To use password hash authentication,
add the following line to **/usr/local/pgsql/data/pg_hba.conf**.
Replace 192.168.0.0/16 with your own network.
Consider changing "trust" to "md5" for local and loopback IP address connections.

{% highlight sh %}
host    all             all             192.168.0.0/16          md5
{% endhighlight %}

Enable PostgreSQL in **/etc/rc.conf**.

{% highlight sh %}
echo 'postgresql_enable="YES"' >> /etc/rc.conf
{% endhighlight %}

Start PostgreSQL.

{% highlight sh %}
service postgresql start
{% endhighlight %}

Add a PostgreSQL super-user with database and role creation privileges.
Replace username with your unprivileged FreeBSD user login.

{% highlight sh %}
su pgsql
createuser -sdrP username
{% endhighlight %}

You should now be able to start **psql** as your non-root user.

{% highlight sh %}
psql
{% endhighlight %}

## Installing Elixir and Phoenix

Install Elixir and Phoenix.

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

Create a simple JSON memo service.

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

Tests should pass.

{% highlight sh %}
mix test
{% endhighlight %}

# Running the Sample Project

Start the server.

{% highlight sh %}
mix phoenix.server
{% endhighlight %}

The following **curl** commands can be used to interact with the running JSON API.
My [previous post][phoenix_shell] covers a shell script for interacting with this sample app.

{% highlight sh %}
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://localhost:4000/api/memos
# PATCH id 1
curl -H 'Content-Type: application/json' -X PATCH -d '{"memo": {"title": "Patched Title"}}' http://localhost:4000/api/memos/1
curl -H 'Content-Type: application/json' -X PATCH -d '{"memo": {"body": "Patched memo body."}}' http://localhost:4000/api/memos/1
# PUT id 1
curl -H 'Content-Type: application/json' -X PUT -d '{"memo": {"title": "Updated Title", "body": "Updated memo body."}}' http://localhost:4000/api/memos/1
# GET all
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos/1
# DELETE id 1
curl -H 'Content-Type: application/json' -X DELETE http://localhost:4000/api/memos/1
{% endhighlight %}

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- "FreeBSD, Installing FreeBSD." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/bsdinstall.html][freebsd_install]
- "Phoenix, Deployment." n.d. www.phoenixframework.org. Accessed October 25, 2026. [http://www.phoenixframework.org/docs/deployment][phoenix_deployment]

### General Sources

- Baird, Jeffrey. n.d. "Building a JSON API with Phoenix." Accessed October 25, 2026. [http://learnwithjeff.com/blog/2015/10/03/building-a-json-api-with-phoenix/][phoenix_json]
- Barnett, Bruce. n.d. "Bourne Shell Tutorial." Accessed October 25, 2026. [http://www.grymoire.com/Unix/Sh.html][sh_tutorial]
- "Installation and Configuration." n.d. Accessed October 25, 2026. [http://www.freebsddiary.org/postgresql.php][postgresql_install3]
- "Installing and Using Postgresql on FreeBSD." 2010. *Rhyous*, August 28. [http://www.rhyous.com/2010/08/27/installing-and-using-postgresql-on-freebsd/][postgresql_install2]
- "Phoenix, Building a versioned REST API with Phoenix Framework." n.d. Accessed October 25, 2026. [https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html][phoenix_versioned_rest]
- "PostgreSQL, Installing PostgreSQL on FreeBSD." n.d. Accessed October 25, 2026. [https://jasonk2600.wordpress.com/2010/01/11/installing-postgresql-on-freebsd/][postgresql_install]

### Related Posts

- Sechter, Brendan. 2016. "Elixir as a Service on FreeBSD." *Brendan A R Sechter's Development Blog*, January 16. [https://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service\_on\_freebsd.html][elixir_service]
- Sechter, Brendan. 2016. "A Shell Script for Working with Phoenix JSON APIs." *Brendan A R Sechter's Development Blog*, March 19. [https://sgeos.github.io/phoenix/elixir/sh/2016/03/19/a-shell-script-for-working-with-phoenix-json-apis.html][phoenix_shell]

[elixir_service]: {% post_url 2016-01-16-elixir-as-a-service_on_freebsd %}
[freebsd_install]: https://www.freebsd.org/doc/handbook/bsdinstall.html
[phoenix_deployment]: http://www.phoenixframework.org/docs/deployment
[phoenix_json]: http://learnwithjeff.com/blog/2015/10/03/building-a-json-api-with-phoenix/
[phoenix_shell]: {% post_url 2016-03-19-a-shell-script-for-working-with-phoenix-json-apis %}
[phoenix_versioned_rest]: https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html
[postgresql_install]: https://jasonk2600.wordpress.com/2010/01/11/installing-postgresql-on-freebsd/
[postgresql_install2]: http://www.rhyous.com/2010/08/27/installing-and-using-postgresql-on-freebsd/
[postgresql_install3]: http://www.freebsddiary.org/postgresql.php
[sh_tutorial]: http://www.grymoire.com/Unix/Sh.html
