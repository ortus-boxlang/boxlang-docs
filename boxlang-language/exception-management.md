# Exception Management

## Try/Catch/Finally

The BoxLang language also provides you with a traditional approach to deal with error handling at the code block level. This is usually a trio of constructs:

* `try`: The try block allows you to demarcate the code to test if it fails or passes ([https://cfdocs.org/cftry](https://cfdocs.org/cftry))
* `catch` : The catch block is executed when the try block fails ([https://cfdocs.org/cfcatch](https://cfdocs.org/cfcatch))
* `finally` : The finally block executes no matter if the try fails or passes. It is guaranteed to always execute. ([https://cfdocs.org/cffinally](https://cfdocs.org/cffinally))

Basically, a try and catch statement attempts some code. If the code fails, BoxLang will do whatever is in the exception to try to handle it without breaking. Of course, many different types of exceptions can occur, which should sometimes be handled in a different manner than the others.

```java
try{
    // code to try to execute
} catch( any e ) {
    // the any type catches ALL errors from the try above
} catch( myType e ){
    // Catch the `myType` only type of exception
} finally {
    // this code executes no matter what
}
```

## Catch Types

The catch construct can take an `any` or a custom exception type declared by the BoxLang engine, Java code or custom exceptions within your code. This is a great way to be able to intercept for specific exception types and address them differently.

```java
try{

} catch( database e ){

} catch( template e ){

}
```

### Native Exception Types

Some of the exception types found in BoxLang are the following

* `application`: catches application exceptions
* `database`: catches database exceptions
* `template`: catches BoxLang page exceptions
* `security`: catches security exceptions
* `object`: catches object exceptions
* `missingInclude`: catches missing include file exceptions
* `expression`: catches expression exceptions
* `lock`: catches lock exceptions
* `custom_type`: catches the specified custom exception type that is defined in a [cfthrow](https://cfdocs.org/cfthrow) tag
* `java.lang.Exception`: catches Java object exceptions
* `searchengine`: catches Verity search engine exceptions
* `any`: catches all exception types

### Custom Exception Types

Custom exception types are defined by you the programmer and they can also be intercepted via their defined name. Let's say that the exception type is "`InvalidInteger`" then you can listen to it like this:

```java
try{
    throw( type="invalidInteger" );
} catch ( "InvalidInteger" e ){

}
```

## Throwing Exceptions

Now that you have seen how to listen to exceptions, let's discover the `throw` or `cfthrow` constructs used to throw a developer-specific exception. ([https://cfdocs.org/cfthrow](https://cfdocs.org/cfthrow))

The `throw()` function or tag has several attributes:

* **Type** : A custom or BoxLang core type
* **Message** : Describes the exception event
* **Detail** : A detailed description of the event
* **errorCode** : A custom error code
* **extendedInfo** : Custom extended information to send in the exception, can be anything
* **object** : Mutually exclusive with the other attributes, usually another exception object or a raw Java exception type.

```java
try {
    throw( message="Oops", detail="xyz", errorCode=12 );
} catch (any e) {
    writeOutput( "Error: " & e.message);
} finally {
    writeOutput( "I run even if no error" );
}
```

## Rethrowing Exceptions

The `rethrow` or `cfrethrow` construct allows you to well, `rethrow` the active exception by preserving all of the exception information and types. Usually you use `rethrow` within a catch block after you have done some type of operations on the incoming exception. ([https://cfdocs.org/cfrethrow](https://cfdocs.org/cfrethrow))

```java
try{
	runAroundEachClosures( arguments.suite, arguments.spec );
} catch( any e ){
	rethrow;
} finally {
	runAfterEachClosures( arguments.suite, arguments.spec );
}

// Mix In Stub
try{
	// include it
	arguments.targetObject.$include = variables.$include;
	arguments.targetObject.$include( instance.mockBox.getGenerationPath() & tmpFile );
	structDelete( arguments.targetObject, "$include" );
	// Remove Stub
	removeStub( genPath & tmpFile );
} catch( any e ) {
	// Remove Stub
	removeStub( genPath & tmpFile);
	rethrow;
}
```
