---
layout: post
mathjax: false
comments: true
title:  "YouTube Video Speed Bookmarklets"
date:   2017-10-29 14:19:20 +0000
categories: youtube javascript bookmarklet
---
Using the provided controls, YouTube video speeds can only be
adjusted from 0.25x to 2.00x.  A speed outside of that range
is sometimes desirable.

I generally prefer to listen to videos at 2.75x.  It depends
on the video, however, 2.00x or 2.50x is often a little too
slow and 3.00x is generally a little to fast.  Your mileage
may vary.

A bookmarklet is a bookmark that executes JavaScript instead
of redirecting the browser to another page.  Bookmarklets can
be created to control video playback speed in ways that are
not possible with the default controls.

## Instructions

Create a new bookmark and name it something like 2.75x.  Change
the address to the following code for a 2.75x YouTube video
speed bookmarklet.

**2.75x**
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=2.75
{% endhighlight %}

Different bookmarklets can be made for different fixed speeds.
Just create another bookmark with the correct name, add the
above code, and change the value of the playbackRate variable
in that code to the correct value.  I have a YouTube folder
on my bookmark bar that contains a list of bookmarklets with
different playback speeds.

**1.00x** (to reset the video speed)
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=1.00
{% endhighlight %}

**2.00x** (useful in a bookmarklet list)
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=2.00
{% endhighlight %}

**3.00x**
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=3.00
{% endhighlight %}

**4.00x** (generally too fast)
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=4.00
{% endhighlight %}

Alternatively, the following code can be used to prompt for
the desired playback speed.  Note that video playback may
stop while the prompt is active, depending on the browser
being used.

**Custom**
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=parseFloat(prompt('Video%20Playback%20Speed','2.75'))
{% endhighlight %}

## Ads

The bookmarklets can additionally be used to speed up ads.
Either use the above bookmarklets to efficiently absorb
advertising material, or use something like a speed of
100.00x for rapid playback without audio.

**100.00x**
{% highlight javascript %}
javascript:document.querySelector('video').playbackRate=100.00
{% endhighlight %}

