---
description: >-
  BoxLang is an event-driven language and you can not only listen, but register
  and announce events.
icon: jet-fighter-up
---

# Interceptors

BoxLang is an event-driven language and it emits events throughout many different life-cycles.  The entire framework for events is also extensible and can be used not only by Module developers but by anybody using the language in either BoxLang or Java.  There are several core events that are emitted and you can register your own events we call **interception points**.

{% hint style="info" %}
If you are familiar with the intercepting filter pattern, or observer/observable pattern, then that's what BoxLang follows.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

## Event Driven Programming

The way that interceptors are used is usually referred to as **event-driven programming**, which can be very familiar if you are already doing any Nodejs or observer/observable coding. You can listen and execute intercepting points anywhere you like in your application, you can even produce content whenever you announce these events.

Events have unique names like: `onRequestStart, onHTTPRequest, onParse`

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Event Emitters aka Interceptor Pools <a href="#resources" id="resources"></a>

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

BoxLang has 3 interceptor pools that will emit events:

* `Global Runtime` - The entire BoxLang runtime
* `Application.bx Request Listener` - The request listener for an application
* `CacheProviders` - The BoxCache providers



When you register interceptors, they will be registered within any of these pools.

## Interceptors <a href="#resources" id="resources"></a>

In BoxLang, listeners are referred to as **Interceptors.**  These can be built in Java or BoxLang as classes or closures/lambdas.  If they are classes they can listen to multiple interception points and have a `configure` method.

{% tabs %}
{% tab title="BoxLang" %}
```javascript
class{
    
    function configure(){
        // Any code to setup the interceptor
    }
    
    // Any methods that are the same name as the events
    
    function onHTTPRequest( struct event ){
    }
    
    function preFunctionInvoke( struct event ){
    
    }
    
}
```
{% endtab %}

{% tab title="Java" %}
```java

/**
 * An interceptor
 */
@Interceptor( autoLoad = false )
public class MyInterceptor extends BaseInterceptor{

 /**
  * No Arg Constructor
  */
 public MyInterceptor(){
 }
 
 @InterceptionPoint
 public void onHTTPRequest( IStruct data ){
    }
    
 @InterceptionPoint
 public void preFunctionInvoke( IStruct data ){
    
  }
 

}
```
{% endtab %}
{% endtabs %}

If they are closures, they will have the following format:

```java
( event ) => {
  // Closure listener
}

( event ) -> {
  // Lambda listener
}
```

### Registration <a href="#resources" id="resources"></a>

Interceptors can be registered via the following approaches into the different pools

* A module
  * Registers into the global runtime
  * ModuleConfig.bx `interceptors` array
  * A Java class via Service Loader
* BIFs
  * `boxRegisterInterceptor()` - Register into the global runtime
  * `boxRegisterRequestInterceptor()` - Register into the request listener
* Java `InterceptorService`
  * The interceptor service has several registration method according to different types.  The `InterceptorService` is the global runtime.
  * `register( IInterceptor )`
  * `register( IInterceptor, properties )`
  * `register( IClassRunnable )`
  * `register( DynamicObject, states... )`
  * `register( IInterceptorLambda, states... )`
* CacheProvider specific poool
  * Each cache provider (BoxCache) has a `getInterceptorPool()` method which you can invoke and then you can use all of the pool methods for registration above.

#### ModuleConfig.bx

You can create an `interceptors` array for registration inside the `ModuleConfig.bx`&#x20;

```groovy
// Interceptors registration
interceptors = [
    {
        class : "#moduleRecord.invocationPath#.interceptors.Listener"
        properties : {
            // configuration
        }
    }
];

```

#### BIFs <a href="#resources" id="resources"></a>

* `boxRegisterInterceptor( interceptor, [states=[]] )`
* `boxRegisterRequestInterceptor( interceptor, [states=[]] )`

The `states` are the interception points to SPECICALLY register an interceptor to.  If you omit it, then we will scan the interceptor for interception point states.

{% hint style="danger" %}
A closure/lambda when registered REQUIRES to which states to register to.
{% endhint %}

```
// Register an interceptor class in all discovered states
boxRegisterInterceptor( new MyInterceptor() )

// Register an interceptor class in all the passed states
// If those states have not been registered, register them
```

### Configure() <a href="#resources" id="resources"></a>

The `configure()` method in the interceptor can be used to bootstrap anything you might need once the interceptor is loaded and registered by the runtime.  The Java counterparts have a `BaseInterceptor` class and the configurations can have a structure of setup `properties`.

{% tabs %}
{% tab title="BoxLang" %}
```javascript
function configure(){

}
```
{% endtab %}

{% tab title="Java" %}
```java
public void configure( IStruct properties ){
  this.properties = properties;
  // YOur Code 
}

public void configure(){
  // Or here if you have no properties
}
```
{% endtab %}
{% endtabs %}

### Properties

Interceptors when defined in a module can be defined using a structure of properties which are passed to (Java) and injected (BoxLang).

```groovy
interceptors = [
{ 
	class : "#moduleRecord.invocationPath#.interceptors.Listener", 
	properties : {
	  createdOn : now(),
	  by : "Luis Majano"
	} 
}
];
```

### Injections <a href="#resources" id="resources"></a>

If you are building BoxLang interceptors then you get a set of injections into your class' `variables` scope.

<table><thead><tr><th width="200">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code></td><td>The name of the interceptor, if any</td></tr><tr><td><code>properties</code></td><td>The structure of properties</td></tr><tr><td><code>log</code></td><td>A BoxLang logger that maps to the <code>runtime</code> log file</td></tr><tr><td><code>interceptorService</code></td><td>A reference to the Interceptor Service</td></tr><tr><td><code>boxRuntime</code></td><td>A refernce to the Box Runtime class.</td></tr><tr><td><code>moduleRecord</code></td><td>If this interceptor belongs to a module, a reference to the modules record class will be injected as well.</td></tr></tbody></table>



## Resources <a href="#resources" id="resources"></a>

* [http://en.wikipedia.org/wiki/Observer\_pattern](http://en.wikipedia.org/wiki/Observer_pattern)
* [http://sourcemaking.com/design\_patterns/observer](http://sourcemaking.com/design_patterns/observer)
* [http://java.sun.com/blueprints/corej2eepatterns/Patterns/InterceptingFilter.html](http://java.sun.com/blueprints/corej2eepatterns/Patterns/InterceptingFilter.html)

## For what can I use them <a href="#for-what-can-i-use-them" id="for-what-can-i-use-them"></a>

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
