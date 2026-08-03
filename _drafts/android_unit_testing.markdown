---
layout: post
mathjax: true
comments: true
title: "Android Unit Testing"
date: 2026-02-27 00:01:00 +0000
categories: android testing kotlin rust
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

Android unit testing has evolved substantially since the framework's early years.
The original `android.test` package and its `ApplicationTestCase` class have been deprecated
in favor of the AndroidX Test libraries,
which provide a unified API that works across local and instrumented test environments.
Modern Android projects written in Kotlin benefit from a mature ecosystem of testing tools
including JUnit 4 as the standard test runner,
Robolectric for simulating the Android framework on the host JVM,
and MockK for idiomatic Kotlin mocking.

The Android testing model divides tests into two categories based on execution environment.
Local unit tests run on the development machine's JVM and reside in the `src/test/` directory.
They execute quickly and do not require a device or emulator.
Instrumented tests run on a physical device or emulator and reside in the `src/androidTest/` directory.
Robolectric bridges these categories by providing a simulated Android environment that runs locally,
enabling tests that depend on Android framework classes to execute without device deployment.

This post demonstrates testing at every layer of an Android application that includes both Kotlin and native code.
The test subject is a calculator application that implements concentrated liquidity mathematics
in both Kotlin and Rust.
Local unit tests verify the pure Kotlin computation.
Robolectric tests verify the Activity behavior on the host JVM.
Instrumented tests verify the application on a device.
The NDK unit testing section covers testing Rust native code with `cargo test`,
testing the Java Native Interface boundary,
and integrating GoogleTest for C++ native libraries.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-27 00:01:00 +0000

# OS and Version
$ uname -vm
TODO

# Java
$ java -version
TODO

# Gradle
$ ./gradlew --version | head -n 3
TODO

# Android SDK
$ sdkmanager --version
TODO

# Android NDK
$ ls $ANDROID_HOME/ndk/
TODO

# Kotlin
$ kotlinc -version
TODO

# Rust
$ rustc --version
TODO

# cargo-ndk
$ cargo ndk --version
TODO
```

## Test Subject

The test subject for this post is a Concentrated Liquidity Market Maker calculator application.
The application computes token reserves from liquidity depth and liquidity depth from token reserves,
following the concentrated liquidity model introduced by Uniswap v3.
The [CLMM Mathematics][related_post_clmm] post provides the full mathematical derivation.
The [Android Development on FreeBSD][related_post_android_freebsd] post
provides full build and deployment instructions for this application.

The reserve computation follows three regimes
based on the position of the current price $p_c$
relative to the range boundaries $p_a$ and $p_b$.
When the current price falls within the range, the token reserves are

$$x = L \cdot \frac{\sqrt{p_b} - \sqrt{p_c}}{\sqrt{p_c} \cdot \sqrt{p_b}} \qquad y = L \cdot (\sqrt{p_c} - \sqrt{p_a})$$

where $L$ is the liquidity depth.
When the current price is below the range, all liquidity is held as token $x$.
When the current price is above the range, all liquidity is held as token $y$.

The application has four testable components.
The `ClmmCalculator` Kotlin object encapsulates the mathematics with no Android framework dependencies.
The `MainActivity` reads user input and calls the calculator.
The Rust native library implements the same computation for performance-critical deployments.
The JNI bridge marshals data between Kotlin and Rust.

The project directory tree follows the standard Android convention
with separate directories for source, local tests, and instrumented tests.

```
clmm-android/
  app/
    src/
      main/java/com/example/clmm/
        ClmmCalculator.kt
        MainActivity.kt
      test/java/com/example/clmm/
        ClmmCalculatorTest.kt
        MainActivityTest.kt
      androidTest/java/com/example/clmm/
        MainActivityInstrumentedTest.kt
    build.gradle.kts
  rust/
    src/
      lib.rs
    Cargo.toml
  build.gradle.kts
  settings.gradle.kts
