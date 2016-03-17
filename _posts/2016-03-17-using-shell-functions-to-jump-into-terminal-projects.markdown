---
layout: post
comments: true
title:  "Using Shell Functions to Jump Into Terminal Projects"
date:   2016-03-17 04:52:56 +0000
categories: unix sh
---
If you are like me, you often have number of terminal windows
open and logged into another machine.
When that machine reboots, you need to log in again and pick up
where you left off.

This post covers putting a shell function in **.profile** to
easily jump between projects.
A function for setting the terminal title is also provided.
This post is written for **sh**.
If you are using another shell, the same principles apply, but
the details may be a little different.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-03-17 04:52:56 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r296709: Sat Mar 12 21:18:38 JST 2016     root@mirage.sennue.com:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions

First, create a few test directories.

{% highlight sh %}
mkdir -p $HOME/test_project/a
mkdir -p $HOME/test_project/b
mkdir -p $HOME/test_project/c
{% endhighlight %}

Next, add the following to **$HOME/.profile**

**.profile**
{% highlight sh %}
termtitle(){
  printf "\033]0;${1}\007"
}
{% endhighlight %}

The above function can be used to set the terminal title.
Reload the profile your open terminal and open a couple more terminals.

{% highlight sh %}
# terminals open before editing $HOME/.profile
. $HOME/.profile

# terminal a
cd $HOME/test_project/a
termtitle a

# terminal b
cd $HOME/test_project/b
termtitle b

# terminal c
cd $HOME/test_project/c
termtitle c

# clear terminal title
termtitle
{% endhighlight %}

You now have three named terminals working on three different projects.
The above works, but we can do better.
Add the following to **$HOME/.profile**

**.profile**
{% highlight sh %}
workon(){
  if [ "${2}" ]
  then
    termtitle "${2}"
  else
    termtitle "${1}"
  fi
  clear
  case "${1}" in
    admin)
      OLD_DIR=$(pwd)
      cd /root
      pwd
      su
      cd $OLD_DIR
      ;;
    a)
      cd $HOME/test_project/a
      ;;
    b)
      cd $HOME/test_project/b
      ;;
    c)
      cd $HOME/test_project/c
      ;;
    *)
      cd $HOME
      ;;
  esac
  pwd
}
{% endhighlight %}

Close all but one terminal and reload  **$HOME/.profile**

{% highlight sh %}
. $HOME/.profile
{% endhighlight %}

Switch between projects with the following commands.
Notice that the terminal title changes when switching from project to project.

{% highlight sh %}
# project a
workon a

# project b
workon b

# project c
workon c

# home directory
workon

# root home directory as root, requires password
workon admin
exit # stop being root, reverts to previous directory
{% endhighlight %}

The terminal title can also be specified with the project.
Open another terminal and enter the following commands.
This simulates a pair of terminals- one for development and one for preview.

{% highlight sh %}
# terminal 1
workon a A-Development

# terminal 2
workon a A-Preview
{% endhighlight %}

In the examples in this post, the case statements just **cd**
into the project directory,
but other commands can be added on a project by project basis.
The admin case is an example of this.

Replace the test project cases in this post with your real projects.
Remove the test directories when you no longer need them.

{% highlight sh %}
rm -rf $HOME/test_project
{% endhighlight %}

If you work with ssh key based **git**, consider installing **keychain** and
adding the following line to your profile.

{% highlight sh %}
eval `keychain --eval --agents ssh id_rsa`
{% endhighlight %}

## References:
- [Keychain Official Project Page][keychain]

[keychain]: http://www.funtoo.org/Keychain

