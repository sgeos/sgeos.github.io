---
layout: post
mathjax: false
comments: true
title:  "Installing SonarQube on FreeBSD"
date:   2017-02-22 20:09:23 +0000
categories: freebsd sonarqube
---

<!-- A52 -->

SonarQube is a static analysis tool that supports many popular languages.
It can be integrated with tools like Jenkins and JIRA.
This post covers installing it on FreeBSD.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-02-22 20:09:23 +0000
$ uname -vm
FreeBSD 11.0-RELEASE-p1 #0 r306420: Thu Sep 29 01:43:23 UTC 2016     root@releng2.nyi.freebsd.org:/usr/obj/usr/src/sys/GENERIC  amd64
{% endhighlight %}

## Instructions

Install **sonarqube**.

**sh**
{% highlight sh %}
pkg install sonarqube
{% endhighlight %}

Create the database for **sonarqube**.

**sh**
{% highlight sh %}
SONARQUBE_USER="sonarqube"
SONARQUBE_DATABASE="sonarqube"
SONARQUBE_PASSWORD="secret.password"

createuser "${SONARQUBE_USER}"
psql -c "ALTER USER ${SONARQUBE_USER} WITH PASSWORD '${SONARQUBE_PASSWORD}';"
createdb "${SONARQUBE_DATABASE}"
psql -c "GRANT ALL PRIVILEGES ON DATABASE ${SONARQUBE_DATABASE} TO ${SONARQUBE_USER};"
{% endhighlight %}

Configure **sonarqube**.

**/usr/local/sonarqube/conf/sonar.properties** partial listing
{% highlight sh %}
#--------------------------------------------------------------------------------------------------
# DATABASE
#
# IMPORTANT: the embedded H2 database is used by default. It is recommended for tests but not for
# production use. Supported databases are MySQL, Oracle, PostgreSQL and Microsoft SQLServer.

# User credentials.
# Permissions to create tables, indices and triggers must be granted to JDBC user.
# The schema must be created first.
sonar.jdbc.username=sonarqube
sonar.jdbc.password=secret.password

#----- Embedded Database (default)
# H2 embedded database server listening port, defaults to 9092
#sonar.embeddedDatabase.port=9092
#----- MySQL 5.6 or greater
# Only InnoDB storage engine is supported (not myISAM).
# Only the bundled driver is supported. It can not be changed.
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
{% endhighlight %}

Enable **sonarqube**.

**/etc/rc.conf** partial listing
{% highlight sh %}
sonarqube_enable="YES"
{% endhighlight %}

Start **sonarqube**.

**sh**
{% highlight sh %}
service sonarqube start
{% endhighlight %}

Alternatively, start the console by calling **sonar.sh** directly if you want verbose output.
This can be useful when troubleshooting.

**sh**
{% highlight sh %}
/usr/local/sonarqube/bin/freebsd/sonar.sh console
{% endhighlight %}

It takes a couple of minutes to start, but **curl** will return html if everything is working.
Alternatively, direct your browser to port 9000 of the server running **sonarqube**.

**sh**
{% highlight sh %}
curl localhost:9000
{% endhighlight %}

**SonarQube** can be configured from the browser.

## References:

- [SonarQube][sonarqube]
- [SonarQube, Documentation][sonarqube-documentation]
- [SonarQube, GitHub][sonarqube-github]
- [SonarQube, DockerHub][sonarqube-dockerhub]
- [SonarQube, FreshPorts][sonarqube-freshports]
- [SonarQube, Using SonarQube with Jenkins Continuous Integration and GitHub to Improve Code Review][sonarqube-jenkins]
- [SonarQube, How to Install SonarQube with Nginx on Ubuntu 16.04][sonarqube-nginx-ubuntu]
- [SonarQube, SonarQube with Postgres DB][sonarqube-postgres]

[sonarqube]: https://www.sonarqube.org
[sonarqube-documentation]: https://docs.sonarqube.org/display/HOME/SonarQube+Platform
[sonarqube-github]: https://github.com/SonarSource/sonarqube
[sonarqube-dockerhub]: https://hub.docker.com/_/sonarqube/
[sonarqube-freshports]: https://www.freshports.org/devel/sonarqube/
[sonarqube-jenkins]: http://macoscope.com/blog/using-sonarqube-with-jenkins-continuous-integration-and-github-to-improve-code-review/
[sonarqube-nginx-ubuntu]: http://linoxide.com/linux-how-to/install-sonarqube-ubuntu-16-04-ngnix/
[sonarqube-postgres]: http://stackoverflow.com/questions/30778850/sonarqube-with-postgres-db

