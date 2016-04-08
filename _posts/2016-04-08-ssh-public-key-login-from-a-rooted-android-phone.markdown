---
layout: post
comments: true
title:  "SSH Public Key Login From a Rooted Android Phone"
date:   2016-04-08 19:58:32 +0000
categories: ssh android unix
---
I wanted to be able to used my phone to log into my MacBook.
The catch?  I do not want passwords enabled.
This post covers what I did to achieve this goal.

Android does not store users in **/etc/passwd** so it is
exceedingly difficult to add users for command line work.
Home directories for the users that are available seem to default to **/** or **/data**.
In light of this, this solution is written such that root calls **ssh** to log into another box.

The solution in this post assumes a rooted phone with busybox.
My phone is a Nexus 5 running Cyanogenmod 13.
As written, this solution may need minor modifications to work other phones.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-04-08 19:58:32 +0000
$ uname -vm
Darwin Kernel Version 15.4.0: Fri Feb 26 22:08:05 PST 2016; root:xnu-3248.40.184~3/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.4
$ adb shell "uname -a" # Nexus 5; Cyanogenmod CM-13.0-20160407-NIGHTLY; Android 6.0.1
Linux localhost 3.4.0-g9b167b4 #1 SMP PREEMPT Wed Apr 6 21:49:26 PDT 2016 armv7l
{% endhighlight %}

## Disable Password Based SSH

SSH can be enabled on OSX by going to Preferences → Sharing and selecting Remote Login.
Optionally allow access for all users.

Password login can be disabled by adding the following lines to **/etc/ssh/sshd_config** as root.
Note that the file is **sshd**_config, not **ssh**_config.

**/etc/ssh/sshd_config** partial listing
{% highlight sh %}
# Disable Password Login
UsePam no
ChallengeResponseAuthentication no
PasswordAuthentication no
kbdInteractiveAuthentication no
{% endhighlight %}

Restart **sshd** as root after making any configuration changes.

{% highlight sh %}
launchctl unload  /System/Library/LaunchDaemons/ssh.plist
launchctl load -w /System/Library/LaunchDaemons/ssh.plist
{% endhighlight %}

## Adding an SSH Key to a Rooted Android Device

Open a shell on your phone as root.

{% highlight sh %}
adb shell
su
{% endhighlight %}

The root home directory is **/** on my phone.
Remount it for writing, and add the **.ssh** directory.

{% highlight sh %}
mount -o remount,rw /
mkdir /.ssh
{% endhighlight %}

Add **.ssh/known_hosts**.
This file will ultimately be mounted read only,
but it is probably a good idea to add hosts to it while file can be written to.

{% highlight sh %}
touch /.ssh/known_hosts
{% endhighlight %}

Generate the SSH key.

{% highlight sh %}
ssh-keygen -t rsa -f /.ssh/id_rsa
{% endhighlight %}

Permissions should look like this.

{% highlight sh %}
chmod 700 /.ssh
chmod 600 /.ssh/id_rsa
chmod 644 /.ssh/id_rsa.pub
chmod 644 /.ssh/known_hosts
{% endhighlight %}

Copy the Android public key from the phone to to
**.ssh/authorized_keys** on any machines you want to log into.

{% highlight sh %}
cat /.ssh/id_rsa.pub
{% endhighlight %}

As root on the Android phone, **ssh** into the remote machine to add it to **.ssh/known_hosts**.
After all the machines you want to log into have been added,
it will not matter if **.ssh/known_hosts** is mounted read only.

{% highlight sh %}
ssh -i /.ssh/id_rsa username@alpha.org
{% endhighlight %}

## Convenience SSH Shell Script

Doing command line work with a tiny touch screen keyboard is painful.
Convenience shell functions makes this task less painful.

I could not get **.profile** to work out of the box on Android.
Evidently **/system/etc/mkshrc** is the file that is automatically
started after the shell starts running.
Add the following convenience function to log into different machines.
Replace the alpha and beta entries with your own machines.

Redefine **SSH_ID** if you want to store **.ssh** in another location.
Note that **ssh** will refuse to use the keys if they are user readable,
so using the SD card is not an option.

**/system/etc/mkshrc** partial listing
{% highlight sh %}
workon() {
  SSH_ID="/.ssh/id_rsa"
  case "${1}" in
    admin)
      su -c "cd; clear; pwd"; su
      ;;
    alpha)
      su -c "ssh -i ${SSH_ID} username@alpha.org"
      ;;
    beta)
      su -c "ssh -i ${SSH_ID} username@192.168.0.123"
      ;;
    *)
      if [ -n "${1}" ]
      then
        su -c "ssh -i ${SSH_ID} username@${1-localhost}"
      else
        cd; clear; pwd
      fi
      ;;
  esac
}
{% endhighlight %}

Now the Android phone can log into machine Alpha like this.

{% highlight sh %}
workon alpha
{% endhighlight %}

As a bonus, the following can be used to get ready to do admin work on the Android phone.

{% highlight sh %}
workon admin
{% endhighlight %}

## References:
- [Android, Is there a .bashrc equivalent for android?][android-profile]
- [Android, A terminal command for a rooted Android to remount /System as read/write][android-remount]
- [SSH, How do I force SSH to only allow uses with a key to log in?][ssh-force-key]
- [SSH, Make a passwordless SSH Connection between OSX 10.10 Yosemite and Linux Server][ssh-key-connection]
- [SSH, How do I set up SSH public-key authentication to connect to a remote system?][ssh-keygen]
- [SSH, RSA vs. DSA for SSH authentication keys][ssh-rsa]
- [SSH, How To Enable SSH on Your Mac][ssh-osx]
- [SSH, How to start/stop/restart launchd services from the command line?][ssh-osx-restart]
- [SSH, Disable password authentication on SSH server on OS X Server 10.8][ssh-osx-disable]
- [SSH, man ssh][ssh-man]
- [SSH, man sshd_config][sshd_config-man]
- [UNIX, Using Shell Functions to Jump Into Terminal Projects][unix-workon]

[android-profile]: http://forum.xda-developers.com/showthread.php?t=514470
[android-remount]: http://stackoverflow.com/questions/5467881/a-terminal-command-for-a-rooted-android-to-remount-system-as-read-write
[ssh-force-key]: http://askubuntu.com/questions/346857/how-do-i-force-ssh-to-only-allow-uses-with-a-key-to-log-in
[ssh-key-connection]: https://coolestguidesontheplanet.com/make-passwordless-ssh-connection-osx-10-9-mavericks-linux/
[ssh-keygen]: https://kb.iu.edu/d/aews
[ssh-rsa]: http://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys
[ssh-osx]: http://www.techradar.com/us/how-to/computing/apple/how-to-enable-ssh-on-your-mac-1305644
[ssh-osx-restart]: http://serverfault.com/questions/194832/how-to-start-stop-restart-launchd-services-from-the-command-line
[ssh-osx-disable]: http://apple.stackexchange.com/questions/84523/disable-password-authentication-on-ssh-server-on-os-x-server-10-8
[ssh-man]: https://www.freebsd.org/cgi/man.cgi?query=ssh&sektion=1
[sshd_config-man]: https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/sshd_config.5.html
[unix-workon]: https://sgeos.github.io/unix/sh/2016/03/17/using-shell-functions-to-jump-into-terminal-projects.html

