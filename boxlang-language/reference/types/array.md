[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Array`

The primary array class in BoxLang.

This class wraps a Java List and provides additional functionality for BoxLang.

 BoxLang indices are one-based, so the first element is at index 1, not 0.

## Array Methods

<dl>
<dt><code>append(value=[any], merge=[boolean])</code></dt><dd>Append a value to an array

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `merge` | `boolean` | `false` | `false` |

</dd>
<dt><code>avg()</code></dt><dd>Return length of array</dd>
<dt><code>clear()</code></dt><dd>Clear all items from array</dd>
<dt><code>contains(value=[any], substringMatch=[boolean])</code></dt><dd>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `substringMatch` | `boolean` | `false` | `false` |

</dd>
<dt><code>containsNoCase(value=[any], substringMatch=[boolean])</code></dt><dd>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `substringMatch` | `boolean` | `false` | `false` |

</dd>
<dt><code>copyOf(arr=[any])</code></dt><dd>Create a new Array from a list of values.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `arr` | `any` | `true` | null |

</dd>
<dt><code>delete(value=[any], scope=[string])</code></dt><dd>Delete first occurance of item in array case sensitive

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>deleteAt(index=[integer])</code></dt><dd>Delete item at specified index in array

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `integer` | `true` | `` |

</dd>
<dt><code>deleteNoCase(value=[any], scope=[string])</code></dt><dd>Delete first occurance of item in array case sensitive

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])</code></dt><dd>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `ordered` | `boolean` | `false` | `false` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>equals(obj=[any])</code></dt><dd>Verifies equality with the following rules:
 - Same object
 - Super class

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `obj` | `any` | `true` | null |

</dd>
<dt><code>every(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></dt><dd>Returns true if every closure returns true, otherwise false

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></dt><dd>Used to filter an array to items for which the closure function returns true.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>find(value=[any], substringMatch=[boolean])</code></dt><dd>This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `substringMatch` | `boolean` | `false` | `false` |

</dd>
<dt><code>findAll(value=[any])</code></dt><dd>Return an array containing the indexes of matched values

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |

</dd>
<dt><code>findAllNoCase(value=[any])</code></dt><dd>Return an array containing the indexes of matched values

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |

</dd>
<dt><code>findNoCase(value=[any], substringMatch=[boolean])</code></dt><dd>Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |
| `substringMatch` | `boolean` | `false` | `false` |

</dd>
<dt><code>first()</code></dt><dd>Return first item in array</dd>
<dt><code>getMetadata()</code></dt><dd>Gets metadata for items of an array and indicates the array type.</dd>
<dt><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></dt><dd>Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</dd>
<dt><code>indexExists(index=[any])</code></dt><dd>Returns whether there exists an item in the array at the selected index.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `any` | `true` | `` |

</dd>
<dt><code>insertAt(position=[integer], value=[any])</code></dt><dd>Append a value to an array

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |
| `value` | `any` | `true` | `` |

</dd>
<dt><code>isDefined(index=[any])</code></dt><dd>Returns whether there exists an item in the array at the selected index.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `any` | `true` | `` |

</dd>
<dt><code>isEmpty()</code></dt><dd>Determine whether a given value is empty</dd>
<dt><code>join(delimiter=[String], initialValue=[any])</code></dt><dd>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `String` | `false` | `,` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>last()</code></dt><dd>Return first item in array</dd>
<dt><code>len()</code></dt><dd>Returns the absolute value of a number</dd>
<dt><code>map(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></dt><dd>Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>max()</code></dt><dd>Return length of array</dd>
<dt><code>median()</code></dt><dd>Return the median value of an array.

Will only work on arrays that contain only numeric values.</dd>
<dt><code>merge(array2=[array], leaveIndex=[boolean])</code></dt><dd>This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `array2` | `array` | `true` | `` |
| `leaveIndex` | `boolean` | `true` | `false` |

</dd>
<dt><code>mid(start=[integer], length=[integer])</code></dt><dd>Extracts a sub array from an existing array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `1` |
| `length` | `integer` | `false` | `0` |

</dd>
<dt><code>min()</code></dt><dd>Return length of array</dd>
<dt><code>of(values=[any])</code></dt><dd>Create an Array from a list of values.

Each value is passed in as a separate argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | null |

</dd>
<dt><code>parallelStream()</code></dt><dd>Returns a parallel stream of the array</dd>
<dt><code>pop(defaultValue=[any])</code></dt><dd>Remove last item in array and return it

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `defaultValue` | `any` | `false` | `` |

</dd>
<dt><code>prepend(value=[any])</code></dt><dd>Append a value to the start an array

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |

</dd>
<dt><code>push(value=[any])</code></dt><dd>Adds an element or an object to the end of an array, then returns the size of the modified array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `` |

</dd>
<dt><code>reduce(callback=[function], initialValue=[any])</code></dt><dd>Run the provided udf over the array to reduce the values to a single output

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>reduceRight(callback=[function], initialValue=[any])</code></dt><dd>This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>resize(size=[any])</code></dt><dd>Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `size` | `any` | `true` | `` |

</dd>
<dt><code>reverse()</code></dt><dd>Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.</dd>
<dt><code>set(start=[any], end=[any], value=[any])</code></dt><dd>In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `any` | `true` | `` |
| `end` | `any` | `true` | `` |
| `value` | `any` | `true` | `` |

</dd>
<dt><code>shift(defaultValue=[any])</code></dt><dd>Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an
 exception will be thrown.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `defaultValue` | `any` | `false` | `` |

</dd>
<dt><code>slice(start=[integer], length=[integer])</code></dt><dd>Extracts a sub array from an existing array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `1` |
| `length` | `integer` | `false` | `0` |

</dd>
<dt><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></dt><dd>Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[any])</code></dt><dd>Sorts array elements.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `` |
| `sortOrder` | `string` | `false` | `asc` |
| `localeSensitive` | `boolean` | `false` | `` |
| `callback` | `any` | `false` | `` |

</dd>
<dt><code>splice(index=[numeric], elementCountForRemoval=[numeric], replacements=[array])</code></dt><dd>Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `numeric` | `true` | `` |
| `elementCountForRemoval` | `numeric` | `false` | `0` |
| `replacements` | `array` | `false` | `` |

</dd>
<dt><code>stream()</code></dt><dd>Returns a stream of the array</dd>
<dt><code>sum()</code></dt><dd>Returns the sum of all values in an array</dd>
<dt><code>swap(position1=[any], position2=[any])</code></dt><dd>Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position1` | `any` | `true` | `` |
| `position2` | `any` | `true` | `` |

</dd>
<dt><code>toImmutable()</code></dt><dd>Convert an array, struct or query to its immutable counterpart.</dd>
<dt><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></dt><dd>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `` |

</dd>
<dt><code>toList(delimiter=[String], initialValue=[any])</code></dt><dd>Used to iterate over an array and run the function closure for each item in the array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `String` | `false` | `,` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>toMutable()</code></dt><dd>Convert an array, struct or query to its mutable counterpart.</dd>
<dt><code>toStruct()</code></dt><dd>Transform the array to a struct, the index of the array is the key of the struct</dd>
<dt><code>unshift(object=[any])</code></dt><dd>This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `object` | `any` | `true` | `` |

</dd>

</dl>

## Examples
