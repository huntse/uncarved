+++
tags = "computers"
aliases = [ "/articles/helpers_github" ]
last_modified = "2011-06-02T18:18:09Z"
+++
# Getting started with github

## Before we can do our marketmaking system, you need to be able to get the software.

To share the marketmaking software that I talked about in the [first][5]
marketmaking article, we need to have a repository set up, so I decided
to get going with [github.][6] You'll need to [7]set up git, and you'll
need [maven][8] 2 to build everything. I thought I'd put out a small
article to get people started with building a small package we're going
to depend on for the bigger system. Assuming this goes ok, I'll push
the actual software that interfaces with bullionvault.

Once you've got git and maven2 set up, it should be simple enough. On
my linux boxes I just do:
git clone git://github.com/huntse/helpers.git
cd helpers
mvn test

...and with any luck, git will get the software, maven2 will download
the internet and some time later build and run the tests, and you'll
see something like this:
+++----------------------------------------------------
T E S T S
+++----------------------------------------------------
There are no tests to run.

Results :

Tests run: 0, Failures: 0, Errors: 0, Skipped: 0

[INFO]
[INFO] +++ maven-scalatest-plugin:1.1-SNAPSHOT:test (default) @ helpers ---
[INFO] org.scalatest.tools.Runner.run(-p, "/home/sean/tmp/helpers/target/classes
/home/sean/tmp/helpers/target/test-classes", -o, -fNCXEHLOWFD, /home/sean/tmp/h
elpers/target/scalatest-reports/file/constrained.txt, -f, /home/sean/tmp/helpers
/target/scalatest-reports/file/full.txt, -u, /home/sean/tmp/helpers/target/scala
test-reports/xml, -h, /home/sean/tmp/helpers/target/scalatest-reports/html/repor
t.html)
Run starting. Expected test count is: 7
Suite Starting - DiscoverySuite
BasicClientSpec:
An BasicClient object
- should be able to get theflautadors.org
- should be able to reget theflautadors.org using conditional get
- should be able to get HEAD of uncarved.com
- should be able to GET uncarved with parameters
- should be able to get xml
- should be able to handle redirects
- should be able to do a POST with values
Suite Completed - DiscoverySuite
Run completed in 2 seconds, 266 milliseconds.
Total number of tests run: 7
Suites: completed 2, aborted 0
Tests: succeeded 7, failed 0, ignored 0, pending 0
All tests passed.
THAT'S ALL FOLKS!
[INFO] +++---------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] +++---------------------------------------------------------------------
[INFO] Total time: 23.140s
[INFO] Finished at: Wed Jun 01 10:27:36 GMT 2011
[INFO] Final Memory: 6M/11M
[INFO] +++---------------------------------------------------------------------
mvn test  22.79s user 0.74s system 94% cpu 24.793 total

I don't use eclipse or anything like that, but it should be possible
too get this working with eclipse too, just don't ask me how.

[1]: http://www.uncarved.com/articles/helpers_github
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.uncarved.com/blog/mm_1.mrk
[6]: http://github.com/
[7]: http://help.github.com/set-up-git-redirect
[8]: http://maven.apache.org/
[9]: http://www.uncarved.com/tags/computers
[10]: mailto:sean@uncarved.com
[11]: http://creativecommons.org/licenses/by-sa/4.0/
