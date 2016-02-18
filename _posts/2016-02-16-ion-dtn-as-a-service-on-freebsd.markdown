---
layout: post
comments: true
title:  "ION DTN as a Service on FreeBSD"
date:   2016-02-16 06:36:10 +0900
categories: freebsd ion dtn
---
This post covers installing ION DTN as a service on FreeBSD.
The goal is to create an **iondtn** service that can be used like any other service.

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

The **iondtn** service will also be configured to start when the machine boots.
This functionality can be disabled.

This post is follow up to [Getting Started with ION-DTN 3.4.0 on FreeBSD][freebsd-ion].

## Software Versions

{% highlight sh %}
$ date
February 16, 2016 at 06:36:10 AM JST
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

Add the rc script to **/usr/local/etc/rc.d/iondtn** as root.
The **install_dir** in the script can be modified to accommodate different installation directories.
The script can be configured in **/etc/rc.conf** with the following options.

- **iondtn_enable** : enable the service and start it when the machine boots
- **iondtn_user** : user to run the servie as
- **iondtn_config** : location of the configuration file
- **iondtn_log_dir** : directory **ion.log** is placed in

The status command polls the various ion subcomponents.
The rest of the script should be straight forward.

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
extra_commands="status killm"

load_rc_config $name
: ${iondtn_enable:="no"}
: ${iondtn_user:=${name}}
: ${iondtn_config:="${install_dir}/etc/${name}.rc"}
: ${iondtn_log_dir:="${install_dir}/${name}"}

iondtn_start()
{
  su -m "${iondtn_user}" -c "cd ${iondtn_log_dir} && ionstart -I '${iondtn_config}'"
}

iondtn_stop()
{
  su -m "${iondtn_user}" -c "ionstop"
}

iondtn_status()
{
  timeout=1
  echo "t p ${timeout}" | ${install_dir}/bin/ionadmin | sed -n "s/: //; /started/p"
  echo "t p ${timeout}" | ${install_dir}/bin/bpadmin | sed -n "s/: //; /started/p"
  echo "t p ${timeout}" | ${install_dir}/bin/ltpadmin | sed -n "s/: //; /started/p"
  echo "t p ${timeout}" | ${install_dir}/bin/dtpcadmin | sed -n "s/: //; /started/p"
  echo "t p ${timeout}" | ${install_dir}/bin/cfdpadmin | sed -n "s/: //; /started/p"
}

iondtn_killm()
{
  su -m "${iondtn_user}" -c "killm"
}

load_rc_config $name
run_rc_command "$1"
{% endhighlight %}

Make the above script read only and executable.

{% highlight sh %}
chmod 555 /usr/local/etc/rc.d/iondtn
{% endhighlight %}

The **iondtn** service uses combined configuration files produced by **ionscript**.
By default the configuration file in **/usr/local/etc/iondtn.rc** will be used.

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

By default, the **iondtn** service will be run by a user of the same name and
**ion.log** will be located in **/usr/local/iondtn/ion.log**.
As root, create the **iondtn** user and **/usr/local/iondtn/** directory.

{% highlight sh %}
su
sh
SERVICE=iondtn
INSTALL_DIR=/usr/local
pw adduser $SERVICE -d $INSTALL_DIR/$SERVICE -s /usr/sbin/nologin -c "$SERVICE system service user"
mkdir -p $INSTALL_DIR/$SERVICE
chown -R $SERVICE:$SERVICE $INSTALL_DIR/$SERVICE
{% endhighlight %}

The **iondtn** service needs to be able to write to **/tmp/ion.sdrlog**,
so change the owner of the file or the write permissions.

{% highlight sh %}
chown $SERVICE:$SERVICE /tmp/ion.sdrlog
chmod 666 /tmp/ion.sdrlog
{% endhighlight %}

If multiple users will be using ion, those users need to be able to write to **ion.log**.

{% highlight sh %}
touch /usr/local/iondtn/ion.log
chown $SERVICE:$SERVICE /usr/local/iondtn/ion.log
chmod 666 /usr/local/iondtn/ion.log
{% endhighlight %}

The following command can be used to clear the log without changing the owner or permissions.

{% highlight sh %}
echo -n "" >/usr/local/iondtn/ion.log
{% endhighlight %}

Enable the **iondtn** service in **/etc/rc.conf**.
Only the iondtn_enable line is required.
Removing this line or changing the value to "NO" will disable
**iondtn** and it will not start when the machine boots.
The other lines list optional configuration variables and the default values.
These lines can be omitted.

{% highlight sh %}
iondtn_enable="YES"
iondtn_user="iondtn"
iondtn_config="/usr/local/etc/iondtn.rc"
iondtn_log_dir="/usr/local/iondtn/"
{% endhighlight %}

Due to the way memory is shared, running ION-DTN and ION applications as different users may not work reliably.
The solution is to run everything as the **iondtn** user,
or configure the service to rus as the same user that runs the applications.
For example, an **/etc/rc.conf** snippet that runs the **iondtn** service as the bsechter user looks like this.

{% highlight sh %}
iondtn_enable="YES"
iondtn_user="bsechter"
iondtn_config="/usr/local/etc/iondtn.rc"
iondtn_log_dir="/usr/home/bsechter/iondtn/"
{% endhighlight %}

The **iondtn** service can now be started from any directory
and **ion.log** will be in a known location.

{% highlight sh %}
service iondtn start
{ echo "Hello, World!"; sleep 2; } | bpchat ipn:1.1 ipn:1.1 # test that it works
service iondtn status
service iondtn restart
cat /usr/local/iondtn/ion.log
service iondtn stop
service iondtn killm
service iondtn status
{% endhighlight %}

Note that due to the **su** commands in the rc script, the service can only be started or stopped by root.
Any user can use find out if **iondtn** is running with `service iondtn status`.

## References:
- [ION-DTN, Re: {% raw %}[Ion-dtn-users]{% endraw %} Blog Post: Getting Started with ION-DTN 3.4.0 on FreeBSD][freebsd-rc]
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
- [UNIX, How to skip lines matching a string][unix-sed-skip]
- [UNIX, Linux / Unix sed: Delete Word From File / Input][unix-sed-delete]
- [UNIX, Bourne Shell Reference][unix-sh]

[ion-dtn-users]: https://sourceforge.net/p/ion-dtn/mailman/message/34856065/
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
[unix-sed-skip]: http://stackoverflow.com/questions/6684857/how-to-skip-lines-matching-a-string
[unix-sed-delete]: http://www.cyberciti.biz/faq/howto-delete-word-using-sed-under-unix-linux-bsd-appleosx/
[unix-sh]: http://cis.stvincent.edu/html/tutorials/unix/bshellref

