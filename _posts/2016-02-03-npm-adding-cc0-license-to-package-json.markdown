---
layout: post
comments: true
title:  "npm, Adding a CC0 License to package.json"
date:   2016-02-03 04:05:29 +0900
categories: npm
---

<!-- A9 -->

When installing dependencies for a new phoenix project, I got the following
warning.
**npm WARN package.json @ No license field.**

This post covers fixing that problem by specifying a [CC0][spdx-cc0] license.

## Software Versions
{% highlight sh %}
$ date
February  3, 2016 at 04:05:29 AM JST
$ uname -mv
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ npm --version
2.14.7
$ node --version
v5.5.0
{% endhighlight %}

## Instructions
Add the following line to **package.json**.
{% highlight javascript %}
  "license": "CC0-1.0",
{% endhighlight %}

The file should look something like this.
{% highlight javascript %}
{
  "license": "CC0-1.0",
  "repository": {
  },
  "dependencies": {
  }
}
{% endhighlight %}

SPDX maintains a [list of valid license identifiers][spdx-list].

## References:
- [npm, package.json][npm-package]
- [SPDX, CC0 v1.0][spdx-cc0]
- [SPDX, License List][spdx-list]

[npm-package]: https://docs.npmjs.com/files/package.json
[spdx-cc0]: https://spdx.org/licenses/CC0-1.0.html
[spdx-list]: https://spdx.org/licenses/

