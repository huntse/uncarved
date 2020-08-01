+++
title="Partial Function Application is not Currying"
description="These two related concepts are often confused.  Until yesterday I thought they were the same thing myself."
aliases=["/articles/not_currying", "/articles/not_currying.mrk"]
+++

Often you will see in computer books and articles a pattern where a function is
applied to some but not all of it's required arguments, resulting in a function
of fewer arguments.  In python, this looks like this (from [PEP 309](http://www.python.org/dev/peps/pep-0309/):

    def papply(fn, *cargs, **ckwargs):
        def call_fn(*fargs, **fkwargs):
            d = ckwargs.copy()
            d.update(fkwargs)
            return fn(*(cargs + fargs), **d)
        return call_fn

This is called "partial function application" - it returns a function which
acts like the function you pass in but which takes fewer arguments, the others
having been "bound in".  The author of this code, however, had the (very
common) misconception that this is
[currying](http://en.wikipedia.org/wiki/Currying), and called his function
"curry" as a result.  I shared this misconception for some time, and thought
that currying and partial application were the same thing.  In fact they are to
certain extent opposites.

Where partial application takes a function and from it builds a function which takes fewer arguments, currying builds functions which take multiple arguments by composition of functions which each take a single argument.  Thus we curry in python like this:

    def addN(n):
        return lambda x: x + n

    def plus(a, b):
        addA=addN(a)
        return addA(b)

Now why would we ever want to do that?  Well, in some pure functional languages
this is exactly how functions with multiple arguments are built up.  In ocaml,
a function which takes two ints and returns a float is actually a function
which takes an int and returns a function which takes an int and returns a
float.  In this world, partial application just happens without any extra code:

    % rlwrap ocaml
        Objective Caml version 3.09.3

    # let add a b=a+b;;
    val add : int -> int -> int = <fun>


So the type of `add` is a function which takes an int and returns a function
which takes an int and returns an int.

    # let add2=add 2;;
    val add2 : int -> int = <fun>

`add` is a curried function, so here we can partially apply by just calling
with a single arg- it returns the function that takes the other arg and returns
the result.

    # add2 34;;
    - : int = 36

...and we can call `add2` with a single argument as you would expect.  Because
ocaml curries `add` for us, the function has been partially applied.
It's interesting to note that in ocaml if you label your function arguments,
they can be partially applied in any order.

