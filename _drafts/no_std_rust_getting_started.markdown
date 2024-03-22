---
layout: post
mathjax: false
comments: true
title:  "Getting Started with no_std Rust Programming"
date:   2024-03-20 02:09:14 +0000
categories: rust no_std embedded
---

`no_std` [Rust][rust_homepage] programming involves developing applications
without relying on Rust's standard library (`std`). This constraint is typical
in embedded systems, where resources are limited or when direct control over
hardware is required. Why use `no_std` Rust?

- **Bare-Metal Requirement**: `std` assumes an operating system, and it has not
  been ported to many specialized systems.
- **Cross-Platform Compatibility**: Enables development for various architectures 
  and platforms without the overhead or assumptions of the standard library.
- **Resource Efficiency**: Operates in environments with limited memory and 
  storage.
- **Direct Hardware Control**: Allows developers to write software that directly 
  interacts with hardware.

This post introduces `no_std` Rust, providing the foundation you need
to start your journey in the world of embedded development with Rust. After that,
it covers how the `no_std` `core` and `alloc` functionality is exposed to `std`
Rust programs before giveing pointers to more in-depth information.

This post assumes a general familiarity with Rust, `rustup` and `cargo`.
Readers who are not familiar with Rust and the ecosystem tooling should consider
starting with "[The Rust Programming Language Book][rust_book_rust]".
([rustup][rust_book_rustup] and [cargo][rust_book_cargo] also have extensive
documentaiton.)

## Software Versions

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2024-03-20 02:09:14 +0000
$ uname -vm
Darwin Kernel Version 23.2.0: Wed Nov 15 21:53:18 PST 2023; root:xnu-10002.61.3~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 14.2.1
$ sysctl -n machdep.cpu.brand_string
Apple M1 Max
$ echo "${SHELL}"
/bin/bash
$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)
$ cargo --version
cargo 1.78.0-nightly (2fe739fcf 2024-03-15)
````

## Creating a no_std Rust Library

Start by creating a new Rust project using Cargo.

```sh
PROJECT="no_std_example"
cargo new --lib "${PROJECT}"
cd "${PROJECT}"
```

In your `lib.rs`, declare the project as `no_std` and start coding.
In the following example, note that the
[ideal rocket equation][nasa_ideal_rocket_equation] includes a
natural logarithm, so `ln` needs to be pulled in from `libm`.
Neither the [specific impulse equation][nasa_rocket_specific_impulse]
nor the [rocket thrust equation][nasa_rocket_thrust] use anything beyond
arithmetic, so they do not require the dependency.

```rust
// src/lib.rs

#![no_std]

extern crate libm;

/// Standard gravity (m/s^2)
pub const G0: f32 = 9.80665;

/// Calculates the thrust given the mass flow rate of the propellant (m dot),
/// the exhaust velocity (Ve), the pressure at the nozzle exit (Pe),
/// the ambient pressure (P0), and the exit area of the nozzle (Ae).
///
/// # Arguments
///
/// * `m_dot` - Mass flow rate of the propellant (kg/s).
/// * `ve` - Exhaust velocity (m/s).
/// * `pe` - Pressure at the nozzle exit (Pa).
/// * `p0` - Ambient pressure (Pa).
/// * `ae` - Exit area of the nozzle (m^2).
///
/// # Returns
///
/// Thrust in Newtons.
pub fn calculate_thrust(m_dot: f32, ve: f32, pe: f32, p0: f32, ae: f32) -> f32 {
  m_dot * ve + (pe - p0) * ae
}

/// Calculates the specific impulse given the thrust and the mass flow rate.
///
/// # Arguments
///
/// * `thrust` - The thrust in Newtons (N).
/// * `m_dot` - The mass flow rate in kilograms per second (kg/s).
///
/// # Returns
///
/// * Specific impulse in seconds (s).
pub fn calculate_specific_impulse(thrust: f32, m_dot: f32) -> f32 {
  thrust / (m_dot * G0)
}

/// Calculates the delta-v of a rocket using the Tsiolkovsky rocket equation.
///
/// # Arguments
///
/// * `isp` - The specific impulse in seconds (s).
/// * `m0` - The initial total mass of the rocket (including propellant) in kilograms (kg).
/// * `mf` - The final mass of the rocket (without propellant) in kilograms (kg).
///
/// # Returns
///
/// * Delta-v in meters per second (m/s).
pub fn calculate_delta_v(isp: f32, m0: f32, mf: f32) -> f32 {
  isp * G0 * libm::logf(m0 / mf)
}

#[cfg(test)]
mod tests {
    use super::*;
    use libm::expf;

    const ACCEPTABLE_ERROR: f32 = 1e-3;

    #[test]
    fn test_calculate_thrust() {
        let m_dot = 5.0; // Mass flow rate (kg/s)
        let ve = 2500.0; // Exhaust velocity (m/s)
        let pe = 101325.0; // Pressure at nozzle exit (Pa) - Atmospheric pressure
        let p0 = 101325.0; // Ambient pressure (Pa) - Atmospheric pressure
        let ae = 0.1; // Exit area of the nozzle (m^2)
        let expected_thrust = 12500.0; // Expected thrust (N)

        let thrust = calculate_thrust(m_dot, ve, pe, p0, ae);
        // Ensure the calculated thrust is as expected
        assert!( (thrust - expected_thrust).abs() < ACCEPTABLE_ERROR);
    }

    #[test]
    fn test_calculate_specific_impulse() {
        let thrust = 12500.0; // Thrust (N)
        let m_dot = 5.0; // Mass flow rate (kg/s)
        let expected_isp = 254.929; // Expected specific impulse (s)

        let isp = calculate_specific_impulse(thrust, m_dot);
        // Ensure the calculated thrust is as expected
        assert!( (isp - expected_isp).abs() < ACCEPTABLE_ERROR);
    }

    #[test]
    fn test_calculate_delta_v() {
        let isp = 254.6479; // Specific impulse (s)
        let m0 = 1000.0; // Initial mass of the rocket (kg)
        let mf = 100.0; // Final mass of the rocket (kg)
        let expected_delta_v = 5750.114; // Expected delta-v (m/s)

        let delta_v = calculate_delta_v(isp, m0, mf);
        // Ensure the calculated delta-v is as expected
        assert!( (delta_v - expected_delta_v).abs() < ACCEPTABLE_ERROR);
    }
}
```