```

### Calculator

The `ClmmCalculator` object implements the concentrated liquidity mathematics in pure Kotlin.
It has no Android framework dependencies and can be tested with standard JUnit assertions on the host JVM.

`app/src/main/java/com/example/clmm/ClmmCalculator.kt` full listing
```kotlin
package com.example.clmm

import kotlin.math.min
import kotlin.math.sqrt

object ClmmCalculator {
    data class Reserves(val x: Double, val y: Double)

    fun computeReserves(pA: Double, pC: Double, pB: Double, l: Double): Reserves {
        if (pA <= 0.0 || pB <= 0.0 || pB <= pA || l < 0.0) {
            return Reserves(0.0, 0.0)
        }
        val sqrtA = sqrt(pA)
        val sqrtB = sqrt(pB)
        val sqrtC = sqrt(pC)

        return when {
            pC <= pA -> Reserves(
                x = l * (sqrtB - sqrtA) / (sqrtA * sqrtB),
                y = 0.0
            )
            pC >= pB -> Reserves(
                x = 0.0,
                y = l * (sqrtB - sqrtA)
            )
            else -> Reserves(
                x = l * (sqrtB - sqrtC) / (sqrtC * sqrtB),
                y = l * (sqrtC - sqrtA)
            )
        }
    }

    fun computeLiquidity(pA: Double, pC: Double, pB: Double, x: Double, y: Double): Double {
        if (pA <= 0.0 || pB <= 0.0 || pB <= pA) {
            return 0.0
        }
        val sqrtA = sqrt(pA)
        val sqrtB = sqrt(pB)
        val sqrtC = sqrt(pC)

        return when {
            pC <= pA -> x * sqrtA * sqrtB / (sqrtB - sqrtA)
            pC >= pB -> y / (sqrtB - sqrtA)
            else -> {
                val lX = x * sqrtC * sqrtB / (sqrtB - sqrtC)
                val lY = y / (sqrtC - sqrtA)
                min(lX, lY)
            }
        }
    }
}
```

### Activity

The Activity reads user input from text fields, calls `ClmmCalculator`, and displays the results.
This is the layer that depends on the Android framework and benefits from Robolectric testing.

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
            val pA = editMinPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pC = editCurPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pB = editMaxPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val l = editLiquidity.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val result = ClmmCalculator.computeReserves(pA, pC, pB, l)
            editTokenX.setText(String.format("%.6f", result.x))
            editTokenY.setText(String.format("%.6f", result.y))
            textResult.text = "Reserves calculated from liquidity"
        }

        findViewById<Button>(R.id.btnCalculateLiquidity).setOnClickListener {
            val pA = editMinPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pC = editCurPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val pB = editMaxPrice.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val x = editTokenX.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val y = editTokenY.text.toString().toDoubleOrNull() ?: return@setOnClickListener
            val l = ClmmCalculator.computeLiquidity(pA, pC, pB, x, y)
            editLiquidity.setText(String.format("%.6f", l))
            textResult.text = "Liquidity calculated from reserves"
        }
    }
}
```

### Native Library

The Rust native library implements the same computation for performance-critical deployments.
The pure logic functions mirror the Kotlin implementation.
The JNI bridge functions, which are thin wrappers that marshal data between Kotlin and Rust,
are documented in the [Android Development on FreeBSD][related_post_android_freebsd] post.

`rust/src/lib.rs` partial listing
```rust
fn compute_reserves(p_a: f64, p_c: f64, p_b: f64, l: f64) -> (f64, f64) {
    if p_a <= 0.0 || p_b <= 0.0 || p_b <= p_a || l < 0.0 {
        return (0.0, 0.0);
    }
    let sqrt_a = p_a.sqrt();
    let sqrt_b = p_b.sqrt();
    let sqrt_c = p_c.sqrt();

    if p_c <= p_a {
        let x = l * (sqrt_b - sqrt_a) / (sqrt_a * sqrt_b);
        (x, 0.0)
    } else if p_c >= p_b {
        let y = l * (sqrt_b - sqrt_a);
        (0.0, y)
    } else {
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
```

