---
layout: post
mathjax: false
comments: true
title:  "Building Android APKs on FreeBSD"
date:   2017-01-27 10:06:31 +0000
categories: android freebsd
---
It can be useful to build Android APKs on a FreeBSD system if you need to build APKs serverside or
if FreeBSD happens to be your preferred development environment.
This post covers the setup required to build an existing Android repository on FreeBSD.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
FreeBSD 11.0-RELEASE-p1 #0 r306420: Thu Sep 29 01:43:23 UTC 2016     root@releng2.nyi.freebsd.org:/usr/obj/usr/src/sys/GENERIC  amd64
$ uname -vm
2017-01-27 10:06:31 +0000
{% endhighlight %}

## Instructions

On a fresh FreeBSD install, the ports tree may need to be installed and some basic utilities may handy.
Your needs and preferences may vary.

**sh**
{% highlight sh %}
pkg install vim screen
portsnap fetch extract
{% endhighlight %}

The Android SDK can be used on FreeBSD, but it relies on the Linux emulation layer.
Furthermore, recent versions of the SDK use 64 bit binaries.
FreeBSD 10.3 and newer support 64 bit Linux emulation, but the base Linux utilities need to be installed separately.
The **linux_base** ports will install the 64 bit utilities if a 64 environment is detected.

The package will only install the 32 bit utilities, so **linux_base** must be built from source using the package.
Also, newer utilities seems to be required.
The upshot is that **linux_base-c7** should be installed.
Execute the following as root to install **linux_base-c7** with 64-bit support.

**sh**
{% highlight sh %}
kldload linux linux64
pkg install bash git gradle python wget rpm4
ln -s /usr/local/bin/bash /bin/bash
echo "# 64-bit Linux" >> /etc/make.conf
echo "DEFAULT_VERSIONS+=linux=c7_64" >> /etc/make.conf
echo "OVERRIDE_LINUX_NONBASE_PORTS=c7_64" >> /etc/make.conf
(cd /usr/ports/emulators/linux_base-c7 && make install distclean)
printf "linprocfs\t\t/compat/linux/proc\tlinprocfs\trw\t\t0\t0\n" >> /etc/fstab
printf "tmpfs\t\t\t/compat/linux/dev/shm\ttmpfs\t\trw,mode=1777\t0\t0\n" >> /etc/fstab
echo 'linux_enable="YES"' >> /etc/rc.conf
mount /compat/linux/proc
mount /compat/linux/dev/shm
{% endhighlight %}

A script to install the Android build tools looks something like this.
The components to install are toward the end of the script.

**android_install.sh** complete listing
{% highlight sh %}
#!/bin/sh

: ${SDK_VERSION:="25.2.5"}
: ${NDK_VERSION:="13b"}
: ${BUILD_TOOLS_VERSION:="25.0.2"}
: ${API_LEVEL:="25"}
: ${SDK_URL:="https://dl.google.com/android/repository/tools_r${SDK_VERSION}-linux.zip"}
: ${NDK_URL:="https://dl.google.com/android/repository/android-ndk-r${NDK_VERSION}-linux-x86_64.zip"}
: ${ANDROID_SDK:="$HOME/android/sdk"}
: ${ANDROID_NDK:="$HOME/android/ndk"}
: ${ANDROID_HOME:="${ANDROID_SDK}"}
: ${PATCH_HOME:="$HOME/projects/install/android-platform-tools-base"}
: ${BOOTSTRAP:="false"}
: ${NUKE_SDK:="false"}
: ${NUKE_NDK:="false"}

export PATH="$ANDROID_NDK:$ANDROID_SDK/tools:$ANDROID_SDK/tools/bin:$ANDROID_SDK/platform-tools:$HOME/bin:$ANDROID_SDK/build-tools/$BUILD_TOOLS_VERSION:$PATH"

TOP_DIRECTORY=$(pwd)

