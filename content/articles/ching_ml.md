+++
title = "I Ching in ML"
description = "In which I write yet another implementation of the book of changes (this time in ocaml)"
date = 2008-12-09T13:42:33Z
aliases = [ "/articles/ching_ml" ]
+++


I decided to rewrite my python I Ching in ocaml. This is interesting to
do in some respects as it's not really a traditional functional
programming task.

First we define the two basic oracles, the coin oracle and the yarrow
stalk oracle. Obviously on a computer we are actually sampling the same
probability distribution as the oracle, not simulating the process
itself. How I do this is to just make a static array of all the
outcomes and then choose from them with uniform probability. This is a
lot easier to write (and understand) than trying to make a multifaceted
biased coin and is equivalent from a probability point of view.

```Ocaml
let (consult_coin, consult_yarrow) =
  (** choose one item from a given array with uniform probability *)
  let choose arr =
    let size = Array.length arr in
    let idx = Random.int(size) in
    arr.(idx)
  in
  (* ...use this to consult the coin oracle... *)
  let consult_coin () =
    let outcomes = [|
      9; 9;               (* Moving Yang --- x --- *)
      7; 7; 7; 7; 7; 7;   (* Stable Yang --------- *)
      8; 8; 8; 8; 8; 8;   (* Stable Yin  ---   --- *)
      6; 6                (* Moving Yin  --- o --- *)
    |]
    in
      choose outcomes
  in
  (* ...and the yarrow oracle also. *)
  let consult_yarrow () =
    let outcomes = [|
      9; 9; 9;             (* Moving Yang --- x --- *)
      7; 7; 7; 7; 7;       (* Stable Yang --------- *)
      8; 8; 8; 8; 8; 8; 8; (* Stable Yin  ---   --- *)
      6;                   (* Moving Yin  --- o --- *)
    |]
    in
      choose outcomes
  in
    (consult_coin, consult_yarrow)
```

This is an example of how you define let binding which is private, yet
shared by more than one function. In this case it's "choose", a helper
function which just picks an element from an array. So we just define
two public functions:

```Ocaml
val consult_coin : unit -> int = <fun>
val consult_yarrow : unit -> int = <fun>
```

Given those two functions, it's easy to return a hexagram using a given
oracle.

```Ocaml
let get_hexagram ?(oracle=consult_yarrow) () =
  let rec pick lis =
    let len = List.length lis in
    if(len==6) then lis else pick ((oracle ())::lis)
  in
    pick []
```

A single divination actually derives two hexagrams, representing a
change from one state to another. The original single hexagram contains
"moving" lines which are inverted in the second one.

```ml
let get_hexagram_pair ?(oracle=consult_yarrow) ?(lines=[]) () =
  let lines = if(lines==[]) then (get_hexagram ~oracle ()) else lines in
  (* Given a hexagram, return a version with no moving lines by
   * simply disregarding their moving statement.  Moving yang becomes
   * yang, moving yin becomes yin *)
  let rec ignore_moving =
    function
        [] -> []
      | 9::res -> 7::(ignore_moving res)
      | 6::res -> 8::(ignore_moving res)
      | hd::res -> hd::(ignore_moving res)
  in
  (* Given a hexagram, return a version with no moving lines by
   * inverting moving lines.  Moving yang becomes yin, moving yin
   * becomes yang *)
  let rec invert_moving =
    function
        [] -> []
      | 9::res -> 8::(invert_moving res)
      | 6::res -> 7::(invert_moving res)
      | hd::res -> hd::(invert_moving res)
  in
    (ignore_moving lines),(invert_moving lines)
```

Now you have the guts of a working I Ching.
