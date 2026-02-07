---
layout: post
mathjax: true
comments: true
title:  "Adding MathJax to a GitHub Pages Jekyll Blog"
date:   2016-08-21 23:41:54 +0000
categories: github jekyll
---

<!-- A39 -->

This post covers adding [MathJax][mathjax] support to a [GitHub Pages][github_pages] [Jekyll blog][jekyll].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-08-21 23:41:54 +0000
$ uname -vm
FreeBSD 11.0-ALPHA6 #0 r302384: Thu Jul  7 22:40:47 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ruby --version
ruby 2.2.5p319 (2016-04-26 revision 54774) [amd64-freebsd11]
$ jekyll --version
jekyll 3.0.1
{% endhighlight %}

## Instructions

Add the following code to **_includes/mathjax.html**.

**_includes/mathjax.html**.
{% highlight html %}
{% raw %}{% if page.mathjax %}{% endraw %}
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script
  type="text/javascript"
  charset="utf-8"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
>
</script>
<script
  type="text/javascript"
  charset="utf-8"
  src="https://vincenttam.github.io/javascripts/MathJaxLocal.js"
>
</script>
{% raw %}{% endif %}{% endraw %}
{% endhighlight %}

Add the following line to the header in **_layouts/post.html** or anywhere else you want to use MathJax.

**_layouts/post.html** partial listing
{% highlight html %}
{% raw %}{% include mathjax.html %}{% endraw %}
{% endhighlight %}

Add the following line to the [YAML front matter][jekyll-frontmatter] of a post to enable MathJax on a post by post basis.

{% highlight yaml %}
mathjax: true
{% endhighlight %}

For example, the front matter of this post looks like this.
Note that [Disqus][disqus] comments have been added with the [same strategy][jekyll_disqus].

{% highlight yaml %}
---
layout: post
mathjax: true
comments: true
title:  "Adding MathJax to a GitHub Pages Jekyll Blog"
date:   2016-08-21 23:41:54 +0000
categories: github jekyll
---
{% endhighlight %}

If all goes well, you should be able to use MathJax inline and display modes.
Note that the [MathJax dynamic preview][mathjax_preview] can be useful when formatting complex equations.

{% highlight html %}
In N-dimensional simplex noise, the squared kernel summation radius $r^2$ is $\frac 1 2$
for all values of N. This is because the edge length of the N-simplex $s = \sqrt {\frac {N} {N + 1}}$
divides out of the N-simplex height $h = s \sqrt {\frac {N + 1} {2N}}$.
The kerel summation radius $r$ is equal to the N-simplex height $h$.

$$ r = h = \sqrt{\frac {1} {2}} = \sqrt{\frac {N} {N+1}} \sqrt{\frac {N+1} {2N}} $$
{% endhighlight %}

In N-dimensional simplex noise, the squared kernel summation radius $r^2$ is $\frac 1 2$
for all values of N. This is because the edge length of the N-simplex $s = \sqrt {\frac {N} {N + 1}}$
divides out of the N-simplex height $h = s \sqrt {\frac {N + 1} {2N}}$.
The kerel summation radius $r$ is equal to the N-simplex height $h$.

$$ r = h = \sqrt{\frac {1} {2}} = \sqrt{\frac {N} {N+1}} \sqrt{\frac {N+1} {2N}} $$

## References:

- [GitHub Pages][github_pages]
- [Jekyll][jekyll]
- [Jekyll, YAML Front Matter][jekyll-frontmatter]
- [Jekyll, Adding Disqus to a Jekyll Blog][jekyll_disqus]
- [MathJax][mathjax]
- [MathJax, Loading and Configuring MathJax][mathjax_config]
- [MathJax, Dynamic Preview][mathjax_preview]
- [MathJax, Local Configuration File (Blog Post)][mathjax_config_blog]
- [MathJax, Mathjax inline mode not rendering][mathjax_no_inline]
- [MathJax, Using MathJax on a Github Page?][mathjax_github]

[github_pages]: https://pages.github.com
[jekyll]: https://jekyllrb.com
[jekyll-frontmatter]: http://jekyllrb.com/docs/frontmatter/
[jekyll_disqus]: https://sgeos.github.io/jekyll/disqus/2016/02/14/adding-disqus-to-a-jekyll-blog.html
[mathjax]: https://www.mathjax.org
[mathjax_config]: http://docs.mathjax.org/en/latest/configuration.html
[mathjax_config_blog]: https://vincenttam.github.io/blog/2014/11/09/mathjax-local-configuration-file/
[mathjax_no_inline]: http://tex.stackexchange.com/questions/27633/mathjax-inline-mode-not-rendering
[mathjax_github]: http://stackoverflow.com/questions/34347818/using-mathjax-on-a-github-page
[mathjax_preview]: https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html
[disqus]: https://disqus.com