mod_executable() {
  sh -c "find ${1} -maxdepth 1 -type f -print0" | xargs -0 -n 10 file | grep "${2}" | awk 'BEGIN { FS = ":" } ; {print $1}' | sh -c "xargs ${3}"
}

brand_executable() {
  mod_executable "${1}" "ELF" "brandelf -t Linux"
  mod_executable "${1}" "ELF" "chmod +x"
  mod_executable "${1}" "script" "chmod +x"
  #list_executable "${1}"
}

patch_tools() {
  (cd ${PATCH_HOME} && javac ${PATCH_HOME}/common/src/main/java/com/android/SdkConstants.java)
  (cd ${PATCH_HOME} && javac ${PATCH_HOME}/sdklib/src/main/java/com/android/sdklib/internal/repository/archives/ArchFilter.java -cp "sdklib/src/main/java:common/src/main/java:annotations/src/main/java")
  (cd ${PATCH_HOME}/sdklib/src/main/java/ && jar uf ${ANDROID_HOME}/tools/lib/sdklib.jar com/android/sdklib/internal/repository/archives/ArchFilter.class)
  (cd ${PATCH_HOME}/common/src/main/java && jar uf ${ANDROID_HOME}/tools/lib/common.jar com/android/SdkConstants.class)
}

if [ "true" = "${BOOTSTRAP}" ]
then
  # SDK and NDK Directories
  mkdir -p "${ANDROID_SDK}"
  mkdir -p "${ANDROID_NDK}"

  # FreeBSD JAR Patch
  rm -rf "${PATCH_HOME}"
  mkdir -p "${PATCH_HOME}"
  git clone https://android.googlesource.com/platform/tools/base "${PATCH_HOME}"
  cd "${PATCH_HOME}"
  PATCH_REPLACE='s/else if (os.startsWith("Linux"))/else if (os.startsWith("Linux") || os.startsWith("FreeBSD"))/'
  sed -i.bak "${PATCH_REPLACE}" "common/src/main/java/com/android/SdkConstants.java"
  sed -i.bak "${PATCH_REPLACE}" "sdklib/src/main/java/com/android/sdklib/internal/repository/archives/ArchFilter.java"
  javac common/src/main/java/com/android/SdkConstants.java
  javac sdklib/src/main/java/com/android/sdklib/internal/repository/archives/ArchFilter.java -cp "sdklib/src/main/java:common/src/main/java:annotations/src/main/java"
  cd "${TOP_DIRECTORY}"
fi

if [ "true" = "${NUKE_SDK}" ]
then
  echo "Replacing base Android SDK."
  rm -rf "${ANDROID_SDK}"
  curl -sLk "${SDK_URL}" | unzip - -d "${ANDROID_SDK}"
  patch_tools
  brand_executable "${ANDROID_SDK}/tools/"
fi

# Latest Tools and Platform Tools, Specified Build Tools and Android API Level
echo y | android update sdk --no-ui --all --filter "tools,platform-tools,build-tools-${BUILD_TOOLS_VERSION},android-${API_LEVEL}"
patch_tools
brand_executable "${ANDROID_SDK}/tools/"
brand_executable "${ANDROID_SDK}/tools/bin/"
brand_executable "${ANDROID_SDK}/platform-tools/"
brand_executable "${ANDROID_SDK}/build-tools/*/"

# Other API Levels
echo y | android update sdk --no-ui --all --filter "build-tools-25,build-tools-25.0.1,build-tools-25.0.2,android-25"
echo y | android update sdk --no-ui --all --filter "build-tools-24,build-tools-24.0.1,build-tools-24.0.2,build-tools-24.0.3,android-24,addon-google_apis-google-24"
echo y | android update sdk --no-ui --all --filter "build-tools-23,build-tools-23.0.1,build-tools-23.0.2,build-tools-23.0.3,android-23,addon-google_apis-google-23"
brand_executable "${ANDROID_SDK}/build-tools/*/"