Modify your `Cargo.toml` to pull in the `libm` dependency.

```toml
# Cargo.toml

[package]
name = "no_std_example"
version = "0.1.0"
edition = "2021"

[dependencies]
libm = "0.2.8"
```

Test the library.

```sh
$ cargo test
```

## Using the Library

`no_std` libraries simply fail to take advantage of anything in Rust `std`.
Binaries, on the otherhand, have more requiremets, someone of which are
transparently handled when `std` assumptions hold true. We will need to
define an `eh_personality` for error handling, and but this can only be
done with the nightly toolchain. Therefore, we need to install the nightly
toolchain for the host system and switch to it.

```sh
$ rustup toolchain install nightly
$ rustup default nightly
```

Note that the following command can be used to switch back to stable,
but do not run it now.

```sh
$ rustup default stable
```

Next, add a **src/main.rs** file that uses the library.

```rust
// src/main.rs

#![no_std]
#![no_main]
#![allow(internal_features)]
#![feature(lang_items)]

extern crate libc_print;
use core::panic::PanicInfo;

extern crate no_std_example; // Library name

#[no_mangle]
pub extern "C" fn main() {
    // Example values for thrust calculation
    let m_dot = 5.0; // Mass flow rate in kg/s
    let ve = 2500.0; // Exhaust velocity in m/s
    let pe = 101325.0; // Pressure at nozzle exit in Pa
    let p0 = 101325.0; // Ambient pressure in Pa
    let ae = 0.1; // Exit area of the nozzle in m^2

    // Calculating thrust
    let thrust = no_std_example::calculate_thrust(m_dot, ve, pe, p0, ae);
    libc_print::libc_println!("Thrust: {} N", thrust);

    // Calculating specific impulse
    let isp = no_std_example::calculate_specific_impulse(thrust, m_dot);
    libc_print::libc_println!("Specific Impulse: {} s", isp);

    // Example values for delta-v calculation
    let m0 = 1000.0; // Initial total mass in kg
    let mf = 100.0; // Final mass in kg

    // Calculating delta-v
    let delta_v = no_std_example::calculate_delta_v(isp, m0, mf);
    libc_print::libc_println!("Delta-v: {} m/s", delta_v);
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

// Empty personality function for no_std compatibility.
#[lang = "eh_personality"]
extern "C" fn eh_personality() {}
```

We are using `libc_print` for output in the above binary, so add it as a
dependency in **Cargo.toml**.

```toml
# Cargo.toml, partial listing
[dependencies]
libc-print = "0.1.22"
```

Generally speaking, `libc` can used in conjunction with `no_std` code to
test its functionality on the development host machine. Note that `libc`
is not always available on development targets. Some systems have a
proprietary library that implements key functionality generally found in
`libc`, while others have a quirky proprietary `libc`. In these cases,
it is safe to assume that `libc` related crates cannot be used.


## Debugging and Testing

(Debugging a `no_std` project can be challenging; provide tips or tools that 
might help, such as using hardware debuggers or emulators.)

## Advancing Your `no_std` Skills

- **Exploring Embedded HAL**: Discover the Hardware Abstraction Layer (HAL) for 
  embedded systems programming.
- **Interfacing with Hardware**: Learn how to read sensors and control 
  actuators directly from Rust code.
- **Real-World Projects**: Start with simple projects like blinking an LED and 
  progressively tackle more complex applications.

## Conclusion

`no_std` Rust programming opens up a new realm of possibilities for Rust 
developers in the embedded world. By understanding the basics and progressively 
exploring more complex scenarios, you can leverage Rust's safety and 
performance on platforms where the standard library is not an option.

## References

- [NASA, Ideal Rocket Equation][nasa_ideal_rocket_equation]
- [NASA, Rocket Specific Impulse Equation][nasa_rocket_specific_impulse]
- [NASA, Rocket Thrust Equation][nasa_rocket_thrust]
- [Rust, Home Page][rust_homepage]
- [Rust, The Cargo Book][rust_book_cargo]
- [Rust, The Embedonomicon][rust_book_embedonomicon]
- [Rust, The Rust Embedded Book][rust_book_embedded]
- [Rust, The Rust Programming Language][rust_book_rust]
- [Rust, The rustup Book][rust_book_rustup]

[nasa_ideal_rocket_equation]: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/ideal-rocket-equation/
[nasa_rocket_specific_impulse]: https://www.grc.nasa.gov/www/k-12/airplane/specimp.html
[nasa_rocket_thrust]: https://www.grc.nasa.gov/www/k-12/airplane/rockth.html
[rust_homepage]: https://www.rust-lang.org
[rust_book_cargo]: https://doc.rust-lang.org/cargo/
[rust_book_embedded]: https://docs.rust-embedded.org/book/
[rust_book_embedonomicon]: https://docs.rust-embedded.org/embedonomicon/
[rust_book_rust]: https://doc.rust-lang.org/book/
[rust_book_rustup]: https://rust-lang.github.io/rustup/

