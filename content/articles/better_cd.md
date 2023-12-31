+++
title = "Building a better cd"
description = "Unix shell is very flexible and easy to customise. Here is how I made 'cd' better for me than the builtin one."
aliases = [ "/articles/better_cd" ]
date = 2006-04-21T15:44:45Z
updated = 2006-04-21
[taxonomies]
tags = ["computers"]
+++


One of the key strengths of unix systems is the philosophy of small
tools which can be combined in flexible ways. Writing your own scripts,
functions and aliases to customise your user experience not only makes
your life better and more productive, its also a great way to learn
about unix.

This is the antithesis of the mindset that brings about Integrated
Development Environments. The great thing about the unix shell as an
integrated environment is that it is infinite in potential given that
you can always extend the facilities you have by making other tools
using scripting or by getting them from the web. The shell itself is
extensible in that you can add little scripts or write functions to add
features or do things your way.

For example, the cd builtin in ksh has this tremendous feature for
dealing with long paths. Say I'm in
`/foo/bar/nerf/2003-04-26/conf/frazzle` and I realise I need to be in
`/foo/baz/nerf/2003-04-26/conf/frazzle`, all I do is type `cd bar baz` .
That's pretty useful.

I also often find myself typing `vi /the/path/to/a/file`, then wishing I
could do cd !$ to get to the directory to check the file in or
whatever. So I built a cd function that changes to the parent directory
if the target is a file. When a colleague of mine explained the ksh cd
behaviour, I added his ksh-like cd function to mine to get this:

```sh
cd()
{
    if [ -z "$1" ] ; then
        builtin cd
    else
        if [ -n "$2" ]; then
            TRY="${PWD/$1/$2}"
        else
            TRY="$1"
        fi

        if [ -f "${TRY}" ]; then
            builtin cd "${TRY:h}"
        else
            builtin cd "${TRY}"
        fi
    fi
}
```

Notice that this includes a few zsh-isms which you'll need to change if
you want to use this in bash. `${TRY:h}` is the same as `$( dirname
"${TRY}" )` but I get to skip the backticks and save a fork. I think you
can do this in bash using a string substitution something like
`"${TRY##*/}"` but I haven't bothered to try. If you are using a csh-like
shell I pity you and this cd mechanism will not be enough to save you
from your folly anyway.

