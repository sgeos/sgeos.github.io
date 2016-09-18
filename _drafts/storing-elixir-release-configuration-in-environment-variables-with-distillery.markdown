---
layout: post
mathjax: false
comments: true
title:  "Storing Elixir Release Configuration in Environment Variables with Distillery"
date:   2016-09-18 06:31:36 +0000
categories: phoenix elixir erlang ecto distillery postgresql mysql
---
This post covers storing settings like database configuration in
environment variables with [distillery][distillery].
A [prior post][elixir-exrm-env] covered this with the [Elixir Release Manager (exrm)][exrm].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-09-18 06:31:36 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #0 r304324: Thu Aug 18 13:27:23 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ mix hex.info
Hex:    0.13.0
Elixir: 1.3.2
OTP:    19.0.7
* snip *
$ mix phoenix.new -v
Phoenix v1.2.1
$ cat mix.lock | grep distillery | cut -d" " -f 3,6 | sed 's/[",]//g'
distillery: 0.9.9
{% endhighlight %}

## Creating a Sample Project

Create a new Phoenix project.

{% highlight sh %}
mix phoenix.new phoenix_environment_settings --no-brunch
cd phoenix_environment_settings
mix ecto.create
{% endhighlight %}

Create a simple JSON memo endpoint.

{% highlight sh %}
mix phoenix.gen.json Memo memos title:string body:string
{% endhighlight %}

Revise **web/router.ex**.
Uncomment the "/api" scope and add the "/memos" route.

**web/router.ex**.partial listing
{% highlight sh %}
  scope "/api", PhoenixEnvironmentSettings do
    pipe_through :api

    resources "/memos", MemoController, except: [:new, :edit]
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

Start the server.

{% highlight sh %}
mix phoenix.server
{% endhighlight %}

POST and GET a memo to make sure the server works.
A [prior post][blog-json-api-script] covers a shell script
for conveniently interacting with this sample app.

{% highlight sh %}
# POST new
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "New Title", "body": "This is the new memo body."}}' http://localhost:4000/api/memos
# GET id 1
curl -H 'Content-Type: application/json' http://localhost:4000/api/memos/1
{% endhighlight %}

## Environment Variable Definitions

Define the following environment variables.
Feel free to use different values and a static value for **SECRET_KEY_BASE**.
Note that depending on how your database is configured,
**DB_PASSWORD** may be unnecessary for connections from **localhost**.

{% highlight sh %}
export NODE_NAME=leaf_node
export COOKIE=thin_mints
export DB_USER=phoenix_environment_settings
export DB_PASSWORD=phoenix_environment_settings_password
export DB_NAME=phoenix_environment_settings_prod
export DB_HOST=localhost
export HOST=host.example.org
export PORT=7777
export SECRET_KEY_BASE=$(elixir -e ":crypto.strong_rand_bytes(48) |> Base.encode64 |> IO.puts")
{% endhighlight %}

## Configuring the Application

Set server to true in **config/prod.exs**.
Also add a version entry.
Replace static configuration with dynamic configuration that
will be pulled in from environment variables.
None of this needs to be kept out version control,
so it is safe to delete **config/prod.secret.exs**.
Those settings have been merged in.

**config/prod.exs**
{% highlight elixir %}
use Mix.Config

config :phoenix_environment_settings, PhoenixEnvironmentSettings.Endpoint,
  http: [port: {:system, "PORT"}],
  url: [host: "${HOST}", port: {:system, "PORT"}],
  cache_static_manifest: "priv/static/manifest.json",
  server: true,
  root: ".",
  version: Mix.Project.config[:version]

config :logger, level: :info

config :phoenix_environment_settings, PhoenixEnvironmentSettings.Endpoint,
  secret_key_base: "${SECRET_KEY_BASE}"

config :phoenix_environment_settings, PhoenixEnvironmentSettings.Repo,
  adapter: Ecto.Adapters.Postgres,
  username: "${DB_USER}",
  password: "${DB_PASSWORD}",
  database: "${DB_NAME}",
  hostname: "${DB_HOST}",
  pool_size: 20
{% endhighlight %}

Alternatively, keep hard coded values in **config/prod.secret.exs**
when running local release builds and use a version with dynamic
environment variable settings in a real production environment.

**config/prod.secret.exs**
{% highlight elixir %}
use Mix.Config

config :phoenix_environment_settings, PhoenixEnvironmentSettings.Endpoint,
  secret_key_base: "${SECRET_KEY_BASE}"

