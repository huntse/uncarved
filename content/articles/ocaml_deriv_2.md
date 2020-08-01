+++
tags = "computers"
aliases = [ "/articles/ocaml_deriv_2" ]
last_modified = "2007-06-06T08:58:44Z"
+++
# Derivatives pricing in ocaml Part 2

## Extending the basic mc pricer to handle different payoffs, we see how partial function application works

This is the third article in a series on using functional programming
for financial applications which started [here.][5]

So given our [first][6] Monte Carlo simulator, and the [7]payoff
functions that we started with, it's easy to see how we extend the
pricer to handle Joshi's first question at the end of chapter 1 (to
price puts):
(* mc1b.ml - A rudimentary option pricer to answer the exercises at the
* end of chapter 1 in Joshi.
*
* Written by Sean Hunter <sean@uncarved.com>
*
* This is demonstration code only.  You are free to use it under the
* terms of the Creative Commons Attribution 2.5 license, but don't
* expect it to accurately price real options.
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

(* a vanilla option pays off the difference between the spot price
* and the strike, or expires worthless *)
let put_payoff strike spot =
max ( strike -. spot ) 0.0;;

let call_payoff strike spot =
max (spot -. strike ) 0.0;;

(* Price an option with a flexible payoff using Monte Carlo. *)
let simple_monte_carlo_1a payoff expiry strike spot vol r num_paths =
let variance = vol *. vol *. expiry in
let root_variance = sqrt variance in
let ito_correction = -0.5 *. variance in
let moved_spot = spot *. exp (r *. expiry +. ito_correction) in
let rec do_path i running_sum =
if i < num_paths then begin
let this_gaussian = get_one_gaussian_by_box_muller () in
let this_spot = moved_spot *. (exp (root_variance *. this_gaussian))
in
let this_payoff = payoff strike this_spot in
do_path (i+1) (running_sum +. this_payoff)
end
else (running_sum /. (float_of_int num_paths)) *. (exp (-1.0 *. r *. exp
iry))
in
do_path 0 0.0
;;

(* price one put and one call option struck at the money *)
printf "%f\n" (simple_monte_carlo_1a call_payoff 0.025 195.5 195.5 0.20 0.045 10
0000);;
printf "%f\n" (simple_monte_carlo_1a put_payoff 0.025 195.5 195.5 0.20 0.045 100
000);;

So we pass a payoff function into the Monte Carlo simulator and call
that function for each path. This isn't quite general enough to handle
double digitals though. A double digital is an option that pays 1 if
the spot is between two barrier prices at expiry and zero otherwise.
However, the payoff function here has to take the strike and the spot.
This is where one of the great features of functional programming comes
in: partial function application. In ocaml, if you call a function that
takes 2 parameters, but give it only one, the return type is a function
that takes one parameter. Amazingly partial function application is
just there by default and there's no need for tedious binders like
there are in the STL in C++ for example. This will explain:
% ocaml

Objective Caml version 3.09.3

# let myadd x y=x+y;;
val myadd : int -> int -> int = <fun>
# let add2=myadd 2;;
val add2 : int -> int = <fun>
# add2 5;;
- : int = 7
# add2 16;;
- : int = 18

So myadd adds two numbers, and by calling it with just one (a 2) we
create a function that takes one argument and adds two to it. This is
exactly what we need for our flexible payoff function. You can think of
the partially applied function args as being all the things that are
constant on the termsheet of the trade. Our payoff functions remain the
same, except we add one for double digitals:
let double_digital_payoff low high spot =
if (low <= spot && spot <= high) then 1.0
else 0.0;;

...and we change the mc pricer to just call the payoff func with the
spot on the current mc path. We will partially-apply any other
arguments the payoff functions need when we invoke the pricer:
(* Price an option with a flexible payoff using Monte Carlo. *)
let simple_monte_carlo_1b payoff expiry spot vol r num_paths =
let variance = vol *. vol *. expiry in
let root_variance = sqrt variance in
let ito_correction = -0.5 *. variance in
let moved_spot = spot *. exp (r *. expiry +. ito_correction) in
let rec do_path i running_sum =
if i < num_paths then begin
let this_gaussian = get_one_gaussian_by_box_muller () in
let this_spot = moved_spot *. (exp (root_variance *. this_gaussian))
in
let this_payoff = payoff this_spot in
do_path (i+1) (running_sum +. this_payoff)
end
else (running_sum /. (float_of_int num_paths)) *. (exp (-1.0 *. r *. exp
iry))
in
do_path 0 0.0
;;

Now see how we call this pricer. It's simplicity itself:
printf "%f\n" (simple_monte_carlo_1b (call_payoff 160.0) 0.2 161.3 0.35 0.045 25
0000);;
printf "%f\n" (simple_monte_carlo_1b (put_payoff 170.0) 0.2 161.3 0.31 0.045 250
000);;
printf "%f\n" (simple_monte_carlo_1b (double_digital_payoff 160.0 170.0) 0.2 161
.3 0.29 0.045 250000);;

I find this immensely pleasing. I have hardly started learning the
language, and yet generalising this code was simplicity itself due to
features in the language. Partial function application is available in
imperative languages (C++ notably uses it to provide predicates and
adaptable functions in the STL), but there is a lot of nasty additional
syntax. The way it works so seemlessly in ocaml is terrific.

Its worth coming back to earth a little bit with the observation that
the prices that I am seeing from this thing right now don't match those
I can observe in the market so I am sure there is some debugging yet to
do. I would also like to make the code into a few modules, but I am not
sure how you do that in ocaml yet.

[1]: http://www.uncarved.com/articles/ocaml_deriv_2
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/blog/ocaml_finance.mrk
[6]: http://www.uncarved.com/blog/ocaml_deriv_1.mrk
[7]: http://www.uncarved.com/blog/ocaml_finance.mrk
[8]: http://www.uncarved.com/tags/computers
[9]: mailto:sean@uncarved.com
[10]: http://creativecommons.org/licenses/by-sa/4.0/