### Build Configuration

The application build file configures both the application and its test dependencies.
The test dependencies are explained in the Instructions section that follows.

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

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"

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

    testOptions {
        unitTests {
            isIncludeAndroidResources = true
        }
    }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.7.0")

    // Local unit tests
    testImplementation("junit:junit:4.13.2")
    testImplementation("androidx.test:core:1.7.0")
    testImplementation("androidx.test.ext:junit:1.3.0")
    testImplementation("org.robolectric:robolectric:4.16.1")
    testImplementation("io.mockk:mockk:1.14.9")

    // Instrumented tests
    androidTestImplementation("androidx.test:runner:1.7.0")
    androidTestImplementation("androidx.test.ext:junit:1.3.0")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.7.0")
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

## Instructions

### Test Dependencies

The build file declares test dependencies in two scopes.
The `testImplementation` scope applies to local unit tests that run on the host JVM.
The `androidTestImplementation` scope applies to instrumented tests that run on a device or emulator.

[JUnit 4][ref_junit4] is the standard test runner for Android.
The `junit:junit:4.13.2` dependency provides the `@Test` annotation, assertion methods,
and the `@RunWith` annotation for selecting custom test runners.

The AndroidX Test libraries provide a unified API across test environments.
The `androidx.test:core` library provides `ApplicationProvider` and `ActivityScenario`
for managing application context and Activity lifecycle in tests.
The `androidx.test.ext:junit` library provides the `AndroidJUnit4` runner,
which delegates to the appropriate backend depending on the execution environment.
When running on the host JVM with [Robolectric][ref_robolectric],
it delegates to the Robolectric test runner.
When running on a device, it delegates to the `AndroidJUnitRunner`.

[Robolectric][ref_robolectric] simulates the Android framework on the host JVM.
It intercepts calls to Android framework classes and routes them through shadow implementations
that are compatible with the standard JVM.
The `isIncludeAndroidResources = true` setting in `testOptions` is required
for Robolectric to access layout files and string resources.

[MockK][ref_mockk] provides idiomatic Kotlin mocking.
It handles final classes, coroutines, and object declarations natively.

For instrumented tests, the `AndroidJUnitRunner` coordinates test execution on the device.
The `testInstrumentationRunner` setting in `defaultConfig` tells the Android build system
which runner to use.
Espresso provides UI interaction and assertion APIs for instrumented tests.

### Local Unit Tests

Local unit tests reside in `app/src/test/java/` and run on the host JVM.
They execute in seconds rather than minutes because they do not deploy to a device.

#### Pure Logic Tests

The `ClmmCalculatorTest` class tests the Kotlin calculator with standard JUnit 4 assertions.
Each test method verifies a price regime or edge case.
The `assertEquals` overload with a delta parameter handles floating-point comparison tolerance.

