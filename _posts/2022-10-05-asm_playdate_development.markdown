---
layout: post
mathjax: false
comments: true
title:  "ASM Playdate Development"
date:   2022-10-05 19:28:00 +0000
categories: gamedev playdate asm arm x86
---
The [Panic Playdate][playdate] is a tiny, just for fun indie game console.
This post will discuss getting started with ASM on the Panic Playdate.
The Playdate's CPU is a Cortex M7 that *only* supports Thumb instructions.
The simulator uses the instruction set of the development machine.
The author has tested ASM in versions of the simulator that run on both
X86_64 and Apple Silicon.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-05 19:28:00 +0000
$ uname -vm
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 12.6
$ sysctl -n machdep.cpu.brand_string
Apple M1 Max
$ echo "${SHELL}"
/bin/bash
$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin21)
$ cat "${HOME}/Developer/PlaydateSDK/VERSION.txt"
1.12.3
$ cargo --version
cargo 1.66.0-nightly (f5fed93ba 2022-09-27)
{% endhighlight %}

## Instructions

#### Project Template

When ASM is hand written at all, it is generally used for optimizing native
code.
Therefore, the Hello World C API example will make a reasonable
project template.

{% highlight sh %}
# copy in project template
PROJECT="asm_test"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
cp -r "${PLAYDATE_SDK_PATH}/C_API/Examples/Hello World/" "${PROJECT}"
cd "${PROJECT}"
{% endhighlight %}

Replace the contents of **main.c** with the following.
This program calculates the distance of a diagonal line according to
the Pythagorean theorem.
The bulk of the code is C, but the square root will be calculated in ASM.
Note that the The d-pad, buttons, and crank can be used to control the
distance in different ways.

**src/main.c**
{% highlight c %}
#include "fast_sqrt.h"
#include "main.h"
#include "pd_api.h"

const char* fontpath = "/System/Fonts/Asheville-Sans-14-Bold.pft";
const LCDPattern gray50 = {
  // Bitmap
  0b10101010,
  0b01010101,
  0b10101010,
  0b01010101,
  0b10101010,
  0b01010101,
  0b10101010,
  0b01010101,

  // Mask
  0b11111111,
  0b11111111,
  0b11111111,
  0b11111111,
  0b11111111,
  0b11111111,
  0b11111111,
  0b11111111,
};

void initProgramState(struct ProgramState *ps, PlaydateAPI *pd)
{
  const char *errorMessage;

  ps->pd = pd;
  ps->font = NULL;
  ps->font = pd->graphics->loadFont(fontpath, &errorMessage);
  if (NULL == ps->font) {
    pd->system->error("%s:%i Couldn't load font %s: %s",
      __FILE__, __LINE__, fontpath, errorMessage
    );
  }
  ps->previousInput = 0;
  ps->strokeWidth = 2;
  ps->x = (LCD_COLUMNS - TEXT_WIDTH) / 2;
  ps->y = (LCD_ROWS - TEXT_HEIGHT) / 2;
  ps->dx = 1;
  ps->dy = 1;
}

#ifdef _WINDLL
__declspec(dllexport)
#endif
int eventHandler(PlaydateAPI* pd, PDSystemEvent event, uint32_t arg)
{
  (void)arg; // only used for kEventKeyPressed == event
  static struct ProgramState *ps = NULL;

  switch (event) {
    case kEventInit:
      ps = pd->system->realloc(ps, sizeof(struct ProgramState));
      initProgramState(ps, pd);
      pd->system->setUpdateCallback(update, (void *)ps);
      break;
    case kEventTerminate:
      pd->system->realloc(ps, 0);
      ps = NULL;
      break;
    default:
      // do nothing
    break;
  };

  return 0;
}

static int update(void* userdata)
{
  struct ProgramState *ps = (struct ProgramState *)userdata;
  handleInput(ps);
  draw(ps);
  return 1;
}

