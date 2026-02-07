---
layout: post
mathjax: false
comments: true
title:  "git Repository Environment Management Variable Strategy"
date:   2017-01-26 11:14:13 +0000
categories: sh git
---

<!-- A51 -->

It can be useful to capture environment variable settings in a file.
These files generally want to live with the project.
This presents two problems when working with version control.

- The environment variable settings may contain sensitive information, like passwords.
- The environment variable settings may be specific to the local machine.

Both problems can be solved by commiting an example file with benign defaults instead of a file with sensitive or machine specific values.
This post covers a specific strategy for doing this.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-01-26 11:14:13 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #18 4f888bf(drm-next): Wed Jan 18 14:31:26 UTC 2017     root@gauntlet:/usr/obj/usr/src/sys/GENERIC  amd64
$ git --version
git version 2.11.0
{% endhighlight %}

## Instructions

Create an **environment.sh.example** file template.
This file provides the structure for storing environment variables, but contains benign default values that can be committed to version control.
It also serves as a list of environment variables that need to be or ought to be defined.
A real file may have more comments.

Note that the settings are printed at the end of the file.
Using this strategy, a variable needs to manually be added to the list of values to print after it has been added.
Username:password pairs are also printed, but the password is hidden.
This is not really secure because anyone could **cat** the file, but it is suitable for some projects.

**environment.sh.example** complete listing
{% highlight sh %}
#!/bin/sh

# environment.sh is not in source control because it contains sensitive information.
# Copy this example file and fill in the values for your environment.
#   cp environment.sh.example environment.sh
#
# Then load the values as follows.
#   . environment.sh

# Project Settings
export PROJECT="${HOME}/projects/my_project"
export VARIABLE="Value"
export DEFAULT_VARIABLE="" # use default if empty
export FLAG="true"

# Account Settings
export CREDENTIALS="username:password"

echo_value() {
  sh -c "if [ -n \"\$${1}\" ]; then echo \"${1}=\$${1}\"; else echo '${1}=(default value)'; fi"
}

echo_credentials() {
  sh -c "if [ -n \"\$${1}\" ]; then echo \"${1}=\$${1}\" | sed 's/:.*/:********/' ; else echo '${1}=(default value)'; fi"
}

for setting in \
  PROJECT \
  VARIABLE \
  DEFAULT_VARIABLE \
  FLAG
do
  echo_value "${setting}"
done

for setting in \
  CREDENTIALS
do
  echo_credentials "${setting}"
done
{% endhighlight %}

Add the real non-example **environment.sh** file to **.gitignore**.
At this point the repository can be commited version control.
Note that adding new environment varaibles generally requires updating both **environment.sh.example** with benign defaults and **environment.sh** with real working values.

**.gitignore** partial listing
{% highlight sh %}
environment.sh
{% endhighlight %}

To use this setup, copy **environment.sh.example** to **environment.sh**, customize it and then load the environment variables.

**sh**
{% highlight sh %}
cp environment.sh.example environment.sh
# customize environment.sh here
. environment.sh
{% endhighlight %}

Output will look something like this.

**sh**
{% highlight sh %}
PROJECT=/Users/bsechter/projects/my_project
VARIABLE=Value
DEFAULT_VARIABLE=(default value)
FLAG=true
CREDENTIALS=username:********
{% endhighlight %}

Note that as written blank values are supposedly treated as default values.
This functionality needs to exist where the environment variables are used.
For example, in an **sh** script you can set a variable to a default value if it is not defined as follows.

**some_script.sh** partial listing
{% highlight sh %}
: ${DEFAULT_VARIABLE:="default value"}
{% endhighlight %}

