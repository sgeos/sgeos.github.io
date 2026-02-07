---
layout: post
comments: true
title:  "Getting Started With Command Line Swift"
date:   2016-01-18 09:01:44 +0900
categories: swift
---

<!-- A7 -->

If you want to start learning swift without firing up an IDE, this post is for you.
This post was written because the instructions in the references are slightly out of date.

## Software Versions
{% highlight sh %}
$ date
January 18, 2016 at 09:01:44 AM JST
$ uname -a
Darwin siderite.centurylink.net 15.2.0 Darwin Kernel Version 15.2.0: Fri Nov 13 19:56:56 PST 2015; root:xnu-3248.20.55~2/RELEASE_X86_64 x86_64
$ swift --version # swiftc is the same
Apple Swift version 2.1.1 (swiftlang-700.1.101.15 clang-700.1.81)
Target: x86_64-apple-darwin15.2.0
{% endhighlight %}

## Instructions
Create a simple swift script with a shebang at the top.
Add the following to **arg_echo.swift**
{% highlight swift %}
#!/usr/bin/env swift
print("Command line arguments:")
for arg in Process.arguments {
  print(arg)
}
{% endhighlight %}

Make the script executable.
{% highlight sh %}
chmod +x arg_echo.swift
{% endhighlight %}

The script can be run from the command line.
{% highlight sh %}
./arg_echo.swift a b c
{% endhighlight %}

Alternatively, run the script with the **swift** command.  In this case, the shebang is unneccessary.
{% highlight sh %}
swift arg_echo.swift a b c
{% endhighlight %}

Use **swiftc** to compile an executable.  The shebang will be ignored when compiling, so the above source code will work unchanged.
{% highlight sh %}
swiftc arg_echo.swift -o arg_echo
{% endhighlight %}

The executable can be run from the command line.
{% highlight sh %}
./arg_echo a b c
{% endhighlight %}

## References:
- [Swift scripts: How to write small command line scripts in Swift][swift-script]
- [Minimal Swift command line Hello World][swift-minimal]
- [Swift for CLI tools][swift-cli]

[swift-script]:  http://practicalswift.com/2014/06/07/swift-scripts-how-to-write-small-command-line-scripts-in-swift/
[swift-minimal]: https://gist.github.com/kavu/79f05be2383e97843867
[swift-cli]:     https://speakerdeck.com/supermarin/swift-for-cli-tools

