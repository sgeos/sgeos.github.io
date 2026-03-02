---
layout: post
mathjax: false
comments: true
title: "Android Development on FreeBSD"
date: 2026-02-23 00:01:00 +0000
categories: android freebsd rust
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

This post covers Android SDK and NDK development on FreeBSD using the Linux binary compatibility layer.
FreeBSD does not have native Android toolchain support,
but the Linuxulator allows standard Linux Android SDK and NDK binaries to run on FreeBSD.
This approach enables building, signing, and deploying Android APKs
from a FreeBSD development workstation using only command-line tools.

The post is organized into five parts.
The first part covers environment setup including the Linuxulator, Android SDK, NDK, and Rust toolchain.
The second part covers SDK development with a Kotlin Android application.
The third part covers NDK development by adding a Rust native library exposed through the Java Native Interface (JNI).
The fourth part covers emulator feasibility.
The fifth part covers a sample application that ports the
[Concentrated Liquidity Market Maker (CLMM) calculator][related_post_clmm]
to a native Android app.

The development workflow is entirely command-line driven.
Android Studio is not used.
The Android emulator is out of scope and is not supported on FreeBSD.
All testing is performed on physical hardware connected via the Android Debug Bridge (ADB).

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-23 00:01:00 +0000

# OS and Version
$ uname -vm
TODO

# Java
$ java -version
TODO

# Gradle
$ gradle --version | head -n 3
TODO

# Android SDK
$ sdkmanager --version
TODO

# Android NDK
$ ls $ANDROID_HOME/ndk/
TODO

# Rust
$ rustc --version
TODO

# cargo-ndk
$ cargo ndk --version
TODO

# ADB
$ adb --version
TODO
```

## Environment Setup

### Linux Binary Compatibility

FreeBSD provides optional binary compatibility with Linux through the Linuxulator.
The Linuxulator is not emulation.
It translates Linux system calls into FreeBSD equivalents at the kernel level,
allowing unmodified Linux binaries to run at near-native speed.

Android SDK and NDK packages are distributed as Linux binaries.
The Linuxulator makes it possible to run these tools directly on FreeBSD.
Java, Gradle, and Rust run natively on FreeBSD through their respective ports.

Enable the Linuxulator and install the Rocky Linux 9 base as root.

```sh
# Load kernel modules
kldload linux64

# Enable on boot
sysrc linux_enable="YES"

# Install Rocky Linux 9 base (current default)
pkg install linux_base-rl9

# Start the service
service linux start
```

Add the required filesystem mounts to `/etc/fstab`.

`/etc/fstab` partial listing
```
linprocfs       /compat/linux/proc      linprocfs       rw              0       0
linsysfs        /compat/linux/sys       linsysfs        rw              0       0
tmpfs           /compat/linux/dev/shm   tmpfs           rw,mode=1777    0       0
```

Mount the filesystems.

```sh
mount /compat/linux/proc
mount /compat/linux/sys
mount /compat/linux/dev/shm
```

### Java and Build Tools

Android development requires JDK 17 or later.
Install the required packages as root.

```sh
pkg install openjdk17 bash
```

Gradle is needed once to bootstrap the project wrapper script.
Download Gradle to a local tools directory as a regular user.

```sh
GRADLE_VERSION=8.12.1
mkdir -p $HOME/tools
curl -sL "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
  -o /tmp/gradle.zip
unzip /tmp/gradle.zip -d $HOME/tools/
export PATH="$HOME/tools/gradle-${GRADLE_VERSION}/bin:$PATH"
```

After generating the Gradle wrapper in the project directory,
the system-wide Gradle installation is no longer needed.
The wrapper script downloads the correct Gradle version automatically.

### Android SDK

Download the Android command-line tools for Linux.
The Linux version is used because the Linuxulator will run the native binaries.

```sh
ANDROID_HOME=$HOME/android/sdk
CMDLINE_TOOLS_URL="https://dl.google.com/android/repository/commandlinetools-linux-13114758_latest.zip"

mkdir -p $ANDROID_HOME/cmdline-tools
curl -sL "$CMDLINE_TOOLS_URL" -o /tmp/cmdline-tools.zip
unzip /tmp/cmdline-tools.zip -d $ANDROID_HOME/cmdline-tools/
mv $ANDROID_HOME/cmdline-tools/cmdline-tools $ANDROID_HOME/cmdline-tools/latest
```

The `sdkmanager` tool is a Java application and runs natively on FreeBSD.
Use it to install the platform, build tools, and NDK.

```sh
export ANDROID_HOME=$HOME/android/sdk
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$PATH

