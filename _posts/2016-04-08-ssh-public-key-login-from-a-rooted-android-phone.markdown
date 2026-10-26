---
layout: post
comments: true
title:  "SSH Public Key Login From a Rooted Android Phone"
date:   2016-04-08 19:58:32 +0000
categories: ssh android unix
---

<!-- A32 -->
<script>console.log("A32");</script>

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

**enable-ssh-workon.sh**
{% highlight sh %}
#!/system/bin/env sh

SSH_HOME="/data/.ssh"
printf "Linking '/.ssh' -> '${SSH_HOME}' ... "
mount -o remount,rw /
rm -f "/.ssh"
ln -s "${SSH_HOME}" "/.ssh"
echo "Done."

MKSHRC="/system/etc/mkshrc"
printf "Patching '${MKSHRC}' ... "
mount -o remount,rw /system
BODY=$(cat "${MKSHRC}")
ORIGINAL=": place customisations above this line"
PATCH=$(printf "source /sdcard/workon.sh\n\n${ORIGINAL}")
BODY=$(echo "${BODY/${PATCH}/${ORIGINAL}}")
BODY=$(echo "${BODY/${ORIGINAL}/${PATCH}}")
echo "${BODY}" > "${MKSHRC}"
echo "Done."
{% endhighlight %}

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- "SSH, How do I set up SSH public-key authentication to connect to a remote system?" n.d. kb.iu.edu. Accessed October 25, 2026. [https://kb.iu.edu/d/aews][ssh_keygen]
- "SSH, man ssh." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/cgi/man.cgi?query=ssh&sektion=1][ssh_man]
- "sshd\_config(5) Mac OS X Manual Page." n.d. developer.apple.com. Accessed October 25, 2026. [https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/sshd\_config.5.html][sshd_config_man]
- "UNIX, In Unix, what is a symbolic link, and how do I create one?" n.d. kb.iu.edu. Accessed October 25, 2026. [https://kb.iu.edu/d/abbe][unix_symlink]

### General Sources

- "Android Partitions Explained: Boot, System, Recovery, Data, Cache & Misc." 2011. *AddictiveTips*, May 19. [http://www.addictivetips.com/mobile/android-partitions-explained-boot-system-recovery-data-cache-misc/][android_partitions]
- "Android, man mksh." n.d. Accessed October 25, 2026. [https://www.mirbsd.org/htman/i386/man1/false.htm][android_man_mksh]
- "Encryption: RSA vs. DSA for SSH Authentication Keys." n.d. Accessed October 25, 2026. [http://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys][ssh_rsa]
- "How to Enable SSH on Your Mac." n.d. *TechRadar*. Accessed October 25, 2026. [http://www.techradar.com/us/how-to/computing/apple/how-to-enable-ssh-on-your-mac-1305644][ssh_osx]
- "Is There a .Bashrc Equivalent for Android?" n.d. XDA Developers. Accessed October 25, 2026. [http://forum.xda-developers.com/showthread.php?t=514470][android_profile]
- "Mac Osx: How to Start/stop/restart Launchd Services from the Command Line?" n.d. Accessed October 25, 2026. [http://serverfault.com/questions/194832/how-to-start-stop-restart-launchd-services-from-the-command-line][ssh_osx_restart]
- "Make a Passwordless SSH Connection between OSX 10.10 Yosemite and Linux." 2014. *Coolestguidesontheplanet.com \| Neil Gee*, October 27. [https://coolestguidesontheplanet.com/make-passwordless-ssh-connection-osx-10-9-mavericks-linux/][ssh_key_connection]
- "Mksh: Can I Update the Adb Shell's Environment Variables?" n.d. Accessed October 25, 2026. [http://android.stackexchange.com/questions/53389/can-i-update-the-adb-shells-environment-variables][android_mkshrc]
- "Sshd: How Do I Force SSH to Only Allow Uses with a Key to Log In?" n.d. Accessed October 25, 2026. [http://askubuntu.com/questions/346857/how-do-i-force-ssh-to-only-allow-uses-with-a-key-to-log-in][ssh_force_key]
- "A Terminal Command for a Rooted Android to Remount /System as Read/write." n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/5467881/a-terminal-command-for-a-rooted-android-to-remount-system-as-read-write][android_remount]
- "Terminal: Disable Password Authentication on SSH Server on OS X Server 10.8: Ask Different." n.d. Accessed October 25, 2026. [http://apple.stackexchange.com/questions/84523/disable-password-authentication-on-ssh-server-on-os-x-server-10-8][ssh_osx_disable]
- "UNIX, Bash: Strip trailing linebreak from output." n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/12524308/bash-strip-trailing-linebreak-from-output][unix_newline]
- "UNIX, Find and Replace Inside a Text File from a ash Command." n.d. Accessed October 25, 2026. [http://stackoverflow.com/questions/16974797/find-and-replace-inside-a-text-file-from-a-ash-command][unix_replace]
- "UNIX, Linux Delete Symbolic Link ( Softlink )." n.d. Accessed October 25, 2026. [http://www.cyberciti.biz/faq/linux-remove-delete-symbolic-softlink-command/][unix_unlink]

### Related Posts

- Sechter, Brendan. 2016. "Using Shell Functions to Jump Into Terminal Projects." *Brendan A R Sechter's Development Blog*, March 17. [https://sgeos.github.io/unix/sh/2016/03/17/using-shell-functions-to-jump-into-terminal-projects.html][unix_workon]

[android_man_mksh]: https://www.mirbsd.org/htman/i386/man1/false.htm
[android_mkshrc]: http://android.stackexchange.com/questions/53389/can-i-update-the-adb-shells-environment-variables
[android_partitions]: http://www.addictivetips.com/mobile/android-partitions-explained-boot-system-recovery-data-cache-misc/
[android_profile]: http://forum.xda-developers.com/showthread.php?t=514470
[android_remount]: http://stackoverflow.com/questions/5467881/a-terminal-command-for-a-rooted-android-to-remount-system-as-read-write
[ssh_force_key]: http://askubuntu.com/questions/346857/how-do-i-force-ssh-to-only-allow-uses-with-a-key-to-log-in
[ssh_key_connection]: https://coolestguidesontheplanet.com/make-passwordless-ssh-connection-osx-10-9-mavericks-linux/
[ssh_keygen]: https://kb.iu.edu/d/aews
[ssh_man]: https://www.freebsd.org/cgi/man.cgi?query=ssh&sektion=1
[ssh_osx]: http://www.techradar.com/us/how-to/computing/apple/how-to-enable-ssh-on-your-mac-1305644
[ssh_osx_disable]: http://apple.stackexchange.com/questions/84523/disable-password-authentication-on-ssh-server-on-os-x-server-10-8
[ssh_osx_restart]: http://serverfault.com/questions/194832/how-to-start-stop-restart-launchd-services-from-the-command-line
[ssh_rsa]: http://security.stackexchange.com/questions/5096/rsa-vs-dsa-for-ssh-authentication-keys
[sshd_config_man]: https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/sshd_config.5.html
[unix_newline]: http://stackoverflow.com/questions/12524308/bash-strip-trailing-linebreak-from-output
[unix_replace]: http://stackoverflow.com/questions/16974797/find-and-replace-inside-a-text-file-from-a-ash-command
[unix_symlink]: https://kb.iu.edu/d/abbe
[unix_unlink]: http://www.cyberciti.biz/faq/linux-remove-delete-symbolic-softlink-command/
[unix_workon]: {% post_url 2016-03-17-using-shell-functions-to-jump-into-terminal-projects %}