config :phoenix_environment_settings, PhoenixEnvironmentSettings.Repo,
  adapter: Ecto.Adapters.Postgres,
  username: "${DB_USER}",
  password: "${DB_PASSWORD}",
  database: "${DB_NAME}",
  hostname: "${DB_HOST}",
  pool_size: 20
{% endhighlight %}

Optionally, add dynamic configuration with a default values to **config/dev.exs**.
The environment variable replacement above is **only** suitable for releases.
The interpreted solution below is **only** suitable for development with **mix**.

**config/dev.exs** partial listing
{% highlight elixir %}
config :phoenix_environment_settings, PhoenixEnvironmentSettings.Endpoint,
  http: [port: System.get_env("PORT") || 4000],

# ... at the end of the file ...

# Configure your database
config :phoenix_environment_settings, PhoenixEnvironmentSettings.Repo,
  adapter: Ecto.Adapters.Postgres,
  username: System.get_env("DB_USER") || "postgres",
  password: System.get_env("DB_PASSWORD") || "postgres",
  database: System.get_env("DB_NAME") || "phoenix_environment_settings_dev",
  hostname: System.get_env("DB_HOST") || "localhost",
  pool_size: 10
{% endhighlight %}

## Generating a Release

Add [distillery][distillery] to **mix.exs** as a project dependency.

**mix.exs** partial listing
{% highlight elixir %}
  defp deps do
    [{:phoenix, "~> 1.2.1"},
     {:phoenix_pubsub, "~> 1.0"},
     {:phoenix_ecto, "~> 3.0"},
     {:postgrex, ">= 0.0.0"},
     {:phoenix_html, "~> 2.6"},
     {:phoenix_live_reload, "~> 1.0", only: :dev},
     {:gettext, "~> 0.11"},
     {:distillery, "~> 0.9"}, # this line is new
     {:cowboy, "~> 1.0"}]
  end
{% endhighlight %}

