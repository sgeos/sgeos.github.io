---
layout: post
comments: true
title:  "Getting Started with Kotlin on Android with IntelliJ IDEA EAP 16"
date:   2016-02-21 01:28:56 +0000
categories: android kotlin
---
I recently spoke with some people in Tokyo who are
using [Kotlin][kotlin] in a production Android app.
Kotlin is less cumbersome to write than Java and is therefore easier to maintain.
By using Kotlin, Lambda functions can also be used on Android.
Exciting.

Android work is fascinating in theory.
Working with Java is neither fun nor exciting.
I really like the idea of using something less cumbersome like Kotlin for Android projects.

Kotlin is a modern language with some functional features.
It was written to interoperate seamlessly with Java code.
Kotlin can also be compiled to JavaScript source code.
The home page describes it as a
"statically typed programming language for the JVM, Android and the browser".

Kotlin was primarily developed by [JetBrains][jetbrains], the makers of IntelliJ IDEA.
Android studio is essentially a customized version of IntelliJ.
A lot of thought went into making sure Kotlin works well on Android.

Idiomatic Kotlin with lambda functions does increase total method count.
Multidex and ProGuard can be used to get around the dex file limit of 65,536 methods.
Having said that, it is generally the libraries that push Android apps over the dex limit.

The Kotlin website has a [good guide][kotlin-android] on getting started with Kotlin on Android.
Writing this post is just an excuse for me to give it a shot with IntelliJ EAP instead of Android Studio.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-02-21 01:28:56 +0000
$ uname -vm
Darwin Kernel Version 15.3.0: Thu Dec 10 18:40:58 PST 2015; root:xnu-3248.30.4~1/RELEASE_X86_64 x86_64
$ java -version
java version "1.8.0_25"
Java(TM) SE Runtime Environment (build 1.8.0_25-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.25-b02, mixed mode)
$ cat /Applications/IntelliJ\ IDEA\ 16\ EAP.app/Contents/Info.plist | grep -A 1 CFBundleGetInfoString | grep -v CFBundleGetInfoString | sed 's/^\ *</</; s/<[^>]*>//g'
IntelliJ IDEA EAP IU-144.4199.23, build IU-144.4199.23. Copyright JetBrains s.r.o., (c) 2000-2016
$ cat $ANDROID_SDK/tools/source.properties | grep Pkg.Revision
Pkg.Revision=24.4.1
$ cat $ANDROID_SDK/platform-tools/source.properties | grep Pkg.Revision
Pkg.Revision=23.1
$ ls $ANDROID_SDK/build-tools/
23.0.2
{% endhighlight %}

## Instructions

The first thing I did was download the latest version of [IntelliJ IDEA EAP][idea-eap-16].
I'm not afraid of using software that is not necessarily "stable".
The next thing I did, was use the `android` command to update Android SDK components.

After the setup, I worked through the [guide][kotlin-android] on the Kotlin site.
Their guide covers Android Studio.
Below, I document what I did with IntelliJ IDEA.

Android SDK had to be configured in the new version of IntelliJ.
Go to **Configure | Project Defaults | Project Structure | SDKs**
and enter the **Android SDK home path** and **Build target**.
Apply.  OK.
Go to **Configure | Project Defaults | Project Structure | Project |
Project SDK** and make sure **Android SDK** is selected.

Start a new project.
I did not have a project open, so I clicked **Create New Project**.
If a project is open, **File | New | Project...** can be used.

Select **Android** and fill in the Application Name and Company Domain.
The default Target Android Devices will work.  Next.
Select a **Blank Activity** and name it.  Finish.
The project will be generated.

A preview pops up with hello world text.
Excellent.
Time for a test run.
Hook up a test device via USB.
Go to **Run | Edit Configurations...** and hit the **+** for a new configuration.
Name it.
Set Module to app.
Set Deployment Target Options to USB Device.
Apply.
Cancel.
Select the new configuration from the dropdown by the debug button.
This is in the upper righthand corner of the window.
Hit the debug button.
The build takes a minute or so.
Give permission to run the app and it pops up on the screen.
Note the "rendering problems" report in IntelliJ.
Everything looks good on the phone.  So far, so good.

Open the **MainActivity.java** file or whatever the main activity happens to be named.
Execute **Code | Convert Java File to Kotlin File**.
The conversion takes a few seconds.
Click OK when prompted to correct code in the rest of the project.
Add the Kotlin Java runtime with **Tools | Kotlin | Configure Kotlin in Project** and select OK.
Select **View | Tool Windows | Gradle** and hit the **Refresh all Gradle projects** button.

Hit the debug button.
The app crashes on the phone.
Not entirely unexpected.
At this point I tried a bunch of things try to get the app to run.

