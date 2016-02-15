---
layout: post
comments: true
title:  "Elixir, Executing AST"
date:   2016-02-01 04:49:00 +0900
categories: elixir metaprogramming ast
---
Inspecting AST is a good way to learn about elixir macros.
Executing AST can also be instructional, but it is a little more nuanced than
directly executing elixir code.
This post covers executing AST with **Code.eval_quoted()**.
Note that outside of experimentation, executing AST with **Code.eval_quoted()**
is probably the wrong thing to do.

Thanks to everyone in [#elixir-lang on Freenode][elixir-irc] who answered my
questions about executing AST.

## Software Versions
{% highlight sh %}
$ date 
February  1, 2016 at 04:49:00 AM JST
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
$ elixir --version
Erlang/OTP 18 [erts-7.2.1] [source] [64-bit] [async-threads:10] [hipe] [kernel-poll:false]
Elixir 1.2.2
{% endhighlight %}

## Instructions
This is a single file example of a naive solution that does **not** work.
Put the following in **ast.exs**.

{% highlight elixir %}
#!/usr/bin/env elixir

defmodule MacroLibrary do
  # a simple macro that delegates work to a complex function
  defmacro process_macro(input) do
    quote do
      process_function(unquote(input))
    end
  end

  # the complex function called by the macro
  def process_function(input) do
    input
    |> Enum.each(&IO.puts/1)
  end
end

defmodule Script do
  import MacroLibrary # important

  def main(args) do
    # call the macro directly
    process_macro(["Args:" | args])
    |> IO.puts

    # macro AST
    ast = quote do
      process_macro(["Args:" | args]) # BROKEN line 28
    end

    # display the AST
    ast
    |> Macro.to_string
    |> IO.puts

    # display the expanded AST
    ast
    |> Macro.expand(__ENV__)
    |> Macro.to_string
    |> IO.puts

    # execute the AST
    {result, _binding} = ast
    |> Code.eval_quoted # BROKEN line 44

    # display the result
    result
    |> IO.puts
  end
end

# run the script
Script.main(System.argv)
{% endhighlight %}

Make the script executable.

{% highlight sh %}
$ chmod +x ast.exs
{% endhighlight %}

This is the expected outputed.

{% highlight sh %}
$ ./ast.exs a b c
Args:
a
b
c
ok
process_macro(["Args:" | args])
process_function(["Args:" | args])
Args:
a
b
c
ok
{% endhighlight %}

This is the actual output.
{% highlight sh %}
$ ./ast.exs a b c
Args:
a
b
c
ok
process_macro(["Args:" | args])
process_function(["Args:" | args])
** (CompileError) nofile:1: undefined function process_function/1
    expanding macro: MacroLibrary.process_macro/1
    nofile:1: (file)
{% endhighlight %}

What happened?

Directly invoking the macro works as expected.
The naive expectation is that the AST should just execute because the code
is the same as the direct invocation.

The problem is that context is missing.
The AST evaluates as **process_macro(["Args:" | args])** which expands to
**process_function(["Args:" | args])**.
**process_function** is defined in the **MacroLibrary** module.
The macro library is included in the **Script** module.
That information is stored in the current context.
Without the context, **Code.eval_quoted** does not know where to find
**process_function**.

Change line 44 to the following:
{% highlight elixir %}
    |> Code.eval_quoted([], __ENV__) # BROKEN line 44
{% endhighlight %}

There is another problem.
{% highlight sh %}
$ ./ast.exs a b c
Args:
a
b
c
ok
process_macro(["Args:" | args])
process_function(["Args:" | args])
** (CompileError) ast.exs:44: undefined function args/0
    expanding macro: MacroLibrary.process_macro/1
    ast.exs:44: Script (module)
{% endhighlight %}

When executing the macro directly, **args** resolves properly.
Bindings are not part of the environment context and need to be passed in
separately.

Change line 44 to the following:
{% highlight elixir %}
    |> Code.eval_quoted([args: args], __ENV__) # CORRECT line 44
{% endhighlight %}

This did not fix the problem.
The macro can be directly invoked with **process_macro(["Args:" | args])**,
but executed AST needs to use **var!()** to access variables.
This means that the direct macro call and the executable AST need to be
slightly different.

Change line 28 to the following:
{% highlight elixir %}
      process_macro(["Args:" | var!(args)]) # CORRECT line 28
{% endhighlight %}

The example finally works.
{% highlight sh %}
$ ./ast.exs a b c
Args:
a
b
c
ok
process_macro(["Args:" | var!(args)])
process_function(["Args:" | var!(args)])
Args:
a
b
c
ok
{% endhighlight %}

AST needs to be defined and executed as below.
{% highlight elixir %}
# direct invocation
result = process_macro(["Args:" | args])

# indirect invocation
ast = quote do
  process_macro(["Args:" | var!(args)])
end

{result, _binding} = ast
|> Code.eval_quoted([args: args], __ENV__)
{% endhighlight %}

## References:
- [Elixir, Metaprogramming Elixir][elixir-metaprogramming]
- [Elixir, Macros][elixir-macros]
- [Elixir, Code][elixir-code]
- [Elixir, Single File Elixir Programs][elixir-single]
- [IRC #elixir-lang on Freenode][elixir-irc]

[elixir-metaprogramming]: https://pragprog.com/book/cmelixir/metaprogramming-elixir
[elixir-macros]:          http://elixir-lang.org/getting-started/meta/macros.html
[elixir-code]:            http://elixir-lang.org/docs/master/elixir/Code.html
[elixir-single]:          https://sgeos.github.io/elixir/erlang/2016/01/08/single-file-elixir-programs.html
[elixir-irc]:             irc://irc.freenode.net/elixir-lang

