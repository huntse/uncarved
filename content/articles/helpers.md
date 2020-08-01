+++
title = "helper classes for scala"
description = "My first opensource scala package"
last_modified = "2011-06-01T10:46:47Z"
+++


So I've released my helpers code via [github.][5] Scaladoc is available
[here,][6] although I warn you that my patience with hacking the
stylesheet only goes so far and I don't yet know how to make scaladoc
that is not foul to look at. To build it, and run the tests, do...
mvn test

...after unpacking the tarball somewhere

The motivation behind this package is that I wanted to do some http
stuff and wanted to make my client code be as simple as possible while
still being polite to servers. So that meant supporting conditional get
using Etags, Last-Modified and also supporting gzip encoding. I do all
this by using the apache commons [httpclient-4.x][7] and [8]httpcore-4.x
libraries and wrapping them all up in a class that's convenient and
simple to use. Here's a taster:
import com.uncarved.helpers.http._

val helper = new BasicClient()
//Get a webpage as a string (if you look at the apache http log4j messages you
can see it
//does conditional get and has transparent gzip support)
val str = helper.get("http://www.theflautadors.org/")

//Get some XML (with request parameters supplied)
val params = List(("tag"->""), ("limit"->"5"))
val xml = helper.getXML(Request(RequestType.GET, "http://www.uncarved.com/index
.py/rss1.1.xml", params))
val items = xml \\ "item"

[1]: http://www.uncarved.com/articles/helpers
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://uncarved.com/blog/helpers_github.mrk
[6]: http://www.uncarved.com/static/scala/helpers/doc/index.html
[7]: http://hc.apache.org/httpcomponents-client/index.html
[8]: http://hc.apache.org/httpcomponents-core/index.html
[9]: http://www.uncarved.com/tags/computers
