---
description: >-
  BoxLang is an event-driven language and you can not only listen, but register
  and announce events.
icon: jet-fighter-up
---

# Interceptors

BoxLang is an event-driven language and it emits events throughout many different life-cycles.  The entire framework for events is also extensible and can be used not only by Module developers but by anybody using the language in either BoxLang or Java.

{% hint style="info" %}
If you are familiar with the intercepting filter pattern, or observer/observable pattern, then that's what BoxLang follows.
{% endhint %}

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

The way that interceptors are used is usually referred to as **event-driven programming**, which can be very familiar if you are already doing any Nodejs or observer/observable coding. You can listen and execute intercepting points anywhere you like in your application, you can even produce content whenever you announce these events.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### Resources <a href="#resources" id="resources"></a>

* [http://en.wikipedia.org/wiki/Observer\_pattern](http://en.wikipedia.org/wiki/Observer_pattern)
* [http://sourcemaking.com/design\_patterns/observer](http://sourcemaking.com/design_patterns/observer)
* [http://java.sun.com/blueprints/corej2eepatterns/Patterns/InterceptingFilter.html](http://java.sun.com/blueprints/corej2eepatterns/Patterns/InterceptingFilter.html)

#### For what can I use them <a href="#for-what-can-i-use-them" id="for-what-can-i-use-them"></a>

Below are just a few applications of BoxLang Interceptors:

* Security
* Event based Security
* Method Tracing
* AOP Interceptions
* Publisher/Consumer operations
* Implicit chain of events
* Content Appending or Pre-Pending
* View Manipulations
* Custom SES support
* Cache advices on insert and remove
* Much much more...
