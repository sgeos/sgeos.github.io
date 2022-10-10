---
layout: post
mathjax: false
comments: true
title:  "Fortran Playdate Development"
date:   2022-10-10 21:55:03 +0000
categories: gamedev playdate fortran
---
[Fortran][fortran] is used for heavy number crunching in mathematical and
scientific computing.
This post will start by covering calling Fortran from C.
It will then discuss using Fortran on the [Panic Playdate][playdate],
both the simulator and hardware.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-10 21:55:03 +0000
$ uname -vm
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 12.6
$ echo "${SHELL}"
/bin/bash
$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin21)
$ cat "${HOME}/Developer/PlaydateSDK/VERSION.txt"
1.12.3
$ gfortran -v 2> >(tail -1)
gcc version 12.2.0 (MacPorts gcc12 12.2.0_0+stdlib_flag)
$ arm-none-eabi-gfortran -v 2> >(tail -1)
gcc version 11.3.1 20220712 (Arm GNU Toolchain 11.3.Rel1)
{% endhighlight %}

## Instructions

#### Calling Fortran from C

This section assumes that **gcc** and **gfortran** are installed.
First, create a new project.

{% highlight sh %}
PROJECT="c_fortran_interop_example"
mkdir "${PROJECT}"
cd "${PROJECT}"
{% endhighlight %}

Add **main.c**.

**main.c**
{% highlight c %}
#include <stdio.h>
#include <stdlib.h>
#include "fast_sqrt.h"

int main(int argc, char **argv) {
  for (int i=1; i<argc; i++) {
    double input = atof(argv[i]);
    double output = fast_sqrt(input);
    printf("The square root of %.3f is %.3f.\n", input, output);
  }
  return 0;
}
{% endhighlight %}

Add **fast_sqrt.h** for interoperation with C.

**fast_sqrt.h**
{% highlight c %}
#ifndef FAST_SQRT_H
#define FAST_SQRT_H

extern double fast_sqrt(double);

#endif  // FAST_SQRT_H
{% endhighlight %}

Add the Fortran implementation of **fast_sqrt()**.

**fast_sqrt.f90**
{% highlight fortran %}
function fast_sqrt( x ) result( y ) bind( C, name="fast_sqrt" )
  use iso_c_binding, only: c_double
  implicit none

  real(c_double), VALUE :: x
  real(c_double) :: y

  y = sqrt(x)
end function
{% endhighlight %}

Create a **Makefile** to capture simple logic for building and testing
the program.
The C and Fortran files are compiled into object files to combine into a binary.
The testing code calls the program with the numbers from zero to ten as
test parameters.

**Makefile**
{% highlight make %}
.PHONEY: all clean force run test

CFLAGS=-Wall
FC=gfortran
FCFLAGS=-Wall

TARGET=fast_sqrt
OBJS=main.o fast_sqrt.o

all: $(TARGET)

force: clean all

$(TARGET): $(OBJS)
	$(FC) $(CFLAGS) $^ -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.f90
	$(FC) $(FCFLAGS) -c $< -o $@

test: $(TARGET) run

run:
	for i in {0..10}; do ./$(TARGET) $$i; done

clean:
	rm -rf *.o $(TARGET)
{% endhighlight %}

Build and test the program.

{% highlight sh %}
$ make test
cc -Wall -c main.c -o main.o
The square root of 0.000 is 0.000.
The square root of 1.000 is 1.000.
The square root of 2.000 is 1.414.
The square root of 3.000 is 1.732.
The square root of 4.000 is 2.000.
The square root of 5.000 is 2.236.
The square root of 6.000 is 2.449.
The square root of 7.000 is 2.646.
The square root of 8.000 is 2.828.
The square root of 9.000 is 3.000.
The square root of 10.000 is 3.162.
{% endhighlight %}

#### Running Fortran on the Playdate Simulator

Calling Fortran from C on the Playdate simulator is much the same as in
the previous section.
The Playdate simulator runs on the development machine and uses the host
architecture.
Therefore, cross-compilation is not necessary.
The Hello World C API example is a reasonable project template, so make a copy.

