+++
title = "Testing for put/call parity"
description = "Now let's check the prices from the ocaml Monte-Carlo pricer against the most obvious arbitrage relationship"
aliases = [ "/articles/put_call_parity" ]
last_modified = "2007-06-13T15:59:36Z"
+++


[Put][5] call parity is an important relationship in options pricing.
Let's test our prices to see if they obey this relationship.

To do so I add a simple helper function to payoff.ml to get the npv of
some future cash:
```Ocaml
(* get the net present value of some amount *)
let npv ~amt ~rate ~time = amt *. exp(-1.0 *. rate *. time);;
```

...and the tests themselves. Note that the put/call parity relationship
for digitals is slightly different:

```Ocaml
let assert_nearly ?(tolerance = 0.001) label a b =
    Printf.printf "Test %s - a: %f b: %f\n" label a b;
    assert( abs_float(a-.b) <tolerance );;

let spot = 1.613 in
let expiry = 0.25 in
let r = 0.055 in
let strike = 1.600 in
let discount x = Payoff.npv ~rate:r ~time:expiry ~amt:x in
let mc payoff =
    Mc1c.sim
        ~payoff:payoff
        ~expiry:expiry
        ~spot:spot
        ~vol:0.35
        ~r:r
        ~num_paths:100000 in
let price payoff = mc (payoff ~strike:strike) in
assert_nearly
    "Put call parity"
    ((price Payoff.call) +. (discount strike))
    ((price Payoff.put) +. spot);
assert_nearly
    ~tolerance:0.01
    "Digital put/digital call parity"
    ((price Payoff.digital_put) +. (price Payoff.digital_call))
    (discount 1.0)
;;
```

Here's the output:
```
Test Put call parity - a: 1.707748 b: 1.708199
Test Digital put/digital call parity - a: 0.982665 b: 0.986344
```

Trebles all round! The prices are ok. It's also interesting that ocaml
is actually even faster than I thought. I was running bytecode and if
you use ocamlopt to create native code my examples run about five times
faster.

[5]: http://www.investopedia.com/articles/optioninvestor/05/011905.asp
