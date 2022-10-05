---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Rust on Playdate"
date:   2022-10-04 18:23:42 +0000
categories: gamedev playdate rust
---
The [Panic Playdate][playdate] is a tiny, just for fun indie game console.
[Rust][rust] is a drop-in replacement for C that is fast and memory safe.
This post will discuss getting started with the Panic Playdate using Rust.
It is a followup to my post on
[getting started with Playdate][playdate-getting-started].

[crank][crank] and [crankstart][crankstart] will be used because they are
working, existing solutions for using Rust to develop applications for the
Playdate.
The post will cover installation, running examples, as well as building and
running a couple of existing crankstart projects:
[Klondike solitaire][crankstart-klondike],
and [Nine Lives][crankstart-ninelives].

Familiarity with Rust and the command line are assumed.
It is also assumed that the [Playdate SDK][playdate_sdk_latest] has already
been installed from the [Playdate Developer Page][playdate_dev], and that Rust
has been installed with [rustup][rustup].

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-04 18:23:42 +0000
$ uname -vm
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 12.6
$ echo "${SHELL}"
/bin/bash
$ "${SHELL}" --version
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin21)
Copyright (C) 2007 Free Software Foundation, Inc.
$ cat "${HOME}/Developer/PlaydateSDK/VERSION.txt"
1.12.3
$ cargo --version
cargo 1.66.0-nightly (f5fed93ba 2022-09-27)
{% endhighlight %}

## Instructions

#### Installation

First, install [crank][crank] according to the README.

{% highlight sh %}
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
git clone git@github.com:pd-rs/crank.git
cd crank
cargo install --path . --force
{% endhighlight %}

Next, clone the [crankstart][crankstart] repository to run the examples.

{% highlight sh %}
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
git clone git@github.com:pd-rs/crankstart.git
{% endhighlight %}

#### Running Examples

The hello_world and life examples can simply be run.

{% highlight sh %}
PROJECT="crankstart"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
EXAMPLE="hello_world"
crank run --release --example "${EXAMPLE}"
EXAMPLE="life"
crank run --release --example "${EXAMPLE}"
{% endhighlight %}

Assets from the C_API need to be copied in before running the sprite_game
example.

{% highlight sh %}
cp -a "${PLAYDATE_SDK_PATH}/C_API/Examples/Sprite Game/Source/images/." sprite_game_images
EXAMPLE="sprite_game"
crank run --release --example "${EXAMPLE}"
{% endhighlight %}

#### Klondike Solitaire

The author of crank and crankstart wrote a
[Klondike solitaire][crankstart-klondike] game in Rust.
Use the following commands to build and run it.

{% highlight sh %}
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
git clone git@github.com:pd-rs/crankstart-klondike.git
cd crankstart-klondike
crank run --release
{% endhighlight %}

#### Nine Lives

A third party, bravely, wrote the
[Nine Lives][crankstart-ninelives] game in Rust.
It can be built and run as follows.

{% highlight sh %}
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
git clone git@github.com:bravely/nine_lives.git
cd nine_lives
crank run --release
{% endhighlight %}

#### Running on Hardware

[cargo-xbuild][rust_cargo_xbuild] is required to build for hardware.

{% highlight sh %}
cargo install cargo-xbuild
{% endhighlight %}

xbuild requires source to be installed, so it needs to be installed with
[rustup][rustup].

{% highlight sh %}
rustup component add rust-src
{% endhighlight %}

The build subcommand takes a --device flag that can be used to target hardware
exclusively.
Alternatively, the package subcommand can be used to build binaries for both
the device and simulator.
To upload a PDX file to hardware, first run it in the simulator.
Then either "Upload Game to Device" from the "Device" menu or Playdate icon on
the lower lefthand corner of the simulator (with the crank controls collapsed).
Once the game is on the device, pdutil can be used to launch it.

{% highlight sh %}
# example (build)
EXAMPLE="life"
PDX_FILE="Life"
PROJECT="crankstart"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
crank build --device --release --example "${EXAMPLE}"
playdate_simulator "target/${PDX_FILE}.pdx"
# from simulator: "Device > Upload Game to Device
# once game is on devce
pdutil /dev/cu.usbmodemPD* run "/Games/${PDX_FILE}.pdx"