{% highlight sh %}
PROJECT="fortran_test"
PROJECT_PATH="my_playdate_projects"
cd "${PROJECT_PATH}"
cp -r "${PLAYDATE_SDK_PATH}/C_API/Examples/Hello World/" "${PROJECT}"
cd "${PROJECT}"
{% endhighlight %}

Next, update **pdxinfo**.

**Source/pdxinfo**
{% highlight sh %}
name=FortranTest
author=Brendan Sechter
description=Fortran on Playdate proof of concept.
bundleID=com.sennue.poc_fortrantest
imagePath=
{% endhighlight %}

The **main.c** and **main.h** files from an earlier post,
[ASM Playdate Development][playdate_asm], can be used for this project.
Modify **main.c**.

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

Take the **fast_sqrt.f90** and **fast_sqrt.h** files from the previous section.

{% highlight sh %}
PREVIOUS_PROJECT_PATH="path_to_project_in_previous_section"
cp "${PREVIOUS_PROJECT_PATH}/fast_sqrt.f90" "${PREVIOUS_PROJECT_PATH}/fast_sqrt.h" src/
{% endhighlight %}

Change the **PRODUCT** and **SRC** lines in the **Makefile**.

**Makefile** Partial Listing
{% highlight make %}
PRODUCT = FortranTest.pdx

# List C source files here
SRC = src/main.c

# List Fortran source files here
FSRC = src/fast_sqrt.f90

# last line of Makefile
include common.mk
{% endhighlight %}

