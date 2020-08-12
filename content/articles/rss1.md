+++
title = "RSS 1.1 Feed now available"
description = "RDF + Syndication = RSS 1"
date = 2006-05-11T19:32:31Z
[taxonomies]
tags = ["computers"]
+++


Now that I am getting the hang of rdf, the next logical step was to
link metadata with content and provide an [rss][5] 1.1 feed. Rss 1.1 is a
fantastic specification in many ways because it allows machine-readable
content (it is an application of rdf and xml), and has namespaces that
allow content syndication, so you can embed metadata in with articles
and include the foaf file and the pgp key of the authors if that's the
sort of thing you like. In my RSS 1.1 feed I include the full content
of the site with metadata and license information for the full feed and
metadata for individual items as appropriate. To see the full end
result, click on the rss1.1 link at the bottom of the index page.

Note that rss 2 is not a more recent spec that rss 1.1 (or rss 1)- they
are seperate specs for doing a similar thing (content syndication), but
the specification [forked.][6] Rss 2 is considered simpler by it's
adherents because it is an application of xml but not of rdf. That,
however, is also it's weakness because it's not as extensible and is
not seemlessly part of the semantic web. Certainly for any programmer,
rss 1 is no more complex than rss 2 to support and implement and is a
great deal richer and more extensible.

For what it's worth, my cheetah template looks like this:
```xml
<pre><code><?xml version="1.0" encoding="utf-8"?>
<Channel xmlns="http://purl.org/net/rss1.1#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:p="http://purl.org/net/rss1.1/payload#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:cc="http://web.resource.org/cc/"
    rdf:about="http://www.uncarved.com/index.py/rss1.1.xml?limit=1">
    <rdf:Description rdf:about="http://www.uncarved.com/index.py/rss1.1.xml?limit=1">
        <dc:creator>Sean Hunter</dc:creator>
        <dc:title>The Uncarved Block</dc:title>
        <dc:description>A collection of articles and software</dc:description>
        <dc:date>2006-05-11T13:32:57Z</dc:date>
        <dc:type>Text</dc:type>
        <dc:format>text/html</dc:format>
        <dc:identifier>http://www.uncarved.com/index.py/rss1.1.xml?limit=1</dc:identifier>
        <dc:language>en-GB</dc:language>
    </rdf:Description>
    <cc:Work rdf:about="http://www.uncarved.com/index.py/rss1.1.xml?limit=1">
        <cc:license rdf:resource="http://creativecommons.org/licenses/by/2.5/" />
    </cc:Work>
    <cc:License rdf:about="http://creativecommons.org/licenses/by/2.5/">
        <cc:permits rdf:resource="http://web.resource.org/cc/Reproduction"/>
        <cc:permits rdf:resource="http://web.resource.org/cc/Distribution"/>
        <cc:requires rdf:resource="http://web.resource.org/cc/Notice"/>
        <cc:requires rdf:resource="http://web.resource.org/cc/Attribution"/>
        <cc:permits rdf:resource="http://web.resource.org/cc/DerivativeWorks"/>
    </cc:License>
    <title>The Uncarved Block</title>
    <description xml:lang="en-GB">Software, unix tips and sundry other things</description>
    <link>http://www.uncarved.com/index.py/</link>
    <items rdf:parseType="daml:collection">
        <item rdf:about="/articles/rss1">
            <title>RSS 1.1 Feed now available</title>
            <link>/articles/rss1</link>
            <description xml:lang="en-GB">RDF + Syndication = RSS 1</description>
            <dc:date>2006-05-11T13:08:47Z</dc:date>
            <p:payload rdf:parseType="Literal">
<pre><code>#filter Filter
<?xml version="1.0" encoding="utf-8"?>
<Channel xmlns="http://purl.org/net/rss1.1#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:p="http://purl.org/net/rss1.1/payload#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:cc="http://web.resource.org/cc/"
    rdf:about="$self_link">
    <rdf:Description rdf:about="$self_link">
        <dc:creator>Sean Hunter</dc:creator>
        #if $current_tagname
        <dc:title>The Uncarved Block/$current_tagname</dc:title>
        <dc:subject>$current_tagname</dc:subject>
        #else
        <dc:title>The Uncarved Block</dc:title>
        #end if
        <dc:description>A collection of articles and software</dc:description>
        <dc:date>$most_recent_w3c</dc:date>
        <dc:type>Text</dc:type>
        <dc:format>text/html</dc:format>
        <dc:identifier>$self_link</dc:identifier>
        <dc:language>en-GB</dc:language>
    </rdf:Description>
    <cc:Work rdf:about="$self_link">
        <cc:license rdf:resource="http://creativecommons.org/licenses/by/2.5/" />
    </cc:Work>
    <cc:License rdf:about="http://creativecommons.org/licenses/by/2.5/">
        <cc:permits rdf:resource="http://web.resource.org/cc/Reproduction"/>
        <cc:permits rdf:resource="http://web.resource.org/cc/Distribution"/>
        <cc:requires rdf:resource="http://web.resource.org/cc/Notice"/>
        <cc:requires rdf:resource="http://web.resource.org/cc/Attribution"/>
        <cc:permits rdf:resource="http://web.resource.org/cc/DerivativeWorks"/>
    </cc:License>
    #if $current_tagname
    <title>The Uncarved Block/$current_tagname</title>
    #else
    <title>The Uncarved Block</title>
    #end if
    <description xml:lang="en-GB">Software, unix tips and sundry other things</description>
    <link>$home_link</link>
    <items rdf:parseType="daml:collection">
        #for $article in $articles
        <item rdf:about="http://www.uncarved.com/$article.name">
            <title>$article.title</title>
            <link>http://www.uncarved.com/$article.name</link>
            #if $article.precis
            <description xml:lang="en-GB">$article.precis</description>
            #end if
            <dc:date>$article.updated</dc:date>
            <p:payload rdf:parseType="Literal">
                $article.body
            </p:payload>
        </item>
        #end for
    </items>
</Channel>
```

The feed is available [here][7] and the output for a tag with just this
article in it (I've truncated the content slightly) looks like:
```
```
I hope you enjoy creating your own rss 1.1 feeds. You can find out more
about all the site syndication variants on the [wikipedia.][8]

[1]: http://www.uncarved.com/articles/rss1
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://inamidst.com/rss1.1/
[6]: http://diveintomark.org/archives/2002/09/06/history_of_the_rss_fork
[7]: http://www.uncarved.com/rss1.1.xml
[8]: http://en.wikipedia.org/wiki/RSS_(file_format)
[9]: http://www.uncarved.com/tags/computers
[11]: http://creativecommons.org/licenses/by-sa/4.0/