# Other Packages
echo y | android update sdk --no-ui --all --filter "extra-google-google_play_services,extra-google-m2repository"
echo y | android update sdk --no-ui --all --filter "extra-android-support,extra-android-m2repository"

# Accept Licenses for Automatic Dependency Download
mkdir -p "${ANDROID_HOME}/licenses"
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "${ANDROID_HOME}/licenses/android-sdk-license"
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "${ANDROID_HOME}/licenses/android-sdk-preview-license"

# Stub for Unwritten NDK Installation Functionality
if [ "true" = "${NUKE_NDK}" ]
then
  echo "Replacing Android NDK."
  rm -rf "$(dirname ${ANDROID_NDK})/android-ndk-r${NDK_VERSION}"
  mkdir -p "${ANDROID_NDK}"
  curl -sLk "${NDK_URL}" | unzip - -d "$(dirname ${ANDROID_NDK})"
  rmdir "${ANDROID_NDK}"
  ln -s "$(dirname ${ANDROID_NDK})/android-ndk-r${NDK_VERSION}" "${ANDROID_NDK}"
  brand_executable "${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/tools"
  brand_executable "${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin"
  echo "Installing CMake for Android NDK."
  INSTALL_CMAKE_URL="https://github.com/Commit451/android-cmake-installer/releases/download/1.1.0/install-cmake.sh"
  rm -rf "${ANDROID_HOME}/cmake"
  curl -sLk "${INSTALL_CMAKE_URL}" | sh
  CMAKE_DIRECTORY="$(cd ${ANDROID_HOME}/cmake/*/bin; pwd)"
  brand_executable "${CMAKE_DIRECTORY}/cmake"
  brand_executable "${CMAKE_DIRECTORY}/cpack"
  brand_executable "${CMAKE_DIRECTORY}/ctest"
  brand_executable "${CMAKE_DIRECTORY}/ninja"
fi
{% endhighlight %}

Running for the first time.

**sh**
{% highlight sh %}
chmod +x android_install.sh
BOOTSTRAP=true NUKE_SDK=true NUKE_NDK=true ./android_install.sh
{% endhighlight %}

The version of **adb** installed with Android SDK did not work on FreeBSD for me.
Luckily, there is a **devel/android-tools-adb-devel** port that does work.
For what it is worth, at the time of writing this I can only get **adb** work as root on FreeBSD.

**sh**
{% highlight sh %}
pkg install android-tools-adb-devel
adb devices
# authorize the device if you need to
adb shell input text "Hello,\ World!\ "
{% endhighlight %}

Add Android SDK and NDK to the path in **${HOME}/.profile** or equivalent.
**${HOME}/.profile** partial listing
{% highlight sh %}
# PATH += Android SDK
export ANDROID_SDK="${HOME}/android/sdk"
export ANDROID_HOME="${ANDROID_SDK}"
export ANDROID_BUILD_TOOLS_VERSION="25.0.2"
export PATH="${ANDROID_SDK}/tools:${ANDROID_SDK}/tools/bin:${ANDROID_SDK}/platform-tools:${ANDROID_SDK}/build-tools/${ANDROID_BUILD_TOOLS_VERSION}:${PATH}"

# PATH += Android NDK
export ANDROID_NDK="${HOME}/android/ndk"
export ANDROID_NDK_HOME="${ANDROID_NDK}"
export ANDROID_NDK_ROOT="${ANDROID_NDK}"
export PATH="${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/tools:${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin:${PATH}"
{% endhighlight %}

Testing the installation.  Install a coupe libraries as root.