void handleInput(struct ProgramState *ps) {
  PlaydateAPI* pd = ps->pd;

  int x_direction = 0;
  int y_direction = 0;

  // dpad input
  PDButtons currentInput;
  pd->system->getButtonState(&currentInput, NULL, NULL);
  if ( currentInput & kButtonUp ) {
    ps->y--;
  } else if ( currentInput & kButtonDown ) {
    ps->y++;
  } else {
    y_direction = 1;
  }
  if ( currentInput & kButtonLeft ) {
    ps->x--;
  } else if ( currentInput & kButtonRight ) {
    ps->x++;
  } else {
    x_direction = 1;
  }
  if (( currentInput & kButtonA ) && !( ps->previousInput & kButtonA )) {
    ps->dx *= -1;
  }
  if (( currentInput & kButtonB ) && !( ps->previousInput & kButtonB )) {
    ps->dy *= -1;
  }
  ps->previousInput = currentInput;

  int steps;

  if (pd->system->isCrankDocked()) {
    steps = 1;
  } else {
    steps = pd->system->getCrankChange();
    if (steps < 0) {
      steps = -steps;
      x_direction = -1;
      y_direction = -1;
    }
  }

  for (int i = 0; i < steps; i++) {
    ps->x += ps->dx * x_direction;
    ps->y += ps->dy * y_direction;

    // bounce
    if ( ps->x < 0 || LCD_COLUMNS < ps->x ) {
      ps->dx *= -1;
    }
    if ( ps->y < 0 || LCD_ROWS < ps->y ) {
      ps->dy *= -1;
    }
  }
}

int adjustTextPosition(int x, int w, int min, int max) {
  if (x < min) {
    return min;
  } else if (max < x + w) {
    return max - w;
  } // else
  return x;
}

void keepTextOnScreen(int *x_ptr, int *y_ptr, int x, int y) {
  *x_ptr = adjustTextPosition(x, TEXT_WIDTH, 0, LCD_COLUMNS);
  *y_ptr = adjustTextPosition(y, TEXT_HEIGHT, 0, LCD_ROWS);
}

void drawOutlinedText(
  PlaydateAPI* pd,
  const char *message,
  int x,
  int y,
  int outlineWidth,
  LCDColor textColor,
  LCDColor outlineColor
) {
  pd->graphics->setDrawMode(outlineColor);
  pd->graphics->drawText(
    message, strlen(message), kASCIIEncoding, x - outlineWidth, y
  );
  pd->graphics->drawText(
    message, strlen(message), kASCIIEncoding, x + outlineWidth, y
  );
  pd->graphics->drawText(
    message, strlen(message), kASCIIEncoding, x, y - outlineWidth
  );
  pd->graphics->drawText(
    message, strlen(message), kASCIIEncoding, x, y + outlineWidth
  );
  pd->graphics->setDrawMode(textColor);
  pd->graphics->drawText(message, strlen(message), kASCIIEncoding, x, y);
}

void draw(struct ProgramState *ps)
{
  PlaydateAPI* pd = ps->pd;
  int stroke = ps->strokeWidth;;
  int x = ps->x;
  int y = ps->y;

  char *message = NULL;
  int text_x, text_y;

  pd->graphics->clear((LCDColor)gray50);
  pd->graphics->setFont(ps->font);

  // distance visual
  pd->graphics->fillRect(stroke, stroke, x-2*stroke, y-2*stroke, kColorBlack);
  pd->graphics->drawLine(0, 0, x, y, stroke, kColorWhite);
  pd->graphics->drawLine(x, 0, x, y, stroke, kColorBlack);
  pd->graphics->drawLine(0, y, x, y, stroke, kColorBlack);

  // distance message
  pd->system->formatString(&message, "d=%.3f", fast_sqrt(x*x + y*y));
  keepTextOnScreen(
    &text_x, &text_y, (x - TEXT_WIDTH) / 2, (y - TEXT_HEIGHT) / 2
  );
  drawOutlinedText(
    pd, message, text_x, text_y, stroke, kDrawModeInverted, kDrawModeCopy
  );

  // position message
  pd->system->formatString(&message, "(%d, %d)", x, y);
  keepTextOnScreen(&text_x, &text_y, x, y);
  drawOutlinedText(
    pd, message, text_x, text_y, stroke, kDrawModeCopy, kDrawModeInverted
  );

  // FPS display
  pd->system->drawFPS(0,0);

  // cleanup
  pd->system->realloc(message, 0);
}
{% endhighlight %}

Add **main.h**.

**src/main.h**
{% highlight c %}
#ifndef MAIN_H
#define MAIN_H

#include "pd_api.h"

#define TEXT_WIDTH 86
#define TEXT_HEIGHT 16
extern const char* fontpath;
extern const LCDPattern gray50;

struct ProgramState {
  PlaydateAPI *pd;
  LCDFont *font;
  PDButtons previousInput;
  int strokeWidth;
  int x;
  int y;
  int dx;
  int dy;
};

