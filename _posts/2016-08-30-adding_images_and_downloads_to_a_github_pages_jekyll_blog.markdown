---
layout: post
mathjax: false
comments: true
title:  "Adding Images and Downloads to a GitHub Pages Jekyll Blog"
date:   2016-08-30 19:45:55 +0000
categories: github jekyll
---
This post covers adding images to a [GitHub Pages][github_pages] [Jekyll blog][jekyll].
This solution also works for downloads, like PDFs.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-08-30 19:45:55 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #0 r304324: Thu Aug 18 13:27:23 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ruby --version
ruby 2.2.5p319 (2016-04-26 revision 54774) [amd64-freebsd11]
$ jekyll --version
jekyll 3.0.1
{% endhighlight %}

## Instructions

First, create an **assets** directory.

{% highlight sh %}
mkdir assets
{% endhighlight %}

Add an image to the **assets** directory.

{% highlight sh %}
cp path/to/image.png ./assets/
{% endhighlight %}

The image can be displayed as follows.

{% highlight liquid %}
{% raw %}![useful image]({{ site.url }}/assets/image.png){% endraw %}
{% endhighlight %}

![useful image]({{ site.url }}/assets/image.png)

Note that downloads can be made available with the same strategy.

{% highlight liquid %}
You can download the PDF {% raw %}[here]({{ site.url }}/assets/document.pdf){% endraw %}.
{% endhighlight %}

You can download the PDF [here]({{ site.url }}/assets/document.pdf).

## References:

- [GitHub Pages][github_pages]
- [Jekyll][jekyll]
- [Jekyll, Writing posts][jekyll-posts]

[github_pages]: https://pages.github.com
[jekyll]: https://jekyllrb.com
[jekyll-posts]: https://jekyllrb.com/docs/posts/

