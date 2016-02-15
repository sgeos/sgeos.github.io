---
layout: post
comments: true
title:  "ION DTN as a Service on FreeBSD"
date:   2016-02-15 10:13:57 +0900
categories: freebsd ion dtn
---
This post covers installing ION DTN as a service on FreeBSD.
The goal is to be able to start, stop and restart DTN-ION like any other service.

{% highlight sh %}
service iondtn start
service iondtn stop
service iondtn restart
service iondtn status
{% endhighlight %}

A **killm** command will also be added to force stop ion if a stop or restart hangs.

{% highlight sh %}
service iondtn killm
{% endhighlight %}

## Software Versions

{% highlight sh %}
$ date
February 15, 2016 at 10:13:57 PM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ ionadmin
: v
ION OPEN SOURCE 3.4.0
{% endhighlight %}

## Instructions

ION-DTN needs to [be installed][freebsd-ion].

{% highlight sh %}
ION_TAR='ion-3.4.0b.tar.gz'
wget "http://downloads.sourceforge.net/project/ion-dtn/$ION_TAR"
tar -zxvf "$ION_TAR" 
cd ion-open-source/
su
portmaster devel/gmake shells/bash devel/autotools
find ./ -type f -print0 | xargs -0 sed -i '' 's:#!/bin/bash:#!/usr/bin/env bash:'
echo kern.ipc.shmmni=192 >>/boot/loader.conf
echo kern.ipc.shmseg=128 >>/boot/loader.conf
echo kern.ipc.semmns=32000 >>/boot/loader.conf
echo kern.ipc.semmni=128 >>/boot/loader.conf
echo kern.ipc.shmmax=536870912 >>/boot/loader.conf
echo kern.ipc.shmmin=1 >>/boot/loader.conf
echo kern.ipc.shmall=131072 >>/boot/loader.conf
echo net.inet.udp.maxdgram=32000 >>/boot/loader.conf
echo kern.ipc.shm_use_phys=0 >>/boot/loader.conf
echo kern.ipc.shm_allow_removed=0 >>/boot/loader.conf
shutdown -r now
# after reboot
su
./configure --mandir=/usr/local/man
gmake clean
gmake
gmake install
ldconfig
{% endhighlight %}

Add the run control script as root.

**/usr/local/etc/rc.d/iondtn**

{% highlight sh %}
#!/bin/sh
#
# PROVIDE: iondtn
# REQUIRE: networking
# KEYWORD:
 
. /etc/rc.subr
 
name="iondtn"
rcvar="${name}_enable"
install_dir="/usr/local"
 
start_cmd="${name}_start"
stop_cmd="${name}_stop"
status_cmd="${name}_status"
killm_cmd="${name}_killm"
extra_commands="killm"

load_rc_config $name
: ${iondtn_enable:="no"}
: ${iondtn_user:=${name}}
: ${iondtn_rc:="${install_dir}/etc/${name}.rc"}
: ${iondtn_log_dir:="${install_dir}/${name}"}

iondtn_start()
{
  su -m "$iondtn_user" -c "cd ${iondtn_log_dir}; ionstart -I '${iondtn_rc}'"
}

iondtn_stop()
{
  su -m "$iondtn_user" -c "ionstop"
}

iondtn_status()
{
  # $rfxclock_pid=$(ps -ax | grep "rfxclock" | grep -v "grep" | awk '{ print $1 }')
  # if [ $rfxclock_pid ]
  daemon=rfxclock
  if [ ps -ax | grep "$daemon" | grep -v "grep" ]
  then
    echo "$name is running."
  else
    echo "$name is not running."
  fi
}

iondtn_killm()
{
  su -m "$iondtn_user" -c "killm"
}

load_rc_config $name
run_rc_command "$1"
{% endhighlight %}

Create the configuration file.

**/usr/local/etc/iondtn.rc**
{% highlight txt %}
## File created by /usr/local/bin/ionscript
## February 13, 2016 at 03:29:28 AM JST
## Run the following command to start ION node:
##	% ionstart -I "host1.rc"

