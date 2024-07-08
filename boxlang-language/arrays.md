---
description: An array is a data structure consisting of a collection of elements.
---

# Arrays

Almost every programming language allows you to represent different types of collections. In BoxLang, we have three types of collections: arrays, [structures](structures.md), and [queries](queries.md).

An array is a number-indexed list. Imagine you had a blank piece of paper and drew a set of three small boxes in a line:

```
 ---  ---  ---
|   ||   ||   |
 ---  ---  ---
```

You could number each one by its position from left to right:

```
 ---  ---  ---
|   ||   ||   |
 ---  ---  ---
  1    2    3
```

Then put strings in each box:

```
 -------------  ---------  ----------
| "Breakfast" || "Lunch" || "Dinner" |
 -------------  ---------  ----------
       1            2           3
```

We have a three-element Array. BoxLang arrays can grow and shrink dynamically at runtime, just like Array Lists or Vectors in Java, so if we added an element, it’d usually go on the end or be appended at the end.

```
 -------------  ---------  ----------  -----------
| "Breakfast" || "Lunch" || "Dinner" || "Dessert" |
 -------------  ---------  ----------  -----------
       1            2           3           4
```

If you asked the array for the element in position two, you’d get back `Lunch`. Ask for the last element, and you’ll get back: `Dessert`.

## The Story of One

Now, have you detected something funny with the ordering of the elements? Come on, look closer....... They start with `1` and not `0`, now isn't that funny. BoxLang is one of the few languages where array indexes start at `1` and not `0`. So if you have a PHP, Ruby, or Java background, remember that `1` is where you start. Is this good or bad? Well, we will refrain from pointing fingers for now.

{% hint style="info" %}
All arrays in BoxLang are passed by **passed by reference**. Please remember this when working with arrays and passing them to functions. There is also the `passby=reference|value` attribute to function arguments where you can decide whether to pass by reference or value.
{% endhint %}

## Arrays in Code

Let's go ahead and model some code in BoxLang using our fancy REPL tool CommandBox:

![](../.gitbook/assets/arrays\_in\_code.png)

Check it out:

* The array was created by putting pieces of data between square brackets (`[]`) and separated by commas
* We added an element to the array using the member function `append()`
* We fetched the element at a specific position by using square brackets (`[ x ]`) and replaced `x` with the index, we wanted
* We retrieved the size of the array by using the member function `len()`
* We searched the contents of the array using the member function `findNoCase()` , and it gave us the index position of the element in the array.

Please note that all member functions can also be used as traditional [array functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array). However, [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) look much better for readability.

{% hint style="success" %}
**Tip:** You can use the `toString()` call on any array to get a string representation of its values: `grid.toString()`
{% endhint %}

## Multi-Dimensional Arrays

To create grids or matrix constructs, you must create two-dimensional arrays. This gives you an **x** and **y** axis of data. You will do so using the `arrayNew( dimensions = max 3 )` method:

```javascript
grid = arrayNew( 2 );
grid[ 1 ][ 1 ] = 'Hammer';
grid[ 1 ][ 2 ] = 'Nail';
grid[ 2 ][ 1 ] = 'Screwdriver';
grid[ 1 ][ 2 ] = 'Screw';
```

{% hint style="success" %}
**Tip:** BoxLang only supports two and three-dimensional arrays, so you can easily represent x, y, and z axis.
{% endhint %}

## Common Methods

The best way to learn about using arrays is to check out the available [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) and [array functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array).

```javascript
// Sort an array
meals.sort( "textnocase" );

// Clear the array
meals.clear();

// Go on a diet
meals.delete( "Dessert" );
meals.deleteAt( 4 );

// Iterate
meals.each( function( element, index) {
   systemOutput( element & " " & index );
} );

// Filter an array
meals.filter( function( item ){
 return item.findNoCase( "unch" ) gt 0 ? true : false;
} );

// Convert to a list
meals.toList();

// Map/ Reduce
complexData = [ {a: 4}, {a: 18}, {a: 51} ];
newArray = arrayMap( complexData, function(item){
   return item.a;
});
writeDump(newArray);

complexData = [ {a: 4}, {a: 18}, {a: 51} ];
 sum = arrayReduce( complexData, function(prev, element)
 {
 return prev + element.a;
 }, 0 );
writeDump(sum);
```

