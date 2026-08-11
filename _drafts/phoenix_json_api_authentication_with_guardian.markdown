---
layout: post
mathjax: false
comments: true
title:  "Authenticating a Phoenix JSON API with Guardian and Ueberauth"
date:   2026-08-17 00:01:00 +0000
categories: phoenix elixir
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

Phoenix JSON API authentication has evolved significantly since the framework's early releases.
Modern Phoenix applications use context modules to separate business logic from HTTP concerns,
verified routes for compile-time path checking, and dedicated JSON rendering modules.
The authentication ecosystem has matured in parallel, with Guardian reaching a stable 2.x release
that replaces the original serializer pattern with a cleaner implementation module design.

Guardian manages the JSON Web Token (JWT) lifecycle including encoding, signing, verification,
and resource loading through a plug pipeline.
Ueberauth handles the initial identity verification step, providing a structured callback interface
for credential validation across multiple authentication strategies.
Together they form a two-layer authentication architecture
where Ueberauth confirms identity and Guardian issues and manages session tokens.

This post demonstrates building a JSON API with user registration,
JWT-based login, and protected CRUD resources.
The example application is a memo service
where authenticated users create, read, update, and delete personal memos.
The article targets Phoenix 1.7 or later, Guardian 2.x, and bcrypt_elixir for password hashing.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
TODO

# OS and Version
$ uname -vm
TODO

# Elixir and OTP
$ elixir --version
TODO

# Hex
$ mix hex.info
TODO

# Phoenix
$ mix phx.new --version
TODO

# PostgreSQL
$ psql --version
TODO
```

## Instructions

### Creating the Project

Create a new API-only Phoenix project.
The `--no-html` and `--no-assets` flags exclude browser-oriented components
that are not needed for a JSON API.

```sh
$ mix phx.new memo_api --no-html --no-assets
$ cd memo_api
```

Add Guardian, Ueberauth, and bcrypt_elixir to the dependency list in `mix.exs`.
Modern Elixir infers application dependencies from `mix.exs` automatically,
so the `:applications` list in `def application` does not require manual entries.

`mix.exs` partial listing

```elixir
  defp deps do
    [
      {:phoenix, "~> 1.7"},
      {:phoenix_ecto, "~> 4.5"},
      {:ecto_sql, "~> 3.10"},
      {:postgrex, ">= 0.0.0"},
      {:phoenix_live_dashboard, "~> 0.8"},
      {:telemetry_metrics, "~> 1.0"},
      {:telemetry_poller, "~> 1.0"},
      {:jason, "~> 1.4"},
      {:dns_cluster, "~> 0.1"},
      {:bandit, "~> 1.5"},
      {:guardian, "~> 2.3"},
      {:ueberauth, "~> 0.10"},
      {:ueberauth_identity, "~> 0.4"},
      {:bcrypt_elixir, "~> 3.0"}
    ]
  end
