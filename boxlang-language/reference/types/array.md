# Type: `array`



## array Methods

### array

#### Functions:

 * `hash`: Creates an algorithmic hash of an object
 * `prepend`: Append a value to the start an array
 * `resize`: Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.
 * `reduce`: Run the provided udf over the array to reduce the values to a single output
 * `merge`: This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).
 * `indexExists`: Returns whether there exists an item in the array at the selected index.
 * `isDefined`: Returns whether there exists an item in the array at the selected index.
 * `findAll`: Return an array containing the indexes of matched values
 * `findAllNoCase`: Return an array containing the indexes of matched values
 * `sum`: Returns the sum of all values in an array
 * `splice`: Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.
 * `reduceRight`: This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.
 * `reverse`: Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.
 * `find`: Return int position of value in array, case sensitive
 * `findNoCase`: Return int position of value in array, case sensitive
 * `contains`: Return int position of value in array, case sensitive
 * `containsNoCase`: Return int position of value in array, case sensitive
 * `push`: Adds an element or an object to the end of an array, then returns the size of the modified array.
 * `getMetadata`: Gets metadata for items of an array and indicates the array type.
 * `map`: Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned
 * `isEmpty`: Determine whether a given value is empty
 * `pop`: Remove last item in array and return it
 * `some`: Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true
 * `delete`: Delete first occurance of item in array case sensitive
 * `median`: Return the median value of an array.

Will only work on arrays that contain only numeric values.
 * `avg`: Return length of array
 * `toList`: Used to iterate over an array and run the function closure for each item in the array.
 * `join`: Used to iterate over an array and run the function closure for each item in the array.
 * `filter`: Used to filter an array to items for which the closure function returns true.
 * `deleteNoCase`: Delete first occurance of item in array case insensitive
 * `clear`: Clear all items from array
 * `swap`: Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements
 * `shift`: Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an
 exception will be thrown.
 * `toStruct`: Transform the array to a struct, the index of the array is the key of the struct
 * `unshift`: This function adds one or more elements to the beginning of the original array and returns the length of the modified array.
 * `slice`: Extracts a sub array from an existing array.
 * `mid`: Extracts a sub array from an existing array.
 * `insertAt`: Append a value to an array
 * `set`: In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.
 * `max`: Return length of array
 * `first`: Return first item in array
 * `deleteAt`: Delete item at specified index in array
 * `sort`: Sorts array elements.
 * `each`: Used to iterate over an array and run the function closure for each item in the array.
 * `append`: Append a value to an array
 * `every`: Returns true if every closure returns true, otherwise false
 * `last`: Return first item in array
 * `min`: Return length of array
 * `len`: Returns the absolute value of a number
 * `toJSON`: Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.




## Examples
