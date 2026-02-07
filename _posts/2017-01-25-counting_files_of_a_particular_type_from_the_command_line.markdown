---
layout: post
mathjax: false
comments: true
title:  "Counting Files of a Particular Type from the Command Line"
date:   2017-01-25 09:46:14 +0000
categories: sh freebsd
---

<!-- A49 -->

Sometimes it can be useful to know how many files of a particular type are in a directory.
This post presents a single line command and a shell function that count the number of files with a given extenstion in the current directory.
Directories are searched recursively.
A version of the shell function in a stand alone script is also presented.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-01-25 09:46:14 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #18 4f888bf(drm-next): Wed Jan 18 14:31:26 UTC 2017     root@gauntlet:/usr/obj/usr/src/sys/GENERIC  amd64
{% endhighlight %}

## Instructions

The basic command to recursively tally files with a given extension looks like this.

**sh**
{% highlight sh %}
EXTENSION=.sh
ls -lR | grep "${EXTENSION}" | wc -l
{% endhighlight %}

The can be used as the basis of a shell script.

**countfiles.sh** complete listing
{% highlight sh %}
#!/bin/sh

countfiles() {
  for extension in $@
  do
    count=$(ls -lR | grep "${extension}" | wc -l)
    printf "${extension}\t${count}\n"
  done
}

countfiles $@
{% endhighlight %}

The shell script can be used as follows.

{% highlight sh %}
chmod +x countfiles.sh
./countfiles.sh .java .kt .sh
{% endhighlight %}

Output will look something like this.

{% highlight sh %}
.java	     892
.kt	       2
.sh	     251
{% endhighlight %}

Obviously, the countfiles function can be entered in the shell or **.profile**.
In that case it can be used as follows.

**.profile** partial listing
{% highlight sh %}
countfiles() {
  for extension in $@
  do
    count=$(ls -lR | grep "${extension}" | wc -l)
    printf "${extension}\t${count}\n"
  done
}
{% endhighlight %}

**sh**
{% highlight sh %}
countfiles.sh .java .kt .sh
{% endhighlight %}

Obviously, the output is exactly the same as above.

