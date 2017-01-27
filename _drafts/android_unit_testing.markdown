---
layout: post
mathjax: false
comments: true
title:  "Android Unit Testing"
date:   2017-01-26 13:44:18 +0000
categories: android unit testing
---
Problem description here.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2017-01-26 13:44:18 +0000
$ uname -vm
Darwin Kernel Version 16.3.0: Thu Nov 17 20:23:58 PST 2016; root:xnu-3789.31.2~1/RELEASE_X86_64 x86_64
$ java -version
java version "1.8.0_112"
Java(TM) SE Runtime Environment (build 1.8.0_112-b16)
Java HotSpot(TM) 64-Bit Server VM (build 25.112-b16, mixed mode)
$ cat /Applications/Android\ Studio.app/Contents/Info.plist | grep -A 1 CFBundleGetInfoString | grep -v CFBundleGetInfoString | sed 's/^\ *</</; s/<[^>]*>//g'
Android Studio 2.2, build AI-145.3537739. Copyright JetBrains s.r.o., (c) 2000-2016
$ cat $ANDROID_SDK/tools/source.properties | grep Pkg.Revision
Pkg.Revision=25.2.5
$ cat $ANDROID_SDK/platform-tools/source.properties | grep Pkg.Revision
Pkg.Revision=25.0.3
$ ls $ANDROID_SDK/build-tools/
19.1.0	20.0.0	21.1.2	22.0.1	23.0.0	23.0.1	23.0.2	23.0.3	24.0.0	24.0.1	24.0.2	24.0.3	25.0.0	25.0.1	25.0.2
{% endhighlight %}

## Instructions

Instructions for solution here.

**sh**
{% highlight sh %}
./gradlew test
./gradlew check
./gradlew connectedCheck
./gradlew deviceCheck
./gradlew uninstallAll
./gradlew installDebug
./gradlew installRelease
{% endhighlight %}

**Project/app/src/androidTest/java/com/mycompany/domain/ApplicationTest.java** complete listing
{% highlight java %}
package jp.unext.api;

import android.app.Application;
import android.test.ApplicationTestCase;

/**
 * <a href="http://d.android.com/tools/testing/testing_android.html">Testing Fundamentals</a>
 */
public class ApplicationTest extends ApplicationTestCase<Application> {
    public ApplicationTest() {
        super(Application.class);
    }
}
{% endhighlight %}

{% highlight sh %}
echo "Code here."
{% endhighlight %}

## References:

- [Android, Gradle Plugin User Guide][android-gradle-plugin-info]
- [Android Studio, Test your app][android-studio-test-your-app]
- [Android, How to create a release signed apk file using Gradle?][android-git-release-keychain]
- [Android, Getting Started with Testing][android-getting-started-with-testing]

[android-gradle-plugin-info]: http://tools.android.com/tech-docs/new-build-system/user-guide
[android-studio-test-your-app]: https://developer.android.com/studio/test/index.html
[android-git-release-keychain]:  http://stackoverflow.com/questions/18328730/how-to-create-a-release-signed-apk-file-using-gradle
[android-getting-started-with-testing]: https://developer.android.com/training/testing/start/index.html
- [][]: 

