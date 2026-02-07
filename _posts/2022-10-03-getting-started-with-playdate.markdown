---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Playdate"
date:   2022-10-03 20:21:04 +0000
categories: gamedev playdate c c++ lua
---

<!-- A55 -->

The [Panic Playdate][playdate] is a tiny, just-for-fun indie game console.
This post will discuss getting started with the Panic Playdate.
It will cover downloading the [SDK][playdate_sdk_latest], installing it,
and running the examples.
macOS will be used, but the steps should be largely the same for other
platforms.
This post assumes familiarity with the command line.

Note that command line familiarity is not needed for Playdate development.
Downloading the SDK is enough to get started if Pulp is sufficient for your
needs.
For most developers, [Lua][lua] knowledge and a Playdate-integrated editor,
like [Nova][nova] (link to [Playdate Extensions][nova_playdate]), will be
enough to make their Playdate development dreams come true.
(Dedication to see a project to completion is also required.)

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-03 20:21:04 +0000
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
{% endhighlight %}

## Instructions

#### Installation

First, download the [latest Playdate SDK][playdate_sdk_latest]
(link to [all versions][playdate_sdk_all]) from the
[Playdate Developer Page][playdate_dev].
Update the path, set the SDK path, and consider adding an alias for the
Playdate simulator.

{% highlight sh %}
# update path
echo 'export PATH="${HOME}/Developer/PlaydateSDK/bin:${PATH}"' >> "${HOME}/.profile"

# set the Playdate SDK path
echo 'export PLAYDATE_SDK_PATH="${HOME}/Developer/PlaydateSDK"' >> "${HOME}/.bash_profile"

# add alias for simulator
echo 'alias playdate_simulator="open ${HOME}/Developer/PlaydateSDK/bin/Playdate\ Simulator.app"' >> "${HOME}/.bash_profile"

# reload profiles, if necessary
. "${HOME}/.profile"
. "${HOME}/.bash_profile"
{% endhighlight %}

#### Pulp

[Pulp][playdate_pulp] is a web-based game editor for the Playdate.
The target audience is entry-level game developers and people who want to
rapidly prototype.
All development and testing can be done in the browser.
Pulp has a lot of limitations, but it is also
[easy to learn][playdate_pulp_tutorials]!
(Links to documentation for [Pulp][playdate_pulp_docs] and
[PulpScript][playdate_pulpscript_docs].)
Pulp is a good choice for people who are not ready to learn to program.

Entire games can be exported and imported in JSON format.
To run a game developed with Pulp in the simulator, click the "DOWNLOAD PDX"
button, and then pass the PDX file to the simulator.

{% highlight sh %}
GAME="my-game"
GAME_PATH="${HOME}/Downloads"
playdate_simulator "${GAME_PATH}/${GAME}.pdx"
{% endhighlight %}

#### Lua Examples

The [Lua][lua] scripting language can also be used to develop Playdate games.
The target audience is moderately sophisticated developers.
Lua is a popular scripting language commonly used in game development,
and the Lua API is not as restricted as Pulp's web-based development model.
(Link to [Lua documentation][playdate_lua_docs].)
Lua is generally the best choice for projects with a programmer.

Regular project-based Lua examples can be run as follows.

{% highlight sh %}
# cd to location of examples directory
cd "${HOME}/Developer/PlaydateSDK/Examples/"

# run the "2020" exmaple
EXAMPLE="2020"
pdc "${EXAMPLE}/Source" "${EXAMPLE}.pdx"
playdate_simulator "${EXAMPLE}".pdx

# cleanup file when no longer needed
rm -rf "${EXAMPLE}.pdx"
{% endhighlight %}

Single file Lua examples can be run as follows.

{% highlight sh %}
# cd to location of examples directory
cd "${HOME}/Developer/PlaydateSDK/Examples/"

# run the "animator" exmaple
EXAMPLE="animator"
pdc -m "Single File Examples/${EXAMPLE}.lua" "${EXAMPLE}.pdx"
playdate_simulator "${EXAMPLE}.pdx"

# cleanup file when no longer needed
rm -rf "${EXAMPLE}.pdx"
{% endhighlight %}

#### C API Examples

Sophisticated developers can use the C API to make software for the Playdate.
Many professional AAA game developers use C++, but C is the language they used
in the past.
(Link to [C API documentation][playdate_c_api_docs].)
Only use the C API if you know why you need to use it.

The C API examples can be run as follows.

{% highlight sh %}
# cd to location of examples directory
cd "${HOME}/Developer/PlaydateSDK/C_API/Examples/"

# run the "3D library" exmaple
EXAMPLE="3D library"
(cd "./${EXAMPLE}"; make; playdate_simulator *.pdx)

# cleanup file when no longer needed
(cd "./${EXAMPLE}"; make clean)
{% endhighlight %}

#### More Information

Consider visiting the [Playdate Developer Page][playdate_dev] and
[Playdate Developer Forums][playdate_dev_forum] for more information!

## References:

- [Lua Home Page][lua]
- [Nova Homepage][nova]
- [Nova, Playdate Extensions][nova_playdate]
- [Playdate C API Documentation][playdate_c_api_docs]
- [Playdate Developer Forum][playdate_dev_forum]
- [Playdate Developer Page][playdate_dev]
- [Playdate Homepage][playdate]
- [Playdate Lua Documentation][playdate_lua_docs]
- [Playdate Pulp][playdate_pulp]
- [Playdate Pulp Documentation][playdate_pulp_docs]
- [Playdate Pulp Tutorials][playdate_pulp_tutorials]
- [Playdate PulpScript Documentation][playdate_pulpscript_docs]
- [Playdate SDK, All Downloads][playdate_sdk_all]
- [Playdate SDK, Latest][playdate_sdk_latest]

[lua]: https://www.lua.org
[nova]: https://nova.app
[nova_playdate]: https://extensions.panic.com/extensions/com.panic/com.panic.Playdate/
[playdate]: https://play.date/
[playdate_c_api_docs]: https://sdk.play.date/inside-playdate-with-c
[playdate_dev]: https://play.date/dev/
[playdate_dev_forum]: https://devforum.play.date
[playdate_lua_docs]: https://sdk.play.date/Inside%20Playdate.html#developing-in-lua
[playdate_pulp]: https://play.date/pulp/
[playdate_pulp_docs]: https://play.date/pulp/docs/
[playdate_pulp_tutorials]: https://play.date/dev/links/#devLinksCategorySDKPulp
[playdate_pulpscript_docs]: https://play.date/pulp/docs/pulpscript/
[playdate_sdk_all]: https://download.panic.com/playdate_sdk/
[playdate_sdk_latest]: https://download.panic.com/playdate_sdk/PlaydateSDK-latest.zip