```

Fetch dependencies and create the database.

```sh
$ mix deps.get
$ mix ecto.create
```

### User Schema and Accounts Context

Generate the user JSON resource using the modern Phoenix generator.
The `phx.gen.json` command creates a context module, controller, JSON rendering module,
and database migration in a single step.

```sh
$ mix phx.gen.json Accounts User users email:string password_hash:string
```

This generator produces the following files.

- `lib/memo_api/accounts/user.ex` for the Ecto schema.
- `lib/memo_api/accounts.ex` for the context module containing business logic.
- `lib/memo_api_web/controllers/user_controller.ex` for the HTTP controller.
- `lib/memo_api_web/controllers/user_json.ex` for JSON rendering.
- `priv/repo/migrations/*_create_users.exs` for the database migration.

Modify the User schema to add a virtual password field, a memo association,
password length validation, and bcrypt hashing.
The virtual field accepts the plaintext password from API requests
without persisting it to the database.

`lib/memo_api/accounts/user.ex` full listing

```elixir
defmodule MemoApi.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :email, :string
    field :password_hash, :string
    field :password, :string, virtual: true

    has_many :memos, MemoApi.Memos.Memo

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:email, :password])
    |> validate_required([:email, :password])
    |> validate_format(:email, ~r/@/)
    |> validate_length(:password, min: 8)
    |> unique_constraint(:email)
    |> hash_password()
  end

  defp hash_password(changeset) do
    case get_change(changeset, :password) do
      nil ->
        changeset

      password ->
        changeset
        |> put_change(:password_hash, Bcrypt.hash_pwd_salt(password))
        |> delete_change(:password)
    end
  end
end
```

Modify the migration to add a unique index on the email column.

`priv/repo/migrations/*_create_users.exs` full listing (timestamp will differ)

```elixir
defmodule MemoApi.Repo.Migrations.CreateUsers do
  use Ecto.Migration

  def change do
    create table(:users) do
      add :email, :string, null: false
      add :password_hash, :string, null: false

      timestamps(type: :utc_datetime)
    end

    create unique_index(:users, [:email])
  end
end
```

Add an `authenticate_user/2` function and a `register_user/1` function to the Accounts context.
The `Bcrypt.no_user_verify/0` call provides constant-time comparison when no user is found,
preventing timing attacks that could reveal whether an email address is registered.

`lib/memo_api/accounts.ex` partial listing

```elixir
defmodule MemoApi.Accounts do
  import Ecto.Query, warn: false
  alias MemoApi.Repo
  alias MemoApi.Accounts.User

  def register_user(attrs) do
    %User{}
    |> User.changeset(attrs)
    |> Repo.insert()
  end

  def get_user(id), do: Repo.get(User, id)

  def get_user_by_email(email), do: Repo.get_by(User, email: email)

  def authenticate_user(email, password) do
    user = get_user_by_email(email)

    cond do
      user && Bcrypt.verify_pass(password, user.password_hash) ->
        {:ok, user}

      user ->
        {:error, :invalid_credentials}

      true ->
        Bcrypt.no_user_verify()
        {:error, :invalid_credentials}
    end
  end
end
```

Modify the generated `UserJSON` module to exclude the password hash from API responses.

`lib/memo_api_web/controllers/user_json.ex` partial listing

```elixir
defmodule MemoApiWeb.UserJSON do
  alias MemoApi.Accounts.User

  def data(%{user: user}) do
    %{
      id: user.id,
      email: user.email
    }
  end
end
```

Optionally, reduce the number of bcrypt rounds in the test configuration to speed up test execution.

`config/test.exs` partial listing

```elixir
config :bcrypt_elixir, :log_rounds, 4
```

### Guardian Configuration

Create a Guardian implementation module.
This module replaces the serializer pattern used in Guardian 0.x.
It implements two required callbacks that encode a resource into a token subject
and decode token claims back into a resource.

`lib/memo_api/guardian.ex` full listing

```elixir
defmodule MemoApi.Guardian do
  use Guardian, otp_app: :memo_api

  alias MemoApi.Accounts

  def subject_for_token(%{id: id}, _claims) do
    {:ok, to_string(id)}
  end

  def subject_for_token(_, _) do
    {:error, :invalid_resource}
  end

  def resource_from_claims(%{"sub" => id}) do
    case Accounts.get_user(id) do
      nil -> {:error, :resource_not_found}
      user -> {:ok, user}
    end
  end

  def resource_from_claims(_) do
    {:error, :invalid_claims}
  end
end
```

Add Guardian configuration to `config/config.exs`.
The `secret_key` value should be replaced with a properly generated secret.

`config/config.exs` partial listing

```elixir
config :memo_api, MemoApi.Guardian,
  issuer: "memo_api",
  secret_key: "generate-a-real-secret-key-here"
```

The following command generates a suitable secret key.

```sh
$ mix guardian.gen.secret
```

Create an authentication pipeline module.
The pipeline chains three Guardian plugs that extract the token from the Authorization header,
verify its authenticity, and load the associated user resource.

`lib/memo_api/guardian/auth_pipeline.ex` full listing

```elixir
defmodule MemoApi.Guardian.AuthPipeline do
  use Guardian.Plug.Pipeline,
    otp_app: :memo_api,
    module: MemoApi.Guardian,
    error_handler: MemoApi.Guardian.AuthErrorHandler

  plug Guardian.Plug.VerifyHeader, scheme: "Bearer"
  plug Guardian.Plug.EnsureAuthenticated
  plug Guardian.Plug.LoadResource
end
```

Create an error handler module for authentication failures.
This module implements the `Guardian.Plug.ErrorHandler` behaviour
and returns JSON error responses with appropriate HTTP status codes.

`lib/memo_api/guardian/auth_error_handler.ex` full listing

```elixir
defmodule MemoApi.Guardian.AuthErrorHandler do
  import Plug.Conn

  @behaviour Guardian.Plug.ErrorHandler

  @impl Guardian.Plug.ErrorHandler
  def auth_error(conn, {type, _reason}, _opts) do
    body = Jason.encode!(%{error: to_string(type)})

    conn
    |> put_resp_content_type("application/json")
    |> send_resp(401, body)
  end
end
```

### Authentication Endpoints

Create an authentication controller with three actions for user registration, login, and logout.

`lib/memo_api_web/controllers/authentication_controller.ex` full listing

```elixir
defmodule MemoApiWeb.AuthenticationController do
  use MemoApiWeb, :controller

  alias MemoApi.Accounts
  alias MemoApi.Guardian

  action_fallback MemoApiWeb.FallbackController

  def register(conn, %{"user" => user_params}) do
    with {:ok, user} <- Accounts.register_user(user_params),
         {:ok, token, _claims} <- Guardian.encode_and_sign(user) do
      conn
      |> put_status(:created)
      |> json(%{data: %{user: render_user(user), token: token}})
    end
  end

  def sign_in(conn, %{"user" => %{"email" => email, "password" => password}}) do
    case Accounts.authenticate_user(email, password) do
      {:ok, user} ->
        {:ok, token, _claims} = Guardian.encode_and_sign(user)

        conn
        |> json(%{data: %{user: render_user(user), token: token}})

      {:error, :invalid_credentials} ->
        conn
        |> put_status(:unauthorized)
        |> json(%{error: "Invalid email or password"})
    end
  end

  def sign_out(conn, _params) do
    token = Guardian.Plug.current_token(conn)

    case Guardian.revoke(token) do
      {:ok, _claims} ->
        conn
        |> json(%{data: %{message: "Signed out"}})

      {:error, _reason} ->
        conn
        |> put_status(:unprocessable_entity)
        |> json(%{error: "Sign out failed"})
    end
  end

  defp render_user(user) do
    %{id: user.id, email: user.email}
  end
end
```

Configure the router with two scopes.
The first scope contains public routes for registration and login.
The second scope pipes through the Guardian authentication pipeline,
restricting access to authenticated users.

`lib/memo_api_web/router.ex` full listing

```elixir
defmodule MemoApiWeb.Router do
  use MemoApiWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", MemoApiWeb do
    pipe_through :api

    post "/register", AuthenticationController, :register
    post "/sign_in", AuthenticationController, :sign_in
  end

  scope "/api", MemoApiWeb do
    pipe_through [:api, MemoApi.Guardian.AuthPipeline]

    delete "/sign_out", AuthenticationController, :sign_out
    resources "/users", UserController, only: [:show]
    resources "/memos", MemoController, except: [:new, :edit]
  end

  if Application.compile_env(:memo_api, :dev_routes) do
    import Phoenix.LiveDashboard.Router

    scope "/dev" do
      pipe_through [:fetch_session, :protect_from_forgery]
      live_dashboard "/dashboard", metrics: MemoApiWeb.Telemetry
    end
  end
end
```

### Protected Resources

Generate the memo resource with a foreign key reference to users.

```sh
$ mix phx.gen.json Memos Memo memos title:string body:text user_id:references:users
```

Modify the Memo schema to add the user association.

`lib/memo_api/memos/memo.ex` full listing

```elixir
defmodule MemoApi.Memos.Memo do
  use Ecto.Schema
  import Ecto.Changeset

  schema "memos" do
    field :title, :string
    field :body, :string
    belongs_to :user, MemoApi.Accounts.User

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(memo, attrs) do
    memo
    |> cast(attrs, [:title, :body, :user_id])
    |> validate_required([:title, :body, :user_id])
    |> foreign_key_constraint(:user_id)
  end
end
```

Modify the Memos context to scope all operations to the authenticated user.
This ensures that users can only access their own memos.

`lib/memo_api/memos.ex` partial listing

```elixir
defmodule MemoApi.Memos do
  import Ecto.Query, warn: false
  alias MemoApi.Repo
  alias MemoApi.Memos.Memo

  def list_memos_for_user(user) do
    Memo
    |> where(user_id: ^user.id)
    |> Repo.all()
  end

  def get_memo_for_user!(user, id) do
    Memo
    |> where(user_id: ^user.id)
    |> Repo.get!(id)
  end

  def create_memo(user, attrs) do
    attrs = Map.put(attrs, "user_id", user.id)

    %Memo{}
    |> Memo.changeset(attrs)
    |> Repo.insert()
  end

  def update_memo(%Memo{} = memo, attrs) do
    memo
    |> Memo.changeset(attrs)
    |> Repo.update()
  end

  def delete_memo(%Memo{} = memo) do
    Repo.delete(memo)
  end
end
```

Modify the MemoController to extract the current user from the Guardian plug
and pass it to the context functions.

`lib/memo_api_web/controllers/memo_controller.ex` full listing

```elixir
defmodule MemoApiWeb.MemoController do
  use MemoApiWeb, :controller

  alias MemoApi.Memos
  alias MemoApi.Memos.Memo
  alias MemoApi.Guardian

  action_fallback MemoApiWeb.FallbackController

  def index(conn, _params) do
    user = Guardian.Plug.current_resource(conn)
    memos = Memos.list_memos_for_user(user)
    render(conn, :index, memos: memos)
  end

  def create(conn, %{"memo" => memo_params}) do
    user = Guardian.Plug.current_resource(conn)

    with {:ok, %Memo{} = memo} <- Memos.create_memo(user, memo_params) do
      conn
      |> put_status(:created)
      |> render(:show, memo: memo)
    end
  end

  def show(conn, %{"id" => id}) do
    user = Guardian.Plug.current_resource(conn)
    memo = Memos.get_memo_for_user!(user, id)
    render(conn, :show, memo: memo)
  end

  def update(conn, %{"id" => id, "memo" => memo_params}) do
    user = Guardian.Plug.current_resource(conn)
    memo = Memos.get_memo_for_user!(user, id)

    with {:ok, %Memo{} = memo} <- Memos.update_memo(memo, memo_params) do
      render(conn, :show, memo: memo)
    end
  end

  def delete(conn, %{"id" => id}) do
    user = Guardian.Plug.current_resource(conn)
    memo = Memos.get_memo_for_user!(user, id)

    with {:ok, %Memo{}} <- Memos.delete_memo(memo) do
      send_resp(conn, :no_content, "")
    end
  end
end
```

Create the MemoJSON module for rendering memo data.

`lib/memo_api_web/controllers/memo_json.ex` full listing

```elixir
defmodule MemoApiWeb.MemoJSON do
  alias MemoApi.Memos.Memo

  def index(%{memos: memos}) do
    %{data: for(memo <- memos, do: data(memo))}
  end

  def show(%{memo: memo}) do
    %{data: data(memo)}
  end

  defp data(%Memo{} = memo) do
    %{
      id: memo.id,
      title: memo.title,
      body: memo.body,
      user_id: memo.user_id
    }
  end
end
```

Run the database migrations.

```sh
$ mix ecto.migrate
```

### Ueberauth Integration

Ueberauth provides a structured callback interface for authentication strategies.
The identity strategy handles email and password credential validation,
which is the natural fit for a JSON API.

Add Ueberauth configuration to `config/config.exs`.

`config/config.exs` partial listing

```elixir
config :ueberauth, Ueberauth,
  providers: [
    identity: {Ueberauth.Strategy.Identity, [
      callback_methods: ["POST"],
      param_nesting: "user",
      uid_field: :email
    ]}
  ]
```

The identity strategy extracts credentials from POST parameters
according to the configured field mapping.
The `param_nesting` option tells Ueberauth to look for credentials
inside a `"user"` key in the request parameters,
matching the parameter structure used by the registration and login endpoints.
The `uid_field` option specifies that the email address serves as the unique identifier.

For JSON APIs, the identity strategy provides structured parameter extraction
and validation before credentials reach the application's authentication logic.
This is a simpler integration than OAuth strategies such as `ueberauth_github` or `ueberauth_google`,
which require browser redirect flows for the authorization code grant.
Pure JSON API clients cannot complete OAuth redirect flows without a browser intermediary.

To use Ueberauth in the authentication controller, add the Ueberauth plug
and implement the callback action.
The following example shows how the sign-in action can use the Ueberauth callback pattern.

`lib/memo_api_web/controllers/authentication_controller.ex` partial listing (alternative sign-in with Ueberauth)

```elixir
  # Add to the top of the module
  plug Ueberauth, only: [:identity]

  # Alternative sign_in using Ueberauth callback
  def callback(%{assigns: %{ueberauth_auth: auth}} = conn, _params) do
    email = auth.uid
    password = auth.credentials.other.password

    case Accounts.authenticate_user(email, password) do
      {:ok, user} ->
        {:ok, token, _claims} = Guardian.encode_and_sign(user)

        conn
        |> json(%{data: %{user: render_user(user), token: token}})

      {:error, :invalid_credentials} ->
        conn
        |> put_status(:unauthorized)
        |> json(%{error: "Invalid email or password"})
    end
  end

  def callback(%{assigns: %{ueberauth_failure: _failure}} = conn, _params) do
    conn
    |> put_status(:unauthorized)
    |> json(%{error: "Authentication failed"})
  end
```

The Ueberauth callback pattern becomes more valuable when multiple authentication strategies
are in use, as it provides a uniform interface regardless of the underlying provider.
For a JSON API that only supports email and password authentication,
the direct approach shown in the Authentication Endpoints section above is simpler.

### Testing the API

Start the Phoenix server.

```sh
$ mix phx.server
```

Register a new user.

```sh
$ curl -s -X POST http://localhost:4000/api/register \
  -H "Content-Type: application/json" \
  -d '{"user": {"email": "test@example.com", "password": "secret1234"}}' | python3 -m json.tool
```

Expected response.

```json
{
    "data": {
        "user": {
            "id": 1,
            "email": "test@example.com"
        },
        "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9..."
    }
}
```

Sign in with the registered user.

```sh
$ curl -s -X POST http://localhost:4000/api/sign_in \
  -H "Content-Type: application/json" \
  -d '{"user": {"email": "test@example.com", "password": "secret1234"}}' | python3 -m json.tool
```

Save the token from the response for use in subsequent requests.

```sh
$ TOKEN="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9..."
```

Create a memo using the token.

```sh
$ curl -s -X POST http://localhost:4000/api/memos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${TOKEN}" \
  -d '{"memo": {"title": "First Memo", "body": "Hello, authenticated world."}}' | python3 -m json.tool
```

Expected response.

```json
{
    "data": {
        "id": 1,
        "title": "First Memo",
        "body": "Hello, authenticated world.",
        "user_id": 1
    }
}
```

List all memos for the authenticated user.

```sh
$ curl -s http://localhost:4000/api/memos \
  -H "Authorization: Bearer ${TOKEN}" | python3 -m json.tool
```

Update a memo.

```sh
$ curl -s -X PUT http://localhost:4000/api/memos/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${TOKEN}" \
  -d '{"memo": {"title": "Updated Memo"}}' | python3 -m json.tool
```

Delete a memo.

```sh
$ curl -s -X DELETE http://localhost:4000/api/memos/1 \
  -H "Authorization: Bearer ${TOKEN}"
```

An empty response with HTTP status 204 indicates successful deletion.

Sign out.

```sh
$ curl -s -X DELETE http://localhost:4000/api/sign_out \
  -H "Authorization: Bearer ${TOKEN}" | python3 -m json.tool
```

Attempting to access a protected resource without a valid token returns a 401 error.

```sh
$ curl -s http://localhost:4000/api/memos | python3 -m json.tool
```

Expected response.

```json
{
    "error": "unauthenticated"
}
```

A [shell script for working with Phoenix JSON APIs][related_post_phoenix_shell_script]
can simplify the process of testing multiple endpoints during development.

## Limitations

1. JWTs are stateless by design and cannot be individually revoked before expiration
without maintaining external state.
The `sign_out` action in this article calls `Guardian.revoke/1`,
but without a token storage backend such as GuardianDb,
revocation has no persistent effect.
A revoked token remains valid until its time-to-live expires.

2. GuardianDb adds a database lookup to every token verification request,
partially negating the stateless performance advantage that motivates JWT adoption.
Applications that require immediate token revocation
should evaluate whether session-based authentication is a simpler fit for their use case.

3. This article uses a fixed time-to-live without token refresh.
Token refresh requires careful implementation to prevent token proliferation,
where a client accumulates valid tokens by repeatedly refreshing without revoking the previous token.
Production applications should implement a refresh token rotation strategy
with one-time-use refresh tokens.

4. Ueberauth OAuth strategies such as `ueberauth_github` and `ueberauth_google`
require browser redirect flows for the authorization code grant.
Pure JSON API clients cannot complete these flows without a browser intermediary
such as a WebView or system browser with deep linking.

5. Guardian tokens carry no built-in role or permission claims
beyond what the application explicitly encodes in the token's custom claims.
Role-based access control must be implemented at the application layer,
either through Guardian's permissions extension or through custom plug pipelines.

6. The bcrypt algorithm truncates passwords at 72 bytes.
Passwords longer than 72 bytes are silently reduced to their first 72 bytes before hashing,
making the additional bytes irrelevant to authentication.
This is a property of the bcrypt specification, not of the bcrypt_elixir implementation.

7. Guardian's secret key must be configured at runtime rather than compile time
for production deployments.
BEAM hot code loading can invalidate compile-time configuration references.
Use `config/runtime.exs` with `System.get_env/1` to load the secret key
from an environment variable at application startup.

## Conclusion

This article demonstrated building a JSON API with user registration,
JWT-based authentication, and protected resources
using Phoenix, Guardian, Ueberauth, and bcrypt_elixir.
The context module pattern introduced in Phoenix 1.3 separates authentication and business logic
from HTTP concerns, and the Guardian plug pipeline provides declarative route protection
through a composable middleware chain.

For production applications,
the `mix phx.gen.auth` generator provides a session-based authentication system
that handles email confirmation, password reset, and session management.
JWT-based authentication with Guardian is most appropriate
when the API serves mobile clients, single-page applications,
or third-party consumers that cannot maintain server-side sessions.

## Future Reading

The `mix phx.gen.auth` generator produces a complete session-based authentication system
with email confirmation and password reset workflows.
Token refresh and rotation strategies address the token proliferation problem
described in the Limitations section.
Ueberauth OAuth strategies enable social login through providers such as GitHub and Google,
though the redirect flow requires a browser intermediary for JSON API clients.
The Guardian permissions extension provides a lightweight role-based access control system
that embeds permission claims directly in the JWT.
Absinthe, the GraphQL toolkit for Elixir, integrates with Guardian tokens
for authenticated GraphQL API development.

## References

- [Elixir, bcrypt_elixir][elixir_bcrypt]
- [Elixir, Guardian][elixir_guardian]
- [Elixir, Ueberauth][elixir_ueberauth]
- [Elixir, ueberauth_identity][elixir_ueberauth_identity]
- [Phoenix, Contexts][phoenix_contexts]
- [Phoenix, JSON and APIs Guide][phoenix_json_apis]
- [Phoenix, mix phx.gen.auth][phoenix_gen_auth]
- [Phoenix, mix phx.gen.json][phoenix_gen_json]
- [Reference, JSON Web Token RFC 7519][reference_rfc_7519]
- [Reference, OAuth 2.0 RFC 6749][reference_rfc_6749]
- [Related Post, A Shell Script for Working with Phoenix JSON APIs][related_post_phoenix_shell_script]

[elixir_bcrypt]: https://hexdocs.pm/bcrypt_elixir/Bcrypt.html
[elixir_guardian]: https://hexdocs.pm/guardian/Guardian.html
[elixir_ueberauth]: https://hexdocs.pm/ueberauth/Ueberauth.html
[elixir_ueberauth_identity]: https://hexdocs.pm/ueberauth_identity/Ueberauth.Strategy.Identity.html
[phoenix_contexts]: https://hexdocs.pm/phoenix/contexts.html
[phoenix_gen_auth]: https://hexdocs.pm/phoenix/mix_phx_gen_auth.html
[phoenix_gen_json]: https://hexdocs.pm/phoenix/Mix.Tasks.Phx.Gen.Json.html
[phoenix_json_apis]: https://hexdocs.pm/phoenix/json_and_apis.html
[reference_rfc_6749]: https://tools.ietf.org/html/rfc6749
[reference_rfc_7519]: https://tools.ietf.org/html/rfc7519
[related_post_phoenix_shell_script]: {% post_url 2016-03-19-a-shell-script-for-working-with-phoenix-json-apis %}
