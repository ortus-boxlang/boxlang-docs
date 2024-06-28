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
<summary><code>clear()</code></summary>

Clear all items from array
</details>
<details>
<summary><code>contains(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

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

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>copyOf(arr=[any])</code></summary>

Create a new Array from a list of values.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `arr` | `any` | `true` | `null` |

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
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `ordered` | `boolean` | `false` | `false` |
| `initialValue` | `any` | `false` | `null` |

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
<summary><code>every(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Returns true if every closure returns true, otherwise false

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Used to filter an array to items for which the closure function returns true.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `initialValue` | `any` | `false` | `null` |

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
<summary><code>findNoCase(value=[any], substringMatch=[boolean])</code></summary>

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |
| `substringMatch` | `boolean` | `false` | `false` |

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

Determine whether a given value is empty
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
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>max()</code></summary>

Return length of array
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
<summary><code>of(values=[any])</code></summary>

Create an Array from a list of values.

Each value is passed in as a separate argument

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | `null` |

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
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>

Run the provided udf over the array to reduce the values to a single output

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>reduceRight(callback=[function], initialValue=[any])</code></summary>

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>resize(size=[any])</code></summary>

Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `size` | `any` | `true` | `null` |

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
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[any])</code></summary>

Sorts array elements.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `textnocase` |
| `sortOrder` | `string` | `false` | `asc` |
| `localeSensitive` | `boolean` | `false` | `null` |
| `callback` | `any` | `false` | `null` |

</details>
<details>
<summary><code>splice(index=[numeric], elementCountForRemoval=[numeric], replacements=[array])</code></summary>

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `numeric` | `true` | `null` |
| `elementCountForRemoval` | `numeric` | `false` | `0` |
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
<summary><code>toImmutable()</code></summary>

Convert an array, struct or query to its immutable counterpart.
</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>

Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |

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
<summary><code>toMutable()</code></summary>

Convert an array, struct or query to its mutable counterpart.
</details>
<details>
<summary><code>toStruct()</code></summary>

Transform the array to a struct, the index of the array is the key of the struct
</details>
<details>
<summary><code>unshift(object=[any])</code></summary>

This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `object` | `any` | `true` | `null` |

</details>


## Examples
