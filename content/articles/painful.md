+++
title = "That was painful"
description = "Migrating everything to a new server"
date = 2009-02-06T14:39:14Z
[taxonomies]
tags = ["computers"]
+++


So a couple of weeks ago I finally became annoyed enough at having to
use a virtual linux server that I shelled out the extra and was
upgraded to a dedicated box of my very own in co-lo. Mostly this was
totally seemless and I even looked forward to the differences given
that I was moving to Centos from Debian. One thing, however, was
extremely painful. Moving this website.

So uncarved.com uses a python script that I wrote ages ago using an
early version of [web.py.][5] However, at the time it had pretty whacky
database support, didn't have it's own template engine (so it used
Cheetah) and had a few wierd bugs which I had hacked around in my local
copy. As such, upgrading has been a real pain because I had to change
the code to the new api, then hack all my templates to the new syntax
(I initially tried to carry on using cheetah, but cheetah has changed
and it was even more excruciating to get that working so I took the
plunge). Anyway, it seems to have worked.

*Note:* This has all changed significantly in the last 11 years.

[5]: http://www.webpy.org/