`app/src/test/java/com/example/clmm/ClmmCalculatorTest.kt` full listing
```kotlin
package com.example.clmm

import org.junit.Assert.assertEquals
import org.junit.Test

class ClmmCalculatorTest {
    private val delta = 0.01

    @Test
    fun reservesInRange() {
        val result = ClmmCalculator.computeReserves(1800.0, 2000.0, 2200.0, 1000.0)
        assertEquals(1.04, result.x, delta)
        assertEquals(2294.96, result.y, delta)
    }

    @Test
    fun reservesBelowRange() {
        val result = ClmmCalculator.computeReserves(1800.0, 1500.0, 2200.0, 1000.0)
        assertEquals(2.25, result.x, delta)
        assertEquals(0.0, result.y, delta)
    }

    @Test
    fun reservesAboveRange() {
        val result = ClmmCalculator.computeReserves(1800.0, 2500.0, 2200.0, 1000.0)
        assertEquals(0.0, result.x, delta)
        assertEquals(4477.76, result.y, delta)
    }

    @Test
    fun reservesInvalidPrices() {
        val result = ClmmCalculator.computeReserves(-1.0, 100.0, 200.0, 1000.0)
        assertEquals(0.0, result.x, delta)
        assertEquals(0.0, result.y, delta)
    }

    @Test
    fun reservesZeroLiquidity() {
        val result = ClmmCalculator.computeReserves(1800.0, 2000.0, 2200.0, 0.0)
        assertEquals(0.0, result.x, delta)
        assertEquals(0.0, result.y, delta)
    }

    @Test
    fun liquidityRoundTrip() {
        val reserves = ClmmCalculator.computeReserves(1800.0, 2000.0, 2200.0, 1000.0)
        val liquidity = ClmmCalculator.computeLiquidity(
            1800.0, 2000.0, 2200.0, reserves.x, reserves.y
        )
        assertEquals(1000.0, liquidity, delta)
    }

    @Test
    fun liquidityBelowRange() {
        val liquidity = ClmmCalculator.computeLiquidity(1800.0, 1500.0, 2200.0, 2.25, 0.0)
        assertEquals(1000.0, liquidity, delta)
    }

    @Test
    fun liquidityInvalidPrices() {
        val liquidity = ClmmCalculator.computeLiquidity(200.0, 100.0, 100.0, 1.0, 1.0)
        assertEquals(0.0, liquidity, delta)
    }
}
```

Run the local unit tests with Gradle.

```sh
$ ./gradlew testDebugUnitTest
```

Test reports are generated at `app/build/reports/tests/testDebugUnitTest/index.html`.

#### Robolectric Tests

The `MainActivityTest` class tests the Activity on the host JVM using Robolectric.
The `@RunWith(AndroidJUnit4::class)` annotation selects the unified test runner,
which detects the Robolectric environment and delegates accordingly.
`ActivityScenario.launch` creates and starts the Activity in a simulated Android environment.
The `onActivity` callback provides direct access to the Activity instance
for view state verification.

`app/src/test/java/com/example/clmm/MainActivityTest.kt` full listing
```kotlin
package com.example.clmm

import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.test.core.app.ActivityScenario
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class MainActivityTest {

    @Test
    fun activityLaunches() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            val textResult = activity.findViewById<TextView>(R.id.textResult)
            assertNotNull(textResult)
        }
    }

    @Test
    fun calculateReservesUpdatesResult() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            activity.findViewById<EditText>(R.id.editMinPrice).setText("1800")
            activity.findViewById<EditText>(R.id.editCurPrice).setText("2000")
            activity.findViewById<EditText>(R.id.editMaxPrice).setText("2200")
            activity.findViewById<EditText>(R.id.editLiquidity).setText("1000")
            activity.findViewById<Button>(R.id.btnCalculateReserves).performClick()
            val textResult = activity.findViewById<TextView>(R.id.textResult)
            assertEquals("Reserves calculated from liquidity", textResult.text.toString())
        }
    }

    @Test
    fun calculateReservesPopulatesTokenFields() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            activity.findViewById<EditText>(R.id.editMinPrice).setText("1800")
            activity.findViewById<EditText>(R.id.editCurPrice).setText("2000")
            activity.findViewById<EditText>(R.id.editMaxPrice).setText("2200")
            activity.findViewById<EditText>(R.id.editLiquidity).setText("1000")
            activity.findViewById<Button>(R.id.btnCalculateReserves).performClick()
            val tokenX = activity.findViewById<EditText>(R.id.editTokenX).text.toString()
            val tokenY = activity.findViewById<EditText>(R.id.editTokenY).text.toString()
            assertNotNull(tokenX.toDoubleOrNull())
            assertNotNull(tokenY.toDoubleOrNull())
        }
    }

    @Test
    fun emptyFieldsDoNotCrash() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            activity.findViewById<EditText>(R.id.editMinPrice).setText("")
            activity.findViewById<Button>(R.id.btnCalculateReserves).performClick()
            // No crash means the guard clause works
        }
    }
}
```

