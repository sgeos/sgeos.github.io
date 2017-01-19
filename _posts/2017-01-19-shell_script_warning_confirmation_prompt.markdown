---
layout: post
mathjax: false
comments: true
title:  "Shell Script Confirmation Warning Prompt"
date:   2017-01-19 12:21:09 +0000
categories: sh freebsd
---
Sometimes scripts need to do something really destructive.
It is generally a good idea to display a warning prompt and provide a way to back out before performing these destructive actions.
It is also useful to provide a mechanism whereby the interactive prompt can be disabled.
This post covers one solution for this problem.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-01-19 12:21:09 +0000
$ uname -vm
FreeBSD 12.0-CURRENT #14 f92c24b(drm-next-4.7): Fri Jan  6 19:28:21 UTC 2017     root@gauntlet:/usr/obj/usr/src/sys/GENERIC  amd64
{% endhighlight %}

## Instructions

The following script pretends to perform a destructive action when the **NUKE_ENVIRONMENT** environment variable is set to **true**.
By default, a prompt is displayed that allows the user to interactively proceed, skip the destructive action but execute the rest
of the script, or abort the script.

If the **FORCE** environment variable is also set to **true**, no prompt is displayed.
The script assumes the users knows what they are doing and executes the destructive action unconditionally.

**warn.sh** complete listing
{% highlight sh %}
#!/bin/sh

# case insensitive settings
NUKE_ENVIRONMENT=$(echo "${NUKE_ENVIRONMENT}" | tr '[:upper:]' '[:lower:]')
FORCE=$(echo "${FORCE}" | tr '[:upper:]' '[:lower:]')

# prompt if NUKE_ENVIRONMENT
# skip prompot if FORCE
if [ \( "true" = "${NUKE_ENVIRONMENT}" \) -a \( "true" != "${FORCE}" \) ]
then
  echo "Nuking the environment will do something really destructive."
  echo "This action can not be undone."
  while true
  do
    read -p "Do you really want to nuke the environment? [yes/no/cancel] " result
    case $result in
      [Yy]* ) NUKE_ENVIRONMENT="true"; break;;
      [Nn]* ) NUKE_ENVIRONMENT="false"; break;;
      [Cc]* ) echo "Aborting script."; exit;;
      *) echo "Please answer yes, no or cancel.";;
    esac
  done
fi

# potentially nuke the environment
if [ "true" = "${NUKE_ENVIRONMENT}" ]
then
  echo "* Do something really destructive here. *"
  echo "Nuking environment."
else
  echo "Skip nuking environment."
fi

# do everything else
echo "* Standard procedure here. *"
{% endhighlight %}

The script can be tested with the following commands.

{% highlight sh %}
chmod +x warn.sh
./warn.sh
NUKE_ENVIRONMENT=true ./warn.sh
NUKE_ENVIRONMENT=true FORCE=true ./warn.sh
{% endhighlight %}

This example uses environment variables directly.
A production example my use command line parameters instead.

