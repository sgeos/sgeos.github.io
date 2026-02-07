---
layout: post
comments: true
title:  "Setting the Android SE Linux Mode on a Rooted Device"
date:   2016-05-22 12:35:08 +0000
categories: android selinux
---

<!-- A35 -->

I recently ran into a case where I needed to change the SE Linux mode on
a rooted Android device.
This post gives basic information on how to get and set the SE Linux mode.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-05-22 12:35:08 +0000
$ uname -vm
Darwin Kernel Version 15.5.0: Tue Apr 19 18:36:36 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.5
$ adb shell "uname -a"
Linux localhost 3.4.0-g9b167b4 #1 SMP PREEMPT Sat May 21 22:15:51 PDT 2016 armv7l
$ adb shell 'echo "Android $(cat /system/build.prop | grep build.version.release | sed s/.*=//) ($(cat /system/build.prop | grep ro.build.host | sed s/.*=//) $(cat /system/build.prop | grep ro.modversion | sed s/.*=//))\\n$(cat /system/build.prop | grep ro.product.model | sed s/.*=//) ($(cat /system/build.prop | grep ro.product.device | sed s/#.*// | sed s/.*=// | tr -d \\n))"'
Android 6.0.1 (cyanogenmod 13.0-20160522-NIGHTLY-hammerhead)
Nexus 5 (hammerhead)
{% endhighlight %}

## Instructions

The current SE Linux mode can be viewed by going to Settings → System →
About phone → SELinux status.
The **getenforce** command can be used to get the current SE Linux mode
from the command line.

{% highlight sh %}
adb shell "su -c 'getenforce'"
{% endhighlight %}

The **setenforce** command can be used to set the current SE Linux mode.
Note that the SE Linux mode will reset when the device is restarted.

{% highlight sh %}
adb shell "su -c 'setenforce permissive'"
adb shell "su -c 'setenforce enforcing'"
adb shell "su -c 'setenforce 0'" # Permissive
adb shell "su -c 'setenforce 1'" # Enforcing
{% endhighlight %}

## References:
- [Security Enhancements (SE) for Android™][selinux-android]

[selinux-android]: https://sgeos.github.io

