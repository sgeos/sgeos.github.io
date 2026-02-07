---
layout: post
comments: true
title:  "A Script to Extract App Data From a Rooted Android Device"
date:   2016-04-10 20:03:14 +0000
categories: android
---

<!-- A33 -->

It can be useful to get a copy of all of the data an Android app has stored on the phone.
Specifically, getting SQLite to work with a new app always seems to be a minor hiccup for me.
There are other times when getting a copy of the private app data can be useful.

This post covers a script for OSX that can be used to extract app data from a rooted Android device.
It assumes **adb** is installed on OSX and **busybox** or
some other full feature **toolbox** is installed on the Android device.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-04-10 20:03:14 +0000
$ uname -vm
Darwin Kernel Version 15.4.0: Fri Feb 26 22:08:05 PST 2016; root:xnu-3248.40.184~3/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.4
$ adb shell "uname -a" # Nexus 5; Cyanogenmod CM-13.0-20160409-NIGHTLY; Android 6.0.1
Linux localhost 3.4.0-g9b167b4 #1 SMP PREEMPT Fri Apr 8 21:40:42 PDT 2016 armv7l
{% endhighlight %}

## Instructions

The following script can be used to copy the data from a
rooted Android device and copy it to a machine running OSX.
A default package name can be specified on the second line.
Changing this this is useful if you only work on one app at a time.

**android-app-data-clone.sh**
{% highlight sh %}
#!/usr/bin/env sh
APP_ID=${1-"com.google.android.webview"}
ARCHIVE=${2-"${APP_ID}.$(date -u '+%Y%m%d.%H%M%S')"}

adb_shell_su_command() {
  adb shell "su -c '${1-true}'"
}

adb_shell_su_command "cd '/data/data/${APP_ID}'; tar -zcvf '/sdcard/Download/${ARCHIVE}.tar.gz' ."
adb pull "/sdcard/Download/${ARCHIVE}.tar.gz"
adb_shell_su_command "rm '/sdcard/Download/${ARCHIVE}.tar.gz'"
mkdir -p "${ARCHIVE}"
tar -zxvf "${ARCHIVE}.tar.gz" -C "${ARCHIVE}"
rm "${ARCHIVE}.tar.gz"
open "${ARCHIVE}"
{% endhighlight %}

The script can be used like this.

{% highlight sh %}
chmod +x android-app-data-clone.sh

# default app, default archive name
./android-app-data-clone.sh

# specified app, default archive name
./android-app-data-clone.sh com.google.android.youtube

# specified app and archive name
./android-app-data-clone.sh com.google.android.apps.youtube.music YouTubeMusicData
{% endhighlight %}

## References:
- [Android, ApplicationId versus PackageName][android-package]
- [UNIX, How do I Compress a Whole Linux or UNIX Directory?][unix-tar]
- [UNIX, How to extract files to another directory using 'tar' command?][unix-tar-dir]

[android-package]: http://tools.android.com/tech-docs/new-build-system/applicationid-vs-packagename
[unix-tar]: http://www.cyberciti.biz/faq/how-do-i-compress-a-whole-linux-or-unix-directory/
[unix-tar-dir]: http://askubuntu.com/questions/45349/how-to-extract-files-to-another-directory-using-tar-command