**sh**
{% highlight sh %}
rm -f /compat/linux/usr/lib64/libcrypto.so.1.0.0 /compat/linux/usr/lib64/libcrypto.so.1
wget https://dl.dropboxusercontent.com/u/8593574/Spotify/Fedora/libcrypto.so.1.0.0 -O /compat/linux/usr/lib64/libcrypto.so.1.0.0
ln -s /compat/linux/usr/lib64/libcrypto.so.1.0.0 /compat/linux/usr/lib64/libcrypto.so.1
rm -f /compat/linux/usr/lib64/libssl.so.1.0.0 /compat/linux/usr/lib64/libssl.so.1
wget https://dl.dropboxusercontent.com/u/8593574/Spotify/Fedora/libssl.so.1.0.0 -O /compat/linux/usr/lib64/libssl.so.1.0.0
ln -s /compat/linux/usr/lib64/libssl.so.1.0.0 /compat/linux/usr/lib64/libssl.so.1
{% endhighlight %}

Test with the Android NDK Samples.

**sh**
{% highlight sh %}
export ANDROID_HOME="${HOME}/android/sdk"
export ANDROID_NDK_HOME="${HOME}/android/ndk"
git clone git@github.com:googlesamples/android-ndk.git "${HOME}/projects/android-ndk-samples"
# OR the following for HTTP
# git clone https://github.com/googlesamples/android-ndk.git "${HOME}/projects/android-ndk-samples"
cd "${HOME}/projects/android-ndk-samples/hello-libs"
./gradlew --refresh-dependencies
./gradlew clean check build
./gradlew assembleDebug
{% endhighlight %}

## References:

- [Android, Building a continuous-integration Android build server on FreeBSD: Part one: building APKs using Linux emulation][android-freebsd-ci]
- [Android, Android の Linux 環境をターミナルから構築する][android-ndk-terminal-download]
- [Android, How to set ANDROID_NDK_HOME so that Android Studio does not ask for ndk location?][android-ndk-setup]
- [Android, Andrid NDK Notes][android-ndk-notes]
- [Android, NDK Downloads][android-ndk-downloads]
- [Android, NDK Samples (GitHub Repository)][android-ndk-samples]
- [Android, TDD Playground][android-tdd-playground]
- [adb, Using SPACE with adb shell input][adb-text-input-space]
- [Gradle, Gradle Plugin User Guide - Testing][gradle-plugin-user-guide-testing]
- [FreeBSD, FreeBSD Handbook - Linux® Binary Compatibility][freebsd-linux-emulation]
- [FreeBSD, FreeBSD Handbook - Installing Additional Libraries Manually][freebsd-linux-lib-manual-install]
- [FreeBSD, FreshPorts - devel/android-tools-adb-devel][freebsd-port-android-tools-adb-devel]
- [Linux, Install Spotify stable (v 0.9.17) on Fedora 23 64-bit][linux-ssl-lib]

[android-freebsd-ci]: http://zewaren.net/site/node/165/
[android-ndk-terminal-download]: http://qiita.com/tanjo/items/0c6549c6700160d5595b
[android-ndk-setup]: http://stackoverflow.com/questions/39159357/how-to-set-android-ndk-home-so-that-android-studio-does-not-ask-for-ndk-location
[android-ndk-notes]: http://www.stuartaxon.com/2015/07/05/android-ndk-notes/
[android-ndk-downloads]: https://developer.android.com/ndk/downloads/index.html
[android-ndk-samples]: https://github.com/googlesamples/android-ndk
[android-tdd-playground]: https://github.com/pestrada/android-tdd-playground
[adb-text-input-space]: https://plus.google.com/+AaronShang/posts/cYwaZppVbJW
[gradle-plugin-user-guide-testing]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Testing
[freebsd-linux-emulation]: https://www.freebsd.org/doc/handbook/linuxemu.html
[freebsd-linux-lib-manual-install]: https://www.freebsd.org/doc/handbook/linuxemu-lbc-install.html
[freebsd-port-android-tools-adb-devel]: https://www.freshports.org/devel/android-tools-adb-devel/
[linux-ssl-lib]: https://gist.github.com/olejon/54473554be2d4dbacd03

