---
layout: post
comments: true
title:  "Getting Started With Beacons"
date:   2016-05-25 01:53:29 +0000
categories: beacon ios android unity osx
---
Beacon resources and tools for OSX, iOS and Android.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-05-25 01:53:29 +0000
$ uname -vm
Darwin Kernel Version 15.5.0: Tue Apr 19 18:36:36 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
Mac OS X 10.11.5
{% endhighlight %}

## Instructions

Apple's [iBeacon for Developers][apple-ibeacon] page gives a good technical
overview of beacons.
The [Getting Started with iBeacon][apple-ibeacon-getting-started]
PDF is especially useful.

An Apple computer with a Bluetooth 4.0 Low Engergy (BLE) radio running
OSX Yosemite or later can send and receive iBeacons.

[MactsAsBeacon][osx-beacon-mactsasbeacon] allows OSX to transmit beacons.

{% highlight sh %}
git clone git@github.com:timd/MactsAsBeacon.git
cd MactsAsBeacon/
cp -R MactsAsBeacon.app /Applications/
open -a MactsAsBeacon
{% endhighlight %}

[Beacon Scanner][osx-beacon-scanner] can be used to detect beacons on OSX.

{% highlight sh %}
wget https://github.com/mlwelles/BeaconScanner/releases/download/1.11/BeaconScanner-1.11.zip
unzip BeaconScanner-1.11.zip
cp -R "Beacon Scanner.app" /Applications/
open -a "Beacon Scanner"
{% endhighlight %}

The Locate Beacon app for [iOS][ios-locate-beacon] and
[Android][android-locate-beacon] can be used to locate beacons.
It can also be used to transmit beacon information.
Note that only Android 4.3+ devices with BluetoothLE can detect iBeacons.
Android 5.0+ and BluetoothLE is required to transmit iBeacons.

iBeacon support is part of the [Core Location Framework][ios-core-location]
on iOS and OSX.
[AltBeacon][android-altbeacon] can be used to add
beacon support to Android apps.
A Unity 3D [iBeacon Asset][unity3d-ibeacon], and a
Cordova [iBeacon Plugin][cordova-ibeacon] exist.

A Raspberry Pi (or other Linux box) with a Bluetooth LE dongle can
[act as a beacon][rpi-beacon].

## References:
- [Article, Beacons in 2016: What to Expect from iBeacon, Eddystone and more][article-beacons-2016]
- [Article, The Realities of Installing iBeacon to Scale][article-beacons-at-scale]
- [Apple, iBeacon for Developers][apple-ibeacon]
- [Apple, Getting Started with iBeacon][apple-ibeacon-getting-started]
- [Apple, Maps for Developers][apple-maps]
- [Android, AltBeacon][android-altbeacon]
- [Android, Locate Beacon App][android-locate-beacon]
- [Android, Beacon Layouts][android-beacon-layouts]
- [Android, Can an Android device act as an iBeacon?][android-ibeacon-transmit]
- [iOS, Core Location Framework][ios-core-location]
- [iOS, Locate Beacon App][ios-locate-beacon]
- [Unity 3D, iBeacon Asset][unity3d-ibeacon]
- [Cordova, iBeacon Plugin][cordova-ibeacon]
- [OSX, Beacon Scanner][osx-beacon-scanner]
- [OSX, MactsAsBeacon][osx-beacon-mactsasbeacon]
- [OSX, Turn Macbook into iBeacon][osx-macbook-ibeacon]
- [RaspberryPi, piBeacon - DIY Beacon with a Raspberry Pi][rpi-beacon]
- [Quora, How much do iBeacons cost?][quora-beacon-cost]
- [Wikipedia, iBeacons][wikipedia-ibeacon]

[article-beacons-2016]: http://blog.beaconstac.com/2016/02/beacons-in-2016-what-to-expect-from-ibeacon-eddystone-and-more/
[article-beacons-at-scale]: https://www.brooklynmuseum.org/community/blogosphere/2015/02/04/the-realities-of-installing-ibeacon-to-scale/
[apple-ibeacon]: https://developer.apple.com/ibeacon/
[apple-ibeacon-getting-started]: https://developer.apple.com/ibeacon/Getting-Started-with-iBeacon.pdf
[android-ibeacon-transmit]: http://stackoverflow.com/questions/19602913/can-an-android-device-act-as-an-ibeacon
[apple-maps]: https://developer.apple.com/maps/
[android-altbeacon]: https://github.com/AltBeacon/android-beacon-library
[android-locate-beacon]: https://play.google.com/store/apps/details?id=com.radiusnetworks.locate
[android-beacon-layouts]: https://beaconlayout.wordpress.com
[ios-core-location]: https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CoreLocation_Framework/index.htm://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CoreLocation_Framework/index.html
[ios-locate-beacon]: https://itunes.apple.com/us/app/locate-beacon/id738709014?mt=8
[unity3d-ibeacon]: https://www.assetstore.unity3d.com/en/#!/content/15260
[cordova-ibeacon]: https://github.com/petermetz/cordova-plugin-ibeacon
[osx-beacon-scanner]: https://github.com/mlwelles/BeaconScanner
[osx-beacon-mactsasbeacon]: https://github.com/timd/MactsAsBeacon
[osx-macbook-ibeacon]: http://stackoverflow.com/questions/19410398/turn-macbook-into-ibeacon
[rpi-beacon]: https://learn.adafruit.com/pibeacon-ibeacon-with-a-raspberry-pi/overview
[quora-beacon-cost]: https://www.quora.com/How-much-do-ibeacons-cost
[wikipedia-ibeacon]: https://en.wikipedia.org/wiki/IBeacon

