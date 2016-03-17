---
layout: post
comments: true
title:  "Installing Software in $HOME/local"
date:   2016-03-17 17:49:50 +0000
categories: unix
---
Have you ever found yourself in this position?
Your sysadmin is awesome.
Your sysadmin is also busy and does not install software in a timely fashion.
You could install what you need in easily if only you had root privileges.

The truth is that most software does not require root privileges to run.
Root privileges are only needed to install the software in sensitive directories.
There is generally no reason why a local user install will not work.

This post will cover installing software in **$HOME/local**.
Specifically, the **keychain** utility will be built from source and manually installed.
Root privileges are specifically not required.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-17 17:49:50 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r296925: Wed Mar 16 20:53:04 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions

First, create **$HOME/local**.

{% highlight sh %}
mkdir -p $HOME/local/bin
mkdir -p $HOME/local/lib
mkdir -p $HOME/local/share
{% endhighlight %}

Add **$HOME/local/bin** to your path in **$HOME/.profile**.
If you are not using **sh**, this line may belong in another file.
Adding **$HOME/local/bin** before **$PATH** is important.
You probably want your local install to take
precedence over a system wide installation.

**.profile**
{% highlight sh %}
export PATH="$HOME/local/bin:$PATH"
{% endhighlight %}

Reload **$HOME/.profile** so changes take effect.

{% highlight sh %}
. $HOME/.profile
{% endhighlight %}

Clone the **keychain** git repository into **$HOME/local**.

{% highlight sh %}
cd $HOME/local
git clone https://github.com/funtoo/keychain.git
cd keychain
{% endhighlight %}

Build and install **keychain**.
So far as I can tell, **keychain** needs to be manually
installed on systems that do not support RPM.
Other software may have options to configure the installation directory.
In any case, a manual installation is a valuable experience.

{% highlight sh %}
make
install -m0755 keychain $HOME/local/bin
mkdir -p $HOME/local/share/man/man1
install -m0644 keychain.1 $HOME/local/share/man/man1
{% endhighlight %}

The **keychain** utility and **man** page should now be available.

{% highlight sh %}
man keychain
keychain
{% endhighlight %}

Finally, consider letting your sysadmin know what you installed.
A system wide install may make sense.

## References:
- [Keychain Official Project Page][keychain]
- [Keychain Github Repository][keychain-github]
- [RPM, Creating the Spec File][rpm-spec]

[keychain]: http://www.funtoo.org/Keychain
[keychain-github]: https://github.com/funtoo/keychain
[rpm-spec]: http://www.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html

