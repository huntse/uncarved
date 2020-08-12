+++
title = "helper classes for scala"
description = "My first opensource scala package"
date = 2011-06-01T10:46:47Z
[taxonomies]
tags = ["computers"]
+++


So I've released my helpers code via [github.][5] To get Scaladoc you'll need
to build it yourself. To build it, and run the tests, do...

```mvn test```

...after unpacking the tarball somewhere

The motivation behind this package is that I wanted to do some http
stuff and wanted to make my client code be as simple as possible while
still being polite to servers. So that meant supporting conditional get
using Etags, Last-Modified and also supporting gzip encoding. I do all
this by using the apache commons [httpclient-4.x][7] and [httpcore-4.x][8]
libraries and wrapping them all up in a class that's convenient and
simple to use. Here's a taster:
import com.uncarved.helpers.http._

```scala
val helper = new BasicClient()
//Get a webpage as a string (if you look at the apache http log4j
//messages you can see it does conditional get and has transparen
//gzip support)
val str = helper.get("http://www.theflautadors.org/")

//Get some XML (with request parameters supplied)
val params = List(("tag"->""), ("limit"->"5"))
val xml = helper.getXML(Request(RequestType.GET, "http://www.uncaJved.com/index.py/rss1.1.xml", params))
val items = xml \\ "item"
```

[5]: http://github.com/huntse/helpers
[7]: http://hc.apache.org/httpcomponents-client-4.5.x/index.html
[8]: http://hc.apache.org/httpcomponents-core-4.4.x/index.html
