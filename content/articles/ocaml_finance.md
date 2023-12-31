+++
title = "Learning Functional Programming"
description = "I decided to teach myself ocaml by writing a derivatives pricer"
aliases = [ "/articles/ocaml_finance" ]
date = 2007-06-05T21:08:53Z
[taxonomies]
tags = ["computers"]
+++


I have been interested in functional programming for some time, but
finally decided to bite the bullet and learn properly, and that (for me
anyway) means writing some code to accomplish a practical task. My idea
is to reimplement most of the C++ code in [Mark Joshi's][5] excellent
book [C++ Design Patterns and Derivatives Pricing][6], but in [OCaml][7].
Now I'm a newcomer to [functional][8] programming and to ocaml, so what I
write won't be pretty or idiomatic, especially at first. To begin with
I'm learning from the main [tutorial][9]. If I find and use another I'll
post that too.

I will try to explain some of the financial stuff that's going on as I do so,
but for the full lowdown on why derivatives price the way they do, you need to
learn some financial maths. You could do a lot worse that picking up Joshi's
other book, [The Concepts and Practice of Mathematical Finance][10]. A lot of
people get [Hull][11], but I prefer Joshi for a really practical introduction
with great explanations of concepts. When I was at Goldman, a lot of people
were very sarcastic about Hull as a source. I don't really have a credible
opinion about that.

So without further ado, here is my first ocaml program, which defines
payoffs for vanilla European [put][12] and [call][13] options. In fact
Joshi starts off straight away with a [Monte Carlo][14] pricer, but my
copy is downstairs so I'm straying off-piste here. It's my intention to
follow Joshi step by step, and write up each one here as I go.
```Ocaml
open Printf

(* a vanilla option pays off the difference between the spot price
 * and the strike, or expires worthless *)
let put_payoff strike spot=
        max ( strike -. spot ) 0.0;;

let call_payoff strike spot=
        max (spot -. strike ) 0.0;;

let print_payoff payoff strike spot=
        let outcome=payoff strike spot in
        printf "%f\n" outcome;;

print_payoff call_payoff 195.0 190.0;;
print_payoff call_payoff 195.0 200.0;;
print_payoff put_payoff 195.0 190.0;;
print_payoff put_payoff 190.0 195.0;;
```


Now I'm running and writing this on [fedora][15] [Linux][16], and my ocaml
is 3.09.3. When I run this I see:
```
% ocaml tmp/payoff.ml
5.000000
0.000000
0.000000
5.000000
```

Which is what I would expect. Now this is very cheesy at present, but
it's a start and we'll improve it in the next [article.][17] It's worth a
couple of observations about this because already this demonstrates a
few things that strike me as being interesting about ocaml. For one
thing, there isn't any default type promotion or operator overloading,
so we need to explicitly qualify our constants with .0 to get them to
be floats. Secondly, we need to use -. to subtract them. The max
function can operate on any type so it works with floats or ints.

[5]: http://www.markjoshi.com/
[6]: http://www.markjoshi.com/design/index.htm
[7]: http://caml.inria.fr/ocaml/index.en.html
[8]: http://en.wikipedia.org/wiki/Functional_programming
[9]: http://www.ocaml-tutorial.org/
[10]: http://www.markjoshi.com/concepts/index.htm
[11]: http://www.amazon.com/Options-Futures-Other-Derivatives-6th/dp/0131499084/ref=pd_bbs_2/104-9802601-8884745?ie=UTF8&amp;s=books&amp;qid=1181022494&amp;sr=1-2
[12]: http://en.wikipedia.org/wiki/Put_option
[13]: http://en.wikipedia.org/wiki/Call_option
[14]: http://en.wikipedia.org/wiki/Monte_Carlo_method
[15]: http://fedoraproject.org/wiki/
[16]: http://www.linux.org/
[17]: /articles/ocaml_deriv_1
