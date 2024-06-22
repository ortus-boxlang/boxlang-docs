[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Array`

The primary array class in BoxLang.

This class wraps a Java List and provides additional functionality for BoxLang.

 BoxLang indices are one-based, so the first element is at index 1, not 0.

## Array Methods

<details>
<summary><code>append(value=[any], merge=[boolean])</code></summary>
<p>Append a value to an array

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`merge`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>avg()</code></summary>
<p>Return length of array
</p></details>
<details>
<summary><code>clear()</code></summary>
<p>Clear all items from array
</p></details>
<details>
<summary><code>contains(value=[any], substringMatch=[boolean])</code></summary>
<p>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substringMatch`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>containsNoCase(value=[any], substringMatch=[boolean])</code></summary>
<p>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substringMatch`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>copyOf(arr=[any])</code></summary>
<p>Create a new Array from a list of values.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`arr`</td>
<td>`any`</td>
<td>`true`</td>
<td>`null`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>delete(value=[any], scope=[string])</code></summary>
<p>Delete first occurance of item in array case sensitive

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`false`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>deleteAt(index=[integer])</code></summary>
<p>Delete item at specified index in array

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`index`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>deleteNoCase(value=[any], scope=[string])</code></summary>
<p>Delete first occurance of item in array case sensitive

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`false`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])</code></summary>
<p>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`ordered`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>equals(obj=[any])</code></summary>
<p>Verifies equality with the following rules:
 - Same object
 - Super class

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`obj`</td>
<td>`any`</td>
<td>`true`</td>
<td>`null`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>every(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>Returns true if every closure returns true, otherwise false

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>Used to filter an array to items for which the closure function returns true.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>find(value=[any], substringMatch=[boolean])</code></summary>
<p>This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substringMatch`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findAll(value=[any])</code></summary>
<p>Return an array containing the indexes of matched values

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findAllNoCase(value=[any])</code></summary>
<p>Return an array containing the indexes of matched values

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findNoCase(value=[any], substringMatch=[boolean])</code></summary>
<p>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substringMatch`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>first()</code></summary>
<p>Return first item in array
</p></details>
<details>
<summary><code>getMetadata()</code></summary>
<p>Gets metadata for items of an array and indicates the array type.
</p></details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>
<p>Creates an algorithmic hash of an object

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`algorithm`</td>
<td>`string`</td>
<td>`false`</td>
<td>`MD5`</td>
</tr>

<tr>
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>`utf-8`</td>
</tr>

<tr>
<td>`numIterations`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>indexExists(index=[any])</code></summary>
<p>Returns whether there exists an item in the array at the selected index.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`index`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>insertAt(position=[integer], value=[any])</code></summary>
<p>Append a value to an array

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`position`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>isDefined(index=[any])</code></summary>
<p>Returns whether there exists an item in the array at the selected index.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`index`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>isEmpty()</code></summary>
<p>Determine whether a given value is empty
</p></details>
<details>
<summary><code>join(delimiter=[String], initialValue=[any])</code></summary>
<p>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`delimiter`</td>
<td>`String`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>last()</code></summary>
<p>Return first item in array
</p></details>
<details>
<summary><code>len()</code></summary>
<p>Returns the absolute value of a number
</p></details>
<details>
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>max()</code></summary>
<p>Return length of array
</p></details>
<details>
<summary><code>median()</code></summary>
<p>Return the median value of an array.

Will only work on arrays that contain only numeric values.
</p></details>
<details>
<summary><code>merge(array2=[array], leaveIndex=[boolean])</code></summary>
<p>This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`array2`</td>
<td>`array`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`leaveIndex`</td>
<td>`boolean`</td>
<td>`true`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>mid(start=[integer], length=[integer])</code></summary>
<p>Extracts a sub array from an existing array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`true`</td>
<td>`1`</td>
</tr>

<tr>
<td>`length`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`0`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>min()</code></summary>
<p>Return length of array
</p></details>
<details>
<summary><code>of(values=[any])</code></summary>
<p>Create an Array from a list of values.

Each value is passed in as a separate argument

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`values`</td>
<td>`any`</td>
<td>`true`</td>
<td>`null`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>parallelStream()</code></summary>
<p>Returns a parallel stream of the array
</p></details>
<details>
<summary><code>pop(defaultValue=[any])</code></summary>
<p>Remove last item in array and return it

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`defaultValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>prepend(value=[any])</code></summary>
<p>Append a value to the start an array

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>push(value=[any])</code></summary>
<p>Adds an element or an object to the end of an array, then returns the size of the modified array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>
<p>Run the provided udf over the array to reduce the values to a single output

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reduceRight(callback=[function], initialValue=[any])</code></summary>
<p>This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>resize(size=[any])</code></summary>
<p>Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`size`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reverse()</code></summary>
<p>Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.
</p></details>
<details>
<summary><code>set(start=[any], end=[any], value=[any])</code></summary>
<p>In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`start`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`end`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>shift(defaultValue=[any])</code></summary>
<p>Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an
 exception will be thrown.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`defaultValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>slice(start=[integer], length=[integer])</code></summary>
<p>Extracts a sub array from an existing array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`true`</td>
<td>`1`</td>
</tr>

<tr>
<td>`length`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`0`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[any])</code></summary>
<p>Sorts array elements.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`sortType`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`sortOrder`</td>
<td>`string`</td>
<td>`false`</td>
<td>`asc`</td>
</tr>

<tr>
<td>`localeSensitive`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`callback`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>splice(index=[numeric], elementCountForRemoval=[numeric], replacements=[array])</code></summary>
<p>Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`index`</td>
<td>`numeric`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`elementCountForRemoval`</td>
<td>`numeric`</td>
<td>`false`</td>
<td>`0`</td>
</tr>

<tr>
<td>`replacements`</td>
<td>`array`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>stream()</code></summary>
<p>Returns a stream of the array
</p></details>
<details>
<summary><code>sum()</code></summary>
<p>Returns the sum of all values in an array
</p></details>
<details>
<summary><code>swap(position1=[any], position2=[any])</code></summary>
<p>Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`position1`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`position2`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toImmutable()</code></summary>
<p>Convert an array, struct or query to its immutable counterpart.
</p></details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>
<p>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`queryFormat`</td>
<td>`string`</td>
<td>`false`</td>
<td>`row`</td>
</tr>

<tr>
<td>`useSecureJSONPrefix`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`useCustomSerializer`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toList(delimiter=[String], initialValue=[any])</code></summary>
<p>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`delimiter`</td>
<td>`String`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toMutable()</code></summary>
<p>Convert an array, struct or query to its mutable counterpart.
</p></details>
<details>
<summary><code>toStruct()</code></summary>
<p>Transform the array to a struct, the index of the array is the key of the struct
</p></details>
<details>
<summary><code>unshift(object=[any])</code></summary>
<p>This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`object`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>


## Examples