## begin ionadmin 
1 1 ''
s
a contact +1 +3600 1 1 100000
a range +1 +3600 1 1 1
m production 1000000
m consumption 1000000

## end ionadmin 

## begin ionsecadmin 
1

## end ionsecadmin 

## begin ltpadmin 
1 32
a span 1 32 32 1400 10000 1 'udplso localhost:1113'
s 'udplsi localhost:1113'

## end ltpadmin 

## begin bpadmin 
1
a scheme ipn 'ipnfw' 'ipnadminep'
a endpoint ipn:1.0 q
a endpoint ipn:1.1 q
a endpoint ipn:1.2 q
a endpoint ipn:1.3 q
a endpoint ipn:1.4 q
a endpoint ipn:1.5 q
a endpoint ipn:1.6 q
a protocol ltp 1400 100
a induct ltp 1 ltpcli
a outduct ltp 1 ltpclo
s

## end bpadmin 

## begin ipnadmin 
a plan 1 ltp/1

## end ipnadmin 
{% endhighlight %}

Make an iondtn user.  By default, **ion.log** will be located in **/usr/local/iondtn/ion.log**.

{% highlight sh %}
su
sh
SERVICE=iondtn
INSTALL_DIR=/usr/local
pw adduser $SERVICE -d $INSTALL_DIR/$SERVICE -s /usr/sbin/nologin -c "$SERVICE system service user"
mkdir -p $INSTALL_DIR/$SERVICE
chown -R $SERVICE:$SERVICE $INSTALL_DIR/$SERVICE
{% endhighlight %}

## References:
- [FreeBSD, Giving more flexibility to an rc.d script][freebsd-rc]
- [FreeBSD, Directory Structure][freebsd-dir]
- [FreeBSD, The Complete FreeBSD: Documentation from the Source][freebsd-book]
- [FreeBSD, Getting Started with ION-DTN 3.4.0 on FreeBSD][freebsd-ion]
- [FreeBSD, Elixir as a Service on FreeBSD][freebsd-elixir]
- [UNIX, What is the difference between /opt and /usr/local?][unix-opt]
- [UNIX, Oracle Run Control Scripts][unix-rc]
- [UNIX, What does aux mean in ps aux?][unix-ps]
- [UNIX, How to terminate process by name in UNIX][unix-name-kill]
- [UNIX, grep without string][unix-grep-without]
- [UNIX, Bourne Shell Reference][unix-sh]

[freebsd-rc]: https://www.freebsd.org/doc/en/articles/rc-scripting/rcng-args.html
[freebsd-dir]: https://www.freebsd.org/doc/handbook/dirstructure.html
[freebsd-book]: https://books.google.com/books?id=7Y5kfaRmtKUC&pg=PA659&lpg=PA659&dq=/usr/local+log&source=bl&ots=jIhRwf_w1L&sig=m0-alnfyrujbdVvNCulbzgdoups&hl=en&sa=X&ved=0ahUKEwiQuLyNgPvKAhXMXR4KHS8OBgw4ChDoAQhSMAg#v=onepage&q=%2Fusr%2Flocal%20log&f=false
[freebsd-ion]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/07/getting-started-with-ion-dtn-3-4-0-on-freebsd.html
[freebsd-elixir]: https://sgeos.github.io/elixir/erlang/2016/01/16/elixir-as-a-service_on_freebsd.html
[unix-opt]: http://unix.stackexchange.com/questions/11544/what-is-the-difference-between-opt-and-usr-local
[unix-rc]: https://docs.oracle.com/cd/E19455-01/805-7228/6j6q7uepi/index.html
[unix-ps]: http://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux
[unix-name-kill]: http://notetodogself.blogspot.com/2006/07/how-to-terminate-process-by-name-in.html
[unix-grep-without]: http://stackoverflow.com/questions/13260031/grep-without-string
[unix-sh]: http://cis.stvincent.edu/html/tutorials/unix/bshellref

