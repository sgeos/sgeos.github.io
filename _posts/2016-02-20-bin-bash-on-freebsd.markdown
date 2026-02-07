---
layout: post
comments: true
title:  "#!/bin/bash on FreeBSD"
date:   2016-02-20 17:04:07 +0000
categories: freebsd bash
---

<!-- A20 -->

A great number of people write **bash** scripts for Linux.
Most of these scripts start with `#!/bin/bash`.
**bash** is not installed on FreeBSD by default.
When installed, it is installed in **/usr/local/bin/bash**.

This post covers a few strategies for using scripts that start with `#!/bin/bash` on FreeBSD.
I used one of these strategies in a [previous post][ion-started].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-02-20 17:04:07 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions

First, **bash** needs to be installed.

{% highlight sh %}
portmaster shells/bash
{% endhighlight %}

The simplest option is to create a symlink from **/usr/local/bin/bash** to **/bin/bash**.

{% highlight sh %}
su
ln -s /usr/local/bin/bash /bin/bash
{% endhighlight %}

At this point, the following script should work without modification.

**hello_world.sh**
{% highlight sh %}
#!/bin/bash

echo "Hello, World!"
{% endhighlight %}

If you object to adding a symlink, the following command can be used to
replace `#!/bin/bash` with the more portable `#!/usr/bin/env bash`.

{% highlight sh %}
FILENAME=hello_world.sh
sed -i '' 's:^#!/bin/bash:#!/usr/bin/env bash:' "${FILENAME}"
{% endhighlight %}

If a large number of files need to be changed, the following can be
used to recursively patch all files in a directory.

{% highlight sh %}
DIRNAME=.
find "${DIRNAME}" -type f -print0 | xargs -0 sed -i '' 's:^#!/bin/bash:#!/usr/bin/env bash:'
{% endhighlight %}

## References:
- [Getting Started with ION-DTN 3.4.0 on FreeBSD][ion-started]

[ion-started]: https://sgeos.github.io

