---
Tags: computers
Last Modified:2006-05-17T07:35:18Z
---
# Shell Command History and Searching

## Time spent learning how the unix shell works is never wasted

One of the easiest ways to improve your productivity on unix systems is
to become acquainted with your shell's history completion and search
facilities. All of these described here are common to zsh and bash,
although zsh has some additional features that bash does not.

Firstly, if you ever find yourself tapping the up arrow to scroll
through your command history, you are living in a state of sin- either
type history 100 or something similar to actually get a history list or
use Ctrl-R to do a recursive incremental search through your shell
history. Secondly, learn and use some basic history completions:
* !$ completes to the last argument of your previous command. vi file
followed by cvs ci !$ edits a file and checks it in.
* !* completes to all the arguments of your previous command. vi
file1 file2 file{3,4,5} followed by cvs ci !* edits a list of files
and checks then all in.
* !! completes to the whole of your previous command, with args. vi
/etc/passwd gives "permission denied? Use sudo !! to become rootly
without retyping.

There are lots more possible history completions but I use those three
ten times for any one of them. Also useful are:
* !something completes to the whole of the last command I typed that
began with "something". So, for example, say I try vi file and get
"permission denied", but I don't yet have "sudo" permission sorted
out. I become root, fix my sudoers file, then do sudo !vi to run
the whole of the last vi command as root.
* !somenumber completes to the whole of a specific numbered command
from my history.

You can combine these with the first three constructs by adding a
colon, so:
* !vi:* is "all the arguments to the last vi command. Perhaps I have
edited some files, then done a make to see if they build, then I
can svn ci !vi:* to check the changes into subversion.
* !3:$ is the last argument to command number three from my history.

[1]: http://www.uncarved.com/articles/shell_history
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/tags/computers
[6]: mailto:sean@uncarved.com
[7]: http://creativecommons.org/licenses/by-sa/4.0/
