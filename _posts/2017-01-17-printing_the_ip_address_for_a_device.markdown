---
layout: post
mathjax: false
comments: true
title:  "Printing the IP Address for a Device"
date:   2017-01-17 11:24:20 +0000
categories: sh freebsd unix
---

<!-- A47 -->

I often work with VMs.
Sometimes I want to SSH into a physical server or a laptop.
Either way I need to know the IP address of the box to get work done.

This post covers a function that can be used to print the (DHCP) IP for a device on a box you are working on.
If you put it in **.profile**, you can log into a VM or physical box to get the IP address.
You can then use that to SSH into the box.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-01-17 11:24:20 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #14 f92c24b(drm-next-4.7): Fri Jan  6 19:28:21 UTC 2017     root@gauntlet:/usr/obj/usr/src/sys/GENERIC  amd64
{% endhighlight %}

## Instructions

Here is an **sh** function that can be used to print the ip address for a device.
I put it in **.profile**.

**.profile** partial listing
{% highlight sh %}
print_ip_address(){
  ipv4="$(ifconfig "${1}" | grep "inet " | sed -E "s/.*inet.([0-9.]*).*/\1/")"
  ipv6="$(ifconfig "${1}" | grep "inet6 " | sed -E "s/.*inet6.([0-9a-f:]*).*/\1/")"
  printf "${1}\t${ipv4:-(no ipv4)}\t${ipv6:-(no ipv6)}\n"
}
{% endhighlight %}

I also have this at the bottom of **.profile**.

**.profile** partial listing
{% highlight sh %}
hostname
print_ip_address em0
print_ip_address wlan0
{% endhighlight %}

When I log in, I see something like this.

**sh**
{% highlight sh %}
my.hostname.com
em0	(no ipv4)	fe80::3e97:eff:fe34:157c
wlan0	192.168.12.34	(no ipv6)
{% endhighlight %}

A **csh** script (for FreeBSD root) that does the same thing looks something like this.

**print_ip.csh** complete listing
{% highlight csh %}
#!/bin/csh

set device = $1
set ipv4 = `ifconfig "${device}" | grep "inet " | sed -E "s/.*inet.([0-9.]*).*/\1/" | sed 's/^$/(no ipv4)/'`
set ipv6 = `ifconfig "${device}" | grep "inet6 " | sed -E "s/.*inet6.([0-9a-f:]*).*/\1/" | sed 's/^$/(no ipv6)/'`
printf "${device}\t${ipv4}\t${ipv6}\n"
{% endhighlight %}

