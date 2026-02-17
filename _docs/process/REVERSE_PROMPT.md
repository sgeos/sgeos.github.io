# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P9 Modernize Phoenix Guardian Article

---

## Verification

### Phoenix JSON API Authentication Article Modernization

- Complete rewrite from 2016 article (Phoenix 1.1.4, Elixir 1.2.3, Guardian ~0.10.0, Comeonin ~2.1) to contemporary toolchain (Phoenix 1.7+, Guardian ~> 2.3, bcrypt_elixir ~> 3.0, Ueberauth ~> 0.10).
- File renamed from `authenticating-a-phoenix-json-api-with-guardian.markdown` to `phoenix_json_api_authentication_with_guardian.markdown` via `git mv`.
- MemoApi example application preserved from original, fully modernized.
- `MemoApi.Accounts.User` schema with virtual password field, bcrypt hashing via `Bcrypt.hash_pwd_salt/1`, timing-attack-safe authentication via `Bcrypt.no_user_verify/0`.
- `MemoApi.Accounts` context module with `register_user/1` and `authenticate_user/2` functions.
- `MemoApi.Guardian` implementation module with `subject_for_token/2` and `resource_from_claims/1` callbacks replacing the deprecated serializer pattern.
- `MemoApi.Guardian.AuthPipeline` plug pipeline with `VerifyHeader`, `EnsureAuthenticated`, and `LoadResource` plugs.
- `MemoApi.Guardian.AuthErrorHandler` implementing `Guardian.Plug.ErrorHandler` behaviour.
- `MemoApiWeb.AuthenticationController` with register, sign_in, and sign_out actions.
- Router with public scope (register, sign_in) and authenticated scope (sign_out, users, memos).
- `MemoApi.Memos.Memo` schema with user association and `MemoApi.Memos` context with user-scoped CRUD.
- `MemoApiWeb.MemoController` extracting current user via `Guardian.Plug.current_resource/1`.
- Ueberauth Integration section with identity strategy configuration and callback pattern example.
- Testing the API section with curl commands for full flow and expected JSON responses.
- 7 limitations documented.
- 11 references across 4 categories (Elixir, Phoenix, Reference, Related Post).
- All existing content replaced. No content preserved from 2016 draft.

---

## Questions for Human Review

- Software Versions section has TODO placeholders that need to be filled in on the development machine.
- Verify that `mix guardian.gen.secret` is the correct command for generating a Guardian secret key. The alternative is `mix phx.gen.secret`.
- The `register` action returns a JWT immediately upon registration. Some applications require email confirmation before issuing tokens. Verify that the immediate token return matches the intended workflow.
- The `sign_out` action calls `Guardian.revoke/1`, but Limitation 1 notes that without GuardianDb this has no persistent effect. Verify that this honest treatment is acceptable rather than adding GuardianDb as a dependency.
- The Ueberauth identity strategy integration uses `plug Ueberauth, only: [:identity]` in the authentication controller. Verify that this plug directive is compatible with the current ueberauth_identity version.
- The `Memos.create_memo/2` function uses `Map.put(attrs, "user_id", user.id)` to inject the user ID into string-keyed params. Verify that Phoenix 1.7+ `phx.gen.json` generates string-keyed params (via JSON body parsing) rather than atom-keyed params.
- The router includes `live_dashboard` in a dev-only scope with `fetch_session` and `protect_from_forgery` plugs. Verify that this is compatible with the `--no-html` project generation flag, which may not include session-related plugs in the endpoint.
- The `UserJSON.data/1` function signature differs from the generator's default `data/1` signature. Verify that the Phoenix 1.7+ JSON rendering convention uses `%{user: user}` assigns pattern.
- Curl commands pipe output to `python3 -m json.tool` for formatting. Verify that `jq` is not the preferred formatter in the blog's convention.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 6 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- SSH article has no publication dependency on other articles.
- Phoenix Guardian article has no publication dependency on other unpublished articles. References published article A27 via post_url.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