sdkmanager --sdk_root=$ANDROID_HOME \
  "platforms;android-35" \
  "build-tools;35.0.0" \
  "ndk;28.0.12674087" \
  "platform-tools"
```

Accept the license agreement when prompted.

The packages downloaded by `sdkmanager` contain Linux ELF binaries for tools such as `aapt2`, `d8`, and the NDK toolchain.
On FreeBSD 14, unbranded ELF binaries default to Linux execution through the Linuxulator.
If any SDK tools fail to execute, apply explicit ELF branding.

```sh
find $ANDROID_HOME -type f -exec file {} + \
  | grep "ELF" \
  | cut -d: -f1 \
  | xargs brandelf -t Linux 2>/dev/null
```

### ADB Setup

The Linux version of ADB distributed with the Android SDK does not work reliably on FreeBSD.
Install the native FreeBSD ADB from the `devel/android-tools` port instead.

```sh
# As root
pkg install android-tools
```

Verify that ADB detects a connected device.

```sh
adb devices
```

If the device does not appear, enable USB debugging on the Android device
and authorize the connection when prompted.
ADB over TCP/IP is an alternative if USB ADB is unreliable.

```sh
# Connect via TCP/IP (device and workstation on same network)
adb tcpip 5555
adb connect DEVICE_IP:5555
```

### Rust Toolchain

Install Rust from the FreeBSD port or through `rustup`.
Add the Android cross-compilation targets and install `cargo-ndk`.

```sh
# Install Rust (if not already installed)
pkg install rust

# Add Android targets
rustup target add aarch64-linux-android

# Install cargo-ndk
cargo install cargo-ndk
```

The `cargo-ndk` tool invokes the NDK toolchain for cross-compilation.
It calls the NDK's `clang` binary, which is a Linux executable that runs through the Linuxulator.

### Environment Configuration

Add the following to `~/.profile` or the equivalent shell configuration file.

`~/.profile` partial listing
```sh
# Android SDK
export ANDROID_HOME="${HOME}/android/sdk"
export PATH="${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${PATH}"

# Android NDK
export ANDROID_NDK_HOME="${ANDROID_HOME}/ndk/28.0.12674087"
```

Source the file or start a new shell before continuing.

## SDK Development

This section creates a minimal Android application using Kotlin.
The application displays input fields for CLMM calculator parameters
and placeholder text where computed results will appear.
No native code is used yet.
The goal is to verify that the SDK build pipeline works end-to-end on FreeBSD.

### Project Structure

Create the project directory tree.

```sh
PROJECT=$HOME/projects/clmm-android
mkdir -p $PROJECT/app/src/main/java/com/example/clmm
mkdir -p $PROJECT/app/src/main/res/layout
mkdir -p $PROJECT/app/src/main/res/values
mkdir -p $PROJECT/gradle/wrapper
```

### Build Configuration

Create the Gradle settings file.

`settings.gradle.kts` full listing
```kotlin
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode = RepositoriesMode.FAIL_ON_PROJECT_REPOS
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "clmm-android"
include(":app")
```

Create the root build file.

`build.gradle.kts` full listing
```kotlin
plugins {
    id("com.android.application") version "8.9.0" apply false
    id("org.jetbrains.kotlin.android") version "2.1.0" apply false
}
```

Create the application build file.

`app/build.gradle.kts` full listing
```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.clmm"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.clmm"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.7.0")
}
```

Create the Gradle properties file.

`gradle.properties` full listing
```
android.useAndroidX=true
org.gradle.jvmargs=-Xmx2048m
```

Create the Gradle wrapper properties file.

`gradle/wrapper/gradle-wrapper.properties` full listing
```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.12.1-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

Generate the wrapper scripts.

```sh
cd $PROJECT
gradle wrapper
```

This creates `gradlew` and `gradlew.bat` in the project root.
From this point forward, use `./gradlew` instead of the system Gradle installation.

### User Interface

Create the Android manifest.

`app/src/main/AndroidManifest.xml` full listing
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:allowBackup="true"
        android:label="@string/app_name"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

Create the string resources.

