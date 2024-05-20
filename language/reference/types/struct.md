# Type: `struct`



## struct Methods

### struct

#### Functions:

 * `hash`: Creates an algorithmic hash of an object
 * `equals`: Tests equality between two structs
 * `reduce`: Run the provided udf against struct to reduce the values to a single output
 * `isCaseSensitive`: Returns whether the give struct is case sensitive
 * `getFromPath`: Retrieves the value from a struct using a path based expression
 * `delete`: Deletes a key from a struct
 * `filter`: Used to filter a struct and return a new struct containing the result
 * `isOrdered`: Tests whether a struct is ordered ( e.g.

linked )
 * `sort`: Sorts a struct according to the specified arguments and returns an array of struct keys
 * `each`: Used to iterate over a struct and run the function closure for each key/value pair.
 * `toQueryString`: Converts a struct to a query string using the specified delimiter.

<p>,
 The default delimiter is ,{@code "&"}
 * `update`: Updates or sets a key/value pair in to a struct
 * `clear`: Clear all items from struct
 * `getMetadata`: Gets Struct-specific metadata of the requested struct.
 * `keyArray`: Get keys of a struct as an array
 * `toSorted`: Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option
 * `copy`: Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.
 * `findKey`: Searches a struct for a given key and returns an array of values
 * `insert`: Inserts a key/value pair in to a struct - with an optional overwrite argument
 * `map`: Used to map a struct to a new struct of the same type containing the result
 * `findValue`: Searches a struct for a given value and returns an array of results
 * `valueArray`: Returns an array of all values of top level keys in a struct
 * `some`: Used to iterate over a struct and test whether any items meet the test callback.
 * `keyExists`: Tests whether a key exists in a struct and returns a boolean value
 * `translateKeys`: Converts a struct with dot-notated keys in to an unflattened version
 * `every`: Used to iterate over a struct and test whether every item in the struct meets the test.
 * `find`: Finds and retrieves a top-level key from a string in a struct
 * `keyList`: Get keys of a struct as a string list
 * `append`: Appends the contents of a second struct to the first struct either with or without overwrite
 * `count`: Returns the absolute value of a number
 * `len`: Returns the absolute value of a number
 * `toJSON`: Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.
 * `isEmpty`: Determine whether a given value is empty




## Examples
