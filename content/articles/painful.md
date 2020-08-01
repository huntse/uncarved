+++
title = "That was painful"
last_modified = "2009-02-06T14:39:14Z"
+++
# That was painful

## Migrating everything to a new server

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

[1]: http://www.uncarved.com/articles/painful
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.webpy.org/
[6]: http://www.uncarved.com/tags/computers
[7]: mailto:sean@uncarved.com
[8]: http://creativecommons.org/licenses/by-sa/4.0/
