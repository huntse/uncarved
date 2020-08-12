+++
title = "How do unix umasks work?"
description = "Often file permission problems on unix systems are caused by users who don't understand their umask and set it properly"
date = 2009-06-12T03:24:41Z
[taxonomies]
tags = ["computers"]
+++

### What is a umask?

   A umask is a bitmask by means of which a user can affect the default
   permissions of files they create on unix systems. You should find out what
   [file permissions](https://www.uncarved.com/articles/permissions) are if you
   are unsure. Its important to fully appreciate that a umask is not a default
   permission *set* it is a default permission *mask* so bits in the mask are the
   bits which you want not to be in the permissions of the file. A umask of 777
   will thus mean that processes create files with permissions of zero whereas
   one of 0 will create files with full permissions thussly:

```
% umask 777
% touch foo
% umask 0
% touch bar
% ls -l foo bar
-rw-rw-rw-    1 sean   sean             0 Jul  2 11:15 bar
----------    1 sean   sean             0 Jul  2 11:15 foo
```
   Now you might well wonder why (if my umask is zero) the execute bits
   aren't also being set on "bar"? Lets see what "touch" is doing under
   the covers...
```
% strace touch furb 2>&1 | grep furb
execve("/bin/touch", ["touch", "furb"], [/* 137 vars */]) = 0
open("furb", O_WRONLY|O_NONBLOCK|O_CREAT|O_NOCTTY|O_LARGEFILE, 0666) = 3
utime("furb", NULL)                     = 0
```
   As you can see, the `touch` process only tries to create the file with
   permissions of 0666. The permissions requested at `open(2)` are then
   masked by the umask and the bits requested in the `open(2)` call that are
   not in the mask end up in the permissions of the file created.
   Processes (such as compilers) which know they are creating executable
   files will generally use `open(2)` with the execute bits set as well.
   Because umask is a mask it can't raise the permissions higher than the
   process asks for in the `open(2)` call. The same is true of any other
   process which opens files.

### How do I change my umask?

   Now, if you want to change your umask, the command you want is the
   shell builtin called `umask` not `/usr/bin/umask`. From `man umask`:

```
/usr/bin/umask

The umask utility sets the file mode creation  mask  of  the
current  shell  execution environment to the value specified
by the mask operand.  This mask affects the initial value of
the  file permission bits of subsequently created files.  If
umask is called in a subshell or separate utility  execution
environment, such as one of the following:
    (umask 002)
    nohup umask ...
    find . -exec umask ...
it does not affect  the  file  mode  creation  mask  of  the
caller's environment.

If the mask operand is  not  specified,  the  umask  utility
writes  the  value of the invoking process's file mode crea-
tion mask to standard output.
```

Let's just see if that's true, shall we?

```
% umask                 #check my current umask
022
% /usr/bin/umask 0      #try to change it using /usr/bin/umask
% umask                 #Did it work?  No!
022
% umask 0               #try to change it using the builtin umask
% umask                 #Did it work?  Yes!
000
```

So it is true. Why? The reason is that the shell does a `fork(2)` to create a
copy of itself to run the `/usr/bin/umask` process, so then even if that
process sets its own umask, those values happen in the child process and don't
end up in the calling process when the child quits. That's why you need the
shell builtin if you want to change your umask. If you don't understand, just
always type `umask` or `builtin umask` and never `/usr/bin/umask`.

Now you know why you need to use `chmod +x` to set the "execute" bits on the
things you want to be executable. In ancient (pre "git") times it was
particularly important to get file permissions set correctly before checking
them in to version control because all future checkouts of a file have the file
permissions which a file had when it was first checked in unless someone
tinkers in the repository.
