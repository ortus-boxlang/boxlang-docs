# Type: `string`



## string Methods

### string

#### Functions:

 * `hash`: Creates an algorithmic hash of an object
 * `Hmac`: Creates an algorithmic hash of an object
 * `InputBaseN`: Converts a string, using the base specified by radix, to an integer.
 * `ClassSymbol`: Return Yes/No based on whether the input is true/false
 * `listSome`: Tests whether any item in a list meets the specified callback
 * `reduceRight`: Run the provided udf over a reversed delimited list to reduce the values to a single output
 * `listPrepend`: Filters a delimted list and returns the values from the callback test
 * `listFirst`: Returns the first or last item in a delimited list, according to the specified function name
 * `listLast`: Returns the first or last item in a delimited list, according to the specified function name
 * `listIndexExists`: Checks if a list has a given index
 * `listInsertAt`: Filters a delimted list and returns the values from the callback test
 * `listChangeDelims`: Converts the delimiters of a list to the new delimiter.
 * `listFind`: Return int position of value in delimited list, case sensitive or case-insenstive variations
 * `listFindNoCase`: Return int position of value in delimited list, case sensitive or case-insenstive variations
 * `listContains`: Return int position of value in delimited list, case sensitive or case-insenstive variations
 * `listContainsNoCase`: Return int position of value in delimited list, case sensitive or case-insenstive variations
 * `ListCompact`: Compacts a list by removing empty items from the start and end of the list
 * `ListTrim`: Compacts a list by removing empty items from the start and end of the list
 * `listMap`: Used to iterate over a delimited list and run the function closure for each item in the list and create a new list from the returned values.
 * `listDeleteAt`: Describe what the invocation of your bif function does
 * `listRemoveDuplicates`: De-duplicates a delimited list - either case-sensitively or case-insenstively
 * `ListToArray`: Converts a delimited list to an array
 * `ListQualify`: Describe what the invocation of your bif function does
 * `listAppend`: Appends an element to a list
 * `ListValueCount`: returns a count of the number of occurrences of a value in a list
 * `ListValueCountNoCase`: returns a count of the number of occurrences of a value in a list
 * `ListAvg`: Gets the average of all values in a list
 * `listLen`: Calculates the length of a list separated by the specified delimiter
 * `ListRest`: Returns the remainder of a list after removing the first item
 * `listGetAt`: Retrieves an item from a delimited list at the specified position
 * `listEvery`: Tests whether all items in a list meet the specified callback
 * `listEach`: Used to iterate over a delimited list and run the function closure for each item in the list.
 * `listSort`: Sorts a delimited list and returns the result
 * `listSetAt`: Retrieves an item in to a delimited list at the specified position
 * `listFilter`: Filters a delimted list and returns the values from the callback test
 * `GetToken`: Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string.
 If index is greater than the number of tokens in the string, returns an empty string.
 * `listItemTrim`: Trims each item in the list.
 * `toJSON`: Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.
 * `listToJSON`: Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.
 * `SpanIncluding`: Gets characters from a string, from the beginning to a character that is NOT in a specified set of characters.

The search is case-sensitive.
 * `reFind`: Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.
 * `reFindNoCase`: Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.
 * `ascii`: Determine the ASCII value of a character
 * `Val`: Converts numeric characters and the first period found that occur at the beginning of a string to a number.

A period not accompianied by at least
 one numeric digit will be ignored. If no numeric digits are found at the start of the string, zero will be returned.
 * `compare`: Performs a case-sensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2
 * `ReReplace`: Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.
 * `ReReplaceNoCase`: Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.
 * `StripCR`: Deletes return characters from a string.
 * `Insert`: Inserts a substring into another string at a specified position.
 * `Right`: Extract the rightmost count characters from a string
 * `FindOneOf`: Finds the first occurrence of any character in a set of characters, from a specified start position.
 * `SpanExcluding`: Get characters from a string, from the beginning to a character that is in a specified set of characters.

The search is case-sensitive.
 * `compareNoCase`: Performs a case-insensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2
 * `StringReduceRight`: Run the provided udf over a reversed string to reduce the values to a single output
 * `Reverse`: Reverse the order of characters in a string
 * `Replace`: Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made
 * `ReplaceList`: Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.
 * `ReplaceListNoCase`: Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.
 * `Wrap`: null
 * `StringSort`: Sorts a string and returns the result
 * `Trim`: Trim whitespace from the beginning and end of a string
 * `LTrim`: Trim leading whitespace from a string
 * `UCFirst`: Transform the first letter of a string to uppercase or the first letter of each word, and optionally lowercase uppercase characters.
 * `Find`: Finds the first occurrence of a substring in a string, from a specified start position.
 * `FindNoCase`: Finds the first occurrence of a substring in a string, from a specified start position.
 * `reMatch`: Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.
 * `reMatchNoCase`: Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.
 * `LJustify`: Justifies characters in a string of a specified length, either left or right.
 * `RJustify`: Justifies characters in a string of a specified length, either left or right.
 * `Left`: Extract the leftmost count characters from a string
 * `UCase`: Uppercase a string
 * `listReduce`: Run the provided udf over a delimited list to reduce the values to a single output
 * `ReplaceNoCase`: Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made
 * `RemoveChars`: Describe what the invocation of your bif function does
 * `RTrim`: Trim trailing whitespace from a string
 * `CharsetDecode`: Encodes a string to a binary representation
 * `StringSome`: Tests whether any item in a string meets the specified callback
 * `toStruct`: Convert a query string to a struct.

Each key-value pair in the query string is separated by a delimiter.
 The default delimiter is ,{@code "&"},
 ,<p>,
 Example:

 ,<pre>,
 queryStringToStruct( "foo=bar,&amp;,baz=qux" );
 "foo=bar,&amp;,baz=qux".toStruct();
 ,</pre>
 * `Mid`: Extract a substring from a string
 * `LCase`: Uppercase a string
 * `ParagraphFormat`: Describe what the invocation of your bif function does




## Examples
