+++
title = "My life (and mail) in subversion"
description = "Moving my mail into subversion gives me easy backups and all of my homedir in one place. Here's how I did it."
aliases = [ "/articles/svn_mail" ]
last_modified = "2006-05-18T16:26:32Z"
+++


Inspired by ['Keeping your life in subversion'][5] For some time now I
have been slowly migrating all of my personal home directories into the
[subversion][6] version control system and merging back so that I end up
with a spartan configuration and everything gets backed up. Fool that I
am, however, I want to take things one step further and also keep all
of my mail in version control too.

The benefits of keeping mail in a version control system are marginal.
Mails are not typically edited after they are received and sent, so a
lot of people use a system such as [unison][7] and find it more than
adequate. However, since everything else in my homedir is in subversion
I wanted the mail in there too. Happily for my purposes this is not too
hard.

The first thing is that I wanted a simple script that I can run after I
have read or filed my mail that indexes the mail and syncs it to
subversion. For indexing, I use [mairix,][8] which allows me to create
virtual folders and cooperates well with [mutt,][9] my favourite email
client. One possible solution to virtual folders is [here.][10] I decided
to do things a little differently, and here's the shell script that
does it all for me:

```sh
#!/bin/sh

set -e

TODAY=$( date -Iseconds )
cd "${HOME}/mail"
echo "Updating mail index..."
mairix -p       #add '-v' for more verbosity
echo "Emptying search folder"
rm -rf "${HOME}/mail/mfolder/"{cur,new,tmp}/*
echo "svn syncup"
svn status | awk '/^\?/{print $2}' | xargs -r svn add
svn status | awk '/^!/{print $2}' | xargs -r svn rm
svn ci -m "Mail sync for ${TODAY}"
```

Here's my .mairixrc:

```
base=/home/sean/mail
maildir=incoming...:sentmail...
mfolder=mfolder
database=/home/sean/mail/mairix_database
```

All that's needed to get it working in Mutt is to add ~/mail/mfolder to
the mailboxes my .muttrc, and add

```vim
macro index \e\/"<shell-escape>mairix " "Run a mairix search"
```

at the same time. Now, in
mutt to do a search I do Escape-/ and type a regex. All of the hits are
in ~/mail/mfolder and I change to that like a regular mailbox.

...and to keep it all up to date I just run my mailsync script every
now and again.

[5]: http://www.onlamp.com/pub/a/onlamp/2005/01/06/svn_homedir.html
[6]: http://subversion.tigris.org/
[7]: http://www.linuxjournal.com/article/7712
[8]: http://www.rc0.org.uk/mairix/
[9]: http://www.mutt.org/
[10]: http://larve.net/people/hugo/2003/scratchpad/VirtualFoldersInMutt.html
