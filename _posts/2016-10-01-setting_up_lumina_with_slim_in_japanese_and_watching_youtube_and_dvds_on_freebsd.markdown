---
layout: post
mathjax: false
comments: true
title:  "Setting Up Lumina with slim in Japanese and Watching YouTube and DVDs on FreeBSD"
date:   2016-10-01 23:28:23 +0000
categories: freebsd xorg lumina slim chrome vlc
---

<!-- A46 -->
<script>console.log("A46");</script>

This post covers installing Lumina and xdm on a fresh i386 install.
It also covers installing Japanese fonts and a Japanese IME.
The final test is watching DVDs and YouTube videos-
what a computer needs to do for my wife and kids to consider it useful.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-10-01 23:28:23 +0000
$ uname -vm
FreeBSD 11.0-RC3 #0 r305786: Wed Sep 14 04:19:22 UTC 2016     root@releng2.nyi.freebsd.org:/usr/obj/usr/src/sys/GENERIC  i386
{% endhighlight %}

## Install Lumina Desktop and slim

First, do a minimal install of FreeBSD and login as root.

Make your unprivileged user a member of the wheel group.
This will allow you to conveniently shutdown the computer.

{% highlight sh %}
pw groupmod wheel -m username
{% endhighlight %}

**NOTE:** Consider increasing FETCH_TIMEOUT and/or FETCH_RETRY in
**/usr/local/etc/pkg.conf** if you are getting timeouts when installing packages.

**/usr/local/etc/pkg.conf** partial listing
{% highlight sh %}
FETCH_RETRY=5
FETCH_TIMEOUT=90
{% endhighlight %}

I use **vim** to edit files, so that gets installed first.

{% highlight sh %}
pkg install vim
{% endhighlight %}

**lumina** and **slim** need to be installed.
The localized **lumina-i18n** pulls in **lumina** and **xorg**.

{% highlight sh %}
pkg install lumina-i18n slim 
{% endhighlight %}

Enable **slim** and **dbus** in **/etc/rc.conf**.
**slim** needs **dbus** to start Lumina.
**hald** is not strictly necessary, but it tends to be enabled when running xorg.
Also, if you use a mouse, make sure **moused** is enabled in **/etc/rc.conf**.

**/etc/rc.conf** partial listing
{% highlight sh %}
# xorg
slim_enable="YES"
dbus_enable="YES"
hald_enable="YES"
moused_enable="YES"
{% endhighlight %}

Consider enabling **sshd** just in case something goes horribly wrong when configuring xorg.

**/etc/rc.conf** partial listing
{% highlight sh %}
sshd_enable="YES"
{% endhighlight %}

Generate **xorg.conf**.

{% highlight sh %}
Xorg -configure
cp ~/xorg.conf.new /etc/X11/xorg.conf
{% endhighlight %}

Add the `Load "freetype"` to the "Module" section of **/etc/X11/xorg.conf**.

**/etc/X11/xorg.conf** partial listing
{% highlight sh %}
Section "Module"
        Load  "glx"
        Load  "freetype"
EndSection
{% endhighlight %}

Add the `FontPath "/usr/local/share/fonts/dejavu/"` to the "Files" section of **/etc/X11/xorg.conf**.

**/etc/X11/xorg.conf** partial listing
{% highlight sh %}
Section "Files"
        ModulePath   "/usr/local/lib/xorg/modules"
        FontPath     "/usr/local/share/fonts/misc/"
        FontPath     "/usr/local/share/fonts/TTF/"
        FontPath     "/usr/local/share/fonts/OTF/"
        FontPath     "/usr/local/share/fonts/Type1/"
        FontPath     "/usr/local/share/fonts/100dpi/"
        FontPath     "/usr/local/share/fonts/75dpi/"
        FontPath     "/usr/local/share/fonts/dejavu/"
EndSection
{% endhighlight %}

## Japanese Fonts and IME

Install the Japanese fonts and IME.

{% highlight sh %}
pkg install japanese/font-std japanese/scim-anthy
{% endhighlight %}

Create the following **.xinitrc** for new users.

