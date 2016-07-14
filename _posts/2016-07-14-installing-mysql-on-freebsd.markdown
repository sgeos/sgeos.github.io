---
layout: post
comments: true
title:  "Installing MySQL on FreeBSD"
date:   2016-07-14 01:23:55 +0000
categories: mysql freebsd
---
Sometimes it can not be avoided.
MySQL needs to be installed for one reason or another.
This post covers installing MySQL on FreeBSD.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-07-14 01:23:55 +0000
$ uname -vm
FreeBSD 11.0-ALPHA6 #0 r302384: Thu Jul  7 22:40:47 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ mysqladmin -u root -p version
mysqladmin  Ver 8.42 Distrib 5.7.13, for FreeBSD11.0 on amd64

Server version		5.7.13-log
Protocol version	10
*snipped some output*
{% endhighlight %}

## Instructions

Install using packages.

{% highlight sh %}
pkg install mysql57-server mysql57-client
{% endhighlight %}

Alternatively, install using ports.

{% highlight sh %}
portmaster databases/mysql57-server databases/mysql57-client
{% endhighlight %}

Enable MySQL in **rc.conf**.

**/etc/rc.conf** partial listing
{% highlight sh %}
mysql_enable="YES"
{% endhighlight %}

Start MySQL from the command line.
Note that the above **rc.conf** line will automatically start MySQL when
the machine boots.
Note that the default location for **my.conf** is
**/usr/local/etc/mysql/my.cnf**.

{% highlight sh %}
service mysql-server start
{% endhighlight %}

Note that if **/var/db/mysql** exists and is not empty,
**mysql-server** will fail to start the first time.
Backup or remove this directory if you need to.
See [this][freebsd-mysql-failure] blog post to track down other errors when starting
**mysql-server** for the first time.

{% highlight sh %}
# Backup
mv /var/db/mysql /var/db/mysql.old

# Remove
rm -rf /var/db/mysql
{% endhighlight %}

Reset the password.
Note that the initial password is stored in **$HOME/.mysql_secret**.
For example, if you use `mysql -u root -p` the initial password is stored in
**/root/.mysql_secret**.

{% highlight sh %}
mysql -u root -p -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';"
{% endhighlight %}

If upgrading from an earlier version, run **mysql_upgrade**.
Note that the command below upgrades as the root user.

{% highlight sh %}
mysql_upgrade -u root -p
{% endhighlight %}

Uninstall with **pkg**.

{% highlight sh %}
pkg delete mysql57-server mysql57-client
{% endhighlight %}

Uninstall with **portmaster**.

{% highlight sh %}
portmaster -e databases/mysql57-server databases/mysql57-client
{% endhighlight %}

## References:

- [MySQL, Installing MySQL on FreeBSD][mysql-freebsd]
- [MySQL, How to Reset the Root Password][mysql-reset-password]
- [MySQL, MySQL/MariaDB: Run SQL Queries From A Shell Prompt / Command Line][mysql-commandline-query]
- [MySQL, Find Out MySQL Version][mysql-version]
- [FreeBSD, FreeBSD mysql-server failed precmd routine][freebsd-mysql-failure]
- [FreeBSD, Upgrade MySQL 5.1.70 to 5.6.12][freebsd-mysql-upgrade]
- [FreeBSD, Properly deinstall ports and dependencies][freebsd-deinstall]

[mysql-freebsd]: https://dev.mysql.com/doc/refman/5.7/en/freebsd-installation.html
[mysql-reset-password]: http://dev.mysql.com/doc/refman/5.7/en/resetting-permissions.html
[mysql-commandline-query]: http://www.cyberciti.biz/faq/run-sql-query-directly-on-the-command-line/
[mysql-version]: http://www.cyberciti.biz/faq/tell-version-mysql-unix-linux-command/
[freebsd-mysql-failure]: http://www.gamecreatures.com/blog/2016/02/22/freebsd-mysql-server-failed-precmd-routine/
[freebsd-mysql-upgrade]: https://forums.freebsd.org/threads/40833/
[freebsd-deinstall]: https://forums.freebsd.org/threads/35457/

