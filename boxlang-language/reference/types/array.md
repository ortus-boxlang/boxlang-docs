# array

The primary array class in BoxLang.

This class wraps a Java List and provides additional functionality for BoxLang.

BoxLang indices are one-based, so the first element is at index 1, not 0.

## Array Methods

<details>

<summary><code>append(value=[any], merge=[boolean])</code></summary>

Append a value to an array

Arguments:

</details>

<details>

<summary><code>avg()</code></summary>

Return length of array

</details>

<details>

<summary><code>clear()</code></summary>

Clear all items from array

</details>

<details>

<summary><code>contains(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index. If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

,

```
,
( value, index ) => {
return true; // if the value is found, else false
}
,
```

,

Example:

,

```
,
array = [ 1, 2, 3, 4, 5 ];
index = array.find( ( value, index ) -> {
return value == 3;
} );
,
```

,

We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects. They will be faster and more efficient.

Arguments:

</details>

<details>

<summary><code>containsNoCase(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index. If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

,

```
,
( value, index ) => {
return true; // if the value is found, else false
}
,
```

,

Example:

,

```
,
array = [ 1, 2, 3, 4, 5 ];
index = array.find( ( value, index ) -> {
return value == 3;
} );
,
```

,

We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects. They will be faster and more efficient.

Arguments:

</details>

<details>

<summary><code>copyOf(arr=[any])</code></summary>

Create a new Array from a list of values.

Arguments:

</details>

<details>

<summary><code>delete(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

Arguments:

</details>

<details>

<summary><code>deleteAt(index=[integer])</code></summary>

Delete item at specified index in array

Arguments:

</details>

<details>

<summary><code>deleteNoCase(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

Arguments:

</details>

<details>

<summary><code>each(callback=[function:Consumer], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

</details>

<details>

<summary><code>equals(obj=[any])</code></summary>

Verifies equality with the following rules:

* Same object
* Super class

Arguments:

</details>

<details>

<summary><code>every(callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Returns true if every closure returns true, otherwise false

Arguments:

</details>

<details>

<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Used to filter an array to items for which the closure function returns true.

Arguments:

</details>

<details>

<summary><code>find(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is no match.

Arguments:

</details>

<details>

<summary><code>findAll(value=[any])</code></summary>

Return an array containing the indexes of matched values

Arguments:

</details>

<details>

<summary><code>findAllNoCase(value=[any])</code></summary>

Return an array containing the indexes of matched values

Arguments:

</details>

<details>

<summary><code>findNoCase(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index. If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

,

```
,
( value, index ) => {
return true; // if the value is found, else false
}
,
```

,

Example:

,

```
,
array = [ 1, 2, 3, 4, 5 ];
index = array.find( ( value, index ) -> {
return value == 3;
} );
,
```

,

We recommend you use BoxLang lambdas (,{@code ->},) for this purpose, so they only act upon the value and index without any side effects. They will be faster and more efficient.

Arguments:

</details>

<details>

<summary><code>first()</code></summary>

Return first item in array

</details>

<details>

<summary><code>getMetadata()</code></summary>

Gets metadata for items of an array and indicates the array type.

</details>

<details>

<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

Arguments:

</details>

<details>

<summary><code>indexExists(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

Arguments:

</details>

<details>

<summary><code>insertAt(position=[integer], value=[any])</code></summary>

Append a value to an array

Arguments:

</details>

<details>

<summary><code>isDefined(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

Arguments:

</details>

<details>

<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of anything that can be casted to: Array, Struct, Query, or String.

</details>

<details>

<summary><code>join(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

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

<summary><code>map(callback=[function:Function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the same index in a new array and the new array will be returned

Arguments:

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

To add all the data from one array into another without creating a new array see the built in function ArrayAppend(arr1, arr2, true).

Arguments:

</details>

<details>

<summary><code>mid(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

Arguments:

</details>

<details>

<summary><code>min()</code></summary>

Return length of array

</details>

<details>

<summary><code>of(values=[any])</code></summary>

Create an Array from a list of values.

Each value is passed in as a separate argument

Arguments:

</details>

<details>

<summary><code>parallelStream()</code></summary>

Returns a parallel stream of the array

</details>

<details>

<summary><code>pop(defaultValue=[any])</code></summary>

Remove last item in array and return it

Arguments:

</details>

<details>

<summary><code>prepend(value=[any])</code></summary>

Append a value to the start an array

Arguments:

</details>

<details>

<summary><code>push(value=[any])</code></summary>

Adds an element or an object to the end of an array, then returns the size of the modified array.

Arguments:

</details>

<details>

<summary><code>range(to=[numeric])</code></summary>

Build an array out of a range of numbers or using our range syntax: {start}..{end} or using the from and to arguments

, You can also build negative ranges ,

,

,

```
,
arrayRange( "1..5" )
arrayRange( "-10..5" )
arrayRange( 1, 500 )
,
```

Arguments:

</details>

<details>

<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

Run the provided udf over the array to reduce the values to a single output

Arguments:

</details>

<details>

<summary><code>reduceRight(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value, from the right to the left, and return it.

Arguments:

</details>

<details>

<summary><code>resize(size=[any])</code></summary>

Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its expected maximum. For more than 500 elements, use arrayResize immediately after using the ArrayNew BIF.

Arguments:

</details>

<details>

<summary><code>reverse()</code></summary>

Returns an array with all of the elements reversed.

The value in \[0] within the input array will then exist in \[n] in the output array, where n is the amount of elements in the array minus one.

</details>

<details>

<summary><code>set(start=[any], end=[any], value=[any])</code></summary>

In a one-dimensional array, sets the elements in a specified index range to a value.

Useful for initializing an array after a call to arrayNew.

Arguments:

</details>

<details>

<summary><code>shift(defaultValue=[any])</code></summary>

Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an exception will be thrown.

Arguments:

</details>

<details>

<summary><code>slice(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

Arguments:

</details>

<details>

<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

Arguments:

</details>

<details>

<summary><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[function:Comparator])</code></summary>

Sorts array elements.

Arguments:

</details>

<details>

<summary><code>splice(index=[Integer], elementCountForRemoval=[Integer], replacements=[array])</code></summary>

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by elementCountForRemoval, and puts the replacements starting from index position.

Arguments:

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

</details>

<details>

<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string.

Arguments:

</details>

<details>

<summary><code>toList(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

</details>

<details>

<summary><code>toModifiable()</code></summary>

Convert an array, struct or query to its Modifiable counterpart.

</details>

<details>

<summary><code>toStruct()</code></summary>

Transform the array to a struct, the index of the array is the key of the struct

</details>

<details>

<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct or query to its Unmodifiable counterpart.

</details>

<details>

<summary><code>unshift(object=[any])</code></summary>

This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

Arguments:

</details>

## Examples
