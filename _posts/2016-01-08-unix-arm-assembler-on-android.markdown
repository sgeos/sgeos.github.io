---
layout: post
title:  "UNIX ARM Assembler on Android"
date:   2016-01-08 07:12:57 +0900
categories: jekyll github freebsd
---
Months ago, someone on the FreeBSD forums [wanted help][original-post] getting an assebly language program running on a 64 bit intel machine.  I read through the [FreeBSD Developers' Handbook x86 Assembly Language Programming section][freebsd-handbook-asm], and sure enough the 32 bit examples did not work.  x86 and x86-64 assembler are just plain different.  Also, the ABI is completely different.

I managed to find an [x86-64 hello world example for FreeBSD][freebsd-x86-64-hello-world].  The environment works.  Great!  Now what?  The problem with hello world examples is that there is no input.  Without knowing where to go next, a hello world example is not very useful.  Between the [Developer's Handbook][freebsd-handbook-asm], the [System V AMD64 ABI Reference][system-v-abi] and an x86-64 tutorial (that has since disappeared) I managed to write a command line utility in x86-64 ASM that processes command line arguments.

Then I though back to the days when I wrote ARM assembler for the Gameboy Advance and Nintendo DS and wanted to write a command line UNIX utility in ARM assembler.  My Raspberry Pi was halfway around the world, but my Android phone was on my desk.  No FreeBSD on my phone, but both FreeBSD and Linux appear to use the ARM EABI documented on the [ARM site][arm-site].

The [Developer's Handbook][freebsd-handbook-asm] notes that "Assembly language programming under UNIX® is highly undocumented".  I am writing this post to document writing a command line UNIX application in assembler that conforms to the ARM EABI.  Specifically, this application will run on Android.  There has never been an easier time to learn assebler.

My GitHub repository for this project can be found [here][android-asm-github].  Please note that manually linking object files is probably not standard Android NDK usage.  The build instructions may break in the future.  If that happens, good luck figuring the necessary flags to build the examples.  =)

## Software Versions
{% highlight sh %}
$ uname -a
Darwin siderite.local 15.2.0 Darwin Kernel Version 15.2.0: Fri Nov 13 19:56:56 PST 2015; root:xnu-3248.20.55~2/RELEASE_X86_64 x86_64
$ adb shell "uname -a"
Linux localhost 3.4.0-cyanogenmod-g9e39333 #1 SMP PREEMPT Wed Jan 6 19:02:34 PST 2016 armv7l
$ adb version
Android Debug Bridge version 1.0.32
{% endhighlight %}

## Instructions
First, install the [Android SDK][android-sdk] and [Android NDK][android-ndk].  Make sure [ADB][android-debug-bridge] has been installed and you connect to your test device.
{% highlight sh %}
$ adb devices
List of devices attached 
071f7b2ef0e95581	device

$ adb shell "uname"
Linux
{% endhighlight %}

A rooted device is required to run ASM programs on Android with these instructions.  Running ADB as root is handy.  You will need chmod, so you will need to install busybox or some other box that provides the same functionality.
{% highlight sh %}
$ adb root
restarting adbd as root
$ adb shell "chmod +x /root/does_not_exist"
chmod: /root/does_not_exist: No such file or directory
{% endhighlight %}

Next, install the [Android NDK standalone toolchain][android-ndk-standalone].  The sysroot path probably needs to be defined.  Also adding paths for the SDK, NDK and the to be generated standalone NDK is a good idea.  I added these lines to my .profile.  Adjust pathnames as necessary.
{% highlight sh %}
export ANDROID_SDK="$HOME/android-sdk"
export ANDROID_NDK="$HOME/android-ndk"
export ANDROID_NDK_STANDALONE_TOOLCHAIN="$HOME/android-ndk-standalone-toolchain"
export SYSROOT="$ANDROID_NDK_STANDALONE_TOOLCHAIN/sysroot"
export PATH="$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools:$ANDROID_NDK_STANDALONE_TOOLCHAIN/bin:$PATH"
{% endhighlight %}

Next, reload .profile and  generate the standalone toolchain.  The [Android NDK standalone toolchain][android-ndk-standalone] page has instructions for targetting different architectures and Android versions.
{% highlight sh %}
. .profile
$ANDROID_NDK/build/tools/make-standalone-toolchain.sh \
  --toolchain=arm-linux-androideabi-clang3.6 \
  --install-dir=$ANDROID_NDK_STANDALONE_TOOLCHAIN
{% endhighlight %}

The first program to build and run is a hello world example written in C.  In general, it is generally a good idea to have a working C implementation before writing anything in ASM.
{% highlight c %}
// main.c
#include <stdio.h>

int main(int argc, char **argv)
{
	printf("Hello, World! [C]\n");
	return 0;
}
{% endhighlight %}

Build it with the following commands.
{% highlight sh %}
CRT="$SYSROOT/usr/lib/crtbegin_dynamic.o $SYSROOT/usr/lib/crtend_android.o"
$ANDROID_NDK_STANDALONE_TOOLCHAIN/bin/clang --sysroot=$SYSROOT -fPIE -DANDROID -g -c main.c -o main.o 
$ANDROID_NDK_STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-ld --sysroot=$SYSROOT -pie --dynamic-linker=/system/bin/linker main.o $CRT -o c-hello-world -lc
{% endhighlight %}

This is a funny way of building a C program.  What is going on?  The end goal is to build and run assembler programs.  Assembly files need to run through the assebler and the linker.  In order to link ASM object files with C object files all object files need to be manually linked.  The entry point to a C program is main, but the program really takes control in the _start function.  The CRT files contain this _start function.  It has all of the setup code for the "C runtime".  This code zeros memory and does other boilerplate tasks.  Your compiler usually includes the C runtime automatically so you do not need to think about it.  The -lc flag links the standard C library.  This is another step your compiler usually handles automatically.

Running the program on the phone should print "Hello, World! [C]".  This will remount the system partition of your phone in read write mode.  If you do not know what that means do not proceed.
{% highlight sh %}
adb root
adb remount
adb shell "mkdir /system/asm"
adb push c-hello-world /system/asm
adb shell "chmod +x /system/asm/c-hello-world"
adb shell /system/asm/c-hello-world
{% endhighlight %}

With the C version working, it is time to rewrite the program in ARM ASM.  Let us start with a header that defines system calls.
{% highlight asm %}
@ system.inc
@ Android Syscall Reference https://code.google.com/p/android-source-browsing/source/browse/libc/SYSCALLS.TXT?repo=platform--bionic&r=cd15bacf334ab254a5f61c3bba100adde1b6b80a

.set stdin,  0
.set stdout, 1
.set stderr, 2

.set SYS_nosys, 0
.set SYS_exit,  1
.set SYS_fork,  2
.set SYS_read,  3
.set SYS_write, 4
.set SYS_open,  5
.set SYS_close, 6

.macro sys.syscall id
	mov	r7, \id
	swi	$0
.endm

.macro sys.exit
	sys.syscall $SYS_exit
.endm

.macro sys.fork
	sys.syscall $SYS_fork
.endm

.macro sys.read
	sys.syscall $SYS_read
.endm

.macro sys.write
	sys.syscall $SYS_write
.endm

.macro sys.open
	sys.syscall $SYS_open
.endm

.macro sys.close
	sys.syscall $SYS_close
.endm
{% endhighlight %}

Next, the main assembler file.
{% highlight asm %}
.include "system.inc"
	.syntax unified
	.set ALIGNMENT,8

.text
	.align ALIGNMENT
	.global _start
_start:
	nop @ for gbd breakpoint

	@ Hello World
	@ sys.write(stdout, message, length)
	mov	r0,$stdout
	adr	r1,message
	mov	r2,$length
	sys.write

	@ sys.exit(0)
	mov	r0,$0
	sys.exit

@ Data needs to be in .text for PIE
@.data
message:
	.asciz "Hello, World! [ASM]\n"
length = . - message
	.align ALIGNMENT
{% endhighlight %}

The next step is building the ASM version.
{% highlight asm %}
$ANDROID_NDK_STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-as --gdwarf2 start.s -o start.o
$ANDROID_NDK_STANDALONE_TOOLCHAIN/bin/arm-linux-androideabi-ld --sysroot=$SYSROOT -pie --dynamic-linker=/system/bin/linker start.o -o asm-hello-world
{% endhighlight %}

The start.s file contains a start function, so the C runtime is not necessary.  Functions from the C library can be called from assebler, but this function is using system calls, so -lc is not necessary.

Running it on the phone should print "Hello, World! [ASM]".
{% highlight sh %}
adb push asm-hello-world /system/asm
adb shell "chmod +x /system/asm/asm-hello-world"
adb shell /system/asm/asm-hello-world
{% endhighlight %}

A Makefile for the hello world project looks like this.
{% highlight make %}
TOOLCHAIN=$(ANDROID_NDK_STANDALONE_TOOLCHAIN)
SYSROOT=$(TOOLCHAIN)/sysroot
CC=$(TOOLCHAIN)/bin/clang --sysroot=$(SYSROOT)
AS=$(TOOLCHAIN)/bin/arm-linux-androideabi-as
LD=$(TOOLCHAIN)/bin/arm-linux-androideabi-ld --sysroot=$(SYSROOT)
CRT=$(SYSROOT)/usr/lib/crtbegin_dynamic.o $(SYSROOT)/usr/lib/crtend_android.o
INSTALL=/system/test

CFLAGS=-fPIE -DANDROID -g
ASFLAGS=--gdwarf2
LDFLAGS=-pie --dynamic-linker=/system/bin/linker

ASM_TARGET=asm-hello-world
ASM_PARAM=
ASM_DEPS=system.inc
ASM_OBJ=start.o
ASM_LIBS=

C_TARGET=c-hello-world
C_PARAM=
C_DEPS=
C_OBJ=main.o $(CRT)
C_LIBS=-lc

all: $(ASM_TARGET) $(C_TARGET)

force: clean all

$(C_TARGET): $(C_OBJ)
	$(LD) $(LDFLAGS) $^ -o $@ $(C_LIBS)

$(ASM_TARGET): $(ASM_OBJ)
	$(LD) $(LDFLAGS) $^ -o $@ $(ASM_LIBS)

%.o: %.c $(C_DEPS)
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.s $(ASM_DEPS)
	$(AS) $(ASFLAGS) $< -o $@

install: all
	adb root
	adb remount
	adb shell "mkdir $(INSTALL)"
	adb push $(ASM_TARGET) $(INSTALL)
	adb push $(C_TARGET) $(INSTALL)
	adb shell "chmod +x $(INSTALL)/$(ASM_TARGET) $(INSTALL)/$(C_TARGET)"

uninstall:
	adb root
	adb remount
	adb shell "mkdir $(INSTALL)"
	adb shell "rm -rf $(INSTALL)/$(ASM_TARGET) $(INSTALL)/$(C_TARGET)"
	adb shell "rmdir $(INSTALL)"

test:
	adb root
	adb shell "$(INSTALL)/$(ASM_TARGET) $(ASM_PARAM) && $(INSTALL)/$(C_TARGET) $(C_PARAM)"

clean:
	rm -rf $(ASM_TARGET) $(C_TARGET) *.o
{% endhighlight %}

The next program will echo all of the command line arguments.  This is the C source code:
{% highlight c %}
// main.c
#include <stdio.h>
#include <sys/syscall.h>
#include <unistd.h>

#define BUFFER_SIZE  2048
#define MESSAGE      "Args: [C]\n"

char buffer[BUFFER_SIZE];

const char message[] = MESSAGE;
const int  length    = sizeof MESSAGE - 1; // sizeof inclues \0

int main(int argc, char** argv)
{
  // write message
  syscall(SYS_write, STDOUT_FILENO, message, length);

  // loop over argv until argvn_ptr is null
  char *argvn_ptr = *(argv++);
  while (NULL != argvn_ptr) {
    char *buffer_ptr = buffer;
    // copy from argvn_ptr to buffer_ptr until \0 is encountered
    while ('\0' != *argvn_ptr) {
      *(buffer_ptr++) = *(argvn_ptr++);
    }
    // append \n and write buffer
    *buffer_ptr++ = '\n';
    syscall(SYS_write, STDOUT_FILENO, buffer, buffer_ptr - buffer);
    // next arg
    argvn_ptr = *(argv++);
  }
  // done
  syscall(SYS_exit, 0);
}
{% endhighlight %}

This is probably not what you expected to see.  To be fair, the first version looped over argv and used printf.  The C version is, however, supposed to be a C representation of the ASM.  This version C main uses the same algorithm as the following ASM version.
{% highlight c %}
.include "system.inc"
        .syntax unified
	.set ALIGNMENT,8
	.set BUFFER_SIZE,2048

.bss
	.comm buffer,BUFFER_SIZE,ALIGNMENT

.text
	.align ALIGNMENT
        .global _start
_start:
	nop @ for gbd breakpoint

	@ Intro Message
	@ sys.write(stdout, message, length)
	mov	r0,$stdout
	adr	r1,message
	mov	r2,$length
	sys.write

	@ Load Buffer via Global Offset Table
	ldr	r0,.Lgot	@ got_ptr = &GOT - X
	add	r0,r0,pc	@ got_ptr += X
	ldr	r4,.Lbuffer	@ buffer_offset
.Lpie0:	ldr	r4,[r4,r0]	@ buffer = *(got_ptr+buffer_offset)

	@ Write Args
	pop	{r0,r1}	@ pop argc, argvn_ptr = argv[0]
proc_arg:
	teq	r1,$0	@ if NULL != argvn_ptr
	beq	done
	mov	r2,r4	@ buffer_ptr = buffer
copy_char:
	ldrb	r0,[r1],$1	@ c = *argv_ptr++
	teq	r0,$0
	beq	output
	strb	r0,[r2],$1	@ *buffer_ptr++ = c
	b	copy_char
output:
	mov	r0,$0x0A	@ c = '\n'
	strb	r0,[r2],$1	@ *buffer_ptr++ = '\n'
	mov	r0,$stdout
	mov	r1,r4		@ buffer
	sub	r2,r2,r1	@ length = buffer - buffer_ptr
	sys.write
	pop	{r1}	@ argv_ptr = argv[n]
	b	proc_arg
done:
	@ sys.exit(0)
	mov	r0,$0
	sys.exit

@ Data needs to be in .text for PIE
@.data
message:
        .asciz "Args: [ASM]\n"
length = . - message
	.align ALIGNMENT

	@ Global Offset Table
.Lgot:
	.long	_GLOBAL_OFFSET_TABLE_-.Lpie0
.Lbuffer:
	.word	buffer(GOT)
	.align ALIGNMENT
{% endhighlight %}

## References:
- [Android ASM GitHub Project][android-asm-github]
- [Android SDK][android-sdk]
- [Android NDK][android-ndk]
- [Android NDK Standalone Toolchain][android-ndk-standalone]
- [Android Debug Bridge][android-debug-bridge]
- [Android Syscall Reference][android-syscall]
- [ARM EABI Documentation][arm-site]
- [FreeBSD Forums Assembly - simple Hello World][original-post]
- [FreeBSD Developers' Handbook x86 Assembly Language Programming section][freebsd-handbook-asm]
- [FreeBSD x86-64 Hello World][freebsd-x86-64-hello-world]
- [System V AMD64 ABI Reference][system-v-abi]

[android-asm-github]:         https://github.com/Sennue/AndroidARM
[android-sdk]:                 http://developer.android.com/sdk/installing/index.html
[android-ndk]:                 http://developer.android.com/tools/sdk/ndk/index.html
[android-ndk-standalone]:     https://developer.android.com/ndk/guides/standalone_toolchain.html
[android-debug-bridge]:       http://developer.android.com/tools/help/adb.html
[android-syscall]:            https://code.google.com/p/android-source-browsing/source/browse/libc/SYSCALLS.TXT?repo=platform--bionic&r=cd15bacf334ab254a5f61c3bba100adde1b6b80a
[arm-site]:                   http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.subset.swdev.abi/index.html
[original-post]:              https://forums.freebsd.org/threads/assembly-simple-hello-world.53274/#post-299410
[freebsd-handbook-asm]:       https://www.freebsd.org/doc/en_US.ISO8859-1/books/developers-handbook/x86.html
[freebsd-x86-64-hello-world]: https://thebrownnotebook.wordpress.com/2009/10/27/native-64-bit-hello-world-with-nasm-on-freebsd/
[system-v-abi]:               http://x86-64.org/documentation/abi.pdf