`app/src/main/res/values/strings.xml` full listing
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">CLMM Calculator</string>
    <string name="label_min_price">Min Price (p_a)</string>
    <string name="label_cur_price">Current Price (p)</string>
    <string name="label_max_price">Max Price (p_b)</string>
    <string name="label_liquidity">Liquidity (L)</string>
    <string name="label_token_x">Token X</string>
    <string name="label_token_y">Token Y</string>
    <string name="btn_calc_reserves">Calculate Reserves</string>
    <string name="btn_calc_liquidity">Calculate Liquidity</string>
</resources>
```

Create the layout file.

`app/src/main/res/layout/activity_main.xml` full listing
```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/app_name"
            android:textSize="24sp"
            android:layout_marginBottom="16dp" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_min_price" />
        <EditText
            android:id="@+id/editMinPrice"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal"
            android:text="1800" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_cur_price" />
        <EditText
            android:id="@+id/editCurPrice"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal"
            android:text="2000" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_max_price" />
        <EditText
            android:id="@+id/editMaxPrice"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal"
            android:text="2200" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_liquidity" />
        <EditText
            android:id="@+id/editLiquidity"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal"
            android:text="1000" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_token_x"
            android:layout_marginTop="8dp" />
        <EditText
            android:id="@+id/editTokenX"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/label_token_y" />
        <EditText
            android:id="@+id/editTokenY"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="numberDecimal" />

        <Button
            android:id="@+id/btnCalculateReserves"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/btn_calc_reserves"
            android:layout_marginTop="16dp" />

        <Button
            android:id="@+id/btnCalculateLiquidity"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/btn_calc_liquidity" />

        <TextView
            android:id="@+id/textResult"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="16sp"
            android:layout_marginTop="16dp" />
    </LinearLayout>
</ScrollView>
```

### Activity Implementation

Create the initial Kotlin activity with placeholder logic.
The buttons display a message confirming the UI works but do not perform calculations yet.

`app/src/main/java/com/example/clmm/MainActivity.kt` full listing
```kotlin
package com.example.clmm

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val editMinPrice = findViewById<EditText>(R.id.editMinPrice)
        val editCurPrice = findViewById<EditText>(R.id.editCurPrice)
        val editMaxPrice = findViewById<EditText>(R.id.editMaxPrice)
        val editLiquidity = findViewById<EditText>(R.id.editLiquidity)
        val editTokenX = findViewById<EditText>(R.id.editTokenX)
        val editTokenY = findViewById<EditText>(R.id.editTokenY)
        val textResult = findViewById<TextView>(R.id.textResult)

        findViewById<Button>(R.id.btnCalculateReserves).setOnClickListener {
            textResult.text = "SDK build verified. Native math pending."
        }

        findViewById<Button>(R.id.btnCalculateLiquidity).setOnClickListener {
            textResult.text = "SDK build verified. Native math pending."
        }
    }
}
```

### Build and Run

Build the debug APK.

```sh
cd $PROJECT
./gradlew assembleDebug
```

The APK is generated at `app/build/outputs/apk/debug/app-debug.apk`.

Install and launch on a connected device.

```sh
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.example.clmm/.MainActivity
```

Tapping either button should display the placeholder message.
This confirms that the SDK build pipeline and deployment work correctly on FreeBSD.

## NDK Development

This section adds a Rust native library that implements the CLMM reserve and liquidity calculations.
The library is compiled for Android using `cargo-ndk`
and exposed to Kotlin through JNI function declarations.

### Rust Library

Create the Rust project directory.

```sh
mkdir -p $PROJECT/rust/src
```

Create the Cargo manifest.

`rust/Cargo.toml` full listing
```toml
[package]
name = "clmm"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
jni = "0.21"
```

Create the library source file.
The two core functions compute token reserves from liquidity depth
and liquidity depth from token reserves,
following the three price regimes of the concentrated liquidity model.

`rust/src/lib.rs` full listing
```rust
use jni::JNIEnv;
use jni::objects::JObject;
use jni::sys::{jdouble, jdoubleArray};