void initProgramState(struct ProgramState *ps, PlaydateAPI *pd);
#ifdef _WINDLL
__declspec(dllexport)
#endif
int eventHandler(PlaydateAPI* pd, PDSystemEvent event, uint32_t arg);
static int update(void* userdata);
void handleInput(struct ProgramState *ps);
void draw(struct ProgramState *ps);

#endif // MAIN_H
{% endhighlight %}

Add the **fast_sqrt.h** header file for the ASM code.

**src/fast_sqrt.h**
{% highlight c %}
#ifndef FAST_SQRT_H
#define FAST_SQRT_H

extern float fast_sqrt(float);

#endif  // FAST_SQRT_H
{% endhighlight %}

Add a stub **fast_sqrt.c** implementation.

{% highlight c %}
#include "fast_sqrt.h"

float fast_sqrt(float x) {
  // non-functional stub
  return 0.0;
}
{% endhighlight %}

Change the **PRODUCT** and **SRC** lines in the **Makefile**.

{% highlight make %}
PRODUCT = ASMTest.pdx
SRC = src/main.c src/fast_sqrt.c
{% endhighlight %}

Update **pdxinfo**.

**Source/pdxinfo**
{% highlight sh %}
name=ASMTest
author=Brendan Sechter
description=ASM on Playdate proof of concept.
bundleID=com.sennue.poc_asmtest
imagePath=
{% endhighlight %}

Finally, build and run the project to make sure it works.

{% highlight sh %}
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
make
playdate_simulator "${PRODUCT}"
{% endhighlight %}

The distance of the diagonal line should be a fixed value of 0.0.
The goal is to calculate that value with ASM.

#### ASM Square Root Implementations

On modern CPU's, calculating the square root of a number can be done with
a single instruction.
The Cortex M7 uses the ARMv7E-M microarchitecture.
It only supports Thumb instructions.
ARM-Thumb interworking is not possible on the Playdate.

The Thumb ASM for a square root subroutine that will run on hardware follows.

**src/fast_sqrt_armv7.s**
{% highlight nasm %}
        .syntax unified
        .set ALIGNMENT, 4

.text
        .align ALIGNMENT
        .global fast_sqrt
fast_sqrt:
        vsqrt.f32  s0, s0
        bx         lr
{% endhighlight %}

The MacBook Pro this post is being typed up on runs on an Apple M1 Max.
It uses the ARMv8.5-A instruction set.
The Apple Silicon cores only support 64-bit ARM instructions.
Thumb is a thing of the past, and 32-bit ARM instructions are not supported
either.

The ARMv8 ASM for a square root subroutine that will run on the simulator
follows.

**src/fast_sqrt_armv8.s**
{% highlight nasm %}
        .set ALIGNMENT, 8

.text
        .align ALIGNMENT
        .global _fast_sqrt
_fast_sqrt:
        fsqrt   s0, s0
        ret
{% endhighlight %}

The author first experimented with ASM on Playdate using a machine that runs
x86-64 instructions.
This is the ASM for a simulator subroutine that run on a 64-bit Intel processor.

**src/fast_sqrt_x86_64.s**
{% highlight nasm %}
        .intel_syntax
        .set ALIGNMENT, 16

.text
        .global _fast_sqrt
_fast_sqrt:
        sqrtss xmm0, xmm0
        ret
{% endhighlight %}

#### Makefile Modifications

The Playdate Makefiles look like they were written with ASM, but a few
modifications need to be made to properly build the project.
First, the ASM for the device and simulator need to be listed separately.
Update **SRC** and add **ASRC** definitions in the **Makefile**.
Uncomment the **ASRC_SIMULATOR** definition for your development platform.
Also update the last line of the **Makefile** for the next step.

**Makefile**
{% highlight make %}
# List C source files here
SRC = src/main.c

# List ASM source files here
# Uncomment the ASRC_SIMULATOR definition for your development platform.
ASRC_DEVICE = src/fast_sqrt_armv7.s
#ASRC_SIMULATOR = src/fast_sqrt_armv8.s
#ASRC_SIMULATOR = src/fast_sqrt_x86_64.s

# last line of Makefile
include common.mk
{% endhighlight %}

