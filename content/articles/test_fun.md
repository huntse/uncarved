+++
tags = "computers"
aliases = [ "/articles/test_fun" ]
last_modified = "2008-06-16T07:29:20Z"
+++
# A Functional Test Harness

## Using monads to thread state, we make a purely functional version of the test harness

To paraphrase Crocodile Dundee, this isn't a monad tutorial [this][5] is
a monad tutorial. However, I decided to do something that would help me
to understand monads, and that is to use them in a practical way.

The [object-oriented][6] test framework we developed doesn't feel very
idiomatic and as I learn more about FP, and it feels as if we could do
something a lot nicer. So I set about thinking so how to make a purely
functional test framework. The first thing that strikes you is how
useful state is. In a purely functional framework we have to thread
that state through our functions, and one elegant way to do that is
through monads.

Now if you read the monad tutorial, you will realise that a monad is a
magic box and all you can really do with a monad is put something in
the box, or apply a function which will return another magic box. This
is all very well, but its not great at explaining how (in a practical
sense) anything actually gets done.

We start with what it's going to look like when you actually use the
functional test api:
Test.test_begin >>=
Test.ok "Something which should be true" true_thing >>=
Test.not_ok "Something which should not be false" false_thing >>=
Test.fail_if "This should raise an exception" (fun () -> raise (Failure "aiee"))
>>=
Test.test_end

The >>= is borrowed from Haskell, and is the "bind" operator, which
acts as the glue here, sending the state from one function to the next.
So our first function (test_begin) needs to create the monad and bung
in the starting state. The rest of the functions accept as their last
argument the current state in its native form and return the updated
state in the State monad. This means that after the arguments that you
see above have been applied, they are candidates for the "bind"
function.

So without further ado, our monad:
(** The basic type sig of a monad *)
module type MONAD = sig
type 'a t
val return : 'a -> 'a t
val bind : 'a t -> ('a -> 'b t) -> 'b t
end

(** our state monad which will bind all our tests together *)
module State : MONAD = struct
type 'a t = 'a
let return x = x
let bind m f = f m
end

It would be pretty hard to make anything simpler than that, but it
fulfills the requirements to be a monad and it turns out a little goes
a long way. Here's our functional test module:
module Test = struct
(** the actual state which gets threaded through each fn *)
type test_state = {n:int; ok:int}

(** helper fns which return the state when it has succeeded or failed *)
let succeeded s = State.return {n=s.n+1; ok=s.ok+1}
let failed s = State.return {n=s.n+1; ok=s.ok}

(** Pass the initial state into the State monad *)
let test_begin = State.return {n=0; ok=0}

(** we use this func tos implement all the rest.  It takes a string and a
predicate, and the state, then succeeds if the predicate returns true. *)
let pass_if desc pred s =
let dots = String.make (50-(min 50 (String.length desc))) '.' in
Printf.printf "%5.5d: %s ....%s" s.n desc dots;
try
if pred () then
begin
Printf.printf "ok\n" ;
succeeded s
end
else
begin
Printf.printf "not ok\n";
failed s
end
with
_ ->Printf.printf "not ok (threw exception)\n";
failed s

(** Runs a predicate function and fails if it throws or
returns true.  Otherwise it succeeds *)
let fail_if desc pred s = pass_if desc (fun () -> not pred) s


(** Takes a bool and marks the test as succeeded if it is true *)
let ok desc x s = pass_if desc (fun () -> x) s

(** Takes a bool and marks the test as failed if it is true *)
let not_ok desc x s = ok desc (not x) s

let test_end s =
Printf.printf "End tests: %d of %d tests passed\n" s.ok s.n ;
State.return s
end

Nifty, no? You'll notice that the functions are all very similar to
those in the OO version, except that their final argument is a state
record, and instead of updating member data in the object, they simply
update this state record and use "State.return" to pass it into the
State monad. To make the initial code snippet work, the only thing that
remains is:
let ( >>= ) = State.bind

[1]: http://www.uncarved.com/articles/test_fun
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://enfranchisedmind.com/blog/2007/08/06/a-monad-tutorial-for-ocaml/
[6]: http://www.uncarved.com/blog/testing_ocaml.mrk
[7]: http://www.uncarved.com/tags/computers
[8]: mailto:sean@uncarved.com
[9]: http://creativecommons.org/licenses/by-sa/4.0/
