---
layout: post
comments: true
title:  "Working with mix project iex Code Snippets Stored in Files"
date:   2016-03-14 17:08:09 +0000
categories: elixir iex
---

<!-- A24 -->

**iex** can be used for interactively experimenting with **elixir**.
If this experimentation becomes elaborate, it can be useful to store the commands in a file.
This post covers working with files that store **elixir** code snippets.
Attention is paid to code that depends on **mix** project modules.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-14 17:08:09 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r296709: Sat Mar 12 21:18:38 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [async-threads:10] [hipe] [kernel-poll:false]

Elixir 1.2.3
{% endhighlight %}

## Instructions

A single line can be run from the command line.

{% highlight sh %}
elixir -e 'IO.puts("Hello, mix run!")' # general elixir code
mix run -e 'IO.puts("Hello, mix run!")' # project specific code
{% endhighlight %}

Something more elaborate probably wants to live in a file.

**snippets/hello.exs**
{% highlight elixir %}
#!/usr/bin/env elixir

IO.puts "Hello, Elixir!"
{% endhighlight %}

The above file be run from the command line as is, but it will
not have acces to modules in the **mix** project.

{% highlight sh %}
chmod +x snippets/hello.exs
./snippets/hello.exs
{% endhighlight %}

Run the file with **mix run** if any **mix** project modules are referenced.

{% highlight sh %}
mix run snippets/hello.exs
{% endhighlight %}

Note that **c** or **Code.load_file** can be used to load the file in **iex**.

{% highlight elixir %}
c "snippets/hello.exs"
Code.load_file "snippets/hello.exs"
{% endhighlight %}

**Code.load_file** can be used to load one file from another file.
This is fragile if using relative paths.

**snippets/indirect.exs**
{% highlight elixir %}
#!/usr/bin/env elixir

Code.load_file "snippets/hello.exs"
{% endhighlight %}

To run **mix** code snippets directly from the command line,
add the following file to some place on your path.
For example, `$(which mix)-snippet`.

**mix-snippet**
{% highlight sh %}
#!/bin/sh

mix run "$1"
{% endhighlight %}

Make **mix-snippet** executable.

{% highlight sh %}
chmod +x mix-snippet # use the actual path
{% endhighlight %}

The **mix-snippet** shebang can now be used.

**snippets/hello-mix-snippet.exs**
{% highlight elixir %}
#!/usr/bin/env mix-snippet

IO.puts "Hello, mix-snippet!"
{% endhighlight %}

Code snippets that depend on the **mix** project can now
be executed from the command line.

{% highlight sh %}
chmod +x snippets/mix-snippet-hello.exs
./snippets/mix-snippet-hello.exs
{% endhighlight %}

## References:
- [Elixir, Mix.Tasks.Run][elixir-mix-run]
- [Elixir, Single File Elixir Programs][elixir-single]
- [Elixir, Erlang/Elixir Syntax: A Crash Course][elixir-crash]
- [Elixir, expect iex][elixir-expect]

[elixir-mix-run]: http://elixir-lang.org/docs/stable/mix/Mix.Tasks.Run.html
[elixir-single]: https://sgeos.github.io/elixir/erlang/2016/01/08/single-file-elixir-programs.html
[elixir-crash]: http://elixir-lang.org/crash-course.html
[elixir-expect]: https://bitbucket.org/vincit/mebe/src/b33c48c8db76ae4943a5ae193eb13eeaa7fa4311/refresh.exp?fileviewer=file-view-default


