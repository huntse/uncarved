+++
tags = "computers"
aliases = [ "/articles/testing_ocaml" ]
last_modified = "2007-06-21T06:34:44Z"
+++
# A Simple Ocaml test harness

## It's nice to be able to write tests for code as you go along, so you need a test harness...

I usually like to be able to write tests as I write code, and to have
them run every time the code builds to make sure I haven't broken
anything. To do this, you need a test harness so that adding tests is
as painless as possible. So I wrote this one:
(** test.ml - a simple test harness in ocaml

This is demonstration code only.  You are free to use it under the
terms of the Creative Commons Attribution 2.5 license.

@author Sean Hunter <sean\@uncarved.com>

*)

(** Test harness class.  Tracks numbers of tests run and how many
succeed. *)
class harness =
object(self)
(** The number of tests so far *)
val mutable n = 0

(** The number of tests so far which have succeeded *)
val mutable succeeded = 0

(** A name for the group of tests currenly running *)
val mutable group = ""

(** Runs a predicate function and fails if it throws or
returns false.  Otherwise it succeeds *)
method pass_if desc pred =
n <- n + 1;
let dots = String.make (50-(min 50 (String.length desc))) '.' in
Printf.printf "%5.5d: %s ....%s" n desc dots;

try
if pred () then
begin
Printf.printf "ok\n" ;
succeeded <- succeeded + 1;
true
end
else
begin
Printf.printf "not ok\n";
false
end
with
_ ->Printf.printf "not ok (threw exception)\n"; false

(** Runs a predicate function and fails if it throws or
returns true.  Otherwise it succeeds *)
method fail_if desc pred = self#pass_if desc (fun () -> not pred)

(** Takes a bool and marks the test as succeeded if it is true *)
method ok desc x = self#pass_if desc (fun () -> x)

(** Takes a bool and marks the test as failed if it is true *)
method not_ok desc x = self#ok desc (not x)

(** Evaluate a predicate, ignoring its result. Succeed if it throws
an exception, fail if not *)
method pass_if_throws desc (pred : unit -> bool) =
try
(ignore (pred ()));
self#not_ok desc true
with
exn -> self#ok desc true

(** Evaluate a predicate, ignoring its result. Fail if it throws
an exception, succeed if not *)
method fail_if_throws desc (pred : unit -> bool) =
try
(ignore (pred ()));
self#ok desc true
with
exn -> self#not_ok desc true

(** Check that two floats are within a certain tolerance *)
method pass_if_close ?(eps=1e-9) desc x y =
let diff = abs_float (x-.y) in
self#ok desc (diff <= eps)

(** mark the beginning of a group of tests *)
method start_group name =
n <- 0 ;
succeeded <- 0;
group <- name ;
Printf.printf "Begin test group %s\n" group

(** mark the end of a group of tests, printing out success count *)
method end_group  =
Printf.printf "End test group %s: %d of %d tests passed\n"
group succeeded n
end;;

(* vim: set syn=ocaml sw=4 ts=4 expandtab: *)

Now it's very easy for me to write tests. For example, tests for all my
[payoff][5] functions might look like this:
(** payoff_tests.ml - tests for payoff classes

Written by Sean Hunter <sean@uncarved.com>

This is demonstration code only.  You are free to use it under the
terms of the Creative Commons Attribution 2.5 license, but don't
expect it to accurately price real options.

*)

let tests = new Test.harness;;

tests#start_group "payoff.ml";;

(* tests for vanilla put and call payoffs *)
tests#ok "Vanilla ITM call" ((Payoff.call 100.0 110.0) = 10.0);;
tests#ok "Vanilla ATM call" ((Payoff.call 100.0 100.0) = 0.0);;
tests#ok "Vanilla OTM call" ((Payoff.call 100.0 90.0) = 0.0);;
tests#ok "Vanilla ITM put" ((Payoff.put 100.0 10.0) = 90.0);;
tests#ok "Vanilla ATM put" ((Payoff.put 100.0 100.0) = 0.0);;
tests#ok "Vanilla OTM put" ((Payoff.put 100.0 190.0) = 0.0);;

(* tests for digital payoffs *)
tests#ok "Digital ITM call" ((Payoff.digital_call 100.0 110.0) = 1.0);;
tests#ok "Digital ATM call" ((Payoff.digital_call 100.0 100.0) = 0.0);;
tests#ok "Digital OTM call" ((Payoff.digital_call 100.0 90.0) = 0.0);;
tests#ok "Digital ITM put" ((Payoff.digital_put 100.0 10.0) = 1.0);;
tests#ok "Digital ATM put" ((Payoff.digital_put 100.0 100.0) = 0.0);;
tests#ok "Digital OTM put" ((Payoff.digital_put 100.0 190.0) = 0.0);;
let dd = Payoff.double_digital ~low:90.0 ~high:110.0;;
tests#ok "Double Digital below the low barrier" ((dd 89.0) = 0.0);;
tests#ok "Double Digital at the low barrier" ((dd 90.0) = 1.0);;
tests#ok "Double Digital inside the low barrier" ((dd 90.1) = 1.0);;
tests#ok "Double Digital inside the high barrier" ((dd 109.9) = 1.0);;
tests#ok "Double Digital at the high barrier" ((dd 110.0) = 1.0);;
tests#ok "Double Digital above the high barrier" ((dd 110.1) = 0.0);;

tests#end_group;;

(* vim: set syn=ocaml sw=4 ts=4 expandtab: *)

...and when I run the tests the output looks like this:
Begin test group payoff.ml
00001: Vanilla ITM call ......................................ok
00002: Vanilla ATM call ......................................ok
00003: Vanilla OTM call ......................................ok
00004: Vanilla ITM put .......................................ok
00005: Vanilla ATM put .......................................ok
00006: Vanilla OTM put .......................................ok
00007: Digital ITM call ......................................ok
00008: Digital ATM call ......................................ok
00009: Digital OTM call ......................................ok
00010: Digital ITM put .......................................ok
00011: Digital ATM put .......................................ok
00012: Digital OTM put .......................................ok
00013: Double Digital below the low barrier ..................ok
00014: Double Digital at the low barrier .....................ok
00015: Double Digital inside the low barrier .................ok
00016: Double Digital inside the high barrier ................ok
00017: Double Digital at the high barrier ....................ok
00018: Double Digital above the high barrier .................ok
End test group payoff.ml: 18 of 18 tests passed

[1]: http://www.uncarved.com/articles/testing_ocaml
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/blog/practical_ocaml.mrk
[6]: http://www.uncarved.com/tags/computers
[7]: mailto:sean@uncarved.com
[8]: http://creativecommons.org/licenses/by-sa/4.0/