These tests run with the same `./gradlew testDebugUnitTest` command as the pure logic tests.
Robolectric inflates the layout, resolves view IDs, and handles click events
without requiring a device or emulator.

### Mocking

When testing components that depend on external services or slow computations,
mocking isolates the unit under test from its dependencies.
[MockK][ref_mockk] provides Kotlin-native mocking including support for object declarations.
The `mockkObject` function replaces an object's function implementations with test doubles.

```kotlin
import io.mockk.every
import io.mockk.mockkObject
import io.mockk.unmockkObject
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test

class MockedCalculatorTest {
    @Before
    fun setUp() {
        mockkObject(ClmmCalculator)
    }

    @After
    fun tearDown() {
        unmockkObject(ClmmCalculator)
    }

    @Test
    fun activityHandlesZeroReserves() {
        every {
            ClmmCalculator.computeReserves(any(), any(), any(), any())
        } returns ClmmCalculator.Reserves(0.0, 0.0)

        val result = ClmmCalculator.computeReserves(1800.0, 2000.0, 2200.0, 1000.0)
        assertEquals(0.0, result.x, 0.01)
    }
}
```

Mocking is most useful when the real dependency is slow, non-deterministic, or requires external resources.
For the CLMM calculator, the real implementation is fast and deterministic,
so the pure logic tests above are preferable.
The mocking example above is illustrative.
In larger applications, mocking is essential for isolating ViewModels from repositories,
repositories from network clients, and other dependency boundaries.

### Instrumented Tests

Instrumented tests reside in `app/src/androidTest/java/` and run on a connected device or emulator.
They exercise the application in the real Android runtime environment
including the Activity lifecycle, view rendering, and resource loading.

`app/src/androidTest/java/com/example/clmm/MainActivityInstrumentedTest.kt` full listing
```kotlin
package com.example.clmm

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.action.ViewActions.replaceText
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.isDisplayed
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.espresso.matcher.ViewMatchers.withText
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class MainActivityInstrumentedTest {

    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun activityDisplaysCalculateButton() {
        onView(withId(R.id.btnCalculateReserves)).check(matches(isDisplayed()))
    }

    @Test
    fun calculateReservesDisplaysResult() {
        onView(withId(R.id.editMinPrice)).perform(replaceText("1800"))
        onView(withId(R.id.editCurPrice)).perform(replaceText("2000"))
        onView(withId(R.id.editMaxPrice)).perform(replaceText("2200"))
        onView(withId(R.id.editLiquidity)).perform(replaceText("1000"))
        onView(withId(R.id.btnCalculateReserves)).perform(click())
        onView(withId(R.id.textResult))
            .check(matches(withText("Reserves calculated from liquidity")))
    }
}
```

Run the instrumented tests with Gradle.
A connected device or running emulator is required.

```sh
$ ./gradlew connectedDebugAndroidTest
```

Test reports are generated at `app/build/reports/androidTests/connected/index.html`.

### NDK Unit Testing

Native code testing follows a layered approach.
The majority of test coverage should reside in host-side unit tests
that exercise pure logic without requiring a device.
Integration tests that verify the JNI boundary require either a device or a host-compiled native library.

#### Rust Unit Tests

The most effective strategy for testing Rust native libraries
is to separate pure logic from JNI concerns.
The `compute_reserves` and `compute_liquidity` functions shown in the Test Subject section
contain no JNI dependencies and can be tested with standard `cargo test` on the host machine.
No Android SDK, NDK, or device is needed.

Add a test module to the library source file.

