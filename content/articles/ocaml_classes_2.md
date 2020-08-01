+++
title = "Ocaml objects part 2"
description = "Parameter objects make more sense when we pass piecewise functions to the pricer"
aliases = [ "/articles/ocaml_classes_2" ]
last_modified = "2007-06-21T06:30:35Z"
+++


Unfortunately the class for constant parameters that we developed
[before][5] is just not that useful. We would be better off just using a
float if that was all we wanted. The advantage is, however, that we
have defined the interface we need for these functions, and what we
need is something that can return us the integral of a function and the
integral of the square of a function in an interval:
method integral :       float -> float -> float
method integral_sq :    float -> float -> float

If we can do that, we can use our function in the mc pricer, so let's
define a 'parameters' class for linear functions. This will take two
coefficients a and b and our parameter will model the function f(x) =
ax + b . The integral of f(x) dx is ax^2 + bx because we're trying to
find the area under a triangle for the first term and a rectangle for
the second. I needed a little help with f(x)^2 dx (thanks Iain!), but
here it is:
(** Parameter class that models a linear function f(x) -> ax + b *)
class parameter_linear' a b =
object(self)
inherit parameter
method integral t1 t2 =
let integrate_to x = 0.5 *. x *. a *. x +. x *. b in
integrate_to t2 -. integrate_to t1
method integral_sq t1 t2 =
a ** 2.0 *. (t2 ** 3.0 -. t1 ** 3.0) +.
a *. b *. (t2 ** 2.0 -. t1 ** 1.0) +.
b ** 2.0 *. (t2 -. t1)
end;;

class parameter_linear a b = (parameter_linear' a b : parameter_type);;

This works fine, but what we really want is [piecewise][6] functions and
piecewise constants. These give us the ability to have parameters that
we can calibrate to observable data:
(** For piecewise constants and piecewise linear functions a "piece" is a
* parameter that applies between low and high limits. *)
type piece = Piece of float * float * parameter_type;;

This is what we are going to use to make the pieces of our piecewise
functions- a tuple of low and high limits, and a parameter object that
can give us the integrals in these limits. Integrating the piecewise
function then becomes walking the list of pieces and integrating
everything that is in the region we are interested in.
(** Class for piecewise parameters.  Takes a list of pieces which each
* specify the limits and the linear or const parameter in each region.
*
* At present, does no checking that the pieces are continuous and not
* overlapping *)
class parameter_piecewise' pieces =
(* there's probably a better way of doing this, but anyway...
* Apply a function to each piece, with the parameters being the part of
* the interval from t1 to t2 that is inside the interval of the piece *)
let visit_pieces pieces fn t1 t2 =
let visit_piece piece low high =
if (low > t2 || high < t1) then
0.0
else
let range_start = max t1 low in
let range_end = min t2 high in
(fn piece) range_start range_end in
let rec visit_list so_far lis =
match lis with
[][] -> so_far (** we're done *)
| Piece(low, high, p) :: rest -> visit_list (so_far +. (visit_piece p
low high)) rest
in
visit_list 0.0 pieces
in
object(self)
inherit parameter
method integral t1 t2 = visit_pieces pieces (fun x->x#integral) t1 t2
method integral_sq t1 t2 = visit_pieces pieces (fun x->x#integral_sq) t1 t2
end;;

(** Piecewise parameters class with implementation hidden *)
class parameter_piecewise x = (parameter_piecewise' x : parameter_type);;

As you can see, I have a local visitor function which walks the list of
pieces and calls the right method on each one. I do this using a nifty
little tail-recursive pattern-matcher. This works but I am a bit
dissatisfied with the way I have to trick visit_pieces into calling the
integral or integral_sq methods. There is a better way I'm sure- I just
don't know what it is yet.

I could leave this implementation and it would be
functionally-complete, but it would be a bit of a pain to build the
piecewise functions, so I make a couple of little helper functions:
(** helper funcs to make parts of a piecewise function *)
let make_const_piece low high x = Piece(low, high, new parameter_const x);;
let make_linear_piece low high a b = Piece(low, high, new parameter_linear a b);
;

They're still not ideal- I would like to give a list of 2-tuples
specifying the upper bound and a point for each piece, and have the
function return the piecewise function or constant that "join the
dots", but anyway this gives us the ability to make lists of pieces by
doing this sort of thing:
(* price one option and print the result  *)
let print_mc ?(num_paths=100000) label payoff =
let pieces = [
Param.make_const_piece 0.0 0.25 0.35;
Param.make_const_piece 0.25 1.0 0.25;
] in
let vol=new Param.parameter_piecewise pieces in
let mc payoff =
Mc.sim
~payoff:payoff
~expiry:0.25
~spot:1.613
~vol:vol
~r:(new Param.parameter_const 0.055)
~num_paths:num_paths
in
Printf.printf "%s: %f\n" label (mc payoff)
;;

Note that our piecewise const parameter doesn't require the function to
be continuous. Given this vol function, we can price as before.

[1]: http://www.uncarved.com/articles/ocaml_classes_2
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/blog/ocaml_classes.mrk
[6]: http://mathforum.org/library/drmath/sets/select/dm_piecewise.html
[7]: http://www.uncarved.com/tags/computers
[8]: mailto:sean@uncarved.com
[9]: http://creativecommons.org/licenses/by-sa/4.0/
