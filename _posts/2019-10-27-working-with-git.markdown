---
layout: post
mathjax: false
comments: true
title:  "Working With git and GitHub"
date:   2019-10-27 08:25:20 +0000
categories: 
---
This post will explain the basics of working with git and GitHub.
For more in depth information, read a book on git or work through a proper tutorial.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2019-10-27 08:25:20 +0000
$ uname -vm
Darwin Kernel Version 18.7.0: Tue Aug 20 16:57:14 PDT 2019; root:xnu-4903.271.2~2/RELEASE_X86_64 x86_64
$ git --version
git version 2.21.0 (Apple Git-122)
{% endhighlight %}

## Creating a GitHub Repository

First, create a GitHub account and install git on your computer.
Next, create a new repository on GitHub by clicking "Start a project" on the main page.
If you want other people, like potential employers, to be able see the project, make sure it is public.
If the project contains sensitive client or company details, it should be private.
Name the project and add a description.
It is gnerally a good idea to add a README, .gitignore file for your language of choice, and a license.
I like the BSD licenses and dislike the GNU licenses, but feel free to pick what works for you and your project needs.

If you do not add any files to your project, you will see instructions for initializing the GitHub repository.
The path to the repository will be needed to initialize it.
SSH is more convenient than HTTPS after your SSH keys have been added to GitHub.
The SSH path a GitHub repository will look something like this:

{% highlight sh %}
git@github.com:username/project-name.git
{% endhighlight %}

The HTTP path will look something like this.

{% highlight sh %}
https://github.com/username/project-name.git
{% endhighlight %}

For the purposes of this blog post, the project path will be added to an environment variable.
Feel free to use either the SSH or HTTPS version.

{% highlight sh %}
export GITHUB_PROJECT=git@github.com:username/project-name.git
{% endhighlight %}

A new repository can be created from the command line with the following steps.

{% highlight sh %}
echo "# Project Name" >> README.md
git init
git add README.md
git commit -m "Initial commit."
git remote add origin ${GITHUB_PROJECT}
git push -u origin master
{% endhighlight %}

Alternatively, a new repository can be pushed from the command line.

{% highlight sh %}
git remote add origin ${GITHUB_PROJECT}
git push -u origin master
{% endhighlight %}

Finally, GitHub has an option to import code from another repository.

## Working with git

In practice, most of the work done with git only requires using a few commands.

{% highlight sh %}
# Add a single file
git add file

# Add multiple files
git add file1 file2 ...

# Add all files
git add .

# Commit changes
git commit -m "Commit message."

# Push changes to GitHub
git push

# Pull changes from GitHub
git pull
{% endhighlight %}

Additionally, it can sometimes be useful to rebase so that multiple commits can be squashed into one before pusing to GitHub.
For example, the following command will list the last 3 commits so that they could potentially be squashed.

{% highlight sh %}
git rebase -i HEAD~3
{% endhighlight %}

These are the basics of working with git.
Sometimes situations arise where more complicated commands need to be used.
Additionally, sometimes conflicts need to be resolved when pulling changes.
For more advanced usage requirements, read a proper tutorial or a book.

