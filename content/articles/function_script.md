+++
title = "Shell Functions that are also executables"
description = "Sometimes its handy to have shell functions that can be sourced, but can also be executables in their own right. Here's how."
aliases = [ "/articles/function_script" ]
date = 2006-04-30T14:03:35Z
[taxonomies]
tags = ["computers"]
+++


Sometimes it's useful to have shell functions that can be used both
from within my current shell and sourced inside scripts which I write.
To achieve this is fairly easy if you arrange things according to a
simple convention. What I do is to make a directory called "lib" in my
homedir, and put each function into a seperate file in there that has
the same name as the function.

For example, I wrote a small function to print the name of the file in
a given directory that has most recently been modified. To make this
more generic, I got it to print the n-th from last, rather than
specifically the last. So I make a small file called
`~/lib/printlastfile` containing the following:

```sh
# vim: set syn=zsh:

#if no args are supplied, print the last filename from $TMP
#if one arg, print the n-th from last filename from $TMP
#if two args, the second arg is the name of a dir to use instead of TMP
printlastfile()
{
    RANK=${1:-1}
    #expand $TMPDIR and append a trailing slash if it doesn't have one
    DIR=$( echo ${2:-${TMPDIR:-'/tmp/'}} | sed 's,[^/]$,&/,' )

    ls -t "${DIR}"* | sed -n "${RANK}p;${RANK}q"
}
```

So any time I want that function I can just source that file. Now say I
want an executable that runs printlastfile. I could make
`~/bin/printlastfile` as follows:

```sh
#!/bin/zsh
. ~/lib/printlastfile
printlastfile "${1}" "${2}"
```

... but that gets a bit tedious when you have a few of these things so
I made one generic executable that for any function, will source the
function and then run it. I call it libsquiggle because it turns things
which are in squiggle/lib into executables and it looks like this:

```sh
#!/usr/bin/env zsh

MYNAME="${0:t}"
. "${HOME}/lib/${MYNAME}"

$MYNAME "$@"
```

So I make an executable called libsquiggle that looks like that and for
any function in `~/lib` that I want to work as an executable I make a
symlink in `~/bin` called the name of the function and pointing to
`~/bin/libsquiggle`. Thus:

    ls -l =printlastfile

    lrwxrwxrwx  1 sean sean 11 Oct  5  2005 /home/huntse/bin/printlastfile -> libsquiggle

[1]: http://www.uncarved.com/articles/function_script
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/tags/computers
