+++
title = "Getting Things Done in Text with notation3"
description = "I want a simple means of tracking and grouping tasks that works in text form and is easily parseable. And I want to learn notation3 too..."
aliases = [ "/articles/gtd_in_n3" ]
date = 2006-05-10T04:44:53Z
[taxonomies]
tags = ["computers"]
+++


Inspired by [this article][5] on lifehacker I decided to make my own
"getting things done" toolset. It would ideally need to be just as
flexible from the commandline as the lifehack "todo.txt" file but have
machine readablility too. I have decided to use [notation3][6] as the
basic format. n3 is useful because it is a machine-parseable format
that is easily converted into xml, but it's not as tedious to write as
xml can often be. So far it looks as if I will be able to make a "one
line per item" file that meets all of the "getting things done in txt"
requirements but will also be able to be used online and via the
semantic web toolset. I will be updating this article as I go along,
not least because n3 is entirely new to me and I am bound to change
things as I go along.

So far, the document looks something like this:
```
@prefix : <#> .
:tidy_garden :contexts "@home" ; :next_action "Mow lawn" ; :all_actions "Mow law
n" , "Weed borders" , "Turn compost" , "Prune" , "Tidy front garden" ; :priority
2 .
:sort_finances :contexts "@home" , "@work" ; :next_action "Consolidate pensions"
; :all_actions "Consolidate pensions" , "ebay junk", "make budget" ; :priority
1 .
```

As you can see, for each item, I can list the contexts in which it can
take place, the next action and all the actions I have thought of for
that item so far. For the next actions at the moment I am just using
string literals, but I will soon change those into ":" labels so I can
join the tasks together in a graph and have some tasks dependant on
others. In n3 you can make rules and draw inferences so I could have it
figure out for me what I should be doing next. Since the output is
[rdf][7] I could make a full ontology for tasks etc and then as well as
having a tool for humans, I would have a machine-readable format for
this stuff that would fit into the [semantic web][8]. I may do that.

To get going with notation3, you need a computer with [python][9] and you
need to install [rdflib][10] and [cwm][11]. It's well worth the effort to
do this.

[5]: http://www.lifehacker.com/software/text/geek-to-live-list-your-life-in-txt-166299.php
[6]: http://www.w3.org/2000/10/swap/Primer
[7]: http://en.wikipedia.org/wiki/Resource_Description_Framework
[8]: http://en.wikipedia.org/wiki/Semantic_Web
[9]: http://www.python.org/
[10]: http://rdflib.net/
[11]: http://www.w3.org/2000/10/swap/doc/cwm.html
