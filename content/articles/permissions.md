+++
title = "How do unix file permissions work?"
description = "Unix provides fine-grained access control for files. It's important to understand it."
date = 2009-06-12T03:24:41Z
[taxonomies]
tags = ["computers"]
+++


### What unix file permissions are

At their most basic, unix file permissions are a set of bits which
control who has the permission to read from, write to and execute
files. They have similar, but slightly different meanings as applied to
directories. The mode is normally expressed either as a symbolic string
of gibberish or as a numeric mode.

### Numeric file permissions

A numeric mode is normally expressed as set of three or four octal
digits but can be any length up to four. Any ommitted digits are
assumed to be leading zeroes. The first digit is the sum of the "set
uid" (4), "set gid" (2), and "sticky" (1) attributes. If you need these
you know what they mean. Otherwise, move along please. The second digit
sets permissions for the owner of the file to read(4), write(2), and
execute(1) the file. The third sets permissions for members of the
group specified as the group owner of the file and the fourth for
people not in the file's group, with the same values for read, write
and execute as the user permission digit. You figure out what
permissions you need by adding the bits together. If I want a file to
be readable and writeable by me and its group and just readable by
others, I might run `chmod 664` file to change the mode of the file.

### Symbolic file permissions

commands which deal with file permissions often allow you to specify
symbolic permissions as follows: u user g group o other r read w write
x execute + add specified permission - remove specified permission =
make permission exactly equal to this

So in the example above, I could achieve the results I wanted by
`chmod ug=rw,o=r file` or by looking at the current file mode and using "+" or
"-" as appropriate. For example, to remove group and world write and
execute permissions on a file I might do `chmod go-wx file`. See `man chmod`
for more details. On linux boxes you may have to do `info chmod` to
get all the details because the GNU project don't like manual pages.

### Finding out file permissions

You can see a symbolic representation of the permissions on a file or
directory by using `ls -l`. If you want to understand why files you
create get the permissions they do, read about how [umasks][5] work.

### Special file permissions

I said "move along please", but to reward you for your persistence,
these are the meanings of the leftmost digit of four-digit octal file
permissions. Note: Do not use these unless you really know what you are
doing. The setuid and setgid bits on files in particular have been
responsible for many serious security breaches when thoughtlessly
applied to unworthy programs.

When set on files:

```
Numeric | Symbolic |  Name       | Meaning
-----------------------------------------------------------------------
4000    | u+s      | setuid bit  | If the file is executed, set the effective user id of the resultant process to the owner of the file.
2000    | g+s      | setgid bit  | If the file is executed, set the effective group id of t he resultant process to the group owner of the file.
1000    | t        | sticky bit  | No effect. On ancient systems it means "Save the text image of the program to swap to speed up load time".
```

When applied to directories, the meanings of these bits are subtly
different and more system- and filesystem-dependent:

```
Numeric | Symbolic |  Name                                  |  Meaning
-----------------------------------------------------------------------
4000    | u+s      | setuid bit                             | No effect
2000    | g+s      | setgid bit                             | Set the group owner of files created in this directory to the group of the group owner of the directory instead of the primary group of the file's creator
1000    | t        | sticky bit or "restricted delete flag" | On some systems it means prevent users from removing or renaming files in this directory unless they own the file or directory
```

[5]: /articles/umasks