## Typed Arrays

BoxLang also allow you to create strongly typed arrays. This is useful if you want to determine the array's contents specifically. Similar to [generics](https://www.baeldung.com/java-generic-array) in Java.

This syntax will allow you to define an array as being of a certain type and how many dimensions it has.

```javascript
// array of strings
stringArray = arrayNew[ "String" ]( 1 )
// array of numerics
numericArray = arrayNew[ "Numeric" ]( 1 )
// array of User Classes
aUsers = arrayNew[ "User" ]( 1 )
```

If you want to use typed arrays, then you will have to declare it via the `ArrayNew()` method via the second argument:

```javascript
ArrayNew( dimension, type, synchronized:boolean )
```

{% hint style="warning" %}
Please note that BoxLang will try to cast values automatically into the type defined by the array container.
{% endhint %}

{% hint style="info" %}
**Tip**: By default, all BoxLang arrays are _Unsynchronized_. That means they are not thread-safe when accessing the data from multiple threads or shared scopes.

Unsynchronized arrays are about 93% faster due to lock avoidance. So with much power comes much responsibility.
{% endhint %}

### Array Types

The allowed types are:

* Array
* Binary
* Boolean
* Component
* Class by Name / SubType
* Date / Datetime
* Function
* Numeric
* Query
* String
* Struct

### Literal Syntax

BoxLang also supports a way to make a declaration of a typed array using a literal syntax:

```javascript
[ type ][ elem1, elem2, .. elemN ]
```

This is a nice way to declare them literally:

```javascript
stringArray = [ 'String' ][ 1, "Word1", "Word2" ]
writeDump( stringArray )
```

## Negative Indices

BoxLang also supports the concept of negative indices. This allows you to retrieve the elements from the end of the array backward. So you can easily count back instead of counting forwards:

```javascript
numbers = [1,2,3,4,5]

writedump( numbers[ -1 ] ) // 5
writedump( numbers[ -2 ] ) // 4
writedump( numbers[ -3 ] ) // 3
writedump( numbers[ -4 ] ) // 2
writedump( numbers[ -5 ] ) // 1
writedump( numbers[ -6 ] ) // EXCEPTION!!! Array index out of range
```

## Array Slices

BoxLang supports the [slicing](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array/arrayslice) of an array via the `arraySlice()` method or the `slice()` member function, respectively.

## Looping Over Arrays

You can use different constructs for looping over arrays:

* `for` loops
* `loop` constructs
* `each()` closures

```javascript
for( var thisMeal in meals ){
 systemOutput( "I just had #thisMeal#" );
}

for( var x = 1; x lte meals.len(); x++ ){
 systemOutput( "I just had #meals[ x ]#" );
}

meals.each( function( element, index ){
  systemOutput( "I just had #element#" );
} );

bx:loop( from=1, to=meals.len(), index=x ){
  systemOutput( "I just had #meals[ x ]#" );
}
```

### Multi-Threaded Looping

BoxLang allows you to leverage the `each()` operations in a multi-threaded fashion. The `arrayEach()` or `each()` functions allow for a `parallel` and `maxThreads` arguments so the iteration can happen concurrently on as many `maxThreads` as supported by your JVM.

```java
arrayEach( array, callback, parallel:boolean, maxThreads:numeric );
each( collection, callback, parallel:boolean, maxThreads:numeric );
```

This is incredibly awesome, as your callback will now be called concurrently! However, please note that once you enter concurrency land, you should shiver and tremble. Thread concurrency will be of the utmost importance, and you must ensure that var scoping is done correctly and that appropriate locking strategies are in place when accessing shared scopes and/or resources.

