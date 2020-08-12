+++
title = "Derivatives pricing in ocaml Part 1"
description = "Following on from the 'Learning Functional Programming' article, we write our first call pricer"
aliases = [ "/articles/ocaml_deriv_1" ]
date = 2007-06-06T08:54:54Z
[taxonomies]
tags = ["computers"]
+++


So from the first [article][5] we move on to write the first Monte Carlo
pricer. This is a very close translation of Joshi's implementation in
part 1.3 (listings 1.1 to 1.3) except that I don't read the values in
from stdin, I just hardcode them.

Writing this was fun, but I am extremely short of sleep so it was
actually trickier than I expected. It was made harder by the cryptic
error messages that ocaml gives you when things go wrong. These were
almost always This expression has type int but is here used with type
float which means you are passing int arguments to a float operator or
function, rather than the other way around.
```
% ocaml
Objective Caml version 3.09.3

# 1 /. 2;;
This expression has type int but is here used with type float
# 1.0 / 2.0;;
This expression has type float but is here used with type int
```
I hope that makes it a little clearer. I find it confusing anyway. It's
like the error message has been written by someone for whom English is
a second language. Perhaps that's the case.

Here's the listing without further ado. On my computer it does a
million paths in 13.2 seconds which is pretty decent I think. The
ocamlc compiler is fast as lightning too, compiling this to an
executable in 0.029 secs on my machine. If I go on learning ocaml I
won't be able to go and get coffee while waiting for my code to
compile.
```Ocaml
(* mc1.ml - A rudimentary European call option pricer designed to mimic
* listings 1.1 to 1.3 in Joshi.
*
* Written by Sean Hunter <sean@uncarved.com>
*
* This is demonstration code only.  You are free to use it under the
* Creative Commons Attribution 2.5 license, but don't expect it to
* accurately price real options.
*)
open Random;;
open Printf;;

(* initialize the random number generator *)
Random.self_init;;

(* get a random gaussian using a Box-Muller transform, described
 * here http://en.wikipedia.org/wiki/Box-Muller_transform *)
let rec get_one_gaussian_by_box_muller () =
    (* Generate two uniform numbers from -1 to 1 *)
    let x = Random.float 2.0 -. 1.0 in
    let y = Random.float 2.0 -. 1.0 in
    let s = x*.x +. y*.y in
    if s > 1.0 then get_one_gaussian_by_box_muller ()
    else x *. sqrt (-2.0 *. (log s) /. s)
    ;;

(* Price a European call using Monte Carlo.
 *
 * We pre-compute as much as possible before the simulation, then the
 * actual mc paths are done as a nested recursive function.  This seems
 * more idiomatically functional even though ocaml has for loops.
 *
 * It's also good because I couldn't get the other way to work.*)
let simple_monte_carlo1 expiry strike spot vol r num_paths =
    let variance = vol *. vol *. expiry in
    let root_variance = sqrt variance in
    let ito_correction = -0.5 *. variance in
    let moved_spot = spot *. exp (r *. expiry +. ito_correction) in
    let rec do_path i running_sum =
        if i < num_paths then begin
            let this_gaussian = get_one_gaussian_by_box_muller () in
            let this_spot = moved_spot *. (exp (root_variance *. this_gaussian)) in
            let this_payoff = max (this_spot -. strike) 0.0 in
            do_path (i+1) (running_sum +. this_payoff)
        end
        else (running_sum /. (float_of_int num_paths)) *. (exp (-1.0 *. r *. expiry))
    in
    do_path 0 0.0
    ;;

(* price a three-month call option near to the money.
 * we are using 35% vol and 4.5% interest rates*)
printf "%f\n" (simple_monte_carlo1 0.2 160.0 161.3 0.35 0.045 250000);;
```
This, however, is crying out for more flexibility. The first thing to
do is to see if we can get it to price other simple payoffs. That's the
subject of the [next][6] article.

[1]: http://www.uncarved.com/articles/ocaml_deriv_1
[5]: /articles/ocaml_finance
[6]: /articles/ocaml_deriv_2