`rust/src/lib.rs` partial listing
```rust
#[cfg(test)]
mod tests {
    use super::*;

    const DELTA: f64 = 0.01;

    fn approx_eq(a: f64, b: f64) -> bool {
        (a - b).abs() < DELTA
    }

    #[test]
    fn reserves_in_range() {
        let (x, y) = compute_reserves(1800.0, 2000.0, 2200.0, 1000.0);
        assert!(approx_eq(x, 1.04), "x = {x}");
        assert!(approx_eq(y, 2294.96), "y = {y}");
    }

    #[test]
    fn reserves_below_range() {
        let (x, y) = compute_reserves(1800.0, 1500.0, 2200.0, 1000.0);
        assert!(approx_eq(x, 2.25), "x = {x}");
        assert!(approx_eq(y, 0.0), "y = {y}");
    }

    #[test]
    fn reserves_above_range() {
        let (x, y) = compute_reserves(1800.0, 2500.0, 2200.0, 1000.0);
        assert!(approx_eq(x, 0.0), "x = {x}");
        assert!(approx_eq(y, 4477.76), "y = {y}");
    }

    #[test]
    fn reserves_invalid_prices() {
        let (x, y) = compute_reserves(-1.0, 100.0, 200.0, 1000.0);
        assert_eq!(x, 0.0);
        assert_eq!(y, 0.0);
    }

    #[test]
    fn reserves_zero_liquidity() {
        let (x, y) = compute_reserves(1800.0, 2000.0, 2200.0, 0.0);
        assert_eq!(x, 0.0);
        assert_eq!(y, 0.0);
    }

    #[test]
    fn liquidity_round_trip() {
        let (x, y) = compute_reserves(1800.0, 2000.0, 2200.0, 1000.0);
        let l = compute_liquidity(1800.0, 2000.0, 2200.0, x, y);
        assert!(approx_eq(l, 1000.0), "l = {l}");
    }

    #[test]
    fn liquidity_below_range() {
        let l = compute_liquidity(1800.0, 1500.0, 2200.0, 2.25, 0.0);
        assert!(approx_eq(l, 1000.0), "l = {l}");
    }

    #[test]
    fn liquidity_invalid_prices() {
        let l = compute_liquidity(200.0, 100.0, 100.0, 1.0, 1.0);
        assert_eq!(l, 0.0);
    }
}
```

Run the Rust tests on the host machine.

```sh
$ cd rust
$ cargo test
```

This executes all tests in the module on the host architecture.
The tests verify the same mathematical properties as the Kotlin tests,
providing confidence that both implementations produce consistent results.

#### Testing the JNI Boundary

The JNI bridge functions require a running JVM or Android runtime to provide a valid `JNIEnv` pointer.
Two approaches exist for testing the boundary.

The first approach uses instrumented tests from Kotlin.
These tests call the `external fun` declarations in the Android application
and verify that the native library returns correct results through the full JNI path.
This tests the actual ART runtime, the dynamic linker, and the JNI calling convention.

`app/src/androidTest/java/com/example/clmm/NativeBridgeTest.kt` full listing
```kotlin
package com.example.clmm

import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Assert.assertEquals
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class NativeBridgeTest {
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

    @Test
    fun nativeReservesInRange() {
        val result = calculateReserves(1800.0, 2000.0, 2200.0, 1000.0)
        assertEquals(2, result.size)
        assertEquals(1.04, result[0], 0.01)
        assertEquals(2294.96, result[1], 0.01)
    }

    @Test
    fun nativeLiquidityRoundTrip() {
        val reserves = calculateReserves(1800.0, 2000.0, 2200.0, 1000.0)
        val liquidity = calculateLiquidity(
            1800.0, 2000.0, 2200.0, reserves[0], reserves[1]
        )
        assertEquals(1000.0, liquidity, 0.01)
    }
}
```

