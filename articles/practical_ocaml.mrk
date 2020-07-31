---
Tags: computers
Last Modified:2007-06-13T06:41:39Z
---
# Using Ocaml in Practice

## Starting to learn how to make ocaml programs that are not just toys,
and extending the derivatives pricer further

My experience learning ocaml has been pretty enjoyable so far. A friend
told me about Jason Hickey's pdf book [Introduction][5] to the Objective
Caml Programming Language which is commendably brief and has really
helped as I go on to try ocaml further. The second thing that has
helped is that I have discovered [rlwrap,][6] so the toploop is no longer
such an unfriendly place to be.

Furthermore, I have split the pricer that I [began][7] developing
yesterday into a number of files and build them into a single
executable using ocamlc. First, gaussian.ml, containing the random
number functions:
open Random;;

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

(* get a gaussian through oversampling and subtraction *)
let get_one_gaussian_by_summation () =
let rec add_one limit count so_far =
if count==limit then so_far
else add_one limit (count+1) (so_far +. (Random.float 1.0)) in
(add_one 12 0 0.0) -. 6.0
;;

let get_one_gaussian = get_one_gaussian_by_box_muller

I added the summation method because when I first tried the pricer on
real data the numbers were hopeless (now they are just somewhat out of
line with market observables), and I suspected a bug in my random
numbers. I was correct, I did have incorrect random numbers.

Then I have payoff.ml, containing my payoff functions. I have added a
few more simple payoffs, and moved to named function arguments:
(** a vanilla option pays off the difference between the spot price
** and the strike, or expires worthless *)
let call ~strike ~spot = max (spot -. strike) 0.0;;
let put ~strike ~spot = max (strike -. spot) 0.0;;

let digital payoff = if payoff> 0.0 then 1.0 else 0.0;;
let digital_call ~strike ~spot = digital (call ~strike:strike ~spot:spot);;
let digital_put ~strike ~spot = digital (put ~strike:strike ~spot:spot);;

(** A double digital pays 1 if spot is between two barriers, zero
** otherwise *)
let double_digital ~low ~high ~spot =
assert (low < high);
if (low <= spot && spot <= high) then 1.0
else 0.0;;

mc1c.ml contains the actual Monte Carlo simulator, and it is unchanged
except to use named function arguments, and to qualify the name of the
get_one_gaussian function, which is now in a seperate file:
(* Price an option with a flexible payoff using Monte Carlo. *)
let sim ~payoff ~expiry ~spot ~vol ~r ~num_paths =
let variance = vol *. vol *. expiry in
let root_variance = sqrt variance in
let ito_correction = -0.5 *. variance in
let moved_spot = spot *. exp (r *. expiry +. ito_correction) in
let rec do_path i running_sum =
if i < num_paths then begin
let this_gaussian = Gaussian.get_one_gaussian () in
let this_spot = moved_spot *. (exp (root_variance *. this_gaussian))
in
let this_payoff = payoff ~spot:this_spot in
do_path (i+1) (running_sum +. this_payoff)
end
else (running_sum /. (float_of_int num_paths)) *. (exp (-1.0 *. r *. exp
iry))
in
do_path 0 0.0
;;

Finally I have my test file which runs the test cases. Now that I use
named function args I can partially-apply function args in any order,
so I make a test harness that sets up a particular marketdata scenario
and runs the pricer:
let print_mc ?(num_paths=100000) label payoff =
let mc payoff =
Mc1c.sim
~payoff:payoff
~expiry:0.2
~spot:161.3
~vol:0.35
~r:0.045
~num_paths:num_paths
in
Printf.printf "%s: %f\n" label (mc payoff)
;;

print_mc "call" (Payoff.call ~strike:160.0);;
print_mc "digital call" (Payoff.digital_call ~strike:160.0);;
print_mc "put" (Payoff.put ~strike:170.0);;
print_mc "digital put" (Payoff.digital_put ~strike:170.0);;
print_mc "double digital" (Payoff.double_digital ~low:160.0 ~high:170.0) ~num_pa
ths:250000;;

(* price one option, test the payoff against a target price and
* print the result  *)
let test_mc ?(num_paths=1000) ?(expiry=1.0) ?(r=0.0) label payoff target =
let mc payoff =
Mc1c.sim
~payoff:payoff
~expiry:expiry
~spot:161.3
~vol:0.35
~r:r
~num_paths:num_paths
in
let price = mc payoff in
let tolerance = 0.00001 in
Printf.printf "Test %s - price: %f target: %f\n" label price target;
assert( abs_float(price-.target) < tolerance )
;;

test_mc "Spot to one" (fun ~spot->1.0) 1.0;;
test_mc "Spot to zero" (fun ~spot->0.0) 0.0;;
let r = 0.05 in
let npv =  exp(-1.0 *. r) in
test_mc "Spot to one with rates" (fun ~spot->1.0) npv ~r:r;;

(* vim: set sw=4 ts=4 expandtab: *)

This is pretty cool. As you can see, I made the number of mc paths an
optional parameter. I have added a few assertions that trivial payoff
functions price correctly and that discounting works.

Now I build an object from each ml file using ocamlc and then compile
them all to a built object at the end. You need to be careful to do
them all in the correct order where you have functions defined in one
file, called in another, as we have here.

[1]: http://www.uncarved.com/articles/practical_ocaml
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.cs.caltech.edu/courses/cs134/cs134b/book.pdf
[6]: http://utopia.knoware.nl/~hlub/uck/rlwrap/
[7]: http://www.uncarved.com/blog/ocaml_deriv_1.mrk
[8]: http://www.uncarved.com/tags/computers
[9]: mailto:sean@uncarved.com
[10]: http://creativecommons.org/licenses/by-sa/4.0/