Install and initialize distillery.
This will create the **rel/** directory.

{% highlight sh %}
mix deps.get
mix deps.compile
mix release.init
{% endhighlight %}

Environment variables will be used as knobs to configure the app.
Note that the **REPLACE_OS_VARS=true** environment variable needs to
be defined to use environment variables for dynamic configuration.

The **rel/vm.args** file is primarily used to configure the erlang VM.
It can also be used to define application configuration parameters.
Application configuration parameters defined in this file can be passed
into the program as atoms or integers.
Note that the location of this file can be [configured][distillery-runtime-config]
with the **RELEASE_CONFIG_DIR** environment variable.
Add the following to **rel/vm.args**.

**rel/vm.args**
{% highlight sh %}
## Name of the node
-name ${NODE_NAME}

## Cookie for distributed erlang
-setcookie ${COOKIE}

## App Settings
-phoenix_environment_settings port ${PORT}
{% endhighlight %}

Alternatively, **rel/sys.config** can be used to pass in application configuration parameters.
This file is written in Erlang.

**rel/sys.config**
{% highlight erlang %}
[
  {phoenix_environment_settings, [
    {port, "${PORT}"}
  ]}
].
{% endhighlight %}

The Elixir **config/config.exs** file is probably a better place to
define non-VM settings for an Elixir application.
The **distillery** [documentation][distillery-config] seems to indicate that a release
can either use **sys.config** or **config.exs** but not both.
The exact **config.exs** settings for this project were covered in
the **Configuring the Application** section above.

## Adding Release Tasks

After deploying a release with **distillery**, **mix** is no longer available.
Define a module for release tasks with a `mix ecto.migrate` equivalent.
Note that this is an Erlang module written in Elixir.

**lib/release_tasks.ex**
{% highlight elixir %}
defmodule :release_tasks do
  def migrate do
    {:ok, _} = Application.ensure_all_started(:phoenix_environment_settings)
    path = Application.app_dir(:phoenix_environment_settings, "priv/repo/migrations")
    Ecto.Migrator.run(PhoenixEnvironmentSettings.Repo, path, :up, all: true)
    :init.stop()
  end
end
{% endhighlight %}

After generating a release, this task can be run as follows.

{% highlight sh %}
REPLACE_OS_VARS=true rel/phoenix_environment_settings/bin/phoenix_environment_settings command release_tasks migrate
{% endhighlight %}

The `mix ecto.create` and `mix ecto.drop` tasks are run less frequently
so it probably just makes sense to just manually create or drop the database
and user.  PostgreSQL commands follow.

{% highlight sh %}
# PostgreSQL `mix ecto.create` equivalent
psql -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';"
createdb "${DB_NAME}"
psql -c "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} to ${DB_USER};"

# PostgreSQL `mix ecto.drop` equivalent
dropdb "${DB_NAME}"
dropuser "${DB_USER}"

# PostgresSQL interactive terminal
PGPASSWORD="${DB_PASSWORD}" psql -U "${DB_USER}" "${DB_NAME}"
{% endhighlight %}

The MySQL commands look like this.

{% highlight sh %}
# MySQL `mix ecto.create` equivalent
mysql -e "CREATE USER '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';"
mysql -e "CREATE DATABASE ${DB_NAME};"
mysql -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';"
mysql -e "FLUSH PRIVILEGES;"

# MySQL `mix ecto.drop` equivalent
mysql -e "DROP DATABASE ${DB_NAME};"
mysql -e "DROP USER '${DB_USER}'@'localhost';"

# MySQL interactive terminal
mysql -u"${DB_USER}" -p"${DB_PASSWORD}" "${DB_NAME}"
{% endhighlight %}

Run the `mix ecto.create` equivalent now.

Note that the password security in the above commands is less than ideal.
Also, an existing superuser and password may need to be explicily
specified when creating the new user and database.

## Running the Release

Build the release with the configuration files.

{% highlight sh %}
MIX_ENV=prod mix compile
# brunch build --production # if using brunch
MIX_ENV=prod mix phoenix.digest
MIX_ENV=prod mix release --env=prod
{% endhighlight %}

Run the migration task defined in the **Adding Release Tasks** section.

{% highlight sh %}
REPLACE_OS_VARS=true rel/phoenix_environment_settings/bin/phoenix_environment_settings command release_tasks migrate
{% endhighlight %}

Start the release in the console.

{% highlight sh %}
REPLACE_OS_VARS=true rel/phoenix_environment_settings/bin/phoenix_environment_settings console
{% endhighlight %}

Make sure the server responds.

{% highlight sh %}
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "Memo A", "body": "Alpha memo body."}}' "http://localhost:${PORT}/api/memos"
curl -H 'Content-Type: application/json' -X POST -d '{"memo": {"title": "Memo B", "body": "Beta memo body."}}' "http://localhost:${PORT}/api/memos"
curl "http://localhost:${PORT}/api/memos"
{% endhighlight %}

Exit the console with ^C.

## Custom Application Settings

Add this [configuration gist][config-gist] to **lib/config.ex**.
This [configuration wrapper][distillery-runtime-config] allows the same convenient
`{:system, "VARIABLE", "default"}` convention to be used with both **mix** and releases.
Note that this will not help configure things like **PhoenixEnvironmentSettings.Repo**
because they were not written to get settings via this module.
The linked to version has the typespecs and documentation.

**lib/config.ex**
{% highlight sh %}
defmodule Config do
  def get(app, key, default \\ nil) when is_atom(app) and is_atom(key) do
    case Application.get_env(app, key) do
      {:system, env_var} ->
        case System.get_env(env_var) do
          nil -> default
          val -> val
        end
      {:system, env_var, preconfigured_default} ->
        case System.get_env(env_var) do
          nil -> preconfigured_default
          val -> val
        end
      nil ->
        default
      val ->
        val
    end
  end

  def get_integer(app, key, default \\ nil) do
    case get(app, key, nil) do
      nil -> default
      n when is_integer(n) -> n
      n ->
        case Integer.parse(n) do
          {i, _} -> i
          :error -> default
        end
    end
  end
end
{% endhighlight %}

Add these lines to **config/config.exs**.

**config/config.exs** partial listing
{% highlight sh %}
config :phoenix_environment_settings,
  ecto_repos: [PhoenixEnvironmentSettings.Repo],
  welcome_message: {:system, "WELCOME_MESSAGE", "Hello, world!"},
  magic_number: {:system, "MAGIC_NUMBER", 42}
{% endhighlight %}

Access the settings in `iex -S mix` like this.
You should get the default values.

**iex**
{% highlight elixir %}
Config.get :phoenix_environment_settings, :welcome_message
Config.get_integer :phoenix_environment_settings, :magic_number
{% endhighlight %}

Define the environment variables and run the commands in **iex** again.
You should get the environment variable values this time.

{% highlight sh %}
export WELCOME_MESSAGE="Welcome. Try, but there is no escape."
export MAGIC_NUMBER=-1
{% endhighlight %}

This is useful for defining environment variable knobs to control run time behavior.
It is not a solution for problems that rely on compile time behavior,
like using environment variables to specify [dynamic routes][phoenix-dynamic-gist].

## Other Considerations

Note that when using **REPLACE_OS_VARS=true**, the environment variables in **rel/sys.conf** or
**config/config.exs** will always be replaced with strings.
The following almost certainly does not work as expected.

{% highlight sh %}
export DB_POOL_SIZE=20
{% endhighlight %}

**config/prod.exs** or
**config/prod.secret.exs** partial listing
{% highlight sh %}
  pool_size: "${DB_POOL_SIZE}"
{% endhighlight %}

The following will work in development, but not production.

**config/dev.exs** partial listing
{% highlight sh %}
  pool_size: (System.get_env("DB_POOL_SIZE") || "10") |> String.to_integer
{% endhighlight %}

If integers or atoms need to be passed in directly, use **vm.args**.
The author could not figure out how to pass **DB_POOL_SIZE** to Repo via **vm.args**.

## Next Steps

Consider looking into [conform][conform], a library for working with init-style configuration.
Also consider looking into [edeliver][edeliver] for deployment.

## References:

- [Distillery][distillery]
- [Distillery, Configuration][distillery-config]
- [Distillery, Runtime Configuration][distillery-runtime-config]
- [Elixir Release Manager (exrm)][exrm]
- [Elixir Release Manager Configuration][exrm-config]
- [Elixir Release Manager, How to config environment variables with Elixir and Exrm][exrm-environment-config]
- [Elixir Release Manager, Running migration in an Exrm release][exrm-migration]
- [Elixir Release Manager, How to run Ecto migrations from an exrm release][exrm-migration-gist]
- [Elixir, Useful Config Wrapper Gist][config-gist]
- [Elixir, Understanding Config in Elixir][elixir-understanding-config]
- [Elixir as a Service on FreeBSD][elixir-service]
- [Elixir, Storing Elixir Release Configuration in Environment Variables with exrm][elixir-exrm-env]
- [Elixir, conform][conform]
- [Elixir, edeliver][edeliver]
- [Erlang, man erl][erlang-man-erl]
- [Erlang, man config][erlang-man-config]
- [Phoenix, Dynamic Dispatch Gist][phoenix-dynamic-gist]
- [Phoenix, A Shell Script for Working with Phoenix JSON APIs][blog-json-api-script]
- [Phoenix as a Service on FreeBSD][phoenix-service]
- [Mix, Accessing Mix tasks from release][mix-release]
- [Mix, exrm PostgreSQL/MySQL release equivalents for `mix ecto.create` and `mix ecto.drop`.][mix-ecto-gist]

[exrm]: https://github.com/bitwalker/exrm
[exrm-config]: https://exrm.readme.io/docs/release-configuration
[exrm-environment-config]: http://blog.plataformatec.com.br/2016/05/how-to-config-environment-variables-with-elixir-and-exrm/
[exrm-migration]: http://blog.plataformatec.com.br/2016/04/running-migration-in-an-exrm-release/
[exrm-migration-gist]: https://gist.github.com/antipax/90cc36d29c2a2a5d4629
[config-gist]: https://gist.github.com/bitwalker/a4f73b33aea43951fe19b242d06da7b9
[elixir-understanding-config]: http://sheldonkreger.com/understanding-config-in-elixir.html
[elixir-service]: http://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service_on_freebsd.html
[elixir-exrm-env]: https://sgeos.github.io/phoenix/elixir/erlang/ecto/exrm/postgresql/mysql/2016/09/11/storing-elixir-release-configuration-in-environment-variables.html
[erlang-man-erl]: http://erlang.org/doc/man/erl.html
[erlang-man-config]: http://erlang.org/doc/man/config.html
[phoenix-dynamic-gist]: https://gist.github.com/chrismccord/e0eaefe30d2ecd85b4ac
[blog-json-api-script]: https://sgeos.github.io/phoenix/elixir/sh/2016/03/19/a-shell-script-for-working-with-phoenix-json-apis.html
[phoenix-service]: https://sgeos.github.io/phoenix/elixir/erlang/freebsd/2016/03/21/phoenix-as-a-service-on-freebsd.html
[mix-release]: https://github.com/bitwalker/exrm/issues/67#issuecomment-183457937
[mix-ecto-gist]: https://gist.github.com/sgeos/1fed5eb24d80b97a338249dd95d55082
[distillery]: https://github.com/bitwalker/distillery
[distillery-config]: https://hexdocs.pm/distillery/runtime-configuration.html
[distillery-runtime-config]: https://hexdocs.pm/distillery/runtime-configuration.html
[conform]: https://github.com/bitwalker/conform
[edeliver]: https://github.com/boldpoker/edeliver

