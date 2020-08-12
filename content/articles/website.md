+++
title = "Website Changes"
description = "An occasionally-updated summary of stuff I've changed"
date = 2009-08-07T09:48:28Z
[taxonomies]
tags = ["computers"]
+++


So when I had a day off work this week I decided to fix a few things on
this site that have been bugging me for a while:
* most of the content is dynamic, yet the [sitemap][5] (used by search
engines to figure out how to slurp your site) was not
* I never bothered to put proper [meta][6] description tags on pages
* now that there were quite a few articles things were getting lost
in painful navigation
* The site didn't do gzip encoding

So I've had a go at fixing them. I now generate my sitemaps
automatically using the code I wrote to generate the atom and rss
feeds, transparently gzip stuff if your client can accept that, and
there is a new [articles][8] link on the side to make all the content easier to
get to. Oh, and the pages have proper description tags which should
make them more useful on search engines.

Hope this all helps.

[5]: https://www.sitemaps.org/
[6]: https://support.google.com/webmasters/answer/35624?hl=en&visit_id=637328185320201573-2619774670&rd=1
[8]: http://www.uncarved.com/articles/