```java
myArray.each( function( item ){
   myservice.process( item );
}, true, 20 );
```

Even though this approach to multi-threaded looping is easy, it is not performant and/or flexible. Under the hood, the engine uses a single thread executor for each execution. They do not allow you to deal with exceptions, and if an exception occurs in an element processor, good luck; you will never know about it. This approach can be verbose and error-prone, but it's easy. You also don't control where the processing thread runs and are at the mercy of the engine.

### ColdBox Futures Parallel Programming

If you would like a functional and much more flexible approach to multi-threaded or parallel programming, consider using the ColdBox Futures approach (usable in ANY framework or non-framework code). You can use it by installing ColdBox or WireBox into any BoxLang application and leveraging our `async` programming constructs, which behind the scenes, leverage the entire Java Concurrency and Completable Futures frameworks.

{% embed url="https://coldbox.ortusbooks.com/digging-deeper/promises-async-programming/parallel-computations" %}
ColdBox Futures and Async Programming
{% endembed %}

Here are some methods that will allow you to do parallel computations:

* `all( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures to execute them in parallel. When you call on it, it will return a future that will retrieve an array of the results of all the operations.
* `allApply( items, fn, executor ):array` : This function can accept an array of items or a struct of items of any type and apply a function to each item in parallel. The `fn` argument receives the appropriate item and must return a result. Consider this a parallel `map()` operation.
* `anyOf( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures and will execute them in parallel. However, instead of returning all of the results in an array like `all()`, this method will return the future that executes the fastest! Race Baby!
* `withTimeout( timeout, timeUnit )` : Apply a timeout to `all()` or `allApply()` operations. The `timeUnit` can be days, hours, microseconds, milliseconds, minutes, nanoseconds, and seconds. The default is milliseconds.

```javascript
// Let's find the fastest dns server
var f = asyncManager().anyOf( ()=>dns1.resolve(), ()=>dns2.resolve() );

// Let's process some data
var data = [1,2, ... 100 ];
var results = asyncManager().all( data );

// Process multiple futures
var f1 = asyncManager.newFuture( function(){
    return "hello";
} );
var f2 = asyncManager.newFuture( function(){
    return "world!";
} );
var aResults = asyncManager.newFuture()
    .withTimeout( 5 )
    .all( f1, f2 );

// Process mementos for an array of objects
function index( event, rc, prc ){
    return async().allApply(
        orderService.findAll(),
        ( order ) => order.getMemento()
    );
}
```

## Spread Operator

Arrays also allow the usage of the spread operator syntax to quickly copy all or part of an existing array or object into another array or object. This operator is used by leveraging three dots `...` in specific expressions.

The Spread syntax allows an iterable such as an array expression or string, to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected. Here are some examples to help you understand this operator:

#### Function Calls

```javascript
numbers = [ 1, 2, 3 ]
function sum( x, y, z ){
    return x + y + z;
}
// Call the function using the spread operator
results = sum( ...numbers ) // 6

// Ignore the others
numbers = [ 1, 2, 3, 4, 5 ]
results = sum( ...numbers ) // 6
```

#### Array Definitions

```javascript
numbers = [ 1, 2, 3 ]
myArray = [ 3, 4, ...numbers ]
myArray2 = [ ...numbers ]
myArray2 = [ ...numbers, 4, 66 ]
```

## Rest Operator

The rest operator is similar to the spread operator but behaves oppositely. Instead of expanding the literals, it contracts them into an array you designate via the `...{name}` syntax. You can use this to define endless arguments for a function, for example. In this case, I can create a dynamic `findBy` function that takes in multiple criteria name-value pairs.

```javascript
function findBy( ...args ){
    writeDump( args )
}
findBy( 1, 2, 3, 4, 5 )

function findBy( entityName, ...args ){
    writeDump( args )
}
findBy( "Luis", 1, 2, 3, 4, 5 )
```
