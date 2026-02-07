---
layout: post
comments: true
title:  "Phoenix/Elixir, Adding prod.secret.exs.example to a git Repository"
date:   2016-07-18 02:18:42 +0000
categories: phoenix elixir git
---

<!-- A38 -->

**prod.secret.exs** is not added to the git repository by default.
This is a good thing.
The problem is that when a repository is cloned, **prod.secret.exs** is missing.
The file can usually be copied over, but this is a hassle when possible.
I'm sure there are people out there who can type up a new **prod.secret.exs** from scratch.
I want an easier path.

This post covers adding a **prod.secret.exs.example** file to a project.
This file can be used to regenerate **prod.secret.exs** with a new
**secret_key_base**.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-07-18 02:18:42 +0000
$ uname -vm
FreeBSD 11.0-ALPHA6 #0 r302384: Thu Jul  7 22:40:47 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ mix hex.info
Hex:    0.12.1
Elixir: 1.3.2
OTP:    18.3.4.1

Built with: Elixir 1.2.5 and OTP 18.3.3
* snip *
$ mix phoenix.new -v
Phoenix v1.1.4
{% endhighlight %}

## Instructions

Create a new project.

{% highlight sh %}
mix phoenix.new memo_api
cd memo_api
{% endhighlight %}

Create a git repository and add the project to it.

{% highlight sh %}
git init
git add .
git commit -m "Initial commit."
{% endhighlight %}

Copy **config/prod.secret.exs** to **config/prod.secret.exs.example**.

{% highlight sh %}
cp config/prod.secret.exs config/prod.secret.exs.example
{% endhighlight %}

Change the **secret_key_base** to a value that is not sensitive.
It should be a value that can easily be replaced by **sed**.

**config/prod.secret.exs.example** partial listing
{% highlight elixir %}
# Regenerate config/prod.secret.exs with the following commands
#   $ SECRET_KEY_BASE=$(elixir -e ":crypto.strong_rand_bytes(48) |> Base.encode64 |> IO.puts")
#   $ sed "s|SECRET+KEY+BASE|$SECRET_KEY_BASE|" config/prod.secret.exs.example >config/prod.secret.exs
config :memo_api, MemoApi.Endpoint,
  secret_key_base: "SECRET+KEY+BASE"
{% endhighlight %}

Add **config/prod.secret.exs.example** to git.
{% highlight sh %}
git add config/prod.secret.exs.example
git commit -m "Added config/prod.secret.exs.example."
{% endhighlight %}

**config/prod.secret.exs** can be regenerated with the following commands

{% highlight sh %}
SECRET_KEY_BASE=$(elixir -e ":crypto.strong_rand_bytes(48) |> Base.encode64 |> IO.puts")
sed "s|SECRET+KEY+BASE|$SECRET_KEY_BASE|" config/prod.secret.exs.example >config/prod.secret.exs
{% endhighlight %}

## References:

- [Github, ohr486/tokyoex_handson_demo/config][github-tokyoex-handson]

[github-tokyoex-handson]: https://github.com/ohr486/tokyoex_handson_demo/tree/master/config
