---
layout: post
comments: true
title:  "Authenticating a Phoenix JSON API with Guardian"
date:   2016-03-23 16:52:59 +0000
categories: phoenix elixir
---
This post covers authenticating a Phoenix JSON API with Guardian.
Guardian was chosen because it is popular and it can be used for channel and socket authentication.
My goal is to create a bare bones JSON API that is suitable for mobile consumption.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-23 16:52:59 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r297174: Tue Mar 22 18:13:05 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
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
mix phoenix.new memo_api --no-brunch
cd memo_api
mix ecto.create
{% endhighlight %}

In **mix.exs**, do the following.

- add :comeonin as an application dependency
- add :comeonin as a project dependency
- add :guardian as an application dependency
- add :guardian as a project dependency

**mix.exs** partial listing
{% highlight elixir %}
  def application do
    [mod: {MemoApi, []},
     applications: [:phoenix, :phoenix_html, :cowboy, :logger, :gettext,
                    :phoenix_ecto, :postgrex, :comeonin, :guardian]] # modified
  end 

  # skip some lines

  defp deps do
    [{:phoenix, "~> 1.1.4"},
     {:postgrex, ">= 0.0.0"},
     {:phoenix_ecto, "~> 2.0"},
     {:phoenix_html, "~> 2.4"},
     {:phoenix_live_reload, "~> 1.0", only: :dev},
     {:gettext, "~> 0.9"},
     {:comeonin, "~> 2.1"}, # modified
     {:guardian, "~> 0.10.0"}, # modified
     {:cowboy, "~> 1.0"}]
  end 
{% endhighlight %}

Get dependencies.

{% highlight sh %}
mix deps.get
{% endhighlight %}

Add Guardian settings to **config.exs**.

**config.exs** partial listing
{% highlight elixir %}
config :guardian, Guardian,
  allowed_algos: ["HS512"], # optional
  verify_module: Guardian.JWT,  # optional
  issuer: "MemoApi",
  ttl: { 30, :days },
  verify_issuer: true, # optional
  secret_key: "", # replace with guardian secret key
  serializer: MemoApi.GuardianSerializer
{% endhighlight %}

Note that the following command can be used to generate a secret key from the command line.

{% highlight sh %}
elixir -e ":crypto.strong_rand_bytes(48) |> Base.encode64 |> IO.puts"
{% endhighlight %}

Add a serializer to encode and decode resources into and out of tokens.

**memo_api/guardian_serializer.ex**
{% highlight elixir %}
defmodule MemoApi.GuardianSerializer do
  @behaviour Guardian.Serializer

  alias MemoApi.Repo
  alias MemoApi.User

  def for_token(user = %User{}), do: { :ok, "User:#{user.id}" }
  def for_token(_), do: { :error, "Unknown resource type" }

  def from_token("User:" <> id), do: { :ok, Repo.get(User, id) }
  def from_token(_), do: { :error, "Unknown resource type" }
end
{% endhighlight %}

Optionally, during tests reduce the number of bcrypt, or pbkdf2 rounds to speed things up.

**config/test.exs** partial listing
{% highlight elixir %}
config :comeonin, :bcrypt_log_rounds, 4
config :comeonin, :pbkdf2_rounds, 1
{% endhighlight %}

Create user and memo models.

{% highlight sh %}
mix phoenix.gen.json User users email:string password_hash:string
mix phoenix.gen.json Memo memos title:string body:text user_id:references:users
{% endhighlight %}

In **web/router.ex** do the following.

- uncomment the "/api" scope
- add the "/users" route
- add the "/memos" route

**web/router.ex** partial listing
{% highlight elixir %}
  scope "/api", MemoApi do
    pipe_through :api

    resources "/users", UserController, except: [:new, :edit]
    resources "/memos", MemoController, except: [:new, :edit]
  end
{% endhighlight %}

Add a foreign_key to **web/models/memo.ex** and make **:user_id** a required field.

**web/models/memo.ex** partial listing
{% highlight elixir %}
  schema "memos" do
    field :title, :string
    field :body, :string
    belongs_to :user, MemoApi.User, foreign_key: :user_id # modified

    timestamps
  end

  @required_fields ~w(title body user_id) # modified
  @optional_fields ~w()
{% endhighlight %}

Add the following to  **web/models/user.ex**.

- a has_many :memos relationship
- a virtual password field
- changeset unique email validation
- changeset password length validation
- changeset password hashing

**web/models/user.ex**
{% highlight elixir %}
defmodule MemoApi.User do
  use MemoApi.Web, :model
  import Comeonin.Bcrypt, only: [hashpwsalt: 1]

  schema "users" do
    field :email, :string
    field :password_hash, :string
    field :password, :string, virtual: true

    has_many :memos, MemoApi.Memo

    timestamps
  end 

  @required_fields ~w(email password_hash)
  @optional_fields ~w()

  def changeset(model, params \\ :empty) do
    model
    |> cast(params, @required_fields, @optional_fields)
    |> unique_constraint(:email)
    |> validate_length(:password, min: 6)
    |> hash_password
  end 

  defp hash_password(changeset) do
    if password = get_change(changeset, :password) do
      changeset
      |> put_change(:password_hash, hashpwsalt(password))
    else
      changeset
    end
  end
end
{% endhighlight %}

Remove password and password_hash from the render function in in **web/views/user_view.ex**.

