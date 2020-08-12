+++
title = "Mozilla Ubiquity"
description = "Fun with this amazing mozilla addon"
date = 2010-05-05T04:46:34Z
[taxonomies]
tags = ["computers"]
+++


[Ubiquity][5] is an amazing mozilla addon which gives users a
command-line interface within the browser which you can use to do
various things. Users can easily write their own commands in javascript
and share them via the web. In that spirit, I've written my first
ubiquity command, which searches hoogle, the haskell type-aware search
engine.
```
CmdUtils.makeSearchCommand({
    homepage: "http://www.uncarved.com/",
    author: { name: "Sean Hunter"},
    license: "MPL",
    name: "hoogle-search",
    url: "http://www.haskell.org/hoogle/?hoogle={QUERY}",
    icon: "http://www.haskell.org/favicon.ico",
    description: "Searches haskell.org for functions matching by name or type sign
    ature.",
});
```

As you can see, it's virtually all meta-data and that's because there
are a bunch of functions around search that know how to do everything
you need to do. However, you can write more sophisticated commands that
manipulate the browser, the web page you're on, have little built-in
previews etc. All very nifty.

When you have the above, you can simply invoke ubiquity and say
"`hoogle-search Ord a => a -> a`" or whatever and it will find you
functions matching that type signature. I'll share this command (and
any others I write) at [www.uncarved.com][6] using the subscription
mechanism they recommend.

I was feeling rather proud of the above, however I saw this morning
that if you go on a page with a search box, select it and invoke
ubiquity and type "create-new-search-command" it writes something very
much like the above for you.

[5]: https://addons.mozilla.org/en-US/firefox/addon/9527
[6]: http://www.uncarved.com/