Playdate Makefiles rely on centralized machinery that does not support Fortran
out of the box.
Instead of directly modifying the original
**${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk** file, 
make a copy of **common.mk** for this project.

{% highlight sh %}
cp "${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk" common.mk
{% endhighlight %}

Use the following **diff** as a guide to update **common.mk**.

{% highlight sh %}
$ diff "${PLAYDATE_SDK_PATH}/C_API/buildsupport/common.mk" common.mk
84c84
< _OBJS	= $(SRC:.c=.o)
---
> _OBJS	= $(SRC:.c=.o) $(FSRC:.f90=.o)
106a107,111
> SIMFC=$(shell which gfortran)
> SIMFCFLAGS = -gdwarf-2 -Wall
> FC=$(shell which $(TRGT)gfortran)
> FCFLAGS = $(MCFLAGS) $(OPT) -gdwarf-2 -Wall
>
131c136
< pdc: simulator
---
> pdc: device simulator
140a146,153
> $(OBJDIR)/%.o : %.f90 | OBJDIR DEPDIR
> 	mkdir -p `dirname $@`
> 	$(FC) $(FCFLAGS) -c $< -o $@
>
> $(OBJDIR)/%_simulator.o : %.f90 | OBJDIR DEPDIR
> 	mkdir -p $(dir $@)
> 	$(SIMFC) $(SIMFCFLAGS) -c $< -o $@
>
153,154c166,167
< $(OBJDIR)/pdex.${DYLIB_EXT}: OBJDIR
< 	$(SIMCOMPILER) $(DYLIB_FLAGS) -lm -DTARGET_SIMULATOR=1 -DTARGET_EXTENSION=1 $(INCDIR) -o $(OBJDIR)/pdex.${DYLIB_EXT} $(SRC)
---
> $(OBJDIR)/pdex.${DYLIB_EXT}: OBJDIR $(FSRC:%.f90=$(OBJDIR)/%_simulator.o)
> 	$(SIMCOMPILER) $(DYLIB_FLAGS) -lm -DTARGET_SIMULATOR=1 -DTARGET_EXTENSION=1 $(INCDIR) -o $(OBJDIR)/pdex.${DYLIB_EXT} $(SRC) $(FSRC:%.f90=$(OBJDIR)/%_simulator.o)
{% endhighlight %}

Finally, build and run the project to verify it works.
The square root demo should boot and run in the simulator.

{% highlight sh %}
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
make clean simulator
pdc Source "${PRODUCT}"
playdate_simulator "${PRODUCT}"
{% endhighlight %}

#### Running Fortran on Playdate Hardware

The Playdate SDK does not ship with **arm-none-eabi-gfortran**, but the full
toolchain distributed by ARM includes it.
Download the latest copy of the ARM toolchain for your host platfrom from the
[ARM GNU Toolchain Downloads Page][arm_gnu_toolchain_downloads], and install it.
The author of this post downloaded the
[macOS Hosted Bare-Metal Target (arm-none-eabi) 11.3.rel1 toolchain][arm_gnu_toolchain_macos_11_3_rel1].

The toolchain was installed in **/Applications/ArmGNUToolchain/** on macOS,
The following command can be used to find the installation directory from
the command line.

{% highlight sh %}
dirname $(find / -name "arm-none-eabi-gfortran" 2>/dev/null)
{% endhighlight %}

Add the directory to the **PATH** environment variable.

{% highlight sh %}
ARM_TOOLCHAIN_PATH="/Applications/ArmGNUToolchain/11.3.rel1/arm-none-eabi/bin"
echo 'export PATH="'"${ARM_TOOLCHAIN_PATH}"':${PATH}"' >> "${HOME}/.profile"
{% endhighlight %}

Reload **.profile** if necessary.

{% highlight sh %}
source "${HOME}/.profile"
{% endhighlight %}

The above **diff** contains all of the necessary changes to build a PDX file
that runs on hardware.
After updating the **PATH**, build and run the program to verify it works.
To upload a PDX file to hardware, first run it in the simulator.

{% highlight sh %}
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
make
playdate_simulator "${PRODUCT}"
{% endhighlight %}

Then either “Upload Game to Device” from the “Device” menu or Playdate icon on
the lower lefthand corner of the simulator (with the crank controls collapsed).
Once the game is on the device, **pdutil** can launch it.

{% highlight sh %}
# after the game is on the device
PRODUCT="$(cat Source/pdxinfo | grep name | cut -d "=" -f 2-).pdx"
PDUTIL_DEVICE="$(ls /dev/cu.usbmodemPD* | head -n 1)"
pdutil "${PDUTIL_DEVICE}" run "/Games/${PRODUCT}"
{% endhighlight %}

#### Verification

Pull out the crank and use the D-pad to move the lower righthand point to
(300, 125).
The diagonal length should be 325.000.
Use a calculator to verify other sets of values.

{% highlight c %}
  300 *   300 =  90000
  125 *   125 =  15625
  325 *   325 = 105625
----------------------
90000 + 15625 = 105625
{% endhighlight %}

#### More Information

The Fortran quickstart tutorial has a section on
[Derived Types][fortran_tutorial_derived_types].
Specifically, **bind(c)** offers interoperability with the
C programming language.
gcc also has documention on
[Fortran interoperability with C][fortran_gcc_c_interop].

This post is based on the
"[Fortran on Playdate?][playdate_dev_forum_fortran]" thread on the
[Playdate Developer Forums][playdate_dev_forum].

## References:

- [ARM GNU Toolchain Downloads Page][arm_gnu_toolchain_downloads]
- [ARM GNU Toolchain, macOS Hosted Bare-Metal Target (arm-none-eabi) 11.3.rel1][arm_gnu_toolchain_macos_11_3_rel1]
- [Fortran Homepage][fortran]
- [Fortran Quickstart Tutorial, Derived Types][fortran_tutorial_derived_types]
- [Fortran, gcc Interoperability with C][fortran_gcc_c_interop]
- [Playdate Developer Forum][playdate_dev_forum]
- [Playdate Developer Forum, Fortran on Playdate][playdate_dev_forum_fortran]
- [Playdate Homepage][playdate]
- [Playdate, ASM Playdate Development][playdate_asm]

[arm_gnu_toolchain_downloads]: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads
[arm_gnu_toolchain_macos_11_3_rel1]: arm-gnu-toolchain-11.3.rel1-darwin-x86_64-arm-none-eabi.pkg
[fortran]: https://fortran-lang.org/
[fortran_tutorial_derived_types]: https://fortran-lang.org/en/learn/quickstart/derived_types/
[fortran_gcc_c_interop]: https://gcc.gnu.org/onlinedocs/gfortran/Interoperability-with-C.html
[playdate]: https://play.date/
[playdate_asm]: /gamedev/playdate/asm/arm/x86/2022/10/05/asm_playdate_development.html
[playdate_dev_forum]: https://devforum.play.date/
[playdate_dev_forum_fortran]: https://devforum.play.date/t/fortran-on-playdate/4238