**web/views/user_view.ex** partial listing
{% highlight elixir %}
  def render("user.json", %{user: user}) do
    %{id: user.id,
      email: user.email}
  end
{% endhighlight %}

Make the email address a unique index in the **create_user.exs** migration.

**priv/repo/migrations/yyyymmddhhmmss_create_user.exs** timestamp will differ
{% highlight elixir %}
defmodule MemoApi.Repo.Migrations.CreateUser do
  use Ecto.Migration

  def change do
    create table(:users) do
      add :email, :string
      add :password_hash, :string

      timestamps
    end 

    create unique_index(:users, [:email])
  end 
end
{% endhighlight %}

Migrate the database.

{% highlight sh %}
mix ecto.migrate
{% endhighlight %}

Fixing the broken tests is left as an exercise for the reader.

{% highlight sh %}
mix test
{% endhighlight %}

## Adding Authorization

**web/router.ex**
{% highlight sh %}
  post "/login", AuthenticationController, :create
{% endhighlight %}


## References:
- [Phoenix, Getting Started with Guardian][phoenix-guardian-started]
- [Phoenix, Elixir - Phoenix: Simple Authentication][phoenix-simple-auth]
- [Phoenix, Building a versioned REST API with Phoenix Framework][phoenix-versioned-rest]
- [Phoenix, How to add and test HTTP basic authentication in a Phoenix web application][phoenix-basic-auth]
- [Phoenix, Authentication/Authorization for Phoenix apps][phoenix-auth-reddit]
- [Phoenix, Routing][phoenix-routing]
- [Phoenix, Controllers][phoenix-controllers]
- [Phoenix, Elixir blog in 15 minutes using Phoenix framework - Step by Step][phoenix-blog]
- [Phoenix, Mix.Tasks.Phoenix.Gen.Json][phoenix-mix-gen-json]
- [Phoenix, Ecto Models][phoenix-ecto-models]
- [Phoenix as a Service on FreeBSD][phoenix-freebsd]
- [Elixir, alias, require and import][elixir-import]
- [Elixir, Access project version within elixir application][elixir-otp-vsn]
- [Elixir, Comeonin GitHub][elixir-comeonin]
- [Elixir, Guardian GitHub][elixir-guardian-github]
- [Elixir Nation, Guardian][elixir-guardian]
- [Elixir Nation, Category: Authentication Listing][elixir-auth-listing]
- [Erlang, Building OTP Applications][erlang-otp]
- [Mix, ecto/lib/mix/tasks/ecto.gen.migration.ex Source Code][mix-migration-source]
- [Rails, railties/lib/rails_generator/commands.rb Source Code][mix-migration-source]
- [HTTP, Re: 401 Unauthenticated, 403 Unauthorized?][http-401]
- [JWT, RFC 7519 JSON Web Token (JWT)][rfc-7519]
- [UNIX, What Is The Difference Between Authentication And Authorization?][unix-auth]

[phoenix-guardian-started]: http://hassox.github.io/elixir/guardian/2015/06/19/guardian-getting-started.html
[phoenix-simple-auth]: http://blog.simonstrom.xyz/elixir-phoenix-simple-authentication/
[phoenix-versioned-rest]: https://renatomoya.github.io/2015/05/09/Building-a-versioned-REST-API-with-Phoenix-Framework.html
[phoenix-basic-auth]: http://www.cultivatehq.com/posts/add-basic-authentication-to-a-phoenix-application/
[phoenix-auth-reddit]: https://www.reddit.com/r/elixir/comments/3ijbrd/authenticationauthorization_for_phoenix_apps/
[phoenix-routing]: http://www.phoenixframework.org/v0.11.0/docs/routing
[phoenix-controllers]: http://www.phoenixframework.org/docs/controllers
[phoenix-blog]: http://codetunes.com/2015/phoenix-blog/
[phoenix-mix-gen-json]: https://hexdocs.pm/phoenix/Mix.Tasks.Phoenix.Gen.Json.html
[phoenix-ecto-models]: http://www.phoenixframework.org/docs/ecto-models
[phoenix-freebsd]: https://sgeos.github.io/phoenix/elixir/erlang/freebsd/2016/03/21/phoenix-as-a-service-on-freebsd.html
[elixir-import]: http://elixir-lang.org/getting-started/alias-require-and-import.html
[elixir-otp-vsn]: http://stackoverflow.com/questions/32968253/access-project-version-within-elixir-application
[elixir-comeonin]: https://github.com/elixircnx/comeonin
[elixir-guardian-github]: https://github.com/ueberauth/guardian
[elixir-guardian]: https://elixirnation.io/libraries/guardian-authentication-framework-with-jwt-for-elixir
[elixir-auth-listing]: https://elixirnation.io/libraries/category/authentication
[erlang-otp]: http://learnyousomeerlang.com/building-otp-applications
[mix-migration-source]: https://github.com/elixir-lang/ecto/blob/master/lib/mix/tasks/ecto.gen.migration.ex#L61-L64
[rails-migration-source]: https://github.com/rails/rails/commit/c00de99f69358b58ca2bd6bc732e2de1b667800e#diff-e4c5045a4ae184d56dea432863a37d55
[http-401]: https://lists.w3.org/Archives/Public/ietf-http-wg/2008AprJun/0418.html
[rfc-7519]: https://tools.ietf.org/html/rfc7519
[unix-auth]: http://www.cyberciti.biz/faq/authentication-vs-authorization/

