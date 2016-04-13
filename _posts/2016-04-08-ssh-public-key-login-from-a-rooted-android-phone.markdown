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
**/data** and the SD card survive OS updates, but only root can properly write to **/data**.
In light of this, this solution is written such that root calls **ssh** to log into another box.
The SD card is used to store a script that contains a convenience function so connections can be canned.

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

Open a shell on your phone and switch to root.

{% highlight sh %}
adb shell
su
{% endhighlight %}

Define some variables.
Change these if you want to customize your installation.
Note that the **/data** partition survives OS updates.

{% highlight sh %}
SSH_HOME="/data/.ssh"
SSH_ID="${SSH_HOME}/id_rsa"
{% endhighlight %}

Create the **.ssh** directory.

{% highlight sh %}
mkdir "${SSH_HOME}"
chmod 700 "${SSH_HOME}"
{% endhighlight %}

Create a symlink so root ssh will work.
The root home directory is **/**.
This step will need to be repeated after an OS update.

{% highlight sh %}
mount -o remount,rw /
ln -s "${SSH_HOME}" /.ssh
{% endhighlight %}

Generate the SSH key.

{% highlight sh %}
ssh-keygen -t rsa -f "${SSH_ID}"
{% endhighlight %}

Add **.ssh/known_hosts**.

{% highlight sh %}
touch "${SSH_HOME}/known_hosts"
chmod 644 "${SSH_HOME}/known_hosts"
{% endhighlight %}

Copy the Android public key from the phone to to
**.ssh/authorized_keys** on any machines you want to log into.

{% highlight sh %}
cat "${SSH_ID}.pub" 
{% endhighlight %}

As root on the Android phone, **ssh** into a machine to add it to **.ssh/known_hosts**.

{% highlight sh %}
ssh "username@host.org"
{% endhighlight %}

## Convenience SSH Shell Script

Doing command line work with a tiny touch screen keyboard is painful.
Convenience shell functions make this task bearable.

I could not get **.profile** to work out of the box on Android.
The Android shell always runs **/system/etc/mkshrc**.
The problem is that this script is replaced when the
operating system is updated so the goal is to keep changes minimal.
Remount **/system** in read/write mode so this file can be modified.

{% highlight sh %}
mount -o remount,rw /system
{% endhighlight %}

Add a line to load a script from the SD card to the bottom of **mkshrc**.

**/system/etc/mkshrc** partial listing
{% highlight sh %}
source /sdcard/workon.sh # new line

: place customisations above this line
{% endhighlight %}

Now the **workon.sh** script will be loaded from the SD card when the shell starts.
Files on the SD card can not be executed, so loading the script makes more sense than creating a utility.
If the script were placed in **/data** it could be executed, but only by root.
This solution allows a non-root shell to use the script.

Add the following convenience function to **/sdcard/workon.sh** to log into different machines.
Replace the alpha and beta entries with your own machines.
This file should survive operating system updates because it is on the SD card.

Redefine **SSH_ID** if you want to store **.ssh** in another location.
Note that **ssh** will refuse to use the keys if they are user readable,
so putting them on the SD card is not an option.

**/sdcard/workon.sh**
{% highlight sh %}
#!/system/bin/env sh
workon() {
  SSH_USERNAME="username"
  SSH_ID="/data/.ssh/id_rsa"
  case "${1}" in
    admin)
      su -c "cd; clear; pwd"; su
      ;;
    alpha)
      su -c "ssh -i '${SSH_ID}' '${SSH_USERNAME}@alpha.org'"
      ;;
    beta)
      su -c "ssh -i '${SSH_ID}' '${SSH_USERNAME}@192.168.0.123'"
      ;;
    *)
      if [ -n "${1}" ]
      then
        su -c "ssh -i '${SSH_ID}' '${SSH_USERNAME}@${1-localhost}'"
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

If you want to add the same function to a normal UNIX box, the workon function looks like this.
Put it in something like **${HOME}/.profile**.

**${HOME}/.profile** partial listing
{% highlight sh %}
workon() {
  SSH_USERNAME="username"
  ROOT_HOME="/var/root"
  case "${1}" in
    admin)
      (cd "${ROOT_HOME}"; clear; pwd; su)
      ;;
    alpha)
      ssh "${SSH_USERNAME}@alpha.org"
      ;;
    beta)
      ssh "${SSH_USERNAME}@192.168.0.123"
      ;;
    *)
      if [ -n "${1}" ]
      then
        ssh "${SSH_USERNAME}@{1-localhost}"
      else
        cd; clear; pwd
      fi
      ;;
  esac
}
{% endhighlight %}

## Upgrading

After upgrading the OS, a couple of the steps need to be repeated.

Recreate the **.ssh** symlink.

{% highlight sh %}
mount -o remount,rw /
ln -s "${SSH_HOME}" /.ssh
{% endhighlight %}

Remount **/system**.

{% highlight sh %}
mount -o remount,rw /system
{% endhighlight %}

Add the line to load the SD card script to the bottom of **mkshrc**.

**/system/etc/mkshrc** partial listing
{% highlight sh %}
source /sdcard/workon.sh # new line

: place customisations above this line
{% endhighlight %}

Alternatively, use the following script to perform the
above tasks after upgrading Android.

{% highlight sh %}
#!/system/bin/env sh
SSH_HOME="/data/.ssh"
mount -o remount,rw /
rm -f "/.ssh"
ln -s "${SSH_HOME}" "/.ssh"
mount -o remount,rw /system
MKSHRC="/system/etc/mkshrc"
BODY=$(cat "${MKSHRC}")
ORIGINAL=": place customisations above this line"
PATCH=$(printf "source /sdcard/workon.sh\n\n${ORIGINAL}")
BODY=$(echo "${BODY/${PATCH}/${ORIGINAL}}")
BODY=$(echo "${BODY/${ORIGINAL}/${PATCH}}")
echo "${BODY}" > "${MKSHRC}"
{% endhighlight %}

## References:
- [Android, Is there a .bashrc equivalent for android?][android-profile]
- [Android, A terminal command for a rooted Android to remount /System as read/write][android-remount]
- [Android, Android Partitions Explained: boot, system, recovery, data, cache & misc][android-partitions]
- [Android, Can I update the adb shell's environment variables?][android-mkshrc]
- [Android, man mksh][android-man-mksh]
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
- [UNIX, In Unix, what is a symbolic link, and how do I create one?][unix-symlink]
- [UNIX, Bash: Strip trailing linebreak from output][unix-newline]
- [UNIX, Find and Replace Inside a Text File from a ash Command][unix-replace]

[android-profile]: http://forum.xda-developers.com/showthread.php?t=514470
[android-remount]: http://stackoverflow.com/questions/5467881/a-terminal-command-for-a-rooted-android-to-remount-system-as-read-write
[android-partitions]: http://www.addictivetips.com/mobile/android-partitions-explained-boot-system-recovery-data-cache-misc/
[android-mkshrc]: http://android.stackexchange.com/questions/53389/can-i-update-the-adb-shells-environment-variables
[android-man-mksh]: https://www.mirbsd.org/htman/i386/man1/false.htm
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
[unix-symlink]: https://kb.iu.edu/d/abbe
[unix-newline]: http://stackoverflow.com/questions/12524308/bash-strip-trailing-linebreak-from-output
[unix-replace]: http://stackoverflow.com/questions/16974797/find-and-replace-inside-a-text-file-from-a-ash-command