**/usr/share/skel/dot.xinitrc** complete listing
{% highlight sh %}
#!/bin/sh

# set locale
export LC_ALL=ja_JP.UTF-8
export LANGUAGE=ja_JP.UTF-8
export LANG=ja_JP.UTF-8

# set input method
export XMODIFIERS='@im=SCIM'

# execute scim as a daemon
scim -d

# key board layout
setxkbmap -layout jp

# startx
exec $1
{% endhighlight %}

Copy the above **.xinitrc** to your home directory.

{% highlight sh %}
USERNAME=username
cp /usr/share/skel/dot.xinitrc /home/${USERNAME}/.xinitrc
{% endhighlight %}

After starting xorg, consider running **scim-setup** to configure **scim** for the IME.
By default, switch between kanji and romaji input with *Ctrl-[SPACE]*.

## YouTube

As root, install **chromium** or your broswer of choice.

{% highlight sh %}
pkg install chromium
{% endhighlight %}

As an unprivileged user start **chrome** and watch a [YouTube video][youtube_video].

{% highlight sh %}
chrome https://www.youtube.com/watch?v=CynsucGqMtI
{% endhighlight %}

## DVDs

First, install **vlc** as root.

{% highlight sh %}
pkg install vlc
{% endhighlight %}

Also install **libdvdcss**.
The following *should* work.

{% highlight sh %}
pkg install libdvdcss
{% endhighlight %}

When I tried, the package was not available, so I had to build the port.

{% highlight sh %}
# fetch ports tree
portsnap fetch extract

# install multimedia/libdvdcss port
cd /usr/ports/multimedia/libdvdcss
make config recursive
make install clean
{% endhighlight %}

Add the following line to **/etc/sysctl.conf**.

**/etc/sysctl.conf** partial listing
{% highlight sh %}
vfs.usermount=1
{% endhighlight %}

Verify the device name with **camcontrol**.
It is usually **/dev/cd0**.

{% highlight sh %}
camcontrol devlist
{% endhighlight %}

Next, modify **/etc/sysctl.conf** to make the CDROM/DVDROM mountable by unprivileged users.
Use the device from the previous step.

**/etc/devfs.conf** partial listing
{% highlight sh %}
## Allow members of the operator to mount the cdrom
own　　　　/dev/cd0    root:operator
perm　　　/dev/cd0     0660
{% endhighlight %}

Add your unprivileged user to the operator group.

{% highlight sh %}
pw groupmod operator -m username
{% endhighlight %}

Reboot.

{% highlight sh %}
shutdown -r now
{% endhighlight %}

You should be able to mount and unmount the DVDs as your unprivileged user now.

{% highlight sh %}
CDROM=/dev/cd0
mkdir -p ~/media/cdrom
mount -t cd9660 "${CDROM}" ~/media/cdrom
umount ~/media/cdrom
{% endhighlight %}

As an your unprivileged user, insert a DVD and play it with VLC.

