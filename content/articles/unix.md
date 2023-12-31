+++
title = "Productivity in unix"
description = "Loving the Unix user experience comes from realising how you make it work the way you want"
date = 2007-06-13T15:57:29Z
[taxonomies]
tags = ["computers"]
+++


People who I work with are often bemused by the perculiar setup I have
on my machine, which is the product of constant evolution over the last
five years or so. My setup is designed to work well for me, not to look
pretty or provide distraction. As such, it can be thought of as sort of
the opposite of desktop environments like Gnome. The other thing about
my setup is that it is designed first and foremost to be fast and as
such programs which are slow to start, slow to run or consume a lot of
memory are completely out. For this reason, over the years I have
ditched the emacs family of editors, fancy window managers and silly
meta-environments like Gnome. People who use vim tend to look
productive and slightly wired like this:

![Bram Moolenaar, the author of Vim looking like he's  just had a double espresso][6]

Whereas emacs users have been known to look like this:

![Richard Stallman, dressed as "Saint Ignucius"][7]

I think that proves my point nicely.

I also use a text-mode web browser where I can because it is quick to
start up and makes it quick to find information. Time-wasting web
browsing of sites entirely devoid of real information I still do with a
graphical browser, however. I have found that as computers that I use
have become faster and more powerful, my desire for speed has increased
so I am even more obsessed with small, fast apps than I used to be.
Goals of the setup

These are pretty simple:
* Small memory footprint
* Fast
* Flexible
* Productive
* Maximise available resources (desktop area etc)

Apps I use
* Linux - Let's not kid ourselves. I'm much more productive in Linux
than I am elsewhere.
* The vim editor - As a programmer your editor is your most important
tool and vim is by far and away the best there is (for me anyway). Nowdays I
tend to use [neovim][neovim] rather than old-school vim but
they're very similar
* The [zsh][zsh] shell - The zsh shell is a pretty productive environment
for me, but the jury is still out on this for me. I don't mind bash
either as long as I can use vi keybindings.
* The [i3][8] window manager- The X window manager which allows
you to do away with your mouse and means you are forever liberated
from dragging and resizing and using the annoying mouse.
* [tmux][9] - some time ago I ditched gnu screen for this and it's great.  The one
  feature of screen that I miss is the ability to have shared sessions that
  are not always viewing the same pane.  nbd though
find it on google. Screen is cool though.
* Scripting languages - noone is productive on unix without being
able to write little scripts. As well as the shell, I love
scripting in Perl, sed (sometimes) and Python.


### The shell and the unix philosophy

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
`"${TRY##*/}"`. If you are using a csh-like shell I pity you and this cd
mechanism will not be enough to save you from your folly anyway.

### Shell history completion and searching

One of the easiest ways to improve your productivity on unix systems is
to become acquainted with your shell's history completion and search
facilities. All of these described here are common to zsh and bash,
although zsh has some additional features that bash does not.

Firstly, if you ever find yourself tapping the up arrow to scroll
through your command history, you are living in a state of sin- either
type `history 100` or something similar to actually get a history list or
use Ctrl-R to do a recursive incremental search through your shell
history. Secondly, learn and use some basic history completions:
* `!$` completes to the last argument of your previous command. `vi file` followed by `git commit !$` edits a file and checks it in.
* `!*` completes to all the arguments of your previous command. `vi file1 file2 file{3,4,5}` followed by `git commit !*` edits a list of files and checks then all in.
* `!!` completes to the whole of your previous command, with args. `vi /etc/passwd` gives "permission denied? Use `sudo !!` to become rootly without retyping.

There are lots more possible history completions but I use those three
ten times for any one of them. Also useful are:
* `!something` completes to the whole of the last command I typed that began with "`something`". So, for example, say I try `vi file` and get "permission denied", but I don't yet have "sudo" permission sorted out. I become root, fix my sudoers file, then do `sudo !vi` to run the whole of the last vi command as root.
* `!somenumber` completes to the whole of a specific numbered command from my history.

You can combine these with the first three constructs by adding a
colon, so:
* `!vi:*` is "all the arguments to the last vi command. Perhaps I have edited
  some files, then done a make to see if they build, then I can `git commit
  !vi:*` to check the changes into git.
* `!3:$` is the last argument to command number three from my history.

[5]: https://www.gnome.org/
[6]: /static/images/kopk.jpg
[7]: /static/images/saintignucius.jpg
[8]: https://i3wm.org
[9]: https://github.com/tmux/tmux/wiki
[neovim]: https://neovim.io
[zsh]: https://www.zsh.org