# example (package)
EXAMPLE="hello_world"
PDX_FILE="Hello World"
crank package --example "${EXAMPLE}"
playdate_simulator "target/${PDX_FILE}.pdx"
# from simulator: "Device > Upload Game to Device
# once game is on devce
pdutil /dev/cu.usbmodemPD* run "/Games/${PDX_FILE}.pdx"

# project (build)
PROJECT="crankstart-klondike"
PDX_FILE="Klondike"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
crank build --device --release
playdate_simulator "target/${PDX_FILE}.pdx"
# from simulator: "Device" > "Upload Game to Device"
# once game is on devce
pdutil /dev/cu.usbmodemPD* run "/Games/${PDX_FILE}.pdx"

# project (package)
PROJECT="nine_lives"
PDX_FILE="Nine Lives"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
crank package
playdate_simulator "target/${PDX_FILE}.pdx"
# from simulator: "Device" > "Upload Game to Device"
# once game is on devce
pdutil /dev/cu.usbmodemPD* run "/Games/${PDX_FILE}.pdx"
{% endhighlight %}

The run subcommand should work like the build subcommand, but it is not working
on the author's machice in the latest version of the SDK.  The latest version
of the SDK also seems to have trouble booting PDX files with spaces in the
filename using the simulator and pdutil, but the game can be launched on the
device after it has been uploaded.

{% highlight sh %}
# example
EXAMPLE="sprite_game"
PROJECT="crankstart"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
crank run --device --release --example "${EXAMPLE}"

# project
PROJECT="nine_lives"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}/${PROJECT}"
crank run --device --release
{% endhighlight %}

#### More Information

Note that the Playdate [C API documentation][playdate_c_api_docs] (and to a
lesser extent, the [Lua documentation][playdate_lua_docs]) are useful when
developing applications in Rust.
This post is based on the [Rust development thread][playdate_dev_forum_rust]
from the [Playdate Developer Forum][playdate_dev_forum].

## References:

- [crank, cargo wrapper for building and running Playdate software][crank]
- [crankstart, Klondike Solitaire][crankstart-klondike]
- [crankstart, Rust crate for Playdate application development][crankstart]
- [crankstart, Nine Lives][crankstart-ninelives]
- [Playdate C API Documentation][playdate_c_api_docs]
- [Playdate Developer Forum][playdate_dev_forum]
- [Playdate Developer Forum, Rust Development Thread][playdate_dev_forum_rust]
- [Playdate Developer Page][playdate_dev]
- [Playdate Homepage][playdate]
- [Playdate Lua Documentation][playdate_lua_docs]
- [Playdate, Getting Started with][playdate-getting-started]
- [Playdate SDK, Latest][playdate_sdk_latest]
- [Rust Homepage][rust]
- [Rust, rustup][rustup]
- [Rust, cargo-xbuild][rust_cargo_xbuild]

[crank]: https://github.com/pd-rs/crank
[crankstart]: https://github.com/pd-rs/crankstart
[crankstart-klondike]: https://github.com/pd-rs/crankstart-klondike
[crankstart-ninelives]: https://github.com/bravely/nine_lives
[playdate]: https://play.date/
[playdate_c_api_docs]: https://sdk.play.date/inside-playdate-with-c
[playdate_dev]: https://play.date/dev/
[playdate_dev_forum]: https://devforum.play.date
[playdate_dev_forum_rust]: https://devforum.play.date/t/rust-development-thread/3999
[playdate-getting-started]: /gamedev/playdate/c/c++/lua/2022/10/03/getting-started-with-playdate.html
[playdate_lua_docs]: https://sdk.play.date/Inside%20Playdate.html
[playdate_sdk_latest]: https://download.panic.com/playdate_sdk/PlaydateSDK-latest.zip
[rust]: https://www.rust-lang.org
[rustup]: https://rustup.rs
[rust_cargo_xbuild]: https://docs.rs/crate/cargo-xbuild/latest

