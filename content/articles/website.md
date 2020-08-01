+++
tags = "computers"
last_modified = "2009-08-07T09:48:28Z"
+++
# Website Changes

## An occasionally-updated summary of stuff I've changed

So when I had a day off work this week I decided to fix a few things on
this site that have been bugging me for a while:
* most of the content is dynamic, yet the [sitemap][5] (used by search
engines to figure out how to slurp your site) was not
* I never bothered to put proper [meta][6] description tags on pages
* now that there were quite a few articles things were getting lost
in painful navigation
* The site didn't do gzip encoding
* I've finally added comments thanks to [intense][7] debate

So I've had a go at fixing them. I now generate my sitemaps
automatically using the code I wrote to generate the atom and rss
feeds, transparently gzip stuff if your client can accept that, and
there is a new "[treeview"][8] page on the side to make things easier to
get to. Oh, and the pages have proper description tags which should
make them more useful on search engines.

Hope this all helps.

[1]: http://www.uncarved.com/articles/website
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.sitemaps.org/
[6]: http://www.google.com/support/webmasters/bin/answer.py?answer=35264&hl=en#1
[7]: http://intensedebate.com/
[8]: http://www.uncarved.com/treeview/
[9]: http://www.uncarved.com/tags/computers
[10]: mailto:sean@uncarved.com
[11]: http://creativecommons.org/licenses/by-sa/4.0/