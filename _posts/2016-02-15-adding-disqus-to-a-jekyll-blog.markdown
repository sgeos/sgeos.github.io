---
layout: post
comments: true
title:  "Adding Disqus to a Jekyll Blog"
date:   2016-02-15 05:56:57 +0900
categories: jekyll disqus
---

<!-- A15 -->

A [Jekyll][jekyll] blog is not backed by a database.
Out of the box, there is no way for people to comment on or discuss blog posts.
[Disqus][disqus] is a third party service that can be used to get around that limitation.
This post covers [adding Disqus][disqus-jekyll-install] to a [Jekyll][jekyll] blog.

## Software Versions
{% highlight sh %}
$ date
February 15, 2016 at 05:56:57 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ruby --version
ruby 2.1.8p440 (2015-12-16 revision 53160) [amd64-freebsd11]
$ jekyll --version
jekyll 3.0.1
{% endhighlight %}

## Instructions

First, [install Jekyll][jekyll-freebsd] and [register your site with Disqus][disqus-registration].

Add the following code to **_includes/disqus.html**.
Remember to change the **this.page.url** line to the URL of your blog.
The **s.src** line will need to point to your Disqus short name URL.
Consider copying the [Universal Embed Code directly from Disqus][disqus-embed] instead of this post.

{% highlight html %}
{% raw %}{% if page.comments %}{% endraw %}
<div id="disqus_thread"></div>
<script>
var disqus_config = function () {
this.page.url = "http://BLOG.host.com{% raw %}{{ page.url }}{% endraw %}"; // <--- use canonical URL
this.page.identifier = "{% raw %}{{ page.id }}{% endraw %}";
};
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');

s.src = '//SHORTNAME.disqus.com/embed.js'; // <--- use Disqus shortname

s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
{% raw %}{% endif %}{% endraw %}
{% endhighlight %}

Add the following line to the end of **_layouts/post.html** or anywhere else you want to display comments.

{% highlight html %}
{% raw %}{% include disqus.html %}{% endraw %}
{% endhighlight %}

Add the following line to the [YAML front matter][jekyll-frontmatter] of a post to enable comments on a post by post basis.

{% highlight yaml %}
comments: true
{% endhighlight %}

For example, the front matter of this post looks like this.

{% highlight yaml %}
---
layout: post
comments: true
title:  "Adding Disqus to a Jekyll Blog"
date:   2016-02-15 05:56:57 +0900
categories: jekyll disqus
---
{% endhighlight %}

Optionally, to facilitate displaying comment counts
add the following to **_layouts/default.html** before the closing **body** tag.
Change **SHORTNAME** to the Disqus shortname you are using.

{% highlight html %}
<script id="dsq-count-scr" src="//SHORTNAME.disqus.com/count.js" async></script>
{% endhighlight %}

Add **#disqus_thread** to the end of a URL and Disqus will count the comments on the page the link points to.
For example, my **_layouts/post.html** contains the following code.
Note the comment count at the top of this post.

{% highlight html %}
{% raw %}{% if page.comments %} • <a href="https://sgeos.github.io{{ page.url }}#disqus_thread">0 Comments</a>{% endif %}{% endraw %}
{% endhighlight %}

**index.html** contains the following code to display the comment count for each post in the list.

{% highlight html %}
{% raw %}<a href="https://sgeos.github.io{{ post.url }}#disqus_thread">0 Comments</a>{% endraw %}
{% endhighlight %}

Note that moving a post from **_drafts/** to **_posts/** may change the URL of the post.
This will cause any comments added to the draft to disappear.
The [Disqus Migration Tools][disqus-migrate] can be used move comments to the new URL.


## References:
- [Jekyll][jekyll]
- [Jekyll, Variables][jekyll-variables]
- [Jekyll, Templates][jekyll-templates]
- [Jekyll, YAML Front Matter][jekyll-frontmatter]
- [Jekyll, Highlighting Liquid Code in a Liquid Template with Jekyll (Escape a Liquid Templating Tag)][jekyll-highlight-liquid-code]
- [Jekyll, How I Created a Beautiful and Minimal Blog Using Jekyll, Github Pages, and poole][jekyll-beautiful]
- [Jekyll, Dynamic Links in jekyll][jekyll-dynamic]
- [Jekyll, Creating A Jekyll GitHub Pages Blog and Managing it With FreeBSD][jekyll-freebsd]
- [Disqus][disqus]
- [Disqus, Set Up Disqus On a New Site][disqus-registration]
- [Disqus, Universal Embed Code][disqus-embed]
- [Disqus, Jekyll Installation Instructions][disqus-jekyll-install]
- [Disqus, Use Configuration Variables to Avoid Split Threads and "Missing" Comments][disqus-install-config]
- [Disqus, Migration Tools][disqus-migrate]
- [Disqus, Adding Disqus to your Jekyll][disqus-install-random]
- [Disqus, Jekyll Notes][disqus-jekyll-notes]
- [Disqus, Preserve Disqus Comments with Jekyll][disqus-preserve]
- [Google, Use canonical URLs][google-canonical]

[jekyll]: https://jekyllrb.com
[jekyll-variables]: http://jekyllrb.com/docs/variables/
[jekyll-templates]: http://jekyllrb.com/docs/templates/
[jekyll-frontmatter]: http://jekyllrb.com/docs/frontmatter/
[jekyll-highlight-liquid-code]: http://tesoriere.com/2010/08/25/liquid-code-in-a-liquid-template-with-jekyll/
[jekyll-beautiful]: http://joshualande.com/jekyll-github-pages-poole/
[jekyll-dynamic]: http://stackoverflow.com/questions/22725754/dynamic-links-in-jekyll
[jekyll-freebsd]: https://sgeos.github.io/jekyll/github/freebsd/2016/01/07/creating-a-jekyll-github-pages-blog-and-managing-it-with-freebsd.html
[disqus]: https://disqus.com
[disqus-registration]: https://disqus.com/admin/create/
[disqus-embed]: https://disqus.com/admin/universalcode/
[disqus-jekyll-install]: https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions
[disqus-install-config]: https://help.disqus.com/customer/en/portal/articles/2158629
[disqus-migrate]: https://help.disqus.com/customer/portal/articles/286778-migration-tools
[disqus-install-random]: http://www.perfectlyrandom.org/2014/06/29/adding-disqus-to-your-jekyll-powered-github-pages/
[disqus-jekyll-notes]: http://blog.pzheng.me/2014/07/03/Jekyll-Notes/
[disqus-preserve]: http://haacked.com/archive/2013/12/09/preserving-disqus-comments-with-jekyll/
[google-canonical]: https://support.google.com/webmasters/answer/139066?hl=en