{% highlight sh %}
CDROM=/dev/cd0
vlc dvd://
{% endhighlight %}

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- "5.5. Using Fonts in Xorg." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/x-fonts.html][freebsd_fonts]
- "6.2. Browsers." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/desktop-browsers.html][freebsd_browsers]
- "FreeBSD Handbook, The X Display Manager." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/x-xdm.html][freebsd_display_manager]
- "FreeBSD Handbook, Video Playback." n.d. www.freebsd.org. Accessed October 25, 2026. [https://www.freebsd.org/doc/handbook/video-playback.html][freebsd_video_playback]

### General Sources

- "1. デスクトップ環境構築/Lumina/インストール." n.d. Accessed October 25, 2026. [http://freebsd.sing.ne.jp/desktop/08/01.html][freebsd_japanese_lumina]
- "\[SOLVED\] DVD Won't Play in VLC or MPlayer \[Archive\]." n.d. Accessed October 25, 2026. [https://ubuntuforums.org/archive/index.php/t-1536685.html][dvd_fs]
- "Documentation:Command Line." n.d. Accessed October 25, 2026. [https://wiki.videolan.org/Documentation:Command\_line/\#Opening\_a\_DVD\_or\_VCD.2C\_or\_an\_audio\_CD][vlc_cli]
- "DragonFlyBSD: How to Get to the Desktop." n.d. Accessed October 25, 2026. [https://www.dragonflybsd.org/docs/how\_to\_get\_to\_the\_desktop/][xorg_desktop]
- "FreeBSD での DVD の再生やバックアップなど." n.d. Accessed October 25, 2026. [https://ryogan.org/blog/2012/12/08/freebsd-での-dvd-の再生やバックアップなど/][freebsd_dvd_backup]
- "FreeBSD, デスクトップ環境の構築(Mate 1.12.0 on FreeBSD 10." n.d. Accessed October 25, 2026. [http://silversack.my.coocan.jp/bsd/mate10x-buildmate.htm][freebsd_mate]
- "FreeBSDで遊ぼうのこーな." n.d. Accessed October 25, 2026. [http://legacyos.ichmy.0t0.jp/virtualbsd/][freebsd_play]
- "FS\#13755: Xorg-Xdm Uses the Depreceated Xsm as Default Session Management." n.d. Accessed October 25, 2026. [https://bugs.archlinux.org/task/13755][xdm_xsm]
- "pkg, Operation timed out." n.d. Accessed October 25, 2026. [https://forums.freebsd.org/threads/51501/][freebsd_pkg_timeout]
- "Xorg: What Is '.Xsession' For?" n.d. Accessed October 25, 2026. [http://unix.stackexchange.com/questions/47359/what-is-xsession-for][xdm_xsession]
- "YouTube video." n.d. Accessed October 25, 2026. [https://www.youtube.com/watch?v=CynsucGqMtI][youtube_video]
- "¡ÚFreeBSD¡ÛÆüËÜ¸ìÆþÎÏ´Ä¶­¤ò¹½ÃÛ¤¹¤ë¡Êscim/anthy¡Ë." n.d. Accessed October 25, 2026. [http://www.kishiro.com/FreeBSD/scim-anthy.html][freebsd_scim_anthy]
- "ÆüËÜ¸ì´Ä¶­¤òscim-Anthy¤ÇÀßÄê¤·¤Þ¤·¤¿¡£: hateua123¤ÎÆüµ­." n.d. *¤Ï¤Æ¤Ê¥À¥¤¥¢¥ê¡¼*. Accessed October 25, 2026. [http://d.hatena.ne.jp/hateua123/20121205/1354666208][freebsd_scim_anthy2]

[dvd_fs]: https://ubuntuforums.org/archive/index.php/t-1536685.html
[freebsd_browsers]: https://www.freebsd.org/doc/handbook/desktop-browsers.html
[freebsd_display_manager]: https://www.freebsd.org/doc/handbook/x-xdm.html
[freebsd_dvd_backup]: https://ryogan.org/blog/2012/12/08/freebsd-での-dvd-の再生やバックアップなど/
[freebsd_fonts]: https://www.freebsd.org/doc/handbook/x-fonts.html
[freebsd_japanese_lumina]: http://freebsd.sing.ne.jp/desktop/08/01.html
[freebsd_mate]: http://silversack.my.coocan.jp/bsd/mate10x-buildmate.htm
[freebsd_pkg_timeout]: https://forums.freebsd.org/threads/51501/
[freebsd_play]: http://legacyos.ichmy.0t0.jp/virtualbsd/
[freebsd_scim_anthy]: http://www.kishiro.com/FreeBSD/scim-anthy.html
[freebsd_scim_anthy2]: http://d.hatena.ne.jp/hateua123/20121205/1354666208
[freebsd_video_playback]: https://www.freebsd.org/doc/handbook/video-playback.html
[vlc_cli]: https://wiki.videolan.org/Documentation:Command_line/#Opening_a_DVD_or_VCD.2C_or_an_audio_CD
[xdm_xsession]: http://unix.stackexchange.com/questions/47359/what-is-xsession-for
[xdm_xsm]: https://bugs.archlinux.org/task/13755
[xorg_desktop]: https://www.dragonflybsd.org/docs/how_to_get_to_the_desktop/
[youtube_video]: https://www.youtube.com/watch?v=CynsucGqMtI
