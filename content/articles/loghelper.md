+++
title = "Log4j for Scala"
description = "Scala is nice. Logging is nice. Scala + logging.....?"
last_modified = "2011-06-01T10:40:43Z"
aliases = [ "LogHelper" ]
+++


I've recently been playing about a bit with [Scala.][5] It's a great
language in which you can write real programs very easily. As an
example, in Java you often want to be able to make use of [log4j][6] to
log various tracing info. Well, here's a little helper trait you can
mix in to scala classes make logging completely trivial:
package com.uncarved.helpers

import org.apache.log4j.Logger;

/**
* LogHelper is a trait you can mix in to provide easy log4j logging
* for your scala classes.
**/
trait LogHelper {
val loggerName = this.getClass.getName
lazy val logger = Logger.getLogger(loggerName)
}

You use it like this:
class MyClass extends LogHelper {
logger.debug("We got ourselves a class")
def someMethod(temp: Int) = {
logger.debug("entering someMethod")

if(temp>25) {
logger.info("It's mighty hot in here")

//...do something

}
//..... etc

logger.debug("leaving someMethod")
}
}

Easy peasy logging. This class is one of several that I have released
on [github.][7] Enjoy!

[5]: http://www.scala-lang.org/
[6]: http://logging.apache.org/log4j/
[7]: http://github.com/huntse
