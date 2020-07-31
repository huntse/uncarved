+++
Tags: computers
Last Modified:2009-08-22T06:29:35Z
+++
# n-Bit Gray codes in Haskell

## A first step in what will become a combinatorics library

I have been playing around with Gray's reflected binary code (aka
[Gray][5] codes) and similar things a bit. Before I reveal why I'm doing
this lets just dive in and write some code. Gray's algorithm is
described well [here.][6] The code which follows is in [7]haskell,
because it's a really fantastic language and I'm playing around with it
at the moment. For scala fans, don't worry. I haven't abandoned scala,
this is a parallel effort.

So for starters we need a datatype for representing these things. This
is how you define an algebraic datatype in haskell. In what follows,
lines beginning "--" are single-line comments
-- | 'Bit' is the datatype for representing a bit in a gray code.
data Bit = Zero | One deriving Show

Alright. So we have a type "Bit" with two constructors Zero and One and
a "deriving Show" which means haskell figures out how to turn it into a
string. This is useful when you're in ghci (the interactive haskell
environment) debugging.
-- prepend a given item onto each of a list of lists (probably something to do t
his in the prelude)
prepend :: a -> [[a]] -> [[a]]
prepend t xs = map (t:) xs

A teeny helper function. Given a list of lists and a thing it sticks
the thing on the front of each list in the outer list. This would
append the thing on the end of each list:
append :: a -> [[a]] -> [[a]]
append t xs = map (++[t]) xs

Note I'm writing the type signatures explicitly but there's absolutely
no problem if you leave them off. So let's generate our Gray codes:
-- | 'gray' generates the gray code sequence of length 'n'
gray :: Int -> [[Bit]]
gray 1 = [ [Zero], [One] ]
gray n = prepend Zero (gray (n-1)) ++ prepend One (descGray (n-1))

-- | 'descgray' generates the reversed gray code sequence of length 'n'
descGray :: Int -> [[Bit]]
descGray 1 = [ [One], [Zero] ]
descGray n = prepend One (gray (n-1)) ++ prepend Zero (descGray (n-1))

So we get an ascending and a descending one for free. Since the
descending one is just the ascending one in reverse why (you might say)
don't I just define descGray as descGray = reverse.gray ? Indeed, that
may be a reasonable thing to do. I'm doing it this way to try to
preserve as much laziness as possible, and (although my haskell-fu is
still very weak at the moment) I think that if you reverse a list you
pretty much have to evaluate each thing in the list. If you read the
paper you'll see that this is Gray's (naive) algorithm and there has
been an astonishing amount of research in this area leading to more
efficient algorithms. I'll give those a crack at some point.

Why am I doing this? You'll see. This is at the heart of building a
really cool combinatorics library. I needed something that could
enumerate all combinations and permutations of various generic
distribution-type things. There are similar but more recent orderings
that are comparable to gray codes which I'm also looking into. They'll
all be presented here in due course.

[1]: http://www.uncarved.com/articles/gray_codes
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://en.wikipedia.org/wiki/Gray_code
[6]: http://www.cs.auckland.ac.nz/CDMTCS//researchreports/304bob.pdf
[7]: http://www.haskell.org/
[8]: http://www.uncarved.com/tags/computers
[9]: mailto:sean@uncarved.com
[10]: http://creativecommons.org/licenses/by-sa/4.0/
