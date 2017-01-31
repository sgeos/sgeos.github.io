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

Installation and testing **gradlew** tasks.

{% highlight sh %}
Install tasks
-------------
installDebug - Installs the Debug build.
installDebugAndroidTest - Installs the android (on device) tests for the Debug build.
uninstallAll - Uninstall all applications.
uninstallDebug - Uninstalls the Debug build.
uninstallDebugAndroidTest - Uninstalls the android (on device) tests for the Debug build.
uninstallRelease - Uninstalls the Release build.

Verification tasks
------------------
check - Runs all checks.
connectedAndroidTest - Installs and runs instrumentation tests for all flavors on connected devices.
connectedCheck - Runs all device checks on currently connected devices.
connectedDebugAndroidTest - Installs and runs the tests for debug on connected devices.
deviceAndroidTest - Installs and runs instrumentation tests using all Device Providers.
deviceCheck - Runs all device checks using Device Providers and Test Servers.
lint - Runs lint on all variants.
lintDebug - Runs lint on the Debug build.
lintRelease - Runs lint on the Release build.
test - Run unit tests for all variants.
testDebugUnitTest - Run unit tests for the debug build.
testReleaseUnitTest - Run unit tests for the release build.
{% endhighlight %}

Command line emulator.

**sh**
{% highlight sh %}
sys-img-arm64-v8a-android-24
sys-img-armeabi-v7a-android-24
sys-img-x86_64-android-24
sys-img-x86-android-24
sys-img-arm64-v8a-google_apis-24
sys-img-armeabi-v7a-google_apis-24
sys-img-x86_64-google_apis-24
sys-img-x86-google_apis-24

sys-img-x86-google_apis-25
sys-img-x86_64-google_apis-25
echo y | android update sdk --no-ui --all --filter "sys-img-x86_64-google_apis-25"
yes "" | android -s create avd --force --name android-unit-testing-emulator --target "android-25" --abi "google_apis/x86_64"
emulator -avd android-unit-testing-emulator -no-window
{% endhighlight %}

## References:
- [Android, Gradle Plugin User Guide][android-gradle-plugin-info]
- [Andriod, Android Studio - Test your app][android-studio-test-your-app]
- [Android, How to create a release signed apk file using Gradle?][android-git-release-keychain]
- [Android, Getting Started with Testing][android-getting-started-with-testing]
- [Android, Android Testing Tutorial: Unit Testing like a True Green Droid][android-testing-tutorial]
- [Jenkins, Run android unit tests & instrumentation tests on Jenkins (Gradle)][jenkins-android-unit-testing]
- [Jenkins, How to set up a Continuous Integration server for Android development (Ubuntu + Jenkins + SonarQube)][jenkins-android-ci]
- [Docker, how to build and run android apk on emulator using dockerfile][docker-android-emulator]
- [Docker, Building android project with Docker and Walter, independent from the specific platform][docker-android-build]
- [Testing, Unit Tests, How to Write Testable Code and Why it Matters][testing-unit-test-howto]
- [Emulator, Installing Applications on the Emulator][emulator-installing-applications]
- [Emulator, Android Testing in Headless Emulator][emulator-headless-testing]
- [Emulator, no ABI error , when creating an Android virtual device][emulator-no-abi]

[android-gradle-plugin-info]: http://tools.android.com/tech-docs/new-build-system/user-guide
[android-studio-test-your-app]: https://developer.android.com/studio/test/index.html
[android-git-release-keychain]:  http://stackoverflow.com/questions/18328730/how-to-create-a-release-signed-apk-file-using-gradle
[android-getting-started-with-testing]: https://developer.android.com/training/testing/start/index.html
[android-testing-tutorial]: https://www.toptal.com/android/testing-like-a-true-green-droid
[jenkins-android-unit-testing]: http://stackoverflow.com/questions/28066740/run-android-unit-tests-instrumentation-tests-on-jenkins-gradle
[jenkins-android-ci]: https://pamartinezandres.com/how-to-set-up-a-continuous-integration-server-for-android-development-ubuntu-jenkins-sonarqube-43c1ed6b08d3#.r84hd0pol
[docker-android-emulator]: http://stackoverflow.com/questions/32965204/how-to-build-and-run-android-apk-on-emulator-using-dockerfile
[docker-android-build]: http://ainoya.io/docker-android-walter
[testing-unit-test-howto]: https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters
[emulator-installing-applications]: https://developer.android.com/studio/run/emulator-commandline.html#starting
[emulator-headless-testing]: https://paulemtz.blogspot.jp/2013/05/android-testing-in-headless-emulator.html
[emulator-no-abi]: http://stackoverflow.com/questions/10019532/no-abi-error-when-creating-an-android-virtual-device