fn compute_reserves(p_a: f64, p_c: f64, p_b: f64, l: f64) -> (f64, f64) {
    if p_a <= 0.0 || p_b <= 0.0 || p_b <= p_a || l < 0.0 {
        return (0.0, 0.0);
    }
    let sqrt_a = p_a.sqrt();
    let sqrt_b = p_b.sqrt();
    let sqrt_c = p_c.sqrt();

    if p_c <= p_a {
        // Below range: all Token X
        let x = l * (sqrt_b - sqrt_a) / (sqrt_a * sqrt_b);
        (x, 0.0)
    } else if p_c >= p_b {
        // Above range: all Token Y
        let y = l * (sqrt_b - sqrt_a);
        (0.0, y)
    } else {
        // In range: both tokens
        let x = l * (sqrt_b - sqrt_c) / (sqrt_c * sqrt_b);
        let y = l * (sqrt_c - sqrt_a);
        (x, y)
    }
}

fn compute_liquidity(p_a: f64, p_c: f64, p_b: f64, x: f64, y: f64) -> f64 {
    if p_a <= 0.0 || p_b <= 0.0 || p_b <= p_a {
        return 0.0;
    }
    let sqrt_a = p_a.sqrt();
    let sqrt_b = p_b.sqrt();
    let sqrt_c = p_c.sqrt();

    if p_c <= p_a {
        x * sqrt_a * sqrt_b / (sqrt_b - sqrt_a)
    } else if p_c >= p_b {
        y / (sqrt_b - sqrt_a)
    } else {
        let l_x = x * sqrt_c * sqrt_b / (sqrt_b - sqrt_c);
        let l_y = y / (sqrt_c - sqrt_a);
        l_x.min(l_y)
    }
}

#[no_mangle]
pub extern "system" fn Java_com_example_clmm_MainActivity_calculateReserves<'local>(
    mut env: JNIEnv<'local>,
    _this: JObject<'local>,
    p_a: jdouble,
    p_c: jdouble,
    p_b: jdouble,
    l: jdouble,
) -> jdoubleArray {
    let (x, y) = compute_reserves(p_a, p_c, p_b, l);
    let result = env.new_double_array(2).expect("Failed to create double array");
    env.set_double_array_region(&result, 0, &[x, y])
        .expect("Failed to set double array region");
    result.into_raw()
}

#[no_mangle]
pub extern "system" fn Java_com_example_clmm_MainActivity_calculateLiquidity(
    _env: JNIEnv,
    _this: JObject,
    p_a: jdouble,
    p_c: jdouble,
    p_b: jdouble,
    x: jdouble,
    y: jdouble,
) -> jdouble {
    compute_liquidity(p_a, p_c, p_b, x, y)
}
```

The JNI function names follow the `Java_package_Class_method` convention.
The `extern "system"` calling convention matches the JNI ABI on Android.

### Gradle Integration

Update the application build file to run `cargo ndk` before the Android build.

`app/build.gradle.kts` full listing
```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.clmm"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.clmm"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
        ndk {
            abiFilters += "arm64-v8a"
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.7.0")
}

tasks.register<Exec>("buildRustLib") {
    workingDir = file("../rust")
    commandLine(
        "cargo", "ndk",
        "-t", "arm64-v8a",
        "-o", "../app/src/main/jniLibs",
        "build", "--release"
    )
}

