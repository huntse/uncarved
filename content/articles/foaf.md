+++
title = "Foaf in n3"
description = "Having got started with n3 I made myself a foaf file using it"
date = 2009-06-13T13:18:59Z
[taxonomies]
tags = ["computers"]
+++


So now I've [started][5] with [notation3][6] I am itching for places to use
it. For this reason I decided to make myself a [foaf][7] file. Happily,
this is really straightforward using n3. My foaf.n3 looks like this:

```n3
@keywords a.
@prefix : <http://xmlns.com/foaf/0.1/>.
@prefix wot: <http://xmlns.com/wot/0.1/>.
@prefix dc: <http://purl.org/dc/elements/1.1/>.
@prefix x: <#>.

x:this a PersonalProfileDocument;
wot:assurance "http://www.uncarved.com/static/foaf.rdf.asc";
maker x:me;
primaryTopic x:me;
dc:title "Sean Hunter's FOAF file";
dc:identifier "http://www.uncarved.com/static/foaf.rdf".


x:me a Person;
name "Sean Hunter";
gender "male";
title "Mr";
givenname "Sean";
family_name "Hunter";
homepage <http://www.uncarved.com/>;
mbox_sha1sum "f5a2eaad7e46af80de0bc48e6db72efebe382da0";
plan """
---  ---
---  ---
---  ---             Darkening of the Light. In adversity
--------             It furthers one to be persevering.
---  ---
--------""".
```

...which when I do `python /usr/bin/cwm.py foaf.n3 --rdf >| foaf.rdf`
generates a [foaf.rdf][8] file like this:

```xml
<?xml version="1.0"?>
<!-- Processed by Id: cwm.py,v 1.164 2004/10/28 17:41:59 timbl Exp -->
<!--     using base file:/home/sean/doc/n3/foaf.n3-->
<rdf:RDF xmlns="http://xmlns.com/foaf/0.1/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:wot="http://xmlns.com/wot/0.1/">
  <Person rdf:about="#me">
    <family_name>Hunter</family_name>
    <gender>male</gender>
    <givenname>Sean</givenname>
    <homepage rdf:resource="http://www.uncarved.com/"/>
    <mbox_sha1sum>f5a2eaad7e46af80de0bc48e6db72efebe382da0</mbox_sha1sum>
    <name>Sean Hunter</name>
    <plan>
---  ---
---  ---
---  ---             Darkening of the Light. In adversity
--------             It furthers one to be persevering.
---  ---
--------</plan>
    <title>Mr</title>
  </Person>
  <PersonalProfileDocument rdf:about="#this">
    <dc:identifier>http://www.uncarved.com/static/foaf.rdf</dc:identifier>
    <dc:title>Sean Hunter's FOAF file</dc:title>
    <maker rdf:resource="#me"/>
    <primaryTopic rdf:resource="#me"/>
    <wot:assurance>http://www.uncarved.com/static/foaf.rdf.asc</wot:assurance>
  </PersonalProfileDocument>
</rdf:RDF>
```

...which I link from my homepage. Easy-peasy. I can validate it using
the w3c rdf [validator][9] and it works just fine. Now I just need to add
some friends. If you know me and want to be added to my foaf file, mail
me at [sean@uncarved.com.][10]

[1]: http://www.uncarved.com/articles/foaf
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: /articles/gtd_in_n3
[6]: http://www.w3.org/2000/10/swap/Primer.html
[7]: http://www.foaf-project.org/
[8]: http://www.uncarved.com/static/foaf.rdf
[9]: http://www.w3.org/RDF/Validator/
