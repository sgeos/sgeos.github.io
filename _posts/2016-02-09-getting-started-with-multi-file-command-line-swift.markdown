---
layout: post
comments: true
title:  "Getting Started With Multi File Command Line Swift"
date:   2016-02-09 02:08:36 +0900
categories: swift
---
I wanted to write a post on commandline swift projects that span more than one file.
This post covers a hello world type example that spans three files and prompts for input.
Also covered are a file wrapper for multi file swift scripts and compiled command line executables.

Also see the post on [Getting Started With Command Line Swift][swift-started].

## Software Versions
{% highlight sh %}
$ date
February  9, 2016 at 02:08:36 AM JST
$ uname -mv
Darwin Kernel Version 15.3.0: Thu Dec 10 18:40:58 PST 2015; root:xnu-3248.30.4~1/RELEASE_X86_64 x86_64
$ swift --version # swiftc is the same
Apple Swift version 2.1.1 (swiftlang-700.1.101.15 clang-700.1.81)
Target: x86_64-apple-darwin15.3.0
$ xcrun --version
xcrun version 28.
{% endhighlight %}

## Instructions
First, we will create a multi file project.

Add the following to **main.swift**.
{% highlight swift %}
func main() {
  let name = inputPrompt("What is your name? ")
  sayHello(name)
}

main()
{% endhighlight %}

Add the following to **input_prompt.swift**.
{% highlight swift %}
import Foundation

func inputPrompt(message: String = "> ") -> String {
  print(message, terminator: "")
  fflush(__stdoutp)
  let keyboard = NSFileHandle.fileHandleWithStandardInput()
  let inputData = keyboard.availableData
  let result = NSString(data: inputData, encoding: NSUTF8StringEncoding) as! String
  return result.stringByTrimmingCharactersInSet(
    NSCharacterSet.whitespaceAndNewlineCharacterSet()
  )
}
{% endhighlight %}

Add the following to **hello.swift**.
{% highlight swift %}
func sayHello(name: String) {
  print("Hello, " + name + "!")
}
{% endhighlight %}

To execute **main.swift** and the support files, create a wrapper script.
Add the following to **hello_user.sh**.
{% highlight sh %}
#!/bin/sh
TMPFILE=`mktemp /tmp/Project.swift.XXXXXX` || exit 1
trap "rm -f $TMPFILE" EXIT 
cat *.swift > $TMPFILE
swift $TMPFILE
{% endhighlight %}

Make the wrapper executable.
{% highlight sh %}
chmod +x hello_user.sh
{% endhighlight %}

The wrapper script can be run from the command line.
{% highlight sh %}
./hello_user.sh
{% endhighlight %}

Alternatively, compile the files into an executable with **swiftc**.
{% highlight sh %}
swiftc file_a.swift file_b.swift file_c.swift -o executable_name
{% endhighlight %}

One of the files in this project imports foundation, so **xcrun -sdk macosx swiftc** needs to be used instead of **swiftc**.
{% highlight sh %}
xcrun -sdk macosx swiftc main.swift input_prompt.swift hello.swift -o hello_user
{% endhighlight %}

The executable can be run from the command line.
{% highlight sh %}
./hello_user
{% endhighlight %}

## References:
- [Swift, Getting Started With Command Line Swift][swift-started]
- [Swift, Is there a way to have a Swift script use multiple files][swift-multi]
- [Swift, How to include .swift file from other .swift file in an immediate mode?][swift-include]
- [Swift, Scripting in Swift is Pretty Awesome][swift-awesome]
- [Swift, How to write small command line scripts in Swift][swift-script]
- [Swift, Minimal Swift command line Hello World][swift-minimal]
- [Swift for CLI tools][swift-cli]
- [Swift, Functions][swift-functions]
- [Swift, Input from the keyboard in command line application][swift-input]
- [Swift, 'Use of Unresolved Identifier' in Swift][swift-unresolved]
- [Swift, print without newline in swift 2.0][swift-newline]
- [Swift, Update current line with command line tool in Swift][swift-update]
- [Swift, Does swift has trim method on String?][swift-strip]

[swift-started]:    https://sgeos.github.io/swift/2016/01/18/getting-started-with-command-line-swift.html
[swift-multi]:      http://stackoverflow.com/questions/28069043/is-there-a-way-to-have-a-swift-script-use-multiple-files
[swift-include]:    http://stackoverflow.com/questions/25342940/how-to-include-swift-file-from-other-swift-file-in-an-immediate-mode
[swift-awesome]:    http://krakendev.io/blog/scripting-in-swift
[swift-script]:     http://practicalswift.com/2014/06/07/swift-scripts-how-to-write-small-command-line-scripts-in-swift/
[swift-minimal]:    https://gist.github.com/kavu/79f05be2383e97843867
[swift-cli]:        https://speakerdeck.com/supermarin/swift-for-cli-tools
[swift-functions]:  https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Functions.html
[swift-input]:      http://stackoverflow.com/questions/24004776/input-from-the-keyboard-in-command-line-application
[swift-unresolved]: http://stackoverflow.com/questions/28996730/use-of-unresolved-identifier-in-swift
[swift-newline]:    http://stackoverflow.com/questions/30865233/print-without-newline-in-swift-2-0
[swift-update]:     http://stackoverflow.com/questions/25483292/update-current-line-with-command-line-tool-in-swift
[swift-strip]:      http://stackoverflow.com/questions/26797739/does-swift-has-trim-method-on-string

