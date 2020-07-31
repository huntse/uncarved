+++
tags = "computers"
last_modified = "2009-08-20T21:35:41Z"
+++
# Which language would you use?

## It depends

I got a mail a few days ago about how I wrote a couple of articles with
code for an options pricer in ocaml but all my latest articles were
about scala. So which language would I use today if I were to write an
options pricer. The answer of course is "it depends".

Now in and of themselves both ocaml and scala are fine choices for
writing just about anything. But there are tradeoffs. If I was in
charge of development of a brand new pricing and risk infrastructure
for a big bank that had to be able to price everything from a stock to
a digital multi-asset multi-barrier callable bermudan range-accrual
thingummybobber that was going to be worked on by a thousand people
ranging from the lowliest intern to the most brilliant genius then I
have no hesitation in saying I would use scala.

In fact a friend of mine who is in charge of the development of risk
and pricing systems at a major wall st firm told me that if he was
building this infrastructure far a bank from scratch today he would use
scala. He's the guy who persuaded me to try scala in the first place as
a matter of fact.

The reasons this would be a fine choice should be obvious- it's very
simple to write serious software in scala, it shouldn't take anyone of
reasonable ability much time at all to learn, the syntax is not overly
burdensome and tedious, performance is adequate or better for most
things, the concurrency paradigm is tractable by normal human beings
and there is fantastic library support because you can just use java
stuff. The extensible syntax would help for various things and the
cross-platform support is always a nice thing to have if you want to
have number-crunching on a Linux compute farm and desktop apps on
Windows or whatever.

On the other hand if I was setting up a small quant trading shop/hedge
fund or doing it for my own benefit then the choices are much more
varied. I might use scala still (it would still be an excellent
choice), I might do it in ocaml (or even Haskell in fact), particularly
if I was going to be all or most of the programming myself or I had
access to recruit a decent pipeline of smart functional-programming
aware people.

The benefits of doing it in ocaml (or Haskell) would be that I would
probably have a more mentally-stimulating time doing it (this is can be
an important motivation also if you have a super-bright team), and
would probably end up with something more aesthetically pleasing from a
pure comp-sci point of view.

On the other hand I would certainly have more frustrations (eg Why has
no-one noticed that you can only do one request through the ocaml curl
library because there is a memory scribble? But I digress). I wouldn't
really want to lead a group of 100 guys and have to keep teaching
haskell monad combinators or whatever every time a new person joined.
And maintaining/code reviewing etc could become excruciating when you
were dealing with people of average ability less one or two standard
deviations.

So horses for courses. Ultimately writing good software always requires
thought, discipline and some skill. The right language fits the problem
domain and suits the group and organization. Good programmers can learn
to write good software in any language.

[1]: http://www.uncarved.com/articles/language
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/tags/computers
[6]: mailto:sean@uncarved.com
[7]: http://creativecommons.org/licenses/by-sa/4.0/
