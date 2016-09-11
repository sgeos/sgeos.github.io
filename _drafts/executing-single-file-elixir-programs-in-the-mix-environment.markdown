---
layout: post
comments: true
title:  "Executing Single File Elixir Programs in the mix Environment"
date:   2016-07-18 05:47:42 +0000
categories: elixir erlang mix
---
Writing [single file elixir programs][blog-single-file] can be useful for
experiments that are a little too complicated for **iex**, but that are
not complicated enough to warrant a full blown mix project.

Likewise, experimenting with code that relies on the mix environment
can get complicated enough that putting it in a file is useful.
This post covers stand alone code snippet files that rely on the mix project,
as opposed to mix tasks that are logically part of it.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-07-18 05:47:42 +0000
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

Instructions for solution here.

{% highlight sh %}
echo "Code here."
{% endhighlight %}

## References:

- [Elixir, Single File Elixir Programs][blog-single-file]

[blog-single-file]: https://sgeos.github.io

