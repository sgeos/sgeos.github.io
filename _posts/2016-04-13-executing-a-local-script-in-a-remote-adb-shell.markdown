---
layout: post
comments: true
title:  "Executing a Local Script in a Remote ADB Shell"
date:   2016-04-13 23:01:12 +0000
categories: android adb sh
---
It can be useful to write and store scripts on a local
development machine and run them remotely on one or more
Android devices.  This post covers how this is done.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-04-13 23:01:12 +0000
$ uname -vm
Darwin Kernel Version 15.4.0: Fri Feb 26 22:08:05 PST 2016; root:xnu-3248.40.184~3/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.4
/*
$ adb shell "uname -a" # Nexus 5; Cyanogenmod CM-13.0-20160413-NIGHTLY; Android 6.0.1
Linux localhost 3.4.0-g9b167b4 #1 SMP PREEMPT Wed Apr 13 01:02:03 PDT 2016 armv7l
{% endhighlight %}

## Instructions

Create a sample script to execute.
The shebang line is written for Android.

**script.sh**
{% highlight sh %}
#!/system/bin/env sh
echo "$(whoami)@$(hostname)"
uname -a
which env
which sh
{% endhighlight %}

Executing commands over **ssh** is relatively easy,
however most Android devices do not have **sshd** enabled.

{% highlight sh %}
ssh username@host < script.sh
{% endhighlight %}

A script can not be piped into **adb**.
The following strategy can be used instead.
This will probably only work for **sh** scripts.
The shebang is ignored.

{% highlight sh %}
adb shell "$(cat script.sh)"
{% endhighlight %}

If the shebang is important, a script like the following
can be used to execute other scripts remotely.

**adb-remote-script.sh**
{% highlight sh %}
#!/usr/bin/env sh
for script
do
  SHEBANG=$(head -n 1 "${script}")
  case $SHEBANG in
    '#!'*)
      adb shell "echo '$(cat "${script}")' | ${SHEBANG#'#!'}"
      ;;  
    *)  
      adb shell "$(cat "${script}")"
      ;;  
  esac
done
{% endhighlight %}

The remote execution script can be used as followed.

{% highlight sh %}
chmod +x adb-remote-script.sh
./adb-remote-script.sh script.sh
{% endhighlight %}

The above is a proof of concept.
Interpreters like **perl** and **python** are probably not installed.
If piping input into the shebang does not work, another case can be written.
For example, the following could be used if **elixir** were available.
This case needs to be placed above the other case statements.

{% highlight sh %}
    '#!'*elixir*)
      adb shell "${SHEBANG#'#!'} -e '$(cat "${script}")'"
      ;;  
{% endhighlight %}

## References:
- [Android, mksh][android-man-mksh]
- [Android, Cyanogenmod SSH][android-cyanogenmod-ssh]
- [Android, SSH Public Key Login From a Rooted Android Phone][android-ssh-public]
- [Unix, Passing commands through an SSH shell in a bash script][unix-ssh-command]

[android-man-mksh]: https://sgeos.github.io
[android-cyanogenmod-ssh]: https://wiki.cyanogenmod.org/w/Doc:_sshd
[android-ssh-public]: https://sgeos.github.io/ssh/android/unix/2016/04/08/ssh-public-key-login-from-a-rooted-android-phone.html
[unix-ssh-command]: http://www.linuxquestions.org/questions/linux-newbie-8/passing-commands-through-an-ssh-shell-in-a-bash-script-817072/

