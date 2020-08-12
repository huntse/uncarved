+++
title = "Ocaml objects part 1"
description = "Writing some objects in ocaml, we begin to make the pricer more flexible"
aliases = [ "/articles/ocaml_classes" ]
date = 2007-06-19T19:36:27Z
[taxonomies]
tags = ["computers"]
+++


The next in the somewhat haphazard series that began [here][5] in which I
learn a bit about ocaml objects, and in so doing, also learn why Joshi
proposes a parameter's class and how to calculate simple integrals.

The purpose of this exercise was to learn how to do object-oriented
programming in ocaml, so I pick up where Joshi suggests modifying the
Monte Carlo simulator to take "parameters" objects instead of floats
for vol and rates. The purpose of this modification is that ultimately
we will then be able to use functions as parameters to our models,
rather than just constants. I begin by defining the interface to these
"parameter" classes. This will define what these parameter objects can
do.
```Ocaml
(** interface for all parameter classes. Users of parameter classes expect
* this interface *)
class type parameter_type =
object
method integral :       float -> float -> float
method integral_sq :    float -> float -> float
method mean :           float -> float -> float
method root_mean_sq :   float -> float -> float
end;;

This is a direct translation of Joshi's interface. I'm not 100% sure we
really need this, but it does mean that differences between various
parameters classes and their private members can be hidden behind this
interface.

So given that, we can adapt the mc:
```Ocaml
(* Price an option with a flexible payoff using Monte Carlo.
*
* Use 'parameters' objects for vol and rates to allow passing flexible
* parameters *)
let sim ~payoff ~expiry ~spot ~vol ~r ~num_paths =
    let variance = vol#integral_sq 0.0 expiry in
    let root_variance = sqrt variance in
    let ito_correction = -0.5 *. variance in
    let integral_r = r#integral 0.0 expiry in
    let moved_spot = spot *. exp (integral_r +. ito_correction) in
    let rec do_path i running_sum =
        if i < num_paths then begin
            let this_gaussian = Gaussian.get_one_gaussian () in
            let this_spot = moved_spot *. (exp (root_variance *. this_gaussian)) in
            let this_payoff = payoff ~spot:this_spot in
            do_path (i+1) (running_sum +. this_payoff)
        end
        else (running_sum /. (float_of_int num_paths)) *. (exp (-1.0 *. integral_r))
    in
    do_path 0 0.0
    ;;
```

as you can see, the difference here is that we are calling the
"integral_sq" method on the vol parameter, and the "integral" method on
the rates parameter. If we put this into the toploop the type has
changed to:
```Ocaml
val sim :
payoff:(spot:float -> float) ->
expiry:'a ->
spot:float ->
vol:< integral_sq : float -> 'a -> float; .. > ->
r:< integral : float -> 'a -> float; .. > -> num_paths:int -> float = <fun>
```

So vol and r are params which have an integral and integral_sq method,
which have two arguments, and return a float in each case. We could get
rid of the polymorphic argument by explicitly specifying the type of
the expiry argument, but I'm not sure how to do that for named args.
~expiry:float gives a syntax error anyway- I suppose I could write an
explicit sig for the function but it works without it.

Now we can write the base parameters class. This is an abstract class-
derived classes will specify how to take the integral and the integral
of the square. In this mc model we don't use the concrete methods of
this class but presumably they come in handy later.
```Ocaml
(** base class specifying the mean and root_mean_sq methods in terms of
* the integral and integral_sq, but don't define those.  This allows us
* to define them for any type of parameter *)
class virtual parameter =
object(self)
    method virtual integral :       float -> float -> float
    method virtual integral_sq :    float -> float -> float
    method mean t1 t2 = (self#integral t1 t2) /. (t2 -. t1)
    method root_mean_sq t1 t2 = (self#integral_sq t1 t2) /. (t2 -. t1)
end;;
```

Now it's simplicity itself to write our first class, which models a
constant parameter:
```Ocaml
(** class for constant parameters.  This class will be hidden behind the
* parameter_type interface *)
class parameter_const' x =
object(self)
    inherit parameter
    val x_sq = x*.x
    method integral t1 t2 = (t2-.t1) *. x;
    method integral_sq t1 t2 = (t2-.t1) *. x_sq;
end;;
```

I add an alias to this (without the tick), which hides the
implementation behind the parameter_type interface:
```Ocaml
(** Constant parameters class with implementation hidden *)
class parameter_const x = (parameter_const' x : parameter_type);;
```

The type of parameter_const' is
```Ocaml
class parameter_const' :
float ->
object
    val x_sq : float
    method integral : float -> float -> float
    method integral_sq : float -> float -> float
    method mean : float -> float -> float
    method root_mean_sq : float -> float -> float
end
```

whereas the type of parameter_const is
```Ocaml
class parameter_const : float -> parameter_type
```

...which seems to express the idea of the class much better.

At this point we can run our Monte-Carlo using constant parameters by
doing this sort of thing:
```Ocaml
let mc payoff =
    Mc.sim
        ~payoff:payoff
        ~expiry:0.25
        ~spot:1.613
        ~vol:(new Param.parameter_const 0.35)
        ~r:(new Param.parameter_const 0.055)
        ~num_paths:num_paths
;;
```

If you're thinking "so what? That's no better than what we had before
except probably a bit slower and certainly harder to read", then I am
sympathetic to this point of view. [Next][6] we look at other parameters
classes and suddenly it starts to become useful.

[5]: /articles/ocaml_finance
[6]: /articles/ocaml_classes_2
