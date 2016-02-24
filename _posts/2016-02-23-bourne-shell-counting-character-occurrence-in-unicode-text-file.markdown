---
layout: post
comments: true
title:  "Bourne Shell: Counting Character Occurrence in a Unicode Text File"
date:   2016-02-23 10:40:41 +0000
categories: sh
---
Sometimes it can be useful to get the character occurrence count of a text file.
This post covers a unicode safe Bourne shell solution.
"Unicode" was only tested with mixed Japanese and English text.
The solution in this post can not be used to count whitespace.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2016-02-23 10:40:41 +0000
$ uname -vm
FreeBSD 11.0-CURRENT #0 r287598: Thu Sep 10 14:45:48 JST 2015     root@:/usr/obj/usr/src/sys/MIRAGE_KERNEL  amd64
{% endhighlight %}

## Instructions

The following script can be used to count character occurrence in a text file.
The characters to count are defined in the **CHARSET** variable at the top of the file.
For each character, the script scans the file and prints the result.
Characters are counted for each filename passed to the script.
Usage is printed if no file names are passed.
Whitespace will not make it into the for loop.

**character_count.sh**
{% highlight sh %}
#!/bin/sh

CHARSET='abcmwxyz~!&#jkdefghst@=+{}[]あいうえお、一二三四五。'

echo "CHARSET=${CHARSET}"
CHARSET=$(echo -n $CHARSET | sed "s/./& /g")

if [ "${#}" -lt 1 ]
then
  echo "Usage:"
  echo "  ${0} FILE [FILE...]"
fi

for FILENAME
do
  echo "---${FILENAME}---"
  for CHAR in $CHARSET
  do
    COUNT=$(fgrep -o "${CHAR}" "${FILENAME}" | wc -l | tr -d '[[:space:]]')
    echo "${CHAR} : ${COUNT}"
  done
done
{% endhighlight %}

The script itself can be used as a test file.

{% highlight sh %}
chmod +x character_count.sh
./character_count.sh character_count.sh
{% endhighlight %}

## References:
- [UNIX, count occurences of specific character in the file][unix-count]
- [UNIX, Count occurrences of a char in plain text file][unix-count2]
- [UNIX, How to perform a for loop on each character in a string in BASH?][unix-charloop]
- [UNIX, Replace comma with newline in sed][unix-replace]
- [UNIX, How do I insert a space every four characters in a long line?][unix-space]
- [UNIX, Sh - the Bourne Shell][unix-sh]
- [UNIX, Bourne Shell Scripting/Control flow][unix-sh-flow]

[unix-count]: http://www.unix.com/hp-ux/19176-count-occurences-specific-character-file.html
[unix-count2]: http://stackoverflow.com/questions/1603566/count-occurrences-of-a-char-in-plain-text-file
[unix-charloop]: http://stackoverflow.com/questions/10551981/how-to-perform-a-for-loop-on-each-character-in-a-string-in-bash
[unix-replace]: http://stackoverflow.com/questions/10748453/replace-comma-with-newline-in-sed
[unix-space]: http://unix.stackexchange.com/questions/5980/how-do-i-insert-a-space-every-four-characters-in-a-long-line
[unix-sh]: http://www.grymoire.com/Unix/Sh.html
[unix-sh-flow]: https://en.wikibooks.org/wiki/Bourne_Shell_Scripting/Control_flow

