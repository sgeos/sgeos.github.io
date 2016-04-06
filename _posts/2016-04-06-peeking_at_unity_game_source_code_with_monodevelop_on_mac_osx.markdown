---
layout: post
comments: true
title:  "Peeking at Unity Game Source Code with MonoDevelop on Mac OS X"
date:   2016-04-06 19:12:17 +0000
categories: unity monodevelop decompile android apk
---
I am occasionally curious to peek at the source code of a Unity game,
mainly to see how it is broken into classes.
This is easy to do with MonoDevelop.

The solution in this post has some limitations.
Comments and the project structure will be lost.
Assets can not be viewed.
Obfuscated source code will be unintelligible.

Make sure you are not breaking any EULAs before trying this.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-04-06 19:12:17 +0000
$ uname -vm
Darwin Kernel Version 15.4.0: Fri Feb 26 22:08:05 PST 2016; root:xnu-3248.40.184~3/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.4
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /Applications/Unity/MonoDevelop.app/Contents/Info.plist | grep -E 'CFBundleName|CFBundleShortVersionString' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
MonoDevelop 5.9.6
{% endhighlight %}

## Instructions

The easiest way to peek at the source code of a Unity game is to start with an Android APK.
Find an Android APK that you know or suspect was made with Unity and unzip it.

{% highlight sh %}
unzip unity_game.apk -d unzipped_unity_game
cd unzipped_unity_game
{% endhighlight %}

Open **MonoDevelop** and the **assets/bin/Data/Managed** directory.

{% highlight sh %}
open -a MonoDevelop
open assets/bin/Data/Managed/
{% endhighlight %}

If the APK was made with Unity, **UnityEngine.dll** will be in the directory.
The interesting source code tends to be stored in the following files.
There may also be some libraries that are used by the game.

- Assembly-CSharp-firstpass.dll
- Assembly-CSharp.dll
- Assembly-UnityScript-firstpass.dll
- Assembly-UnityScript.dll

Drag one or all of the above dll files into **MonoDevelop** and an **Assembly Browser** window should open.
Select the class you want to view on left hand side of the window.
Change **Visibility** to **All members** and **Language** to **C#** to see a complete decompiled code listing.

## References:

- [Unity3D, MonoDevelop’s Assembly Browser – Decompile managed plugins][unity-decompile]
- [Unity3D, Exploring Unity With Reflection And The Assembly Browser][unity-reflect]
- [UNIX, man unzip][man-unzip]

[unity-decompile]: http://unitylore.com/articles/monodevelop-assembly-browser/
[unity-reflect]: http://purdyjotut.blogspot.com/2013/10/exploring-unity-with-reflection-and.html
[man-unzip]: https://www.freebsd.org/cgi/man.cgi?query=unzip&sektion=1

