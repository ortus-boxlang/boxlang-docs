[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `String`



## String Methods

<dl>
<dt><code>lSParseDateTime(locale=[string], timezone=[string], format=[string])</code></dt><dd>Parses a locale-specific datetime string or object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |
| `format` | `string` | `false` | `` |

</dd>
<dt><code>parseDateTime(format=[string], timezone=[string])</code></dt><dd>Parses a datetime string or object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `format` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>toDateTime(format=[string], timezone=[string])</code></dt><dd>Parses a datetime string or object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `format` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></dt><dd>Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</dd>
<dt><code>hmac(key=[string], algorithm=[string], encoding=[string], numIterations=[integer])</code></dt><dd>Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `algorithm` | `string` | `false` | `HmacMD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</dd>
<dt><code>inputBaseN(radix=[numeric])</code></dt><dd>Converts a string, using the base specified by radix, to an integer.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `radix` | `numeric` | `true` | `` |

</dd>
<dt><code>xMLFormat(escapeChars=[boolean])</code></dt><dd>Formats a string so that special XML characters can be used as text in XML

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `escapeChars` | `boolean` | `false` | `false` |

</dd>
<dt><code>uRLEncodedFormat()</code></dt><dd>Generates a URL-encoded string.

For example, it replaces spaces with %20, and non-alphanumeric characters with equivalent hexadecimal escape
 sequences. Passes arbitrary strings within a URL. *</dd>
<dt><code>len()</code></dt><dd>Returns the absolute value of a number</dd>
<dt><code>listSome(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Tests whether any item in a list meets the specified callback

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>reduceRight(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Run the provided udf over a reversed delimited list to reduce the values to a single output

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>listPrepend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Filters a delimted list and returns the values from the callback test

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>listFirst(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Returns the first or last item in a delimited list, according to the specified function name

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listLast(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Returns the first or last item in a delimited list, according to the specified function name

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listIndexExists(index=[numeric], delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>Checks if a list has a given index

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `numeric` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listInsertAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Filters a delimted list and returns the values from the callback test

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>listChangeDelims(newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>Converts the delimiters of a list to the new delimiter.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `newDelimiter` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listFind(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Return int position of value in delimited list, case sensitive or case-insenstive variations

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listFindNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Return int position of value in delimited list, case sensitive or case-insenstive variations

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listContains(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Return int position of value in delimited list, case sensitive or case-insenstive variations

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listContainsNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Return int position of value in delimited list, case sensitive or case-insenstive variations

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listCompact(delimiter=[string], multiCharacterDelimiter=[boolean])</code></dt><dd>Compacts a list by removing empty items from the start and end of the list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listTrim(delimiter=[string], multiCharacterDelimiter=[boolean])</code></dt><dd>Compacts a list by removing empty items from the start and end of the list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listMap(callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Used to iterate over a delimited list and run the function closure for each item in the list and create a new list from the returned values.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>listDeleteAt(position=[numeric], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Deletes an element from a list.

Returns a copy of the list, without the
 specified element.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `numeric` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listRemoveDuplicates(delimiter=[string], ignoreCase=[boolean])</code></dt><dd>De-duplicates a delimited list - either case-sensitively or case-insenstively

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `ignoreCase` | `boolean` | `false` | `false` |

</dd>
<dt><code>listToArray(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Converts a delimited list to an array

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listQualify(qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean])</code></dt><dd>Inserts a string at the beginning and end of list elements.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `qualifier` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `elements` | `string` | `false` | `all` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listAppend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Appends an element to a list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>listValueCount(value=[string], delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>returns a count of the number of occurrences of a value in a list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listValueCountNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>returns a count of the number of occurrences of a value in a list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listAvg(delimiter=[string], multiCharacterDelimiter=[boolean])</code></dt><dd>Gets the average of all values in a list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listLen(delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>Calculates the length of a list separated by the specified delimiter

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>listRest(delimiter=[string], includeEmptyFields=[boolean], offset=[integer])</code></dt><dd>Returns the remainder of a list after removing the first item

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `offset` | `integer` | `false` | `0` |

</dd>
<dt><code>listGetAt(position=[numeric], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Retrieves an item from a delimited list at the specified position

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `numeric` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |

</dd>
<dt><code>listEvery(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Tests whether all items in a list meet the specified callback

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>listEach(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], ordered=[boolean])</code></dt><dd>Used to iterate over a delimited list and run the function closure for each item in the list.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `ordered` | `boolean` | `false` | `false` |

</dd>
<dt><code>listSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></dt><dd>Sorts a delimited list and returns the result

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `` |
| `sortOrder` | `string` | `false` | `asc` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |
| `localeSensitive` | `boolean` | `false` | `` |
| `callback` | `any` | `false` | `` |

</dd>
<dt><code>listSetAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Retrieves an item in to a delimited list at the specified position

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |
| `value` | `string` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>listFilter(filter=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Filters a delimted list and returns the values from the callback test

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `filter` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>getToken(index=[integer], delimiter=[string])</code></dt><dd>Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string.
 If index is greater than the number of tokens in the string, returns an empty string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `index` | `integer` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |

</dd>
<dt><code>listItemTrim(delimiter=[string], includeEmptyFields=[boolean])</code></dt><dd>Trims each item in the list.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>prettifyJSON()</code></dt><dd>Prettifies a JSON string.</dd>
<dt><code>jSONDeserialize(strictMapping=[boolean], useCustomSerializer=[string])</code></dt><dd>Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `strictMapping` | `boolean` | `false` | `true` |
| `useCustomSerializer` | `string` | `false` | `` |

</dd>
<dt><code>toBase64(encoding=[string])</code></dt><dd>Calculates the Base64 representation of a string or binary object.

The Base64 format uses printable characters, allowing binary data to be sent in
 forms and e-mail, and stored in a database or file.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `encoding` | `string` | `false` | `UTF-8` |

</dd>
<dt><code>toBinary()</code></dt><dd>Calculates the binary representation of Base64-encoded data.</dd>
<dt><code>to(encoding=[string])</code></dt><dd>Converts a value to a string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `encoding` | `string` | `false` | `` |

</dd>
<dt><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></dt><dd>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `` |

</dd>
<dt><code>listToJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></dt><dd>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `` |

</dd>
<dt><code>booleanFormat()</code></dt><dd>Returns the value formatted as a boolean string</dd>
<dt><code>isEmpty()</code></dt><dd>Determine whether a given value is empty</dd>
<dt><code>spanIncluding(set=[string])</code></dt><dd>Gets characters from a string, from the beginning to a character that is NOT in a specified set of characters.

The search is case-sensitive.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `set` | `string` | `true` | `` |

</dd>
<dt><code>reFind(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></dt><dd>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `reg_expression` | `string` | `true` | `` |
| `start` | `integer` | `false` | `1` |
| `returnSubExpressions` | `boolean` | `false` | `false` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>reFindNoCase(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></dt><dd>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `reg_expression` | `string` | `true` | `` |
| `start` | `integer` | `false` | `1` |
| `returnSubExpressions` | `boolean` | `false` | `false` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>kebabCase()</code></dt><dd>Convert a string to kebab case</dd>
<dt><code>ascii()</code></dt><dd>Determine the ASCII value of a character</dd>
<dt><code>val()</code></dt><dd>Converts numeric characters and the first period found that occur at the beginning of a string to a number.

A period not accompianied by at least
 one numeric digit will be ignored. If no numeric digits are found at the start of the string, zero will be returned.</dd>
<dt><code>compare(string2=[any])</code></dt><dd>Performs a case-sensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `string2` | `any` | `true` | `` |

</dd>
<dt><code>trueFalseFormat()</code></dt><dd>Return Yes/No based on whether the input is true/false</dd>
<dt><code>reReplace(regex=[string], substring=[string], scope=[string])</code></dt><dd>Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `regex` | `string` | `true` | `` |
| `substring` | `string` | `true` | `` |
| `scope` | `string` | `true` | `one` |

</dd>
<dt><code>reReplaceNoCase(regex=[string], substring=[string], scope=[string])</code></dt><dd>Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `regex` | `string` | `true` | `` |
| `substring` | `string` | `true` | `` |
| `scope` | `string` | `true` | `one` |

</dd>
<dt><code>stripCR()</code></dt><dd>Deletes return characters from a string.</dd>
<dt><code>insert(substring=[string], position=[integer])</code></dt><dd>Inserts a substring into another string at a specified position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `substring` | `string` | `true` | `` |
| `position` | `integer` | `true` | `` |

</dd>
<dt><code>camelCase()</code></dt><dd>Convert a string to camel case</dd>
<dt><code>snakeCase()</code></dt><dd>Convert a string to snake case</dd>
<dt><code>right(count=[integer])</code></dt><dd>Extract the rightmost count characters from a string

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `count` | `integer` | `true` | `` |

</dd>
<dt><code>findOneOf(set=[string], start=[integer])</code></dt><dd>Finds the first occurrence of any character in a set of characters, from a specified start position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `set` | `string` | `true` | `` |
| `start` | `integer` | `false` | `1` |

</dd>
<dt><code>spanExcluding(set=[string])</code></dt><dd>Get characters from a string, from the beginning to a character that is in a specified set of characters.

The search is case-sensitive.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `set` | `string` | `true` | `` |

</dd>
<dt><code>compareNoCase(string2=[string])</code></dt><dd>Performs a case-insensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `string2` | `string` | `true` | `` |

</dd>
<dt><code>stringReduceRight(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Run the provided udf over a reversed string to reduce the values to a single output

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>reverse()</code></dt><dd>Reverse the order of characters in a string</dd>
<dt><code>replace(substring1=[string], obj=[string], scope=[string])</code></dt><dd>Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `substring1` | `string` | `true` | `` |
| `obj` | `string` | `true` | `` |
| `scope` | `string` | `true` | `once` |

</dd>
<dt><code>replaceList(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></dt><dd>Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `list1` | `string` | `true` | `` |
| `list2` | `string` | `true` | `` |
| `delimiter_list1` | `string` | `false` | `,` |
| `delimiter_list2` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>replaceListNoCase(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></dt><dd>Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `list1` | `string` | `true` | `` |
| `list2` | `string` | `true` | `` |
| `delimiter_list1` | `string` | `false` | `,` |
| `delimiter_list2` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |

</dd>
<dt><code>slugify(maxLength=[numeric], allow=[string])</code></dt><dd>Slugify a string for URL safety

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `maxLength` | `numeric` | `false` | `0` |
| `allow` | `string` | `false` | `` |

</dd>
<dt><code>wrap(limit=[integer], strip=[boolean])</code></dt><dd>null

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `limit` | `integer` | `true` | `` |
| `strip` | `boolean` | `false` | `false` |

</dd>
<dt><code>pascalCase()</code></dt><dd>Convert a string to pascal case</dd>
<dt><code>stringSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></dt><dd>Sorts a string and returns the result

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `` |
| `sortOrder` | `string` | `false` | `asc` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `false` |
| `localeSensitive` | `boolean` | `false` | `` |
| `callback` | `any` | `false` | `` |

</dd>
<dt><code>trim()</code></dt><dd>Trim whitespace from the beginning and end of a string</dd>
<dt><code>lTrim()</code></dt><dd>Trim leading whitespace from a string</dd>
<dt><code>uCFirst(doAll=[boolean], doLowerIfAllUppercase=[boolean])</code></dt><dd>Transform the first letter of a string to uppercase or the first letter of each word, and optionally lowercase uppercase characters.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `doAll` | `boolean` | `false` | `false` |
| `doLowerIfAllUppercase` | `boolean` | `false` | `false` |

</dd>
<dt><code>find(substring=[string], start=[integer])</code></dt><dd>Finds the first occurrence of a substring in a string, from a specified start position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `substring` | `string` | `true` | `` |
| `start` | `integer` | `false` | `1` |

</dd>
<dt><code>findNoCase(substring=[string], start=[integer])</code></dt><dd>Finds the first occurrence of a substring in a string, from a specified start position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `substring` | `string` | `true` | `` |
| `start` | `integer` | `false` | `1` |

</dd>
<dt><code>reMatch(reg_expression=[string])</code></dt><dd>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `reg_expression` | `string` | `true` | `` |

</dd>
<dt><code>reMatchNoCase(reg_expression=[string])</code></dt><dd>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `reg_expression` | `string` | `true` | `` |

</dd>
<dt><code>lJustify(length=[integer])</code></dt><dd>Justifies characters in a string of a specified length, either left or right.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `length` | `integer` | `true` | `` |

</dd>
<dt><code>rJustify(length=[integer])</code></dt><dd>Justifies characters in a string of a specified length, either left or right.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `length` | `integer` | `true` | `` |

</dd>
<dt><code>left(count=[integer])</code></dt><dd>Extract the leftmost count characters from a string

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `count` | `integer` | `true` | `` |

</dd>
<dt><code>uCase()</code></dt><dd>Uppercase a string</dd>
<dt><code>listReduce(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></dt><dd>Run the provided udf over a delimited list to reduce the values to a single output

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |

</dd>
<dt><code>yesNoFormat()</code></dt><dd>Return Yes/No based on whether the input is true/false</dd>
<dt><code>replaceNoCase(substring1=[string], obj=[string], scope=[string])</code></dt><dd>Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `substring1` | `string` | `true` | `` |
| `obj` | `string` | `true` | `` |
| `scope` | `string` | `true` | `once` |

</dd>
<dt><code>removeChars(start=[integer], count=[integer])</code></dt><dd>Removes characters from a string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `` |
| `count` | `integer` | `true` | `` |

</dd>
<dt><code>rTrim()</code></dt><dd>Trim trailing whitespace from a string</dd>
<dt><code>charsetDecode(encoding=[string])</code></dt><dd>Encodes a string to a binary representation

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `encoding` | `string` | `false` | `utf-8` |

</dd>
<dt><code>stringSome(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Tests whether any item in a string meets the specified callback

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `delimiter` | `string` | `false` | `,` |
| `includeEmptyFields` | `boolean` | `false` | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | `true` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>sQLPrettify()</code></dt><dd>Prettify a SQL string</dd>
<dt><code>toStruct(delimiter=[string])</code></dt><dd>Convert a query string to a struct.

Each key-value pair in the query string is separated by a delimiter.
 The default delimiter is ,{@code "&"},
 ,<p>,
 Example:

 ,<pre>,
 queryStringToStruct( "foo=bar,&amp;,baz=qux" );
 "foo=bar,&amp;,baz=qux".toStruct();
 ,</pre>

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `&` |

</dd>
<dt><code>mid(start=[integer], count=[integer])</code></dt><dd>Extract a substring from a string

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `start` | `integer` | `true` | `` |
| `count` | `integer` | `true` | `` |

</dd>
<dt><code>lCase()</code></dt><dd>Uppercase a string</dd>
<dt><code>paragraphFormat()</code></dt><dd>Replaces characters in a string: Single newline characters (CR/LF sequences) with spaces and double newline characters with HTML paragraph tags</dd>

</dl>

## Examples