The second approach compiles the Rust library for the host platform
and loads it in local JUnit tests via `System.loadLibrary`.
This avoids the need for a device but tests the host JVM's JNI implementation
rather than Android's ART runtime.

```sh
# Compile the Rust library for the host platform
$ cd rust
$ cargo build

# Run host JVM tests with the library path set
$ ./gradlew testDebugUnitTest \
    -Djava.library.path=rust/target/debug
```

The host JVM approach is faster for continuous integration pipelines
but does not catch architecture-specific issues such as alignment differences or endianness.
For release verification, instrumented tests on a device are recommended.

#### GoogleTest for C++

For projects that use C or C++ native code instead of Rust,
the Android NDK ships with [GoogleTest][ref_googletest]
at `${ANDROID_NDK}/sources/third_party/googletest/`.

`CMakeLists.txt` partial listing
```cmake
set(GTEST_DIR ${ANDROID_NDK}/sources/third_party/googletest)

add_library(gtest STATIC
    ${GTEST_DIR}/src/gtest_main.cc
    ${GTEST_DIR}/src/gtest-all.cc)
target_include_directories(gtest PRIVATE ${GTEST_DIR})
target_include_directories(gtest PUBLIC ${GTEST_DIR}/include)

add_executable(native-tests test/my_tests.cpp)
target_link_libraries(native-tests my-native-lib gtest)
```

GoogleTest binaries are cross-compiled for the Android target architecture
and cannot run on the host.
Push the binary to a connected device and run it via `adb shell`.

```sh
$ adb push build/intermediates/cmake/debug/obj/arm64-v8a/native-tests \
    /data/local/tmp/
$ adb shell "LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/native-tests"
```

No built-in Android Gradle Plugin task exists for running native test binaries.
The `adb push` and `adb shell` workflow is the standard approach.

### Running Tests

The following table summarizes the Gradle tasks available for running tests.

| Task | Description |
|------|-------------|
| `testDebugUnitTest` | Run local unit tests for the debug build variant |
| `testReleaseUnitTest` | Run local unit tests for the release build variant |
| `test` | Run all local unit tests across all variants |
| `connectedDebugAndroidTest` | Run instrumented tests on connected devices for the debug variant |
| `connectedAndroidTest` | Run instrumented tests for all variants |
| `check` | Run all verification tasks including tests and lint |
| `lint` | Run Android Lint on all variants |
| `lintDebug` | Run Android Lint on the debug variant |

Run a test class by passing the `--tests` flag.

```sh
$ ./gradlew testDebugUnitTest --tests "com.example.clmm.ClmmCalculatorTest"
```

Run a test method.

```sh
$ ./gradlew testDebugUnitTest \
    --tests "com.example.clmm.ClmmCalculatorTest.reservesInRange"
```

### Code Coverage

JaCoCo is the standard code coverage tool for JVM projects.
Add the JaCoCo plugin to the build file and configure report generation.

`app/build.gradle.kts` partial listing
```kotlin
plugins {
    jacoco
}

jacoco {
    toolVersion = "0.8.12"
}

tasks.jacocoTestReport {
    dependsOn(tasks.named("testDebugUnitTest"))
    reports {
        xml.required.set(true)
        html.required.set(true)
    }
}
```

Kover is an alternative from JetBrains that is designed specifically for Kotlin
and handles inline functions more accurately than JaCoCo.

For Rust code coverage, `cargo-llvm-cov` provides integrated coverage measurement
using LLVM source-based coverage.

```sh
$ cargo install cargo-llvm-cov
$ cd rust
$ cargo llvm-cov
```

## Limitations

1. JUnit 4 is the Android ecosystem standard. JUnit 5 and the newer JUnit 6
require the third-party `android-junit-framework` plugin and careful version management.
The AndroidX Test libraries, Espresso, and Compose testing are all built on JUnit 4 rules and runners.

