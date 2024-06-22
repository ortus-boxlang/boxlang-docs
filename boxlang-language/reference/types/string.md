[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `String`



## String Methods

<details>
<summary><code>lSParseDateTime(locale=[string], timezone=[string], format=[string])</code></summary>
<p>Parses a locale-specific datetime string or object

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
<td>`locale`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`timezone`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`format`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>parseDateTime(format=[string], timezone=[string])</code></summary>
<p>Parses a datetime string or object

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
<td>`format`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`timezone`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toDateTime(format=[string], timezone=[string])</code></summary>
<p>Parses a datetime string or object

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
<td>`format`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`timezone`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

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
<summary><code>hmac(key=[string], algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>
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
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`algorithm`</td>
<td>`string`</td>
<td>`false`</td>
<td>`HmacMD5`</td>
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
<summary><code>inputBaseN(radix=[numeric])</code></summary>
<p>Converts a string, using the base specified by radix, to an integer.

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
<td>`radix`</td>
<td>`numeric`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>xMLFormat(escapeChars=[boolean])</code></summary>
<p>Formats a string so that special XML characters can be used as text in XML

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
<td>`escapeChars`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>uRLEncodedFormat()</code></summary>
<p>Generates a URL-encoded string.

For example, it replaces spaces with %20, and non-alphanumeric characters with equivalent hexadecimal escape
 sequences. Passes arbitrary strings within a URL. *
</p></details>
<details>
<summary><code>len()</code></summary>
<p>Returns the absolute value of a number
</p></details>
<details>
<summary><code>listSome(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Tests whether any item in a list meets the specified callback

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reduceRight(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Run the provided udf over a reversed delimited list to reduce the values to a single output

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
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listPrepend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Filters a delimted list and returns the values from the callback test

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listFirst(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Returns the first or last item in a delimited list, according to the specified function name

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listLast(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Returns the first or last item in a delimited list, according to the specified function name

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listIndexExists(index=[numeric], delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>Checks if a list has a given index

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listInsertAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Filters a delimted list and returns the values from the callback test

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listChangeDelims(newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>Converts the delimiters of a list to the new delimiter.

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
<td>`newDelimiter`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listFind(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Return int position of value in delimited list, case sensitive or case-insenstive variations

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listFindNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Return int position of value in delimited list, case sensitive or case-insenstive variations

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listContains(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Return int position of value in delimited list, case sensitive or case-insenstive variations

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listContainsNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Return int position of value in delimited list, case sensitive or case-insenstive variations

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listCompact(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>
<p>Compacts a list by removing empty items from the start and end of the list

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listTrim(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>
<p>Compacts a list by removing empty items from the start and end of the list

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listMap(callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Used to iterate over a delimited list and run the function closure for each item in the list and create a new list from the returned values.

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listDeleteAt(position=[numeric], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Deletes an element from a list.

Returns a copy of the list, without the
 specified element.

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
<td>`numeric`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listRemoveDuplicates(delimiter=[string], ignoreCase=[boolean])</code></summary>
<p>De-duplicates a delimited list - either case-sensitively or case-insenstively

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`ignoreCase`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listToArray(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Converts a delimited list to an array

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listQualify(qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean])</code></summary>
<p>Inserts a string at the beginning and end of list elements.

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
<td>`qualifier`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`elements`</td>
<td>`string`</td>
<td>`false`</td>
<td>`all`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listAppend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Appends an element to a list

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listValueCount(value=[string], delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>returns a count of the number of occurrences of a value in a list

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listValueCountNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>returns a count of the number of occurrences of a value in a list

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listAvg(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>
<p>Gets the average of all values in a list

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listLen(delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>Calculates the length of a list separated by the specified delimiter

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listRest(delimiter=[string], includeEmptyFields=[boolean], offset=[integer])</code></summary>
<p>Returns the remainder of a list after removing the first item

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`offset`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`0`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listGetAt(position=[numeric], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Retrieves an item from a delimited list at the specified position

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
<td>`numeric`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listEvery(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Tests whether all items in a list meet the specified callback

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listEach(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], ordered=[boolean])</code></summary>
<p>Used to iterate over a delimited list and run the function closure for each item in the list.

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></summary>
<p>Sorts a delimited list and returns the result

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
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
<summary><code>listSetAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Retrieves an item in to a delimited list at the specified position

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
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listFilter(filter=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Filters a delimted list and returns the values from the callback test

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
<td>`filter`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>getToken(index=[integer], delimiter=[string])</code></summary>
<p>Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string.
 If index is greater than the number of tokens in the string, returns an empty string.

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
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>listItemTrim(delimiter=[string], includeEmptyFields=[boolean])</code></summary>
<p>Trims each item in the list.

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
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>prettifyJSON()</code></summary>
<p>Prettifies a JSON string.
</p></details>
<details>
<summary><code>jSONDeserialize(strictMapping=[boolean], useCustomSerializer=[string])</code></summary>
<p>Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

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
<td>`strictMapping`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr>

<tr>
<td>`useCustomSerializer`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toBase64(encoding=[string])</code></summary>
<p>Calculates the Base64 representation of a string or binary object.

The Base64 format uses printable characters, allowing binary data to be sent in
 forms and e-mail, and stored in a database or file.

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
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>`UTF-8`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toBinary()</code></summary>
<p>Calculates the binary representation of Base64-encoded data.
</p></details>
<details>
<summary><code>to(encoding=[string])</code></summary>
<p>Converts a value to a string.

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
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

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
<summary><code>listToJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>
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
<summary><code>booleanFormat()</code></summary>
<p>Returns the value formatted as a boolean string
</p></details>
<details>
<summary><code>isEmpty()</code></summary>
<p>Determine whether a given value is empty
</p></details>
<details>
<summary><code>spanIncluding(set=[string])</code></summary>
<p>Gets characters from a string, from the beginning to a character that is NOT in a specified set of characters.

The search is case-sensitive.

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
<td>`set`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reFind(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></summary>
<p>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

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
<td>`reg_expression`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr>

<tr>
<td>`returnSubExpressions`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
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
<summary><code>reFindNoCase(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></summary>
<p>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

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
<td>`reg_expression`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr>

<tr>
<td>`returnSubExpressions`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
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
<summary><code>kebabCase()</code></summary>
<p>Convert a string to kebab case
</p></details>
<details>
<summary><code>ascii()</code></summary>
<p>Determine the ASCII value of a character
</p></details>
<details>
<summary><code>val()</code></summary>
<p>Converts numeric characters and the first period found that occur at the beginning of a string to a number.

A period not accompianied by at least
 one numeric digit will be ignored. If no numeric digits are found at the start of the string, zero will be returned.
</p></details>
<details>
<summary><code>compare(string2=[any])</code></summary>
<p>Performs a case-sensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

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
<td>`string2`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>trueFalseFormat()</code></summary>
<p>Return Yes/No based on whether the input is true/false
</p></details>
<details>
<summary><code>reReplace(regex=[string], substring=[string], scope=[string])</code></summary>
<p>Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

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
<td>`regex`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substring`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`true`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reReplaceNoCase(regex=[string], substring=[string], scope=[string])</code></summary>
<p>Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

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
<td>`regex`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`substring`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`true`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>stripCR()</code></summary>
<p>Deletes return characters from a string.
</p></details>
<details>
<summary><code>insert(substring=[string], position=[integer])</code></summary>
<p>Inserts a substring into another string at a specified position.

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
<td>`substring`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`position`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>camelCase()</code></summary>
<p>Convert a string to camel case
</p></details>
<details>
<summary><code>snakeCase()</code></summary>
<p>Convert a string to snake case
</p></details>
<details>
<summary><code>right(count=[integer])</code></summary>
<p>Extract the rightmost count characters from a string

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
<td>`count`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findOneOf(set=[string], start=[integer])</code></summary>
<p>Finds the first occurrence of any character in a set of characters, from a specified start position.

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
<td>`set`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>spanExcluding(set=[string])</code></summary>
<p>Get characters from a string, from the beginning to a character that is in a specified set of characters.

The search is case-sensitive.

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
<td>`set`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>compareNoCase(string2=[string])</code></summary>
<p>Performs a case-insensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

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
<td>`string2`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>stringReduceRight(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Run the provided udf over a reversed string to reduce the values to a single output

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
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reverse()</code></summary>
<p>Reverse the order of characters in a string
</p></details>
<details>
<summary><code>replace(substring1=[string], obj=[string], scope=[string])</code></summary>
<p>Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

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
<td>`substring1`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`obj`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`true`</td>
<td>`once`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>replaceList(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></summary>
<p>Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

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
<td>`list1`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`list2`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter_list1`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`delimiter_list2`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>replaceListNoCase(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></summary>
<p>Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

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
<td>`list1`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`list2`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`delimiter_list1`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`delimiter_list2`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>slugify(maxLength=[numeric], allow=[string])</code></summary>
<p>Slugify a string for URL safety

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
<td>`maxLength`</td>
<td>`numeric`</td>
<td>`false`</td>
<td>`0`</td>
</tr>

<tr>
<td>`allow`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>wrap(limit=[integer], strip=[boolean])</code></summary>
<p>null

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
<td>`limit`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`strip`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>pascalCase()</code></summary>
<p>Convert a string to pascal case
</p></details>
<details>
<summary><code>stringSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></summary>
<p>Sorts a string and returns the result

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
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
<summary><code>trim()</code></summary>
<p>Trim whitespace from the beginning and end of a string
</p></details>
<details>
<summary><code>lTrim()</code></summary>
<p>Trim leading whitespace from a string
</p></details>
<details>
<summary><code>uCFirst(doAll=[boolean], doLowerIfAllUppercase=[boolean])</code></summary>
<p>Transform the first letter of a string to uppercase or the first letter of each word, and optionally lowercase uppercase characters.

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
<td>`doAll`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`doLowerIfAllUppercase`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>find(substring=[string], start=[integer])</code></summary>
<p>Finds the first occurrence of a substring in a string, from a specified start position.

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
<td>`substring`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findNoCase(substring=[string], start=[integer])</code></summary>
<p>Finds the first occurrence of a substring in a string, from a specified start position.

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
<td>`substring`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`start`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reMatch(reg_expression=[string])</code></summary>
<p>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

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
<td>`reg_expression`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reMatchNoCase(reg_expression=[string])</code></summary>
<p>Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

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
<td>`reg_expression`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>lJustify(length=[integer])</code></summary>
<p>Justifies characters in a string of a specified length, either left or right.

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
<td>`length`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>rJustify(length=[integer])</code></summary>
<p>Justifies characters in a string of a specified length, either left or right.

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
<td>`length`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>left(count=[integer])</code></summary>
<p>Extract the leftmost count characters from a string

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
<td>`count`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>uCase()</code></summary>
<p>Uppercase a string
</p></details>
<details>
<summary><code>listReduce(callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>
<p>Run the provided udf over a delimited list to reduce the values to a single output

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
</tr>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>yesNoFormat()</code></summary>
<p>Return Yes/No based on whether the input is true/false
</p></details>
<details>
<summary><code>replaceNoCase(substring1=[string], obj=[string], scope=[string])</code></summary>
<p>Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

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
<td>`substring1`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`obj`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`true`</td>
<td>`once`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>removeChars(start=[integer], count=[integer])</code></summary>
<p>Removes characters from a string.

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
<td>``</td>
</tr>

<tr>
<td>`count`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>rTrim()</code></summary>
<p>Trim trailing whitespace from a string
</p></details>
<details>
<summary><code>charsetDecode(encoding=[string])</code></summary>
<p>Encodes a string to a binary representation

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
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>`utf-8`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>stringSome(callback=[function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Tests whether any item in a string meets the specified callback

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
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr>

<tr>
<td>`includeEmptyFields`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`multiCharacterDelimiter`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
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
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>sQLPrettify()</code></summary>
<p>Prettify a SQL string
</p></details>
<details>
<summary><code>toStruct(delimiter=[string])</code></summary>
<p>Convert a query string to a struct.

Each key-value pair in the query string is separated by a delimiter.
 The default delimiter is ,{@code "&"},
 ,<p>,
 Example:

 ,<pre>,
 queryStringToStruct( "foo=bar,&amp;,baz=qux" );
 "foo=bar,&amp;,baz=qux".toStruct();
 ,</pre>

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
<td>`string`</td>
<td>`false`</td>
<td>`&`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>mid(start=[integer], count=[integer])</code></summary>
<p>Extract a substring from a string

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
<td>``</td>
</tr>

<tr>
<td>`count`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>lCase()</code></summary>
<p>Uppercase a string
</p></details>
<details>
<summary><code>paragraphFormat()</code></summary>
<p>Replaces characters in a string: Single newline characters (CR/LF sequences) with spaces and double newline characters with HTML paragraph tags
</p></details>


## Examples