Playdate Makefiles rely on some common machinery that does not entirely
support ASM code.
The **${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk** file could be
modified directly, but it is better to keep the modified copy in the project.
Copy **common.mk** into the project.

{% highlight sh %}
cp "${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk" common.mk
{% endhighlight %}

Three modification need to made to the local **common.mk**.
**ASRC_DEVICE** needs to be appended to **_OBJS**, and **ASRC_SIMULATOR**
needs to be appeded to the **$(OBJDIR)/pdex.${DYLIB_EXT}** target.
Finally, the **pdc** target needs to rely on **device** so that a functional
copy of **pdex.bin** is always included in the "fat" PDX file.
(Hardware runs **pdex.bin** while the simulator uses a dynamic library,
**pdex.dylib** on macOS.)

The following **diff** gives a guide to the changes that need to me made to
**common.mk**.

{% highlight sh %}
$ diff "${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk" common.mk
84c84
< _OBJS	= $(SRC:.c=.o)
---
> _OBJS	= $(SRC:.c=.o) $(ASRC_DEVICE:.s=.o)
131c131
< pdc: simulator
---
> pdc: device simulator
154c154
< 	$(SIMCOMPILER) $(DYLIB_FLAGS) -lm -DTARGET_SIMULATOR=1 -DTARGET_EXTENSION=1 $(INCDIR) -o $(OBJDIR)/pdex.${DYLIB_EXT} $(SRC)
---
> 	$(SIMCOMPILER) $(DYLIB_FLAGS) -lm -DTARGET_SIMULATOR=1 -DTARGET_EXTENSION=1 $(INCDIR) -o $(OBJDIR)/pdex.${DYLIB_EXT} $(SRC) $(ASRC_SIMULATOR)
{% endhighlight %}

Rebuild the project.
If all goes well, the diagonal distance should be calculated and updated in
realtime.
The program will automatically resize the rectangle if the crank is docked.
Undock the crank for manual control and verification.

{% highlight sh %}
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
make
playdate_simulator "${PRODUCT}"
{% endhighlight %}

#### Running on Hardware

To upload a PDX file to hardware, first run it in the simulator.
Then either “Upload Game to Device” from the “Device” menu or Playdate icon on
the lower lefthand corner of the simulator (with the crank controls collapsed).
Once the game is on the device, **pdutil** can be used to launch it.

{% highlight sh %}
# after the game is on the device
pdutil "${PDUTIL_DEVICE}" run "/Games/${PRODUCT}"
{% endhighlight %}

Alternatively, **pdutil** can be used to directly upload the game to hardware
from the command line.

{% highlight sh %}
PDUTIL_DEVICE="$(ls /dev/cu.usbmodemPD* | head -n 1)"
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
DEVICE_PRODUCT_PATH="/Volumes/PLAYDATE/Games/${PRODUCT}"
make device
pdc Source "${PRODUCT}"
pdutil "${PDUTIL_DEVICE}" datadisk
# it may take time for the device to become available
cp -r "${PRODUCT}" "${DEVICE_PRODUCT_PATH}"
MOUNT_DEVICE="$(diskutil list | grep PLAYDATE | grep -oE '[^ ]+$')"
diskutil unmount "${MOUNT_DEVICE}"
# press "A" to get the Playdate out of datadisk mode
{% endhighlight %}

#### More Information

The [ARM Cortext-M7 Processor Technical Reference Manual][arm_cortex_m7] gives
detailed information on the processor used in the Playdate.  Instruction
references for [ARM+Thumb ASM][arm_thumb_card],
[64-bit ARM ASM][arm_armv8_card], and [X86+AMD64 ASM][x86_reference] may be
useful.

This post is based on the
"[Adding ASM .s file to a project][playdate_dev_forum_asm]" thread on the
[Playdate Developer Forums][playdate_dev_forum].

## References:

- [ARMv8 A64 Quick Reference][arm_armv8_card]
- [ARM Cortext-M7 Processor Technical Reference Manual][arm_cortex_m7]
- [ARM and Thumb-2 Instruction Set Quick Reference Card][arm_thumb_card]
- [Playdate Developer Forum][playdate_dev_forum]
- [Playdate Developer Forum, Adding ASM .s file to a project][playdate_dev_forum_asm]
- [Playdate Homepage][playdate]
- [X86 and AMD64 Instruction Reference][x86_reference]

[arm_cortex_m7]: https://developer.arm.com/documentation/ddi0489/f/introduction/about-the-cortex-m7-processor/features
[arm_thumb_card]: https://users.ece.utexas.edu/~valvano/Volume1/QuickReferenceCard.pdf
[arm_armv8_card]: https://courses.cs.washington.edu/courses/cse469/19wi/arm64.pdf
[playdate]: https://play.date/
[playdate_dev_forum]: https://devforum.play.date/
[playdate_dev_forum_asm]: https://devforum.play.date/t/adding-asm-s-file-to-a-project/3804/2
[x86_reference]: https://www.felixcloutier.com/x86/