2. Robolectric cannot load shared libraries compiled for Android target architectures.
Tests that trigger `System.loadLibrary` for an Android-targeted `.so` file
will fail with `UnsatisfiedLinkError` in the Robolectric environment.
JNI boundary tests require either a host-compiled library or instrumented tests on a device.

3. No widely adopted solution exists for mocking `JNIEnv` in Rust unit tests.
The `JNIEnv` type is a raw pointer to a C struct with a complex vtable
that is impractical to construct outside of a running JVM.
Architectural separation of pure logic from the JNI bridge is the practical testing pattern.

4. Native test binaries compiled with GoogleTest or Catch2 must be pushed to a device via `adb`
and run through `adb shell`.
No built-in Android Gradle Plugin task exists for executing native test binaries.
CTest integration with the NDK CMake toolchain is not well-supported.

5. Cross-compiled `cargo test` binaries targeting Android architectures cannot run on the host machine.
They are ARM or x86 Android ELF executables that require a device, emulator, or QEMU to execute.
Use `cargo test` on the host target for pure logic testing only.

6. JaCoCo analyzes JVM bytecode and has limited accuracy for Kotlin-specific constructs.
Inline functions are inlined at the call site and may not be reported accurately.
JetBrains Kover is a Kotlin-native alternative that handles these cases.

7. Instrumented tests require a connected device or running emulator,
adding infrastructure complexity to continuous integration pipelines.
Services such as Firebase Test Lab provide cloud-based device farms
for teams that cannot maintain local device infrastructure.

## Conclusion

The Android testing pyramid provides a structured approach to test coverage.
Local unit tests on the host JVM form the base of the pyramid
and should cover the majority of business logic.
Robolectric tests extend local testing to code that depends on the Android framework.
Instrumented tests at the top of the pyramid verify end-to-end behavior on real hardware.

For applications that include native code,
the architectural separation of pure logic from the JNI bridge is the most effective testing strategy.
Pure Rust logic is tested with `cargo test` on the host machine.
The JNI boundary is tested through instrumented tests on a device.
This layered approach maximizes test coverage while minimizing device dependency.

## Future Reading

Areas for further exploration include
Jetpack Compose UI testing with `ComposeTestRule` and semantic matchers,
property-based testing with Kotest for exhaustive input space coverage,
JUnit 5 migration using the `android-junit-framework` plugin,
and continuous integration with Firebase Test Lab for automated device testing.

## References

- [Android, Build Instrumented Tests][android_instrumented_tests]
- [Android, Build Local Unit Tests][android_local_tests]
- [Android, NDK CMake Guide][android_ndk_cmake]
- [Android, Test from the Command Line][android_test_cli]
- [Reference, GoogleTest][ref_googletest]
- [Reference, JUnit 4][ref_junit4]
- [Reference, MockK][ref_mockk]
- [Reference, Robolectric][ref_robolectric]
- [Related Post, Android Development on FreeBSD][related_post_android_freebsd]
- [Related Post, Concentrated Liquidity Market Maker Mathematics][related_post_clmm]
- [Rust, cargo-ndk][rust_cargo_ndk]
- [Rust, jni][rust_jni]

[android_instrumented_tests]: https://developer.android.com/training/testing/instrumented-tests
[android_local_tests]: https://developer.android.com/training/testing/local-tests
[android_ndk_cmake]: https://developer.android.com/ndk/guides/cmake
[android_test_cli]: https://developer.android.com/studio/test/command-line
[ref_googletest]: https://github.com/google/googletest
[ref_junit4]: https://junit.org/junit4/
[ref_mockk]: https://mockk.io/
[ref_robolectric]: https://robolectric.org/
[related_post_android_freebsd]: {% post_url 2026-02-23-android_development_on_freebsd %}
[related_post_clmm]: {% post_url 2026-02-22-clmm_mathematics %}
[rust_cargo_ndk]: https://crates.io/crates/cargo-ndk
[rust_jni]: https://crates.io/crates/jni