tasks.named("preBuild") {
    dependsOn("buildRustLib")
}
```

The `buildRustLib` task runs `cargo ndk` to cross-compile the Rust library for ARM64 Android.
The compiled shared object is placed in `app/src/main/jniLibs/arm64-v8a/libclmm.so`,
where the Android build system automatically packages it into the APK.

The `abiFilters` setting restricts the APK to 64-bit ARM.
Add additional targets as needed for other architectures.

### Updated Activity

Update the Kotlin activity to load the native library and call the JNI functions.

`app/src/main/java/com/example/clmm/MainActivity.kt` full listing
```kotlin
package com.example.clmm

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    companion object {
        init {
            System.loadLibrary("clmm")
        }
    }

    private external fun calculateReserves(
        pA: Double, pC: Double, pB: Double, l: Double
    ): DoubleArray

    private external fun calculateLiquidity(
        pA: Double, pC: Double, pB: Double, x: Double, y: Double
    ): Double

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val editMinPrice = findViewById<EditText>(R.id.editMinPrice)
        val editCurPrice = findViewById<EditText>(R.id.editCurPrice)
        val editMaxPrice = findViewById<EditText>(R.id.editMaxPrice)
        val editLiquidity = findViewById<EditText>(R.id.editLiquidity)
        val editTokenX = findViewById<EditText>(R.id.editTokenX)
        val editTokenY = findViewById<EditText>(R.id.editTokenY)
        val textResult = findViewById<TextView>(R.id.textResult)

        findViewById<Button>(R.id.btnCalculateReserves).setOnClickListener {
            val pA = editMinPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pC = editCurPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pB = editMaxPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val l = editLiquidity.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val result = calculateReserves(pA, pC, pB, l)
            editTokenX.setText(String.format("%.2f", result[0]))
            editTokenY.setText(String.format("%.2f", result[1]))
            textResult.text = "Reserves calculated from liquidity"
        }

        findViewById<Button>(R.id.btnCalculateLiquidity).setOnClickListener {
            val pA = editMinPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pC = editCurPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pB = editMaxPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val x = editTokenX.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val y = editTokenY.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val l = calculateLiquidity(pA, pC, pB, x, y)
            editLiquidity.setText(String.format("%.6f", l))
            textResult.text = "Liquidity calculated from reserves"
        }
    }
}
```

### Build and Run

Build the APK with NDK support.

```sh
cd $PROJECT
./gradlew assembleDebug
```

The Gradle build first runs `cargo ndk` to compile the Rust library,
then packages the resulting `libclmm.so` into the APK alongside the Kotlin bytecode.

Install and launch the updated application.

```sh
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.example.clmm/.MainActivity
```

Enter CLMM parameters and tap "Calculate Reserves."
The application should display computed token amounts
matching the values produced by the [CLMM calculator widget][related_post_clmm].

## Emulator Feasibility

The Android emulator requires hardware-assisted virtualization through KVM on Linux
or Hypervisor.framework on macOS.
FreeBSD's Linuxulator does not expose KVM to Linux binaries.
FreeBSD does have its own hypervisor, bhyve, but it does not support the Android emulator's requirements.

Running the Android emulator on FreeBSD is not supported.
All testing and debugging must be performed on physical hardware connected via ADB.
This is the recommended workflow for NDK development regardless of host platform,
as emulators do not always reproduce the behavior of real hardware.

## Conclusion

This post demonstrated a complete Android development workflow on FreeBSD
using only command-line tools.
The Linuxulator runs Linux Android SDK and NDK binaries at near-native speed.
Java, Gradle, and Rust run natively through FreeBSD ports.
The sample CLMM calculator application exercises both the SDK pipeline with Kotlin
and the NDK pipeline with Rust exposed through JNI.

The build system is platform-independent.
The same project builds on macOS or Linux by installing the Android SDK and NDK for those platforms.
Only the environment setup section is FreeBSD-specific.

## Future Reading

Areas for further exploration include
continuous integration for Android builds on FreeBSD,
Jetpack Compose for declarative UI as an alternative to XML layouts,
and additional ABI targets for broader device coverage.

## References

- [Android, Command-Line Tools][android_cmdline_tools]
- [Android, NDK Downloads][android_ndk_downloads]
- [Android, sdkmanager][android_sdkmanager]
- [FreeBSD, FreshPorts android-tools][freebsd_android_tools]
- [FreeBSD, FreshPorts linux_base-rl9][freebsd_linux_base_rl9]
- [FreeBSD, Linux Binary Compatibility Handbook][freebsd_linuxemu]
- [FreeBSD, Operate Android Device on FreeBSD, Vermaden][freebsd_vermaden_android]
- [Related Post, Concentrated Liquidity Market Maker Mathematics][related_post_clmm]
- [Rust, cargo-ndk][rust_cargo_ndk]
- [Rust, jni][rust_jni]

[android_cmdline_tools]: https://developer.android.com/tools
[android_ndk_downloads]: https://developer.android.com/ndk/downloads
[android_sdkmanager]: https://developer.android.com/tools/sdkmanager
[freebsd_android_tools]: https://www.freshports.org/devel/android-tools/
[freebsd_linux_base_rl9]: https://www.freshports.org/emulators/linux_base-rl9
[freebsd_linuxemu]: https://docs.freebsd.org/en/books/handbook/linuxemu/
[freebsd_vermaden_android]: https://vermaden.wordpress.com/2024/10/29/operate-android-device-on-freebsd/
[related_post_clmm]: {% post_url 2026-02-22-clmm_mathematics %}
[rust_cargo_ndk]: https://crates.io/crates/cargo-ndk
[rust_jni]: https://crates.io/crates/jni