- Did not work.  Adding the Kotlin Java runtime again and synchronizing.
- Did not work.  **File \| Invalidate Caches / Restart...** followed by **Invalidate and Restart**.
- Wrong file.  Modifying the top level (ProjectName)/**build.gradle**.
- Almost.  Following the official [Kotlin with gradle procedure][kotlin-gradle] and making changes to (ProjectName)/app/**build.gradle**.
- Good idea.  Change (ProjectName)/app/src/main/**java** to **kotlin**.

The problem is that configuring Kotlin with **Tools | Kotlin | Configure Kotlin in Project**
added the libraries to the project,
but it did not modify **build.gradle** like the guide said it would.
I could not get any other official instructions to work.
What I wound up doing is pulling code out of (ProjectName)/app/**build.gradle**
in a [working example project][android-example].

My working (ProjectName)/app/**build.gradle** file looks like this.
Your **applicationId** on line 21 will almost certainly be different.

{% highlight clojure %}
buildscript {
    ext.kotlin_version = '1.0.0'

    repositories {
        jcenter()
    }
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'
apply plugin: 'kotlin-android-extensions'

android {
    compileSdkVersion 23
    buildToolsVersion "23.0.2"

    defaultConfig {
        applicationId "com.sennue.kotlin_hello_world.kotlinhelloworld" // <- line 21
        minSdkVersion 15
        targetSdkVersion 23
        versionCode 1
        versionName "1.0"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
    //noinspection GroovyAssignabilityCheck
    sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }
}

dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    testCompile 'junit:junit:4.12'
    compile 'com.android.support:appcompat-v7:23.1.1'
    compile 'com.android.support:design:23.1.1'
    compile "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
}
{% endhighlight %}

After making the above changes and syncing gradle, the debug build ran again.

Inspecting **IntelliJ IDEA-EAP | Preferences... | Plugins** indicates the
downloadable **kotlin-android** plugin is obsolete.
So far as I can tell, the functionality is baked into IntelliJ IDEA now, but it still needs to be enabled.

I also made the following changes to write a little code in Kotlin.
Set text to "Hello, User!".
Uses the name in the user's profile, if available.

**MainActivity.kt**
{% highlight kotlin %}
// onCreate
val c = application.contentResolver.query(ContactsContract.Profile.CONTENT_URI, null, null, null, null)
val username = when(c.count) {
    0 -> "User"
    else -> {
        c.moveToFirst()
        c.getString(c.getColumnIndex("display_name"))
    }
}
c.close()

val message = findViewById(R.id.message) as TextView
message.text = "Hello, $username!"
{% endhighlight %}

Add permission to read contacts.

**AndroidManifest.xml**
{% highlight xml %}
<uses-permission android:name="android.permission.READ_CONTACTS"/>
{% endhighlight %}

Add an id to the text view.

**content_main.xml**
{% highlight xml %}
android:id="@+id/message"
{% endhighlight %}

## References:
- [Android, Building Apps with Over 65K Methods][android-dex-limit]
- [Android, check android developer tools version command line][android-version]
- [Android, JetBrains/kotlin-examples/android-mixed-java-kotlin-project/app/build.gradle][android-example]
- [IntelliJ IDEA 16 EAP][idea-eap-16]
- [IntelliJ IDEA, Working with IntelliJ IDEA Features from Command Line][idea-eap-command]
- [IntelliJ IDEA, Can't find “Sync Project with Gradle Files” button in IntelliJ IDEA][idea-sync]
- [JetBrains][jetbrains]
- [Kotlin, Statically typed programming language for the JVM, Android and the browser][kotlin]
- [Kotlin, Kotlin 1.0 Released: Pragmatic Language for JVM and Android][kotlin-1-0]
- [Kotlin, Getting Started][kotlin-getting-started]
- [Kotlin, Getting started with Android and Kotlin][kotlin-android]
- [Kotlin, Using Gradle][kotlin-gradle]
- [Wikipedia, Kotlin (programming language)][wikipedia-kotlin]

[android-dex-limit]: http://developer.android.com/tools/building/multidex.html
[android-version]: http://stackoverflow.com/questions/24447687/check-android-developer-tools-version-command-line
[android-example]: https://github.com/JetBrains/kotlin-examples/blob/master/gradle/android-mixed-java-kotlin-project/app/build.gradle
[idea-eap-16]: https://confluence.jetbrains.com/display/IDEADEV/IDEA+16+EAP
[idea-eap-command]: https://www.jetbrains.com/idea/help/working-with-intellij-idea-features-from-command-line.html
[idea-sync]: http://stackoverflow.com/questions/20815998/cant-find-sync-project-with-gradle-files-button-in-intellij-idea
[jetbrains]: https://www.jetbrains.com
[kotlin]: https://kotlinlang.org
[kotlin-1-0]: https://blog.jetbrains.com/kotlin/2016/02/kotlin-1-0-released-pragmatic-language-for-jvm-and-android/
[kotlin-getting-started]: https://kotlinlang.org/docs/reference/basic-syntax.html
[kotlin-android]: https://kotlinlang.org/docs/tutorials/kotlin-android.html
[kotlin-gradle]: https://kotlinlang.org/docs/reference/using-gradle.html
[wikipedia-kotlin]: https://en.wikipedia.org/wiki/Kotlin_(programming_language)

