---
layout: post
comments: true
title:  "Passing Values to C Signal Handlers"
date:   2016-02-24 15:09:21 +0000
categories: unix c signals
---
Signals are inherently global.
There are two ways to handle a signal with external values.

- Put the external data in a global variable and access it from the signal handler.
- Put the signal data in a global variable and access it from the program context.

This post covers the second option.
The signal handler is an isolated part of the program.
The first option can be made to work, but exposing a lot of global state is inelegant.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-02-24 15:09:21 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ clang -v
FreeBSD clang version 3.7.1 (tags/RELEASE_371/final 255217) 20151225
Target: x86_64-unknown-freebsd11.0
Thread model: posix
{% endhighlight %}

## Instructions

The **signal_handler** module covered in this post consists of five functions.

**registerSignalHandler()** takes a null terminated array of signals to handle,
and registers the signal handler with each one.
**signalHandler()** actually responds to the signal.
When a signal is trapped, a flag is set and the signal number is recoreded.
**clearSignal()** clears the flag and signal value.
**pendingSignal()** returns true if the signal flag is set.
**getSignal()** returns the signal value.
If multiple signals are trapped in rapid succession, the signal value will be overwritten.
A more robust solution would have a flag for every signal.

**signal_handler.h**
{% highlight c %}
#ifndef SIGNAL_HANDLER_H
#define SIGNAL_HANDLER_H

#include <stdbool.h>
 
void clearSignal();
bool pendingSignal();
int  getSignal();
void signalHandler(int pSignal);
void registerSignalHandler(int pPriority, int * pSignalList);

#endif // SIGNAL_HANDLER_H
{% endhighlight %}

The function bodies follow.
Note that **gInterrupt** and **gSignal** can only be polled or reset by the outside world.
**syslog** or **printf** can be used to log signal events.

**signal_handler.c**
{% highlight c %}
#include <signal.h>
#include <stdbool.h>
//#include <syslog.h>
//#include <stdio.h>
#include "signal_handler.h"
 
bool gInterrupt;
int  gSignal;

void clearSignal()
{
  gInterrupt = false;
  gSignal = 0;
}

bool pendingSignal()
{
  return gInterrupt;
}

int getSignal()
{
  return gSignal;
}

void signalHandler(int pSignal)
{
  gInterrupt = true;
  gSignal = pSignal;
  //syslog(LOG_NOTICE, "Trapped signal : %d", pSignal);
  //printf(LOG_NOTICE, "Trapped signal : %d", pSignal);
}

void registerSignalHandler(int *pSignalList)
{
  for (int i=0; pSignalList[i]; i++)
  {
    if (SIG_ERR == signal(pSignalList[i], signalHandler))
    {
      //syslog(LOG_WARNING, "Can not catch signal : %d", pSignalList[i]);
      //printf("Can not catch signal : %d", pSignalList[i]);
    }
  }
}
{% endhighlight %}

The signal handler can be registered during initialization.
This is also a good place to clear the signal state for the fist time.

{% highlight c %}
void init()
{
  int signalList[] =
  {
    SIGHUP,
    SIGINT,
    SIGQUIT,
    SIGTERM,
    SIGUSR1,
    SIGUSR2,
    0
  };
  registerSignalHandler(signalList);
  clearSignal();
}
{% endhighlight %}

The signal handler module can be used to write a parameterized function that responds to signals.
The following function does not do anything unless a pending signal needs to be handled.
A switch statement can be used to provide different handling for different signals.
This version just sets a done flag to true.
Finally, the signal state is cleared.

{% highlight c %}
void signalResponse(ProgramState *pProgramState)
{
  if (pendingSignal())
  {
    switch (getSignal())
    {
      // case SIGHUP:
        // /* do something */
        // break
      default:
        pProgramState->done = true;
      break;
    }
    clearSignal();
  }
}
{% endhighlight %}

The above function can be called any place that is convenient.
For example, the following function calls the above **signalResponse()**
function every iteration of the main loop.
The program can trap signals and clean up gracefully

Note that the simple example below has a bug.
**getchar()** blocks, so the **signalResponse()** handler will
not be called until after user input.
If the user hits **^C**, the loop (and program) will not exit until the user hits enter.

{% highlight c %}
int mainLoop(ProgramState *pProgramState)
{
  int c;
  while (!pProgramState->done)
  {
    c = getchar();
    if (c != EOF)
    {
      putchar(c);
      fflush(stdout);
    }
    else
    {
      pProgramState->done = true;
    }
    signalResponse(pProgramState);
  }
  return EXIT_SUCCESS;
}
{% endhighlight %}

## References:
- [FreeBSD, man signal][freebsd-man-signal]
- [UNIX, Linux Signals – Example C Program to Catch Signals (SIGINT, SIGKILL, SIGSTOP, etc.)][unix-linux-signals]
- [UNIX, Signals and Traps][unix-signals-traps]
- [UNIX, Providing/passing argument to signal handler][unix-signal-arg]
- [ION-DTN, Serving a Web Page with ION-DTN bpsendfile and bprecvfile][ion-web]

[freebsd-man-signal]: https://www.freebsd.org/cgi/man.cgi?sektion=3&query=signal
[unix-linux-signals]: http://www.thegeekstuff.com/2012/03/catch-signals-sample-c-code/
[unix-signals-traps]: http://www.tutorialspoint.com/unix/unix-signals-traps.htm
[unix-signal-arg]: http://stackoverflow.com/questions/6970224/providing-passing-argument-to-signal-handler
[ion-web]: https://sgeos.github.io/freebsd/ion/dtn/2016/02/17/serving-a-web-page-with-ion-dtn-bpsendfile-and-bprecvfile.html

