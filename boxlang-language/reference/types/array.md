[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Array`

The primary array class in BoxLang.

This class wraps a Java List and provides additional functionality for BoxLang.

 BoxLang indices are one-based, so the first element is at index 1, not 0.

## Array Methods

<details>
<summary><code>append(value=[any], merge=[boolean])</code></summary>

Append a value to an array

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `merge` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>avg()</code></summary>

Return length of array
</details>
<details>
<summary><code>bxDump(label=[string], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>,
 The available ,<code>,output,</code>, locations are:
 - ,<strong>,buffer,</strong>,: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - ,<strong>,console,</strong>,: The output is printed to the System console.
 - ,<strong>,Absolute File Path,</strong>, The output is written to a file with the specified absolute file path.
 ,</p>,
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `label` | `string` | `false` | `null` |
| `top` | `numeric` | `false` | `null` |
| `expand` | `boolean` | `false` | `true` |
| `abort` | `boolean` | `false` | `false` |
| `output` | `string` | `false` | `null` |
| `format` | `string` | `false` | `null` |
| `showUDFs` | `boolean` | `false` | `true` |

</details>
<details>
<summary><code>chunk(length=[integer])</code></summary>

Chunks the array into an array of arrays of the specified size.

The final chunk may be shorter if the array does not divide evenly.

 ,<pre>,
 numbers = [ 1, 2, 3, 4, 5 ];
 numbers.chunk( 2 ); // [ [ 1, 2 ], [ 3, 4 ], [ 5 ] ]
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `length` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>clear()</code></summary>

Clear all items from array
</details>
<details>
<summary><code>contains(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.
 If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

 ,<pre>,
    ( value, index ) => {
 	  	return true; // if the value is found, else false
   }
 ,</pre>,

 Example:

 ,<pre>,
   array = [ 1, 2, 3, 4, 5 ];
  index = array.find( ( value, index ) -> {
 		return value == 3;
 } );
 ,</pre>,

 We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects.
 They will be faster and more efficient.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>containsNoCase(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.
 If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

 ,<pre>,
    ( value, index ) => {
 	  	return true; // if the value is found, else false
   }
 ,</pre>,

 Example:

 ,<pre>,
   array = [ 1, 2, 3, 4, 5 ];
  index = array.find( ( value, index ) -> {
 		return value == 3;
 } );
 ,</pre>,

 We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects.
 They will be faster and more efficient.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>delete(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `scope` | `string` | `false` | `one` |

</details>
<details>
<summary><code>deleteAt(index=[integer])</code></summary>

Delete item at specified index in array

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>deleteNoCase(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `scope` | `string` | `false` | `one` |

</details>
<details>
<summary><code>duplicate(deep=[boolean])</code></summary>

Duplicates an object - either shallow or deep

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `deep` | `boolean` | `false` | `true` |

</details>
<details>
<summary><code>each(callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

This BIF is used to perform an operation on each item in the array, similar to Java's forEach method.
 It can also be used to perform operations in parallel if the `parallel` argument is set to true.

 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the iterator will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the iterator in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Consumer` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `ordered` | `boolean` | `false` | `false` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>equals(obj=[any])</code></summary>

Verifies equality with the following rules:
 - Same object
 - Super class

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `obj` | `any` | `true` | `null` |

</details>
<details>
<summary><code>every(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 ,<p>,
 ,<strong>,Note:,</strong>, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 ,<p>,
 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large arrays, especially when the test function is computationally expensive or the array is large.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters an array and returns a new array containing the result
 This BIF will invoke the callback function for each item in the array, passing the item, its index, and the array itself.

<ul>,
 ,<li>,If the callback returns true, the item will be included in the new array.,</li>,
 ,<li>,If the callback returns false, the item will be excluded from the new array.,</li>,
 ,<li>,If the callback requires strict arguments, it will only receive the item and its index.,</li>,
 ,<li>,If the callback does not require strict arguments, it will receive the item, its index, and the array itself.,</li>,
 ,</ul>,

 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>find(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>findAll(value=[any])</code></summary>

Return an array containing the indexes of matched values

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>findAllNoCase(value=[any])</code></summary>

Return an array containing the indexes of matched values

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>findFirst(callback=[function], defaultValue=[any], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Return first item in array that matches the predicate function.

<pre>,
 users = [ { name: "Ada" }, { name: "Grace" } ];
 users.findFirst( ( user ) => user.name == "Grace" ); // { name: "Grace" }
 users.findFirst( ( user ) => user.name == "Linus", "Unknown" ); // "Unknown"
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `defaultValue` | `any` | `false` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>findNoCase(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.
 If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

 ,<pre>,
    ( value, index ) => {
 	  	return true; // if the value is found, else false
   }
 ,</pre>,

 Example:

 ,<pre>,
   array = [ 1, 2, 3, 4, 5 ];
  index = array.find( ( value, index ) -> {
 		return value == 3;
 } );
 ,</pre>,

 We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects.
 They will be faster and more efficient.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>first(defaultValue=[any])</code></summary>

Return first item in array

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `defaultValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>flatMap(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Maps each element and flattens the result one level.

<pre>,
 values = [ 1, 2, 3 ];
 values.flatMap( ( value ) => [ value, value * 10 ] );
 // [ 1, 10, 2, 20, 3, 30 ]
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>flatten(depth=[integer])</code></summary>

Flattens nested arrays to the specified depth.

When depth is omitted, the array is flattened completely.

 ,<pre>,
 nested = [ 1, [ 2, [ 3 ] ] ];
 nested.flatten(); // [ 1, 2, 3 ]
 nested.flatten( 1 ); // [ 1, 2, [ 3 ] ]
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `depth` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>getMetadata()</code></summary>

Gets metadata for items of an array and indicates the array type.
</details>
<details>
<summary><code>groupBy(callback=[function])</code></summary>

Returns a struct of keys returned from the predicate function and values of arrays of matching rows.

<pre>,
 values = [ 1, 2, 3, 4 ];
 values.groupBy( ( value ) => value % 2 ? "odd" : "even" );
 // { odd: [ 1, 3 ], even: [ 2, 4 ] }
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |

</details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</details>
<details>
<summary><code>indexExists(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `any` | `true` | `null` |

</details>
<details>
<summary><code>insertAt(position=[integer], value=[any])</code></summary>

Append a value to an array

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `null` |
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>isDefined(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `any` | `true` | `null` |

</details>
<details>
<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of
 anything that can be casted to: Array, Struct, Query, or String.
</details>
<details>
<summary><code>join(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `String` | `false` | `,` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>last()</code></summary>

Return first item in array
</details>
<details>
<summary><code>len()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>map(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>max()</code></summary>

Get the max value from an array
</details>
<details>
<summary><code>median()</code></summary>

Return the median value of an array.

Will only work on arrays that contain only numeric values.
</details>
<details>
<summary><code>merge(array2=[array], leaveIndex=[boolean])</code></summary>

This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `array2` | `array` | `true` | `null` |
| `leaveIndex` | `boolean` | `true` | `false` |

</details>
<details>
<summary><code>mid(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `1` |
| `length` | `integer` | `false` | `0` |

</details>
<details>
<summary><code>min()</code></summary>

Return length of array
</details>
<details>
<summary><code>none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of ,{@link ArraySome},.
 ,<p>,
 The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 ,<p>,
 ,<strong>,Note:,</strong>, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does meet the test condition.
 ,<p>,
 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large arrays, especially when the test function is computationally expensive or the array is large.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>parallelStream()</code></summary>

Returns a parallel stream of the array
</details>
<details>
<summary><code>pop(defaultValue=[any])</code></summary>

Remove last item in array and return it

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `defaultValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>prepend(value=[any])</code></summary>

Append a value to the start an array

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>push(value=[any])</code></summary>

Adds an element or an object to the end of an array, then returns the size of the modified array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>range(to=[numeric])</code></summary>

Build an array out of a range of numbers or using our range syntax: {start}..{end}
 or using the from and to arguments

<p>,
 You can also build negative ranges
 ,<p>,

 ,<pre>,
 arrayRange( "1..5" )
 arrayRange( "-10..5" )
 arrayRange( 1, 500 )
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `to` | `numeric` | `false` | `null` |

</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

Run the provided udf over the array to reduce the values to a single output

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:BiFunction` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>reduceRight(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:BiFunction` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>reject(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters an array and returns a new array containing the result.

This is the inverse of ,{@code ArrayFilter},.

 ,<pre>,
 values = [ 1, 2, 3, 4 ];
 values.reject( ( value ) => value % 2 == 0 ); // [ 1, 3 ]
 ,</pre>,
 
 This BIF will invoke the callback function for each item in the array, passing the item, its index, and the array itself.
 ,<ul>,
 ,<li>,If the callback returns false, the item will be included in the new array.,</li>,
 ,<li>,If the callback returns true, the item will be excluded from the new array.,</li>,
 ,<li>,If the callback requires strict arguments, it will only receive the item and its index.,</li>,
 ,<li>,If the callback does not require strict arguments, it will receive the item, its index, and the array itself.,</li>,
 ,</ul>,

 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>resize(size=[integer])</code></summary>

Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `size` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>reverse()</code></summary>

Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.
</details>
<details>
<summary><code>set(start=[any], end=[any], value=[any])</code></summary>

In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `any` | `true` | `null` |
| `end` | `any` | `true` | `null` |
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>shift(defaultValue=[any])</code></summary>

Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an
 exception will be thrown.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `defaultValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>slice(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `1` |
| `length` | `integer` | `false` | `0` |

</details>
<details>
<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 ,<p>,
 ,<strong>,Note:,</strong>, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.
 ,<p>,
 ,<h2>,Parallel Execution,</h2>,
 If the ,<code>,parallel,</code>, argument is set to true, and no ,<code>,max_threads,</code>, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If ,<code>,max_threads,</code>, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.
 ,<p>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[function:Comparator])</code></summary>

Sorts array elements.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `textnocase` |
| `sortOrder` | `string` | `false` | `asc` |
| `localeSensitive` | `boolean` | `false` | `false` |
| `callback` | `function:Comparator` | `false` | `null` |

</details>
<details>
<summary><code>splice(index=[Integer], elementCountForRemoval=[Integer], replacements=[array])</code></summary>

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `Integer` | `true` | `null` |
| `elementCountForRemoval` | `Integer` | `false` | `0` |
| `replacements` | `array` | `false` | `null` |

</details>
<details>
<summary><code>stream()</code></summary>

Returns a stream of the array
</details>
<details>
<summary><code>sum()</code></summary>

Returns the sum of all values in an array
</details>
<details>
<summary><code>swap(position1=[any], position2=[any])</code></summary>

Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position1` | `any` | `true` | `null` |
| `position2` | `any` | `true` | `null` |

</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>,Query Format Options,</h2>,
 The ,<code>,queryFormat,</code>, argument determines how queries are serialized:
 ,<ul>,
 ,<li>,<code>,row,</code>, or ,<code>,false,</code>,: Serializes the query as a top-level struct with two keys:
 ,<code>,columns,</code>, (an array of column names) and ,<code>,data,</code>, (an array of arrays representing
 each row's data).,</li>,
 ,<li>,<code>,column,</code>, or ,<code>,true,</code>,: Serializes the query as a top-level struct with three keys:
 ,<code>,rowCount,</code>, (the number of rows), ,<code>,columns,</code>, (an array of column names), and
 ,<code>,data,</code>, (a struct where each key is a column name and the value is an array of values for that column).,</li>,
 ,<li>,<code>,struct,</code>,: Serializes the query as an array of structs, where each struct represents a row of data.,</li>,
 ,</ul>,

 ,<h2>,Usage,</h2>,

 ,<pre>,
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `null` |
| `useSecureJSONPrefix` | `string` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |
| `pretty` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>toList(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `String` | `false` | `,` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>toModifiable()</code></summary>

Convert an array, struct, query or set to its Modifiable counterpart.
</details>
<details>
<summary><code>toSet(type=[string], delimiter=[string])</code></summary>

Convert a collection into a Set, deduplicating automatically.

Accepts an Array, a list-delimited String,
 an existing Set, a QueryColumn, an XML node, a bounded Range, or any value castable to a Set. When the
 value is already of the requested variant it is returned as-is; otherwise a new Set of the specified
 variant is created and populated.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `type` | `string` | `false` | `default` |
| `delimiter` | `string` | `false` | `,` |

</details>
<details>
<summary><code>toStruct()</code></summary>

Transform the array to a struct, the index of the array is the key of the struct
</details>
<details>
<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct, query or set to its Unmodifiable counterpart.
</details>
<details>
<summary><code>transpose()</code></summary>

Returns a transposed array based on all passed in arrays.

<pre>,
 arrayTranspose(
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
 );
 // [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
 ,</pre>
</details>
<details>
<summary><code>unique(caseSensitive=[boolean])</code></summary>

Returns a new array with duplicate items removed.

<pre>,
 values = [ 1, 1, 2, 3, 3 ];
 values.unique(); // [ 1, 2, 3 ]
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `caseSensitive` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>unshift(object=[any])</code></summary>

This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `object` | `any` | `true` | `null` |

</details>
<details>
<summary><code>zip(array2=[array], callback=[function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Returns a zipped array.

<pre>,
 arrayZip( [ 1, 2 ], [ "a", "b" ] );
 // [ [ 1, "a" ], [ 2, "b" ] ]

 arrayZip( [ 1, 2 ], [ 10, 20 ], ( a, b ) => a + b );
 // [ 11, 22 ]
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `array2` | `array` | `true` | `null` |
| `callback` | `function` | `false` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `any` | `false` | `null` |
| `virtual` | `boolean` | `false` | `false` |

</details>


## Examples
