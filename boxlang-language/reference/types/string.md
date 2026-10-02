
# Type: `String`

In BoxLang, the `string` type is represented by the native Java class `java.lang.String`. The member functions below are provided by the BoxLang runtime and can be called directly on the value, in addition to the methods of the underlying Java class.

The <code>String</code> class represents character strings.

## String Methods

<details>
<summary><code>ascii()</code></summary>

Determine the ASCII value of a character

### Method Signature

```
ascii()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>bind(placeholders=[structloose])</code></summary>

This BIF allows you to bind a string with placeholders to a set of values.

Each placeholder is defined as <code>${placeholder-name</code>} and can be used anywhere
 and multiple times in the string.

### Method Signature

```
bind(placeholders=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `placeholders` | `struct` | `true` | A struct containing the placeholder values |  |
</details>
<details>
<summary><code>booleanFormat()</code></summary>

Returns the value formatted as a boolean string

### Method Signature

```
booleanFormat()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>
 The available <code>output</code> locations are:
 - <strong>buffer</strong>: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - <strong>console</strong>: The output is printed to the System console.
 - <strong>Absolute File Path</strong> The output is written to a file with the specified absolute file path.
 </p>
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

### Method Signature

```
bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `label` | `string` | `false` | A custom label to display above the dump (Only in HTML output) |  |
| `depth` | `numeric` | `false` | The recursion depth to display when dumping nested collections. 1-based: -1 (default) is unlimited, 0 shows nothing,<br>                 1 shows the top level with no recursion, 2 recurses once, etc. (Only in HTML output) |  |
| `maxRows` | `numeric` | `false` | The maximum number of keys/rows/items to display per level of a collection, array, or query. 1-based: -1 (default)<br>                   is unlimited, 0 shows nothing, 1 shows a single row, etc. (Only in HTML output) |  |
| `top` | `numeric` | `false` | Deprecated: use maxRows instead. When maxRows is not also passed, top's value is used as maxRows.<br>               Kept for backwards compatibility with existing BoxLang code. (Only in HTML output) |  |
| `expand` | `boolean` | `false` | Whether to expand the dump. Be default, we try to expand as much as possible. (Only in HTML output) | `true` |
| `abort` | `boolean` | `false` | Whether to do a hard abort the request after dumping. Default is false | `false` |
| `output` | `string` | `false` | The output format which can be "buffer", "console", or "{absolute file path}". The default is "buffer". |  |
| `format` | `string` | `false` | The format of the output to a <strong>filename</strong>. Can be "html" or "text". The default is according to the output location. |  |
| `showUDFs` | `boolean` | `false` | Show UDFs or not. Default is true. (Only in HTML output) | `true` |
</details>
<details>
<summary><code>camelCase()</code></summary>

Convert a string to camel case

### Method Signature

```
camelCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>charsetDecode(encoding=[string])</code></summary>

Encodes a string to a binary representation

### Method Signature

```
charsetDecode(encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `encoding` | `string` | `false` | The charset encoding to use (default: utf-8 ) | `utf-8` |
</details>
<details>
<summary><code>compare(string2=[any])</code></summary>

Performs a case-sensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

### Method Signature

```
compare(string2=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string2` | `any` | `true` | The second string to compare |  |
</details>
<details>
<summary><code>compareNoCase(string2=[string])</code></summary>

Performs a case-insensitive comparison of two strings.

-1, if string1 is less than string2
 0, if string1 is equal to string2
 1, if string1 is greater than string2

### Method Signature

```
compareNoCase(string2=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string2` | `string` | `true` | The second string to compare |  |
</details>
<details>
<summary><code>dateFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

### Method Signature

```
dateFormat(mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |
</details>
<details>
<summary><code>dateTimeFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

### Method Signature

```
dateTimeFormat(mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |
</details>
<details>
<summary><code>day(timezone=[string], locale=[string])</code></summary>

Returns the day of the month of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
day(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>dayOfWeek(timezone=[string], locale=[string])</code></summary>

Returns the numeric day of the week of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
dayOfWeek(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>dayOfWeekAsString(timezone=[string], locale=[string])</code></summary>

Returns the full day of the week name of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
dayOfWeekAsString(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>dayOfWeekShortAsString(timezone=[string], locale=[string])</code></summary>

Returns the short day of the week name of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
dayOfWeekShortAsString(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>dayOfYear(timezone=[string], locale=[string])</code></summary>

Returns the numeric day of the year of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
dayOfYear(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>daysInMonth(timezone=[string], locale=[string])</code></summary>

Returns the number of days in the month of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
daysInMonth(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>daysInYear(timezone=[string], locale=[string])</code></summary>

Return the number of days in the year of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
daysInYear(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>endsWith(substring=[string])</code></summary>

Determines whether a string ends with a specified suffix.

### Method Signature

```
endsWith(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The suffix to check for. |  |
</details>
<details>
<summary><code>endsWithNoCase(substring=[string])</code></summary>

Determines whether a string ends with a specified suffix, case-insensitive.

### Method Signature

```
endsWithNoCase(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The suffix to check for. |  |
</details>
<details>
<summary><code>find(substring=[string], start=[integer])</code></summary>

Finds the first occurrence of a substring in a string, from a specified start position.

### Method Signature

```
find(substring=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The string you are looking for. |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
</details>
<details>
<summary><code>findNoCase(substring=[string], start=[integer])</code></summary>

Finds the first occurrence of a substring in a string, from a specified start position.

### Method Signature

```
findNoCase(substring=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The string you are looking for. |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
</details>
<details>
<summary><code>findOneOf(set=[string], start=[integer])</code></summary>

Finds the first occurrence of any character in a set of characters, from a specified start position.

### Method Signature

```
findOneOf(set=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `string` | `true` | The set of characters to search for the first occurrence of. |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
</details>
<details>
<summary><code>firstDayOfMonth(timezone=[string], locale=[string])</code></summary>

Returns the first date of the month of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
firstDayOfMonth(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>fromJSON(strictMapping=[boolean], useCustomSerializer=[string])</code></summary>

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

JSON deserialization in BoxLang will always use ordered structs for objects which will preserve the key order of the original JSON string.
 This is handy when reading a JSON file, modifying it, and writing it back out.

### Method Signature

```
fromJSON(strictMapping=[boolean], useCustomSerializer=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `strictMapping` | `boolean` | `false` | A Boolean value that specifies whether to convert the JSON strictly. If true, everything becomes structures. | `true` |
| `useCustomSerializer` | `string` | `false` | A string that specifies the name of a custom serializer to use. (Not used) |  |
</details>
<details>
<summary><code>getnumericdate(timezone=[string], locale=[string])</code></summary>

Returns the numeric date in days from epoch of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
getnumericdate(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>getToken(index=[integer], delimiter=[string])</code></summary>

Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string.
 If index is greater than the number of tokens in the string, returns an empty string.

### Method Signature

```
getToken(index=[integer], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
</details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

### Method Signature

```
hash(algorithm=[string], encoding=[string], numIterations=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `algorithm` | `string` | `false` | The supported <code>java.security.MessageDigest</code> algorithm (case-insensitive) or "quick" for an insecure 64-bit hash | `MD5` |
| `encoding` | `string` | `false` | Applicable to strings ( default "utf-8" ) | `utf-8` |
| `numIterations` | `integer` | `false` | The number of iterations to re-digest the object ( default 1 ); | `1` |
</details>
<details>
<summary><code>hmac(key=[any], algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

### Method Signature

```
hmac(key=[any], algorithm=[string], encoding=[string], numIterations=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The secret key used to generate the HMAC. Can be a string or a binary value. |  |
| `algorithm` | `string` | `false` | The supported <code>java.security.MessageDigest</code> algorithm (case-insensitive) | `HmacMD5` |
| `encoding` | `string` | `false` | Applicable to strings ( default "utf-8" ) | `utf-8` |
| `numIterations` | `integer` | `false` | The number of iterations to re-digest the object ( default 1 ); | `1` |
</details>
<details>
<summary><code>hour(timezone=[string], locale=[string])</code></summary>

Returns the hour of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
hour(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>inputBaseN(radix=[integer])</code></summary>

Converts a string, using the base specified by radix, to an integer.

### Method Signature

```
inputBaseN(radix=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `radix` | `integer` | `true` | Base of the number represented by string, in the range 2-36. |  |
</details>
<details>
<summary><code>insert(substring=[string], position=[integer])</code></summary>

Inserts a substring into another string at a specified position.

### Method Signature

```
insert(substring=[string], position=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The string to insert. |  |
| `position` | `integer` | `true` | The position at which to insert the string. |  |
</details>
<details>
<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of
 anything that can be casted to: Array, Struct, Query, or String.

### Method Signature

```
isEmpty()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>jsFormat()</code></summary>

Escapes special JavaScript characters, such as single quotation mark, double quotation mark, and newline

### Method Signature

```
jsFormat()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>jSONDeserialize(strictMapping=[boolean], useCustomSerializer=[string])</code></summary>

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

JSON deserialization in BoxLang will always use ordered structs for objects which will preserve the key order of the original JSON string.
 This is handy when reading a JSON file, modifying it, and writing it back out.

### Method Signature

```
jSONDeserialize(strictMapping=[boolean], useCustomSerializer=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `strictMapping` | `boolean` | `false` | A Boolean value that specifies whether to convert the JSON strictly. If true, everything becomes structures. | `true` |
| `useCustomSerializer` | `string` | `false` | A string that specifies the name of a custom serializer to use. (Not used) |  |
</details>
<details>
<summary><code>jSONPrettify()</code></summary>

Prettifies a JSON string.

### Method Signature

```
jSONPrettify()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>kebabCase()</code></summary>

Convert a string to kebab case

### Method Signature

```
kebabCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>lCase()</code></summary>

Uppercase a string

### Method Signature

```
lCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>left(count=[integer])</code></summary>

Extract the leftmost count characters from a string

### Method Signature

```
left(count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `count` | `integer` | `true` | The number of characters to retrieve. |  |
</details>
<details>
<summary><code>len()</code></summary>

Returns the absolute value of a number

### Method Signature

```
len()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>listAppend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Appends an element to a list

### Method Signature

```
listAppend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to append |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listAvg(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>

Gets the average of all values in a list

### Method Signature

```
listAvg(delimiter=[string], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listChangeDelims(newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Converts the delimiters of a list to the new delimiter.

### Method Signature

```
listChangeDelims(newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `newDelimiter` | `string` | `true` | string the new list delimiter |  |
| `delimiter` | `string` | `false` | string the old list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listCompact(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>

Compacts a list by removing empty items from the start and end of the list

### Method Signature

```
listCompact(delimiter=[string], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listContains(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Return int position of value in delimited list, case sensitive or case-insenstive variations

### Method Signature

```
listContains(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locate in the list or a function to filter the list |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listContainsNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Return int position of value in delimited list, case sensitive or case-insenstive variations

### Method Signature

```
listContainsNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locate in the list or a function to filter the list |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listDeleteAt(position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Deletes an element from a list.

Returns a copy of the list, without the
 specified element.

### Method Signature

```
listDeleteAt(position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` | The one-based index position of the element to delete. |  |
| `delimiter` | `string` | `false` | The delimiter used in the list. | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the list. | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | Whether the delimiter is a multi-character<br>                                   delimiter. | `false` |
</details>
<details>
<summary><code>listEach(callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Used to iterate over a delimited list and run the function closure for each item in the list.

This BIF is similar to the ArrayEach BIF, but operates on a delimited list instead of an array.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
listEach(callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Consumer which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | Whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listEvery(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a delimited list and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the list.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large lists, especially when the test function is computationally expensive or the list is large.

### Method Signature

```
listEvery(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listFilter(filter=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters a delimted list and returns the values from the callback test
 This BIF will invoke the callback function for each entry in the list, passing the entry as a string.

<ul>
 <li>If the callback returns true, the entry will be included in the new list.</li>
 <li>If the callback returns false, the entry will be excluded from the new list.</li>
 <li>If the callback requires strict arguments, it will only receive the entry as a string.</li>
 <li>If the callback does not require strict arguments, it will receive the entry as a string, the index (0-based), and the original list as a string.</li>
 </ul>
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
listFilter(filter=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filter` | `function:Predicate` | `true` | function closure filter test. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listFind(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Return int position of value in delimited list, case sensitive or case-insenstive variations

### Method Signature

```
listFind(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locate in the list or a function to filter the list |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listFindNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Return int position of value in delimited list, case sensitive or case-insenstive variations

### Method Signature

```
listFindNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locate in the list or a function to filter the list |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listFirst(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Returns the first or last item in a delimited list, according to the specified function name

### Method Signature

```
listFirst(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listGetAt(position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Retrieves an item from a delimited list at the specified position

### Method Signature

```
listGetAt(position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listIndexExists(index=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Checks if a list has a given index

### Method Signature

```
listIndexExists(index=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `integer` | `true` | numeric The index to check for |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listInsertAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Filters a delimted list and returns the values from the callback test

### Method Signature

```
listInsertAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` |  |  |
| `value` | `string` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listItemTrim(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Trims each item in the list.

### Method Signature

```
listItemTrim(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listLast(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Returns the first or last item in a delimited list, according to the specified function name

### Method Signature

```
listLast(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listLen(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Calculates the length of a list separated by the specified delimiter

### Method Signature

```
listLen(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listMap(callback=[function:Function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

This BIF will iterate over each item in the delimited list and invoke the callback function for each item so
 you can do any operation on the item and return a new value that will be set at the same index in a new list.

The callback function will be passed the item as a string, the current index (0-based), and the original list.
 <ul>
 <li>If the callback requires strict arguments, it will only receive the item as a string.</li>
 <li>If the callback does not require strict arguments, it will receive the item as a string, the index (0-based), and the original list.</li>
 </ul>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
listMap(callback=[function:Function], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Function which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listNone(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a delimited list and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of <code>ListSome</code>.
 <p>
 The function will be passed 3 arguments: the value, the index, and the list.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large lists, especially when the test function is computationally expensive or the list is large.

### Method Signature

```
listNone(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listPrepend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Filters a delimted list and returns the values from the callback test

### Method Signature

```
listPrepend(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listQualify(qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Inserts a string at the beginning and end of list elements.

If this BIF is being called from inside of a query component,
 and the qualifier is a single quote, any single quotes in the values will be escaped by doubling them up.
 This protects against SQL Injection attacks.

### Method Signature

```
listQualify(qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `qualifier` | `string` | `true` | The string to insert at the beginning and end of each element. |  |
| `delimiter` | `string` | `false` | The delimiter used in the list. | `,` |
| `elements` | `string` | `false` | The elements to qualify. If set to "char", only elements that are all alphabetic characters will be qualified. | `all` |
| `includeEmptyFields` | `boolean` | `false` | If true, empty fields will be qualified. | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listReduce(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Run the provided udf over a delimited list to reduce the values to a single output

### Method Signature

```
listReduce(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java BiFunction which will only receive the ffirst 2 args. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |
</details>
<details>
<summary><code>listReduceRight(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Run the provided udf over a reversed delimited list to reduce the values to a single output

### Method Signature

```
listReduceRight(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java BiFunction which will only receive the first 2 args. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listRemoveDuplicates(delimiter=[string], ignoreCase=[boolean], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

De-duplicates a delimited list - either case-sensitively or case-insenstively

### Method Signature

```
listRemoveDuplicates(delimiter=[string], ignoreCase=[boolean], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | The delimiter of the list | `,` |
| `ignoreCase` | `boolean` | `false` | Whether case should be ignored or not during deduplication - defaults to false | `false` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listRest(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], offset=[integer])</code></summary>

Returns the remainder of a list after removing the first item

### Method Signature

```
listRest(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], offset=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `offset` | `integer` | `false` |  | `1` |
</details>
<details>
<summary><code>listSetAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Retrieves an item in to a delimited list at the specified position

### Method Signature

```
listSetAt(position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `value` | `string` | `true` | string the value to set at the specified position |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listSome(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], virtual=[boolean])</code></summary>

Used to iterate over a delimited list and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the value, the index, and the list.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
listSome(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>listSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></summary>

Sorts a delimited list and returns the result

### Method Signature

```
listSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortType` | `any` | `false` | Options are text, numeric, or textnocase |  |
| `sortOrder` | `string` | `false` | Options are asc or desc | `asc` |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `localeSensitive` | `boolean` | `false` | Sort based on local rules | `false` |
| `callback` | `any` | `false` | Optional function to use for sorting - if the sort type is a closure, it will be recognized as a callback |  |
</details>
<details>
<summary><code>listToArray(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Converts a delimited list to an array

### Method Signature

```
listToArray(delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listToJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>Query Format Options</h2>
 The <code>queryFormat</code> argument determines how queries are serialized:
 <ul>
 <li><code>row</code> or <code>false</code>: Serializes the query as a top-level struct with two keys:
 <code>columns</code> (an array of column names) and <code>data</code> (an array of arrays representing
 each row's data).</li>
 <li><code>column</code> or <code>true</code>: Serializes the query as a top-level struct with three keys:
 <code>rowCount</code> (the number of rows), <code>columns</code> (an array of column names), and
 <code>data</code> (a struct where each key is a column name and the value is an array of values for that column).</li>
 <li><code>struct</code>: Serializes the query as an array of structs, where each struct represents a row of data.</li>
 </ul>

 <h2>Usage</h2>

 <pre>
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 </pre>

### Method Signature

```
listToJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. Valid values are:<br>                       <code>row</code> same as <code>false</code>, <code>column</code> same as <code>true</code>, or <code>struct</code>. Defaults to <code>row</code>. |  |
| `useSecureJSONPrefix` | `string` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. (Not implemented yet) | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not implemented yet) |  |
| `pretty` | `boolean` | `false` | If true, the JSON string is formatted with indentation and line breaks for readability. Defaults to false. | `false` |
</details>
<details>
<summary><code>listToSet(type=[string], delimiter=[string])</code></summary>

Convert a collection into a Set, deduplicating automatically.

Accepts an Array, a list-delimited String,
 an existing Set, a QueryColumn, an XML node, a bounded Range, or any value castable to a Set. When the
 value is already of the requested variant it is returned as-is; otherwise a new Set of the specified
 variant is created and populated.

### Method Signature

```
listToSet(type=[string], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet),<br>                or "sorted" / "tree" (TreeSet). When omitted, the caster defaults to LINKED for ordered<br>                collections like Arrays. |  |
| `delimiter` | `string` | `false` | When <code>value</code> is a String, the list delimiter to split on. Defaults to <code>","</code>. | `,` |
</details>
<details>
<summary><code>listTrim(delimiter=[string], multiCharacterDelimiter=[boolean])</code></summary>

Compacts a list by removing empty items from the start and end of the list

### Method Signature

```
listTrim(delimiter=[string], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listValueCount(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

returns a count of the number of occurrences of a value in a list

### Method Signature

```
listValueCount(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locale |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>listValueCountNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

returns a count of the number of occurrences of a value in a list

### Method Signature

```
listValueCountNoCase(value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to locale |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
</details>
<details>
<summary><code>lJustify(length=[integer])</code></summary>

Justifies characters in a string of a specified length, either left or right.

### Method Signature

```
lJustify(length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `length` | `integer` | `true` | The specified length of the resulting string. |  |
</details>
<details>
<summary><code>lTrim(chars=[string])</code></summary>

Trim leading whitespace from a string.

If chars is provided, each character in the string is treated as a character to trim instead of whitespace.

### Method Signature

```
lTrim(chars=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `chars` | `string` | `false` | An optional string of characters to trim. Each character is treated individually. |  |
</details>
<details>
<summary><code>mid(start=[integer], count=[integer])</code></summary>

Extract a substring from a string

### Method Signature

```
mid(start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The position of the first character to retrieve. |  |
| `count` | `integer` | `false` | The number of characters to retrieve. |  |
</details>
<details>
<summary><code>millisecond(timezone=[string], locale=[string])</code></summary>

Returns the millisecond of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
millisecond(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>minute(timezone=[string], locale=[string])</code></summary>

Returns the minute of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
minute(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>month(timezone=[string], locale=[string])</code></summary>

Returns the numeric month of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
month(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>monthAsString(timezone=[string], locale=[string])</code></summary>

Returns the full month name of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
monthAsString(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>monthShortAsString(timezone=[string], locale=[string])</code></summary>

Returns the short month name of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
monthShortAsString(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>nanosecond(timezone=[string], locale=[string])</code></summary>

Returns the nanosecond of adate object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
nanosecond(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>offset(timezone=[string], locale=[string])</code></summary>

Returns the timezone offset of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
offset(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>paragraphFormat()</code></summary>

Replaces characters in a string: Single newline characters (CR/LF sequences) with spaces and double newline characters with HTML paragraph tags

### Method Signature

```
paragraphFormat()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>parseDateTime(format=[string], timezone=[string], locale=[string])</code></summary>

Parses a datetime string or object

### Method Signature

```
parseDateTime(format=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `false` | the format mask to use in parsing |  |
| `timezone` | `string` | `false` | the timezone to apply to the parsed datetime |  |
| `locale` | `string` | `false` | optional ISO locale string ( e.g. en-US, en_US, es-SA, es_ES, ru-RU, etc ) used to parse localized formats |  |
</details>
<details>
<summary><code>pascalCase()</code></summary>

Convert a string to pascal case

### Method Signature

```
pascalCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>quarter(timezone=[string], locale=[string])</code></summary>

Returns the quarter of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
quarter(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>reFind(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></summary>

Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

### Method Signature

```
reFind(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `reg_expression` | `string` | `true` | The regular expression to search for |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
| `returnSubExpressions` | `boolean` | `false` | True: if the regular expression is found, the first array element contains the length and position, respectively, of<br>                                the first match. If the regular expression contains parentheses that group subexpressions, each subsequent array<br>                                element contains the length and position, respectively, of the first occurrence of each group. If the regular<br>                                expression is not found, the arrays each contain one element with the value 0. False: the function returns the<br>                                position in the string where the match begins. Default. | `false` |
| `scope` | `string` | `false` | "one": returns the first value that matches the regex. "all": returns all values that match the regex. | `one` |
</details>
<details>
<summary><code>reFindNoCase(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])</code></summary>

Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

### Method Signature

```
reFindNoCase(reg_expression=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `reg_expression` | `string` | `true` | The regular expression to search for |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
| `returnSubExpressions` | `boolean` | `false` | True: if the regular expression is found, the first array element contains the length and position, respectively, of<br>                                the first match. If the regular expression contains parentheses that group subexpressions, each subsequent array<br>                                element contains the length and position, respectively, of the first occurrence of each group. If the regular<br>                                expression is not found, the arrays each contain one element with the value 0. False: the function returns the<br>                                position in the string where the match begins. Default. | `false` |
| `scope` | `string` | `false` | "one": returns the first value that matches the regex. "all": returns all values that match the regex. | `one` |
</details>
<details>
<summary><code>reMatch(reg_expression=[string])</code></summary>

Uses a regular expression (RE) to search a string for a pattern.

### Method Signature

```
reMatch(reg_expression=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `reg_expression` | `string` | `true` | The regular expression to search for |  |
</details>
<details>
<summary><code>reMatchNoCase(reg_expression=[string])</code></summary>

Uses a regular expression (RE) to search a string for a pattern.

### Method Signature

```
reMatchNoCase(reg_expression=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `reg_expression` | `string` | `true` | The regular expression to search for |  |
</details>
<details>
<summary><code>removeChars(start=[integer], count=[integer])</code></summary>

Removes characters from a string.

### Method Signature

```
removeChars(start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The one-based index position of the first character to remove. |  |
| `count` | `integer` | `true` | The number of characters to remove. |  |
</details>
<details>
<summary><code>replace(substring1=[string], obj=[any], scope=[string])</code></summary>

Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

### Method Signature

```
replace(substring1=[string], obj=[any], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring1` | `string` | `true` | The substring to search for |  |
| `obj` | `any` | `true` | The string to replace substring1 with |  |
| `scope` | `string` | `true` | The scope to search in. Valid values are "one" or "all" | `one` |
</details>
<details>
<summary><code>replaceList(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></summary>

Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

### Method Signature

```
replaceList(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list1` | `string` | `true` | The first delimited list of search values |  |
| `list2` | `string` | `true` | The second delimited list of replacement values |  |
| `delimiter_list1` | `string` | `false` | The delimiters for list 1 | `,` |
| `delimiter_list2` | `string` | `false` | The delimiters for list 2 | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the final result | `false` |
</details>
<details>
<summary><code>replaceListNoCase(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])</code></summary>

Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

### Method Signature

```
replaceListNoCase(list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list1` | `string` | `true` | The first delimited list of search values |  |
| `list2` | `string` | `true` | The second delimited list of replacement values |  |
| `delimiter_list1` | `string` | `false` | The delimiters for list 1 | `,` |
| `delimiter_list2` | `string` | `false` | The delimiters for list 2 | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the final result | `false` |
</details>
<details>
<summary><code>replaceNoCase(substring1=[string], obj=[any], scope=[string], start=[string])</code></summary>

Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

### Method Signature

```
replaceNoCase(substring1=[string], obj=[any], scope=[string], start=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring1` | `string` | `true` | The substring to search for |  |
| `obj` | `any` | `true` | The string to replace substring1 with |  |
| `scope` | `string` | `true` | The scope to search in | `one` |
| `start` | `string` | `false` |  | `1` |
</details>
<details>
<summary><code>reReplace(regex=[string], substring=[string], scope=[string])</code></summary>

Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

### Method Signature

```
reReplace(regex=[string], substring=[string], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `regex` | `string` | `true` | The regular expression to search for |  |
| `substring` | `string` | `true` | The string to replace regex with |  |
| `scope` | `string` | `true` | The scope to search in (one, all) | `one` |
</details>
<details>
<summary><code>reReplaceNoCase(regex=[string], substring=[string], scope=[string])</code></summary>

Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

### Method Signature

```
reReplaceNoCase(regex=[string], substring=[string], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `regex` | `string` | `true` | The regular expression to search for |  |
| `substring` | `string` | `true` | The string to replace regex with |  |
| `scope` | `string` | `true` | The scope to search in (one, all) | `one` |
</details>
<details>
<summary><code>reverse()</code></summary>

Reverse the order of characters in a string

### Method Signature

```
reverse()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>right(count=[integer])</code></summary>

Extract the rightmost count characters from a string

### Method Signature

```
right(count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `count` | `integer` | `true` | The number of characters to retrieve. |  |
</details>
<details>
<summary><code>rJustify(length=[integer])</code></summary>

Justifies characters in a string of a specified length, either left or right.

### Method Signature

```
rJustify(length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `length` | `integer` | `true` | The specified length of the resulting string. |  |
</details>
<details>
<summary><code>rTrim(chars=[string])</code></summary>

Trim trailing whitespace from a string.

If chars is provided, each character in the string is treated as a character to trim instead of whitespace.

### Method Signature

```
rTrim(chars=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `chars` | `string` | `false` | An optional string of characters to trim. Each character is treated individually. |  |
</details>
<details>
<summary><code>second(timezone=[string], locale=[string])</code></summary>

Returns the second of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
second(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>slugify(maxLength=[integer], allow=[string])</code></summary>

Slugify a string for URL safety

### Method Signature

```
slugify(maxLength=[integer], allow=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `maxLength` | `integer` | `false` | The maximum number of chracters to allow, 0 is all | `0` |
| `allow` | `string` | `false` | A regex safe list of additional characters to allow. The default is <code>[^a-z0-9]</code> |  |
</details>
<details>
<summary><code>snakeCase()</code></summary>

Convert a string to snake case

### Method Signature

```
snakeCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>spanExcluding(set=[string])</code></summary>

Get characters from a string, from the beginning to a character that is in a specified set of characters.

The search is case-sensitive.

### Method Signature

```
spanExcluding(set=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `string` | `true` | The set of chracters to exclude from the span. |  |
</details>
<details>
<summary><code>spanIncluding(set=[string])</code></summary>

Gets characters from a string, from the beginning to a character that is NOT in a specified set of characters.

The search is case-sensitive.

### Method Signature

```
spanIncluding(set=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `string` | `true` | The set of chracters to exclude from the span. |  |
</details>
<details>
<summary><code>sQLPrettify()</code></summary>

Prettify a SQL string

### Method Signature

```
sQLPrettify()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>startsWith(substring=[string])</code></summary>

Determines whether a string starts with a specified prefix.

### Method Signature

```
startsWith(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The prefix to check for. |  |
</details>
<details>
<summary><code>startsWithNoCase(substring=[string])</code></summary>

Determines whether a string starts with a specified prefix, case-insensitive.

### Method Signature

```
startsWithNoCase(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The prefix to check for. |  |
</details>
<details>
<summary><code>stringReduceRight(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])</code></summary>

Run the provided udf over a reversed string to reduce the values to a single output

### Method Signature

```
stringReduceRight(callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
</details>
<details>
<summary><code>stringSome(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], virtual=[boolean])</code></summary>

Tests whether any item in a string meets the specified callback

### Method Signature

```
stringSome(callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |
| `virtual` | `boolean` | `false` |  | `false` |
</details>
<details>
<summary><code>stringSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])</code></summary>

Sorts a string and returns the result

### Method Signature

```
stringSort(sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortType` | `any` | `false` |  |  |
| `sortOrder` | `string` | `false` |  | `asc` |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
| `localeSensitive` | `boolean` | `false` |  | `false` |
| `callback` | `any` | `false` |  |  |
</details>
<details>
<summary><code>stripCR()</code></summary>

Deletes return characters from a string.

### Method Signature

```
stripCR()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>timeFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

### Method Signature

```
timeFormat(mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |
</details>
<details>
<summary><code>timezone(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

### Method Signature

```
timezone(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>to(encoding=[string])</code></summary>

Converts a value to a string.

### Method Signature

```
to(encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `encoding` | `string` | `false` | The character encoding (character set) of the string, used with binary data. |  |
</details>
<details>
<summary><code>toAST(filepath=[string], returnType=[string], sourceType=[string])</code></summary>

Generates the Abstract Syntax Tree (AST) for BoxLang source code or a file.

The AST represents the syntactic structure of the code and can be used for
 code analysis, transformation, or generation.

 <p>
 <strong>Usage Examples:</strong>
 </p>

 <pre>
 // Parse source code and return as struct (default)
 ast = boxAST( source = "x = 1 + 2" );
 println( ast.ASTType ); // Outputs: BoxAssignment

 // Parse source code and return as JSON
 json = boxAST( source = "function add(a, b) { return a + b; }", returnType = "json" );
 println( json ); // Outputs: JSON representation of the AST

 // Parse source code and return as text
 text = boxAST( source = "if (x > 5) { println('yes'); }", returnType = "text" );
 println( text ); // Outputs: Human-readable text representation

 // Parse a file
 ast = boxAST( filepath = "src/MyClass.bx" );

 // Use as a member function on a string
 source = "a = [1, 2, 3]";
 ast = source.toAST(); // Returns AST as struct
 ast = source.toAST( returnType = "json" ); // Returns AST as JSON string

 // Parse CFML/ColdFusion syntax
 ast = boxAST( source = "cfset x = 1", sourceType = "cfscript" );

 // Parse template syntax
 ast = boxAST( source = "<bx:output>#now()#</bx:output>", sourceType = "template" );
 </pre>

 <p>
 The returned AST structure contains nodes with the following key properties:
 </p>
 <ul>
 <li><strong>ASTType</strong> - The type of AST node (e.g., BoxAssignment, BoxFunctionDeclaration, BoxClass)</li>
 <li><strong>ASTPackage</strong> - The package name of the AST node class</li>
 <li>Additional properties specific to each node type (e.g., name, value, children, etc.)</li>
 </ul>

### Method Signature

```
toAST(filepath=[string], returnType=[string], sourceType=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filepath` | `string` | `false` | The path to a BoxLang file to parse. Either source or filepath must be provided.<br>                    Can be relative (to the current working directory) or absolute. |  |
| `returnType` | `string` | `false` | The format of the returned AST. Valid values are "struct" (default), "json", or "text".<br>                      <ul><br>                      <li><strong>struct</strong> - Returns a nested structure (Map) representing the AST hierarchy</li><br>                      <li><strong>json</strong> - Returns a JSON string representation of the AST</li><br>                      <li><strong>text</strong> - Returns a human-readable text representation of the AST</li><br>                      </ul> | `struct` |
| `sourceType` | `string` | `false` | The type of source code being parsed. Valid values are "script" (default), "template", "cfscript", or "cftemplate".<br>                      <ul><br>                      <li><strong>script</strong> - BoxLang script syntax (BOXSCRIPT)</li><br>                      <li><strong>template</strong> - BoxLang template syntax (BOXTEMPLATE)</li><br>                      <li><strong>cfscript</strong> - ColdFusion script syntax (CFSCRIPT)</li><br>                      <li><strong>cftemplate</strong> - ColdFusion template syntax (CFTEMPLATE)</li><br>                      </ul> | `script` |
</details>
<details>
<summary><code>toBase64(encoding=[string])</code></summary>

Calculates the Base64 representation of a string or binary object.

The Base64 format uses printable characters, allowing binary data to be sent in
 forms and e-mail, and stored in a database or file.

### Method Signature

```
toBase64(encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `encoding` | `string` | `false` | The character encoding (character set) of the string, used with binary data. | `UTF-8` |
</details>
<details>
<summary><code>toBinary()</code></summary>

Calculates the binary representation of Base64-encoded data.

### Method Signature

```
toBinary()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toDateTime(format=[string], timezone=[string], locale=[string])</code></summary>

Parses a datetime string or object

### Method Signature

```
toDateTime(format=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `false` | the format mask to use in parsing |  |
| `timezone` | `string` | `false` | the timezone to apply to the parsed datetime |  |
| `locale` | `string` | `false` | optional ISO locale string ( e.g. en-US, en_US, es-SA, es_ES, ru-RU, etc ) used to parse localized formats |  |
</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>Query Format Options</h2>
 The <code>queryFormat</code> argument determines how queries are serialized:
 <ul>
 <li><code>row</code> or <code>false</code>: Serializes the query as a top-level struct with two keys:
 <code>columns</code> (an array of column names) and <code>data</code> (an array of arrays representing
 each row's data).</li>
 <li><code>column</code> or <code>true</code>: Serializes the query as a top-level struct with three keys:
 <code>rowCount</code> (the number of rows), <code>columns</code> (an array of column names), and
 <code>data</code> (a struct where each key is a column name and the value is an array of values for that column).</li>
 <li><code>struct</code>: Serializes the query as an array of structs, where each struct represents a row of data.</li>
 </ul>

 <h2>Usage</h2>

 <pre>
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 </pre>

### Method Signature

```
toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. Valid values are:<br>                       <code>row</code> same as <code>false</code>, <code>column</code> same as <code>true</code>, or <code>struct</code>. Defaults to <code>row</code>. |  |
| `useSecureJSONPrefix` | `string` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. (Not implemented yet) | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not implemented yet) |  |
| `pretty` | `boolean` | `false` | If true, the JSON string is formatted with indentation and line breaks for readability. Defaults to false. | `false` |
</details>
<details>
<summary><code>trim(chars=[string])</code></summary>

Trim whitespace from the beginning and end of a string.

If chars is provided, each character in the string is treated as a character to trim instead of whitespace.

### Method Signature

```
trim(chars=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `chars` | `string` | `false` | An optional string of characters to trim. Each character is treated individually. |  |
</details>
<details>
<summary><code>trueFalseFormat()</code></summary>

Returns the value formatted as a boolean string

### Method Signature

```
trueFalseFormat()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>uCase()</code></summary>

Uppercase a string

### Method Signature

```
uCase()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>uCFirst(doAll=[boolean], doLowerIfAllUppercase=[boolean])</code></summary>

Transform the first letter of a string to uppercase or the first letter of each word, and optionally lowercase uppercase characters.

### Method Signature

```
uCFirst(doAll=[boolean], doLowerIfAllUppercase=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `doAll` | `boolean` | `false` | Boolean flag indicating whether to transform the first letter of each word. | `false` |
| `doLowerIfAllUppercase` | `boolean` | `false` | Boolean flag indicating whether to lowercase uppercase characters. | `false` |
</details>
<details>
<summary><code>uRLEncodedFormat()</code></summary>

Generates a URL-encoded string.

For example, it replaces spaces with `%20`, and non-alphanumeric characters with equivalent hexadecimal escape
 sequences. Passes arbitrary strings within a URL.

### Method Signature

```
uRLEncodedFormat()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>val()</code></summary>

Converts numeric characters and the first period found that occur at the beginning of a string to a number.

A period not accompianied by at least
 one numeric digit will be ignored. If no numeric digits are found at the start of the string, zero will be returned.

### Method Signature

```
val()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>week(timezone=[string], locale=[string])</code></summary>

Returns the numeric week within a year of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
week(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>wrap(limit=[integer], strip=[boolean])</code></summary>

Wraps a string at the specified limit, breaking at the last space within the limit.

### Method Signature

```
wrap(limit=[integer], strip=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `limit` | `integer` | `true` | The character limit at which to wrap the string. |  |
| `strip` | `boolean` | `false` | If true, replaces all line endings with spaces before wrapping. Default is false. | `false` |
</details>
<details>
<summary><code>xMLFormat(escapeChars=[boolean])</code></summary>

Formats a string so that special XML characters can be used as text in XML

### Method Signature

```
xMLFormat(escapeChars=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `escapeChars` | `boolean` | `false` | whether to escape additional characters restricted as per XML standards. For details, see<br>                       http://www.w3.org/TR/2006/REC-xml11-20060816/#NT-RestrictedChar. | `false` |
</details>
<details>
<summary><code>year(timezone=[string], locale=[string])</code></summary>

Returns the year of a date object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

### Method Signature

```
year(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |
</details>
<details>
<summary><code>yesNoFormat()</code></summary>

Return Yes/No based on whether the input is true/false

### Method Signature

```
yesNoFormat()
```

### Arguments

This function does not accept any arguments
</details>


## Java Methods

> **Use at your own risk:** These are the public methods of the native Java class `java.lang.String`, documented from the JDK 21 javadocs. They are not part of the BoxLang API, are not tested or supported by BoxLang, and may change between Java versions. Java methods with the same name as one of the BoxLang member functions above are not listed, as the BoxLang member function is called instead.

<details>
<summary><code>char charAt(int index)</code></summary>

Returns the <code>char</code> value at the
 specified index. An index ranges from <code>0</code> to
 <code>length() - 1</code>. The first <code>char</code> value of the sequence
 is at index <code>0</code>, the next at index <code>1</code>,
 and so on, as for array indexing.

 <p>If the <code>char</code> value specified by the index is a
 surrogate, the surrogate
 value is returned.

**Parameters:**

* `index` - the index of the <code>char</code> value.

**Returns:** the <code>char</code> value at the specified index of this string.
             The first <code>char</code> value is at index <code>0</code>.

</details>
<details>
<summary><code>IntStream chars()</code></summary>

Returns a stream of <code>int</code> zero-extending the <code>char</code> values
 from this sequence.  Any char which maps to a <code>surrogate code point</code> is passed through
 uninterpreted.

**Returns:** an IntStream of char values from this sequence

</details>
<details>
<summary><code>int codePointAt(int index)</code></summary>

Returns the character (Unicode code point) at the specified
 index. The index refers to <code>char</code> values
 (Unicode code units) and ranges from <code>0</code> to
 <code>#length()</code><code>- 1</code>.

 <p> If the <code>char</code> value specified at the given index
 is in the high-surrogate range, the following index is less
 than the length of this <code>String</code>, and the
 <code>char</code> value at the following index is in the
 low-surrogate range, then the supplementary code point
 corresponding to this surrogate pair is returned. Otherwise,
 the <code>char</code> value at the given index is returned.

**Parameters:**

* `index` - the index to the <code>char</code> values

**Returns:** the code point value of the character at the
             <code>index</code>

</details>
<details>
<summary><code>int codePointBefore(int index)</code></summary>

Returns the character (Unicode code point) before the specified
 index. The index refers to <code>char</code> values
 (Unicode code units) and ranges from <code>1</code> to <code>length</code>.

 <p> If the <code>char</code> value at <code>(index - 1)</code>
 is in the low-surrogate range, <code>(index - 2)</code> is not
 negative, and the <code>char</code> value at <code>(index -
 2)</code> is in the high-surrogate range, then the
 supplementary code point value of the surrogate pair is
 returned. If the <code>char</code> value at <code>index -
 1</code> is an unpaired low-surrogate or a high-surrogate, the
 surrogate value is returned.

**Parameters:**

* `index` - the index following the code point that should be returned

**Returns:** the Unicode code point value before the given index.

</details>
<details>
<summary><code>int codePointCount(int beginIndex, int endIndex)</code></summary>

Returns the number of Unicode code points in the specified text
 range of this <code>String</code>. The text range begins at the
 specified <code>beginIndex</code> and extends to the
 <code>char</code> at index <code>endIndex - 1</code>. Thus the
 length (in <code>char</code>s) of the text range is
 <code>endIndex-beginIndex</code>. Unpaired surrogates within
 the text range count as one code point each.

**Parameters:**

* `beginIndex` - the index to the first <code>char</code> of
 the text range.
* `endIndex` - the index after the last <code>char</code> of
 the text range.

**Returns:** the number of Unicode code points in the specified text
 range

</details>
<details>
<summary><code>IntStream codePoints()</code></summary>

Returns a stream of code point values from this sequence.  Any surrogate
 pairs encountered in the sequence are combined as if by <code>Character.toCodePoint</code> and the result is passed
 to the stream. Any other code units, including ordinary BMP characters,
 unpaired surrogates, and undefined code units, are zero-extended to
 <code>int</code> values which are then passed to the stream.

**Returns:** an IntStream of Unicode code points from this sequence

</details>
<details>
<summary><code>int compareTo(String anotherString)</code></summary>

Compares two strings lexicographically.
 The comparison is based on the Unicode value of each character in
 the strings. The character sequence represented by this
 <code>String</code> object is compared lexicographically to the
 character sequence represented by the argument string. The result is
 a negative integer if this <code>String</code> object
 lexicographically precedes the argument string. The result is a
 positive integer if this <code>String</code> object lexicographically
 follows the argument string. The result is zero if the strings
 are equal; <code>compareTo</code> returns <code>0</code> exactly when
 the <code>#equals(Object)</code> method would return <code>true</code>.
 <p>
 This is the definition of lexicographic ordering. If two strings are
 different, then either they have different characters at some index
 that is a valid index for both strings, or their lengths are different,
 or both. If they have different characters at one or more index
 positions, let <i>k</i> be the smallest such index; then the string
 whose character at position <i>k</i> has the smaller value, as
 determined by using the <code>&lt;</code> operator, lexicographically precedes the
 other string. In this case, <code>compareTo</code> returns the
 difference of the two character values at position <code>k</code> in
 the two string -- that is, the value:
 <blockquote><pre>
 this.charAt(k)-anotherString.charAt(k)
 </pre></blockquote>
 If there is no index position at which they differ, then the shorter
 string lexicographically precedes the longer string. In this case,
 <code>compareTo</code> returns the difference of the lengths of the
 strings -- that is, the value:
 <blockquote><pre>
 this.length()-anotherString.length()
 </pre></blockquote>

 <p>For finer-grained String comparison, refer to
 <code>java.text.Collator</code>.

**Parameters:**

* `anotherString` - the <code>String</code> to be compared.

**Returns:** the value <code>0</code> if the argument string is equal to
          this string; a value less than <code>0</code> if this string
          is lexicographically less than the string argument; and a
          value greater than <code>0</code> if this string is
          lexicographically greater than the string argument.

</details>
<details>
<summary><code>int compareToIgnoreCase(String str)</code></summary>

Compares two strings lexicographically, ignoring case
 differences. This method returns an integer whose sign is that of
 calling <code>compareTo</code> with case folded versions of the strings
 where case differences have been eliminated by calling
 <code>Character.toLowerCase(Character.toUpperCase(int))</code> on
 each Unicode code point.
 <p>
 Note that this method does <em>not</em> take locale into account,
 and will result in an unsatisfactory ordering for certain locales.
 The <code>java.text.Collator</code> class provides locale-sensitive comparison.

**Parameters:**

* `str` - the <code>String</code> to be compared.

**Returns:** a negative integer, zero, or a positive integer as the
          specified String is greater than, equal to, or less
          than this String, ignoring case considerations.

</details>
<details>
<summary><code>String concat(String str)</code></summary>

Concatenates the specified string to the end of this string.
 <p>
 If the length of the argument string is <code>0</code>, then this
 <code>String</code> object is returned. Otherwise, a
 <code>String</code> object is returned that represents a character
 sequence that is the concatenation of the character sequence
 represented by this <code>String</code> object and the character
 sequence represented by the argument string.<p>
 Examples:
 <blockquote><pre>
 "cares".concat("s") returns "caress"
 "to".concat("get").concat("her") returns "together"
 </pre></blockquote>

**Parameters:**

* `str` - the <code>String</code> that is concatenated to the end
                of this <code>String</code>.

**Returns:** a string that represents the concatenation of this object's
          characters followed by the string argument's characters.

</details>
<details>
<summary><code>boolean contains(CharSequence s)</code></summary>

Returns true if and only if this string contains the specified
 sequence of char values.

**Parameters:**

* `s` - the sequence to search for

**Returns:** true if this string contains <code>s</code>, false otherwise

</details>
<details>
<summary><code>boolean contentEquals(CharSequence cs)</code></summary>

Compares this string to the specified <code>CharSequence</code>.  The
 result is <code>true</code> if and only if this <code>String</code> represents the
 same sequence of char values as the specified sequence. Note that if the
 <code>CharSequence</code> is a <code>StringBuffer</code> then the method
 synchronizes on it.

 <p>For finer-grained String comparison, refer to
 <code>java.text.Collator</code>.

**Parameters:**

* `cs` - The sequence to compare this <code>String</code> against

**Returns:** <code>true</code> if this <code>String</code> represents the same
          sequence of char values as the specified sequence, <code>false</code> otherwise

</details>
<details>
<summary><code>boolean contentEquals(StringBuffer sb)</code></summary>

Compares this string to the specified <code>StringBuffer</code>.  The result
 is <code>true</code> if and only if this <code>String</code> represents the same
 sequence of characters as the specified <code>StringBuffer</code>. This method
 synchronizes on the <code>StringBuffer</code>.

 <p>For finer-grained String comparison, refer to
 <code>java.text.Collator</code>.

**Parameters:**

* `sb` - The <code>StringBuffer</code> to compare this <code>String</code> against

**Returns:** <code>true</code> if this <code>String</code> represents the same
          sequence of characters as the specified <code>StringBuffer</code>,
          <code>false</code> otherwise

</details>
<details>
<summary><code>static String copyValueOf(char[] data)</code></summary>

Equivalent to <code>#valueOf(char[])</code>.

**Parameters:**

* `data` - the character array.

**Returns:** a <code>String</code> that contains the characters of the
          character array.

</details>
<details>
<summary><code>static String copyValueOf(char[] data, int offset, int count)</code></summary>

Equivalent to <code>int, int)</code>.

**Parameters:**

* `data` - the character array.
* `offset` - initial offset of the subarray.
* `count` - length of the subarray.

**Returns:** a <code>String</code> that contains the characters of the
          specified subarray of the character array.

</details>
<details>
<summary><code>Optional&lt;String&gt; describeConstable()</code></summary>

Returns an <code>Optional</code> containing the nominal descriptor for this
 instance, which is the instance itself.

**Returns:** an <code>Optional</code> describing the <code>String</code> instance

</details>
<details>
<summary><code>boolean equals(Object anObject)</code></summary>

Compares this string to the specified object.  The result is <code>true</code> if and only if the argument is not <code>null</code> and is a <code>String</code> object that represents the same sequence of characters as this
 object.

 <p>For finer-grained String comparison, refer to
 <code>java.text.Collator</code>.

**Parameters:**

* `anObject` - The object to compare this <code>String</code> against

**Returns:** <code>true</code> if the given object represents a <code>String</code>
          equivalent to this string, <code>false</code> otherwise

</details>
<details>
<summary><code>boolean equalsIgnoreCase(String anotherString)</code></summary>

Compares this <code>String</code> to another <code>String</code>, ignoring case
 considerations.  Two strings are considered equal ignoring case if they
 are of the same length and corresponding Unicode code points in the two
 strings are equal ignoring case.

 <p> Two Unicode code points are considered the same
 ignoring case if at least one of the following is true:
 <ul>
   <li> The two Unicode code points are the same (as compared by the
        <code>==</code> operator)
   <li> Calling <code>Character.toLowerCase(Character.toUpperCase(int))</code>
        on each Unicode code point produces the same result
 </ul>

 <p>Note that this method does <em>not</em> take locale into account, and
 will result in unsatisfactory results for certain locales.  The
 <code>java.text.Collator</code> class provides locale-sensitive comparison.

**Parameters:**

* `anotherString` - The <code>String</code> to compare this <code>String</code> against

**Returns:** <code>true</code> if the argument is not <code>null</code> and it
          represents an equivalent <code>String</code> ignoring case; <code>false</code> otherwise

</details>
<details>
<summary><code>static String format(Locale l, String format, Object[] args)</code></summary>

Returns a formatted string using the specified locale, format string,
 and arguments.

**Parameters:**

* `l` - The <code>locale</code> to apply during
         formatting.  If <code>l</code> is <code>null</code> then no localization
         is applied.
* `format` - A format string
* `args` - Arguments referenced by the format specifiers in the format
         string.  If there are more arguments than format specifiers, the
         extra arguments are ignored.  The number of arguments is
         variable and may be zero.  The maximum number of arguments is
         limited by the maximum dimension of a Java array as defined by
         <cite>The Java Virtual Machine Specification</cite>.
         The behaviour on a
         <code>null</code> argument depends on the
         conversion.

**Returns:** A formatted string

</details>
<details>
<summary><code>static String format(String format, Object[] args)</code></summary>

Returns a formatted string using the specified format string and
 arguments.

 <p> The locale always used is the one returned by <code>Locale.getDefault(Locale.Category)</code> with
 <code>FORMAT</code> category specified.

**Parameters:**

* `format` - A format string
* `args` - Arguments referenced by the format specifiers in the format
         string.  If there are more arguments than format specifiers, the
         extra arguments are ignored.  The number of arguments is
         variable and may be zero.  The maximum number of arguments is
         limited by the maximum dimension of a Java array as defined by
         <cite>The Java Virtual Machine Specification</cite>.
         The behaviour on a
         <code>null</code> argument depends on the conversion.

**Returns:** A formatted string

</details>
<details>
<summary><code>String formatted(Object[] args)</code></summary>

Formats using this string as the format string, and the supplied
 arguments.

**Parameters:**

* `args` - Arguments referenced by the format specifiers in this string.

**Returns:** A formatted string

</details>
<details>
<summary><code>byte[] getBytes()</code></summary>

Encodes this <code>String</code> into a sequence of bytes using the
 <code>default charset</code>, storing the result
 into a new byte array.

 <p> The behavior of this method when this string cannot be encoded in
 the default charset is unspecified.  The <code>java.nio.charset.CharsetEncoder</code> class should be used when more control
 over the encoding process is required.

**Returns:** The resultant byte array

</details>
<details>
<summary><code>byte[] getBytes(Charset charset)</code></summary>

Encodes this <code>String</code> into a sequence of bytes using the given
 <code>charset</code>, storing the result into a
 new byte array.

 <p> This method always replaces malformed-input and unmappable-character
 sequences with this charset's default replacement byte array.  The
 <code>java.nio.charset.CharsetEncoder</code> class should be used when more
 control over the encoding process is required.

**Parameters:**

* `charset` - The <code>java.nio.charset.Charset</code> to be used to encode
         the <code>String</code>

**Returns:** The resultant byte array

</details>
<details>
<summary><code>byte[] getBytes(String charsetName)</code></summary>

Encodes this <code>String</code> into a sequence of bytes using the named
 charset, storing the result into a new byte array.

 <p> The behavior of this method when this string cannot be encoded in
 the given charset is unspecified.  The <code>java.nio.charset.CharsetEncoder</code> class should be used when more control
 over the encoding process is required.

**Parameters:**

* `charsetName` - The name of a supported <code>charset</code>

**Returns:** The resultant byte array

</details>
<details>
<summary><code>void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)</code></summary>

Copies characters from this string into the destination character
 array.
 <p>
 The first character to be copied is at index <code>srcBegin</code>;
 the last character to be copied is at index <code>srcEnd-1</code>
 (thus the total number of characters to be copied is
 <code>srcEnd-srcBegin</code>). The characters are copied into the
 subarray of <code>dst</code> starting at index <code>dstBegin</code>
 and ending at index:
 <blockquote><pre>
     dstBegin + (srcEnd-srcBegin) - 1
 </pre></blockquote>

**Parameters:**

* `srcBegin` - index of the first character in the string
                        to copy.
* `srcEnd` - index after the last character in the string
                        to copy.
* `dst` - the destination array.
* `dstBegin` - the start offset in the destination array.

</details>
<details>
<summary><code>int hashCode()</code></summary>

Returns a hash code for this string. The hash code for a
 <code>String</code> object is computed as
 <blockquote><pre>
 s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
 </pre></blockquote>
 using <code>int</code> arithmetic, where <code>s[i]</code> is the
 <i>i</i>th character of the string, <code>n</code> is the length of
 the string, and <code>^</code> indicates exponentiation.
 (The hash value of the empty string is zero.)

**Returns:** a hash code value for this object.

</details>
<details>
<summary><code>String indent(int n)</code></summary>

Adjusts the indentation of each line of this string based on the value of
 <code>n</code>, and normalizes line termination characters.
 <p>
 This string is conceptually separated into lines using
 <code>String#lines()</code>. Each line is then adjusted as described below
 and then suffixed with a line feed <code>"\n"</code> (U+000A). The resulting
 lines are then concatenated and returned.
 <p>
 If <code>n &gt; 0</code> then <code>n</code> spaces (U+0020) are inserted at the
 beginning of each line.
 <p>
 If <code>n &lt; 0</code> then up to <code>n</code>
 <code>white space characters</code> are removed
 from the beginning of each line. If a given line does not contain
 sufficient white space then all leading
 <code>white space characters</code> are removed.
 Each white space character is treated as a single character. In
 particular, the tab character <code>"\t"</code> (U+0009) is considered a
 single character; it is not expanded.
 <p>
 If <code>n == 0</code> then the line remains unchanged. However, line
 terminators are still normalized.

**Parameters:**

* `n` - number of leading
           <code>white space characters</code>
           to add or remove

**Returns:** string with indentation adjusted and line endings normalized

</details>
<details>
<summary><code>int indexOf(String str)</code></summary>

Returns the index within this string of the first occurrence of the
 specified substring.

 <p>The returned index is the smallest value <code>k</code> for which:
 <pre><code>this.startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.

**Returns:** the index of the first occurrence of the specified substring,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int indexOf(String str, int beginIndex, int endIndex)</code></summary>

Returns the index of the first occurrence of the specified substring
 within the specified index range of <code>this</code> string.

 <p>This method returns the same result as the one of the invocation
 <pre><code>s.substring(beginIndex, endIndex).indexOf(str) + beginIndex</code></pre>
 if the index returned by <code>#indexOf(String)</code> is non-negative,
 and returns -1 otherwise.
 (No substring is instantiated, though.)

**Parameters:**

* `str` - the substring to search for.
* `beginIndex` - the index to start the search from (included).
* `endIndex` - the index to stop the search at (excluded).

**Returns:** the index of the first occurrence of the specified substring
          within the specified index range,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int indexOf(String str, int fromIndex)</code></summary>

Returns the index within this string of the first occurrence of the
 specified substring, starting at the specified index.

 <p>The returned index is the smallest value <code>k</code> for which:
 <pre><code>k &gt;= Math.min(fromIndex, this.length()) &amp;&amp;
                   this.startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.
* `fromIndex` - the index from which to start the search.

**Returns:** the index of the first occurrence of the specified substring,
          starting at the specified index,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int indexOf(int ch)</code></summary>

Returns the index within this string of the first occurrence of
 the specified character. If a character with value
 <code>ch</code> occurs in the character sequence represented by
 this <code>String</code> object, then the index (in Unicode
 code units) of the first such occurrence is returned. For
 values of <code>ch</code> in the range from 0 to 0xFFFF
 (inclusive), this is the smallest value <i>k</i> such that:
 <blockquote><pre>
 this.charAt(<i>k</i>) == ch
 </pre></blockquote>
 is true. For other values of <code>ch</code>, it is the
 smallest value <i>k</i> such that:
 <blockquote><pre>
 this.codePointAt(<i>k</i>) == ch
 </pre></blockquote>
 is true. In either case, if no such character occurs in this
 string, then <code>-1</code> is returned.

**Parameters:**

* `ch` - a character (Unicode code point).

**Returns:** the index of the first occurrence of the character in the
          character sequence represented by this object, or
          <code>-1</code> if the character does not occur.

</details>
<details>
<summary><code>int indexOf(int ch, int beginIndex, int endIndex)</code></summary>

Returns the index within this string of the first occurrence of the
 specified character, starting the search at <code>beginIndex</code> and
 stopping before <code>endIndex</code>.

 <p>If a character with value <code>ch</code> occurs in the
 character sequence represented by this <code>String</code>
 object at an index no smaller than <code>beginIndex</code> but smaller than
 <code>endIndex</code>, then
 the index of the first such occurrence is returned. For values
 of <code>ch</code> in the range from 0 to 0xFFFF (inclusive),
 this is the smallest value <i>k</i> such that:
 <blockquote><pre>
 (this.charAt(<i>k</i>) == ch) &amp;&amp; (beginIndex &lt;= <i>k</i> &lt; endIndex)
 </pre></blockquote>
 is true. For other values of <code>ch</code>, it is the
 smallest value <i>k</i> such that:
 <blockquote><pre>
 (this.codePointAt(<i>k</i>) == ch) &amp;&amp; (beginIndex &lt;= <i>k</i> &lt; endIndex)
 </pre></blockquote>
 is true. In either case, if no such character occurs in this
 string at or after position <code>beginIndex</code> and before position
 <code>endIndex</code>, then <code>-1</code> is returned.

 <p>All indices are specified in <code>char</code> values
 (Unicode code units).

**Parameters:**

* `ch` - a character (Unicode code point).
* `beginIndex` - the index to start the search from (included).
* `endIndex` - the index to stop the search at (excluded).

**Returns:** the index of the first occurrence of the character in the
          character sequence represented by this object that is greater
          than or equal to <code>beginIndex</code> and less than <code>endIndex</code>,
          or <code>-1</code> if the character does not occur.

</details>
<details>
<summary><code>int indexOf(int ch, int fromIndex)</code></summary>

Returns the index within this string of the first occurrence of the
 specified character, starting the search at the specified index.
 <p>
 If a character with value <code>ch</code> occurs in the
 character sequence represented by this <code>String</code>
 object at an index no smaller than <code>fromIndex</code>, then
 the index of the first such occurrence is returned. For values
 of <code>ch</code> in the range from 0 to 0xFFFF (inclusive),
 this is the smallest value <i>k</i> such that:
 <blockquote><pre>
 (this.charAt(<i>k</i>) == ch) <code>&amp;&amp;</code> (<i>k</i> &gt;= fromIndex)
 </pre></blockquote>
 is true. For other values of <code>ch</code>, it is the
 smallest value <i>k</i> such that:
 <blockquote><pre>
 (this.codePointAt(<i>k</i>) == ch) <code>&amp;&amp;</code> (<i>k</i> &gt;= fromIndex)
 </pre></blockquote>
 is true. In either case, if no such character occurs in this
 string at or after position <code>fromIndex</code>, then
 <code>-1</code> is returned.

 <p>
 There is no restriction on the value of <code>fromIndex</code>. If it
 is negative, it has the same effect as if it were zero: this entire
 string may be searched. If it is greater than the length of this
 string, it has the same effect as if it were equal to the length of
 this string: <code>-1</code> is returned.

 <p>All indices are specified in <code>char</code> values
 (Unicode code units).

**Parameters:**

* `ch` - a character (Unicode code point).
* `fromIndex` - the index to start the search from.

**Returns:** the index of the first occurrence of the character in the
          character sequence represented by this object that is greater
          than or equal to <code>fromIndex</code>, or <code>-1</code>
          if the character does not occur.

</details>
<details>
<summary><code>String intern()</code></summary>

Returns a canonical representation for the string object.
 <p>
 A pool of strings, initially empty, is maintained privately by the
 class <code>String</code>.
 <p>
 When the intern method is invoked, if the pool already contains a
 string equal to this <code>String</code> object as determined by
 the <code>#equals(Object)</code> method, then the string from the pool is
 returned. Otherwise, this <code>String</code> object is added to the
 pool and a reference to this <code>String</code> object is returned.
 <p>
 It follows that for any two strings <code>s</code> and <code>t</code>,
 <code>s.intern() == t.intern()</code> is <code>true</code>
 if and only if <code>s.equals(t)</code> is <code>true</code>.
 <p>
 All literal strings and string-valued constant expressions are
 interned. String literals are defined in section JLS 3.10.5 of the
 <cite>The Java Language Specification</cite>.

**Returns:** a string that has the same contents as this string, but is
          guaranteed to be from a pool of unique strings.

</details>
<details>
<summary><code>boolean isBlank()</code></summary>

Returns <code>true</code> if the string is empty or contains only
 <code>white space</code> codepoints,
 otherwise <code>false</code>.

**Returns:** <code>true</code> if the string is empty or contains only
         <code>white space</code> codepoints,
         otherwise <code>false</code>

</details>
<details>
<summary><code>static String join(CharSequence delimiter, CharSequence[] elements)</code></summary>

Returns a new String composed of copies of the
 <code>CharSequence elements</code> joined together with a copy of
 the specified <code>delimiter</code>.

 <blockquote>For example,
 <pre><code>String message = String.join("-", "Java", "is", "cool");
     // message returned is: "Java-is-cool"</code></pre></blockquote>

 Note that if an element is null, then <code>"null"</code> is added.

**Parameters:**

* `delimiter` - the delimiter that separates each element
* `elements` - the elements to join together.

**Returns:** a new <code>String</code> that is composed of the <code>elements</code>
         separated by the <code>delimiter</code>

</details>
<details>
<summary><code>static String join(CharSequence delimiter, Iterable&lt;? extends CharSequence&gt; elements)</code></summary>

Returns a new <code>String</code> composed of copies of the
 <code>CharSequence elements</code> joined together with a copy of the
 specified <code>delimiter</code>.

 <blockquote>For example,
 <pre><code>List&lt;String&gt; strings = List.of("Java", "is", "cool");
     String message = String.join(" ", strings);
     // message returned is: "Java is cool"

     Set&lt;String&gt; strings =
         new LinkedHashSet&lt;&gt;(List.of("Java", "is", "very", "cool"));
     String message = String.join("-", strings);
     // message returned is: "Java-is-very-cool"</code></pre></blockquote>

 Note that if an individual element is <code>null</code>, then <code>"null"</code> is added.

**Parameters:**

* `delimiter` - a sequence of characters that is used to separate each
         of the <code>elements</code> in the resulting <code>String</code>
* `elements` - an <code>Iterable</code> that will have its <code>elements</code>
         joined together.

**Returns:** a new <code>String</code> that is composed from the <code>elements</code>
         argument

</details>
<details>
<summary><code>int lastIndexOf(String str)</code></summary>

Returns the index within this string of the last occurrence of the
 specified substring.  The last occurrence of the empty string ""
 is considered to occur at the index value <code>this.length()</code>.

 <p>The returned index is the largest value <code>k</code> for which:
 <pre><code>this.startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.

**Returns:** the index of the last occurrence of the specified substring,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int lastIndexOf(String str, int fromIndex)</code></summary>

Returns the index within this string of the last occurrence of the
 specified substring, searching backward starting at the specified index.

 <p>The returned index is the largest value <code>k</code> for which:
 <pre><code>k &lt;= Math.min(fromIndex, this.length()) &amp;&amp;
                   this.startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.
* `fromIndex` - the index to start the search from.

**Returns:** the index of the last occurrence of the specified substring,
          searching backward from the specified index,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int lastIndexOf(int ch)</code></summary>

Returns the index within this string of the last occurrence of
 the specified character. For values of <code>ch</code> in the
 range from 0 to 0xFFFF (inclusive), the index (in Unicode code
 units) returned is the largest value <i>k</i> such that:
 <blockquote><pre>
 this.charAt(<i>k</i>) == ch
 </pre></blockquote>
 is true. For other values of <code>ch</code>, it is the
 largest value <i>k</i> such that:
 <blockquote><pre>
 this.codePointAt(<i>k</i>) == ch
 </pre></blockquote>
 is true.  In either case, if no such character occurs in this
 string, then <code>-1</code> is returned.  The
 <code>String</code> is searched backwards starting at the last
 character.

**Parameters:**

* `ch` - a character (Unicode code point).

**Returns:** the index of the last occurrence of the character in the
          character sequence represented by this object, or
          <code>-1</code> if the character does not occur.

</details>
<details>
<summary><code>int lastIndexOf(int ch, int fromIndex)</code></summary>

Returns the index within this string of the last occurrence of
 the specified character, searching backward starting at the
 specified index. For values of <code>ch</code> in the range
 from 0 to 0xFFFF (inclusive), the index returned is the largest
 value <i>k</i> such that:
 <blockquote><pre>
 (this.charAt(<i>k</i>) == ch) <code>&amp;&amp;</code> (<i>k</i> &lt;= fromIndex)
 </pre></blockquote>
 is true. For other values of <code>ch</code>, it is the
 largest value <i>k</i> such that:
 <blockquote><pre>
 (this.codePointAt(<i>k</i>) == ch) <code>&amp;&amp;</code> (<i>k</i> &lt;= fromIndex)
 </pre></blockquote>
 is true. In either case, if no such character occurs in this
 string at or before position <code>fromIndex</code>, then
 <code>-1</code> is returned.

 <p>All indices are specified in <code>char</code> values
 (Unicode code units).

**Parameters:**

* `ch` - a character (Unicode code point).
* `fromIndex` - the index to start the search from. There is no
          restriction on the value of <code>fromIndex</code>. If it is
          greater than or equal to the length of this string, it has
          the same effect as if it were equal to one less than the
          length of this string: this entire string may be searched.
          If it is negative, it has the same effect as if it were -1:
          -1 is returned.

**Returns:** the index of the last occurrence of the character in the
          character sequence represented by this object that is less
          than or equal to <code>fromIndex</code>, or <code>-1</code>
          if the character does not occur before that point.

</details>
<details>
<summary><code>int length()</code></summary>

Returns the length of this string.
 The length is equal to the number of Unicode
 code units in the string.

**Returns:** the length of the sequence of characters represented by this
          object.

</details>
<details>
<summary><code>Stream&lt;String&gt; lines()</code></summary>

Returns a stream of lines extracted from this string,
 separated by line terminators.
 <p>
 A <i>line terminator</i> is one of the following:
 a line feed character <code>"\n"</code> (U+000A),
 a carriage return character <code>"\r"</code> (U+000D),
 or a carriage return followed immediately by a line feed
 <code>"\r\n"</code> (U+000D U+000A).
 <p>
 A <i>line</i> is either a sequence of zero or more characters
 followed by a line terminator, or it is a sequence of one or
 more characters followed by the end of the string. A
 line does not include the line terminator.
 <p>
 The stream returned by this method contains the lines from
 this string in the order in which they occur.

**Returns:** the stream of lines extracted from this string

</details>
<details>
<summary><code>boolean matches(String regex)</code></summary>

Tells whether or not this string matches the given regular expression.

 <p> An invocation of this method of the form
 <i>str</i><code>.matches(</code><i>regex</i><code>)</code> yields exactly the
 same result as the expression

 <blockquote>
 <code>java.util.regex.Pattern</code>.<code>matches(&lt;i&gt;regex&lt;/i&gt;, &lt;i&gt;str&lt;/i&gt;)</code>
 </blockquote>

**Parameters:**

* `regex` - the regular expression to which this string is to be matched

**Returns:** <code>true</code> if, and only if, this string matches the
          given regular expression

</details>
<details>
<summary><code>int offsetByCodePoints(int index, int codePointOffset)</code></summary>

Returns the index within this <code>String</code> that is
 offset from the given <code>index</code> by
 <code>codePointOffset</code> code points. Unpaired surrogates
 within the text range given by <code>index</code> and
 <code>codePointOffset</code> count as one code point each.

**Parameters:**

* `index` - the index to be offset
* `codePointOffset` - the offset in code points

**Returns:** the index within this <code>String</code>

</details>
<details>
<summary><code>boolean regionMatches(boolean ignoreCase, int toffset, String other, int ooffset, int len)</code></summary>

Tests if two string regions are equal.
 <p>
 A substring of this <code>String</code> object is compared to a substring
 of the argument <code>other</code>. The result is <code>true</code> if these
 substrings represent Unicode code point sequences that are the same,
 ignoring case if and only if <code>ignoreCase</code> is true.
 The sequences <code>tsequence</code> and <code>osequence</code> are compared,
 where <code>tsequence</code> is the sequence produced as if by calling
 <code>this.substring(toffset, toffset + len).codePoints()</code> and
 <code>osequence</code> is the sequence produced as if by calling
 <code>other.substring(ooffset, ooffset + len).codePoints()</code>.
 The result is <code>true</code> if and only if all of the following
 are true:
 <ul><li><code>toffset</code> is non-negative.
 <li><code>ooffset</code> is non-negative.
 <li><code>toffset+len</code> is less than or equal to the length of this
 <code>String</code> object.
 <li><code>ooffset+len</code> is less than or equal to the length of the other
 argument.
 <li>if <code>ignoreCase</code> is <code>false</code>, all pairs of corresponding Unicode
 code points are equal integer values; or if <code>ignoreCase</code> is <code>true</code>,
 <code>Character.toLowerCase(</code>
 <code>Character#toUpperCase(int)</code><code>)</code> on all pairs of Unicode code points
 results in equal integer values.
 </ul>

 <p>Note that this method does <em>not</em> take locale into account,
 and will result in unsatisfactory results for certain locales when
 <code>ignoreCase</code> is <code>true</code>.  The <code>java.text.Collator</code> class
 provides locale-sensitive comparison.

**Parameters:**

* `ignoreCase` - if <code>true</code>, ignore case when comparing
                       characters.
* `toffset` - the starting offset of the subregion in this
                       string.
* `other` - the string argument.
* `ooffset` - the starting offset of the subregion in the string
                       argument.
* `len` - the number of characters (Unicode code units -
                       16bit <code>char</code> value) to compare.

**Returns:** <code>true</code> if the specified subregion of this string
          matches the specified subregion of the string argument;
          <code>false</code> otherwise. Whether the matching is exact
          or case insensitive depends on the <code>ignoreCase</code>
          argument.

</details>
<details>
<summary><code>boolean regionMatches(int toffset, String other, int ooffset, int len)</code></summary>

Tests if two string regions are equal.
 <p>
 A substring of this <code>String</code> object is compared to a substring
 of the argument other. The result is true if these substrings
 represent identical character sequences. The substring of this
 <code>String</code> object to be compared begins at index <code>toffset</code>
 and has length <code>len</code>. The substring of other to be compared
 begins at index <code>ooffset</code> and has length <code>len</code>. The
 result is <code>false</code> if and only if at least one of the following
 is true:
 <ul><li><code>toffset</code> is negative.
 <li><code>ooffset</code> is negative.
 <li><code>toffset+len</code> is greater than the length of this
 <code>String</code> object.
 <li><code>ooffset+len</code> is greater than the length of the other
 argument.
 <li>There is some nonnegative integer <i>k</i> less than <code>len</code>
 such that:
 <code>this.charAt(toffset +</code><i>k</i><code>) != other.charAt(ooffset +</code>
 <i>k</i><code>)</code>
 </ul>

 <p>Note that this method does <em>not</em> take locale into account.  The
 <code>java.text.Collator</code> class provides locale-sensitive comparison.

**Parameters:**

* `toffset` - the starting offset of the subregion in this string.
* `other` - the string argument.
* `ooffset` - the starting offset of the subregion in the string
                    argument.
* `len` - the number of characters to compare.

**Returns:** <code>true</code> if the specified subregion of this string
          exactly matches the specified subregion of the string argument;
          <code>false</code> otherwise.

</details>
<details>
<summary><code>String repeat(int count)</code></summary>

Returns a string whose value is the concatenation of this
 string repeated <code>count</code> times.
 <p>
 If this string is empty or count is zero then the empty
 string is returned.

**Parameters:**

* `count` - number of times to repeat

**Returns:** A string composed of this string repeated
          <code>count</code> times or the empty string if this
          string is empty or count is zero

</details>
<details>
<summary><code>String replaceAll(String regex, String replacement)</code></summary>

Replaces each substring of this string that matches the given regular expression with the
 given replacement.

 <p> An invocation of this method of the form
 <i>str</i><code>.replaceAll(</code><i>regex</i><code>,</code> <i>repl</i><code>)</code>
 yields exactly the same result as the expression

 <blockquote>
 <code>
 <code>java.util.regex.Pattern</code>.<code>compile</code>(<i>regex</i>).<code>matcher</code>(<i>str</i>).<code>replaceAll</code>(<i>repl</i>)
 </code>
 </blockquote>

<p>
 Note that backslashes (<code>\</code>) and dollar signs (<code>$</code>) in the
 replacement string may cause the results to be different than if it were
 being treated as a literal replacement string; see
 <code>Matcher.replaceAll</code>.
 Use <code>java.util.regex.Matcher#quoteReplacement</code> to suppress the special
 meaning of these characters, if desired.

**Parameters:**

* `regex` - the regular expression to which this string is to be matched
* `replacement` - the string to be substituted for each match

**Returns:** The resulting <code>String</code>

</details>
<details>
<summary><code>String replaceFirst(String regex, String replacement)</code></summary>

Replaces the first substring of this string that matches the given regular expression with the
 given replacement.

 <p> An invocation of this method of the form
 <i>str</i><code>.replaceFirst(</code><i>regex</i><code>,</code> <i>repl</i><code>)</code>
 yields exactly the same result as the expression

 <blockquote>
 <code>
 <code>java.util.regex.Pattern</code>.<code>compile</code>(<i>regex</i>).<code>matcher</code>(<i>str</i>).<code>replaceFirst</code>(<i>repl</i>)
 </code>
 </blockquote>

<p>
 Note that backslashes (<code>\</code>) and dollar signs (<code>$</code>) in the
 replacement string may cause the results to be different than if it were
 being treated as a literal replacement string; see
 <code>java.util.regex.Matcher#replaceFirst</code>.
 Use <code>java.util.regex.Matcher#quoteReplacement</code> to suppress the special
 meaning of these characters, if desired.

**Parameters:**

* `regex` - the regular expression to which this string is to be matched
* `replacement` - the string to be substituted for the first match

**Returns:** The resulting <code>String</code>

</details>
<details>
<summary><code>String resolveConstantDesc(MethodHandles.Lookup lookup)</code></summary>

Resolves this instance as a <code>ConstantDesc</code>, the result of which is
 the instance itself.

**Parameters:**

* `lookup` - ignored

**Returns:** the <code>String</code> instance

</details>
<details>
<summary><code>String[] split(String regex)</code></summary>

Splits this string around matches of the given regular expression.

 <p> This method works as if by invoking the two-argument <code>int) split</code> method with the given expression and a limit
 argument of zero.  Trailing empty strings are therefore not included in
 the resulting array.

 <p> The string <code>"boo:and:foo"</code>, for example, yields the following
 results with these expressions:

 <blockquote><table class="plain">
 <caption style="display:none">Split examples showing regex and result</caption>
 <thead>
 <tr>
  <th scope="col">Regex</th>
  <th scope="col">Result</th>
 </tr>
 </thead>
 <tbody>
 <tr><th scope="row" style="text-weight:normal">:</th>
     <td><code>{ "boo", "and", "foo"</code>}</td></tr>
 <tr><th scope="row" style="text-weight:normal">o</th>
     <td><code>{ "b", "", ":and:f"</code>}</td></tr>
 </tbody>
 </table></blockquote>

**Parameters:**

* `regex` - the delimiting regular expression

**Returns:** the array of strings computed by splitting this string
          around matches of the given regular expression

</details>
<details>
<summary><code>String[] split(String regex, int limit)</code></summary>

Splits this string around matches of the given
 regular expression.

 <p> The array returned by this method contains each substring of this
 string that is terminated by another substring that matches the given
 expression or is terminated by the end of the string.  The substrings in
 the array are in the order in which they occur in this string.  If the
 expression does not match any part of the input then the resulting array
 has just one element, namely this string.

 <p> When there is a positive-width match at the beginning of this
 string then an empty leading substring is included at the beginning
 of the resulting array. A zero-width match at the beginning however
 never produces such empty leading substring.

 <p> The <code>limit</code> parameter controls the number of times the
 pattern is applied and therefore affects the length of the resulting
 array.
 <ul>
    <li><p>
    If the <i>limit</i> is positive then the pattern will be applied
    at most <i>limit</i>&nbsp;-&nbsp;1 times, the array's length will be
    no greater than <i>limit</i>, and the array's last entry will contain
    all input beyond the last matched delimiter.</p></li>

    <li><p>
    If the <i>limit</i> is zero then the pattern will be applied as
    many times as possible, the array can have any length, and trailing
    empty strings will be discarded.</p></li>

    <li><p>
    If the <i>limit</i> is negative then the pattern will be applied
    as many times as possible and the array can have any length.</p></li>
 </ul>

 <p> The string <code>"boo:and:foo"</code>, for example, yields the
 following results with these parameters:

 <blockquote><table class="plain">
 <caption style="display:none">Split example showing regex, limit, and result</caption>
 <thead>
 <tr>
     <th scope="col">Regex</th>
     <th scope="col">Limit</th>
     <th scope="col">Result</th>
 </tr>
 </thead>
 <tbody>
 <tr><th scope="row" rowspan="3" style="font-weight:normal">:</th>
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">2</th>
     <td><code>{ "boo", "and:foo"</code>}</td></tr>
 <tr><!-- : -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
     <td><code>{ "boo", "and", "foo"</code>}</td></tr>
 <tr><!-- : -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-2</th>
     <td><code>{ "boo", "and", "foo"</code>}</td></tr>
 <tr><th scope="row" rowspan="3" style="font-weight:normal">o</th>
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
     <td><code>{ "b", "", ":and:f", "", ""</code>}</td></tr>
 <tr><!-- o -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-2</th>
     <td><code>{ "b", "", ":and:f", "", ""</code>}</td></tr>
 <tr><!-- o -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">0</th>
     <td><code>{ "b", "", ":and:f"</code>}</td></tr>
 </tbody>
 </table></blockquote>

 <p> An invocation of this method of the form
 <i>str.</i><code>split(</code><i>regex</i><code>,</code>&nbsp;<i>n</i><code>)</code>
 yields the same result as the expression

 <blockquote>
 <code>
 <code>java.util.regex.Pattern</code>.<code>compile</code>(<i>regex</i>).<code>split</code>(<i>str</i>,&nbsp;<i>n</i>)
 </code>
 </blockquote>

**Parameters:**

* `regex` - the delimiting regular expression
* `limit` - the result threshold, as described above

**Returns:** the array of strings computed by splitting this string
          around matches of the given regular expression

</details>
<details>
<summary><code>String[] splitWithDelimiters(String regex, int limit)</code></summary>

Splits this string around matches of the given regular expression and
 returns both the strings and the matching delimiters.

 <p> The array returned by this method contains each substring of this
 string that is terminated by another substring that matches the given
 expression or is terminated by the end of the string.
 Each substring is immediately followed by the subsequence (the delimiter)
 that matches the given expression, <em>except</em> for the last
 substring, which is not followed by anything.
 The substrings in the array and the delimiters are in the order in which
 they occur in the input.
 If the expression does not match any part of the input then the resulting
 array has just one element, namely this string.

 <p> When there is a positive-width match at the beginning of this
 string then an empty leading substring is included at the beginning
 of the resulting array. A zero-width match at the beginning however
 never produces such empty leading substring nor the empty delimiter.

 <p> The <code>limit</code> parameter controls the number of times the
 pattern is applied and therefore affects the length of the resulting
 array.
 <ul>
    <li> If the <i>limit</i> is positive then the pattern will be applied
    at most <i>limit</i>&nbsp;-&nbsp;1 times, the array's length will be
    no greater than 2 &times; <i>limit</i> - 1, and the array's last
    entry will contain all input beyond the last matched delimiter.</li>

    <li> If the <i>limit</i> is zero then the pattern will be applied as
    many times as possible, the array can have any length, and trailing
    empty strings will be discarded.</li>

    <li> If the <i>limit</i> is negative then the pattern will be applied
    as many times as possible and the array can have any length.</li>
 </ul>

 <p> The input <code>"boo:::and::foo"</code>, for example, yields the following
 results with these parameters:

 <table class="plain" style="margin-left:2em;">
 <caption style="display:none">Split example showing regex, limit, and result</caption>
 <thead>
 <tr>
     <th scope="col">Regex</th>
     <th scope="col">Limit</th>
     <th scope="col">Result</th>
 </tr>
 </thead>
 <tbody>
 <tr><th scope="row" rowspan="3" style="font-weight:normal">:+</th>
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">2</th>
     <td><code>{ "boo", ":::", "and::foo"</code>}</td></tr>
 <tr><!-- : -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
     <td><code>{ "boo", ":::", "and", "::", "foo"</code>}</td></tr>
 <tr><!-- : -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-1</th>
     <td><code>{ "boo", ":::", "and", "::", "foo"</code>}</td></tr>
 <tr><th scope="row" rowspan="3" style="font-weight:normal">o</th>
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">5</th>
     <td><code>{ "b", "o", "", "o", ":::and::f", "o", "", "o", ""</code>}</td></tr>
 <tr><!-- o -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">-1</th>
     <td><code>{ "b", "o", "", "o", ":::and::f", "o", "", "o", ""</code>}</td></tr>
 <tr><!-- o -->
     <th scope="row" style="font-weight:normal; text-align:right; padding-right:1em">0</th>
     <td><code>{ "b", "o", "", "o", ":::and::f", "o", "", "o"</code>}</td></tr>
 </tbody>
 </table>

**Parameters:**

* `regex` - the delimiting regular expression
* `limit` - the result threshold, as described above

**Returns:** the array of strings computed by splitting this string
          around matches of the given regular expression, alternating
          substrings and matching delimiters

</details>
<details>
<summary><code>String strip()</code></summary>

Returns a string whose value is this string, with all leading
 and trailing <code>white space</code>
 removed.
 <p>
 If this <code>String</code> object represents an empty string,
 or if all code points in this string are
 <code>white space</code>, then an empty string
 is returned.
 <p>
 Otherwise, returns a substring of this string beginning with the first
 code point that is not a <code>white space</code>
 up to and including the last code point that is not a
 <code>white space</code>.
 <p>
 This method may be used to strip
 <code>white space</code> from
 the beginning and end of a string.

**Returns:** a string whose value is this string, with all leading
          and trailing white space removed

</details>
<details>
<summary><code>String stripIndent()</code></summary>

Returns a string whose value is this string, with incidental
 <code>white space</code> removed from
 the beginning and end of every line.
 <p>
 Incidental <code>white space</code>
 is often present in a text block to align the content with the opening
 delimiter. For example, in the following code, dots represent incidental
 <code>white space</code>:
 <blockquote><pre>
 String html = """
 ..............&lt;html&gt;
 ..............    &lt;body&gt;
 ..............        &lt;p&gt;Hello, world&lt;/p&gt;
 ..............    &lt;/body&gt;
 ..............&lt;/html&gt;
 ..............""";
 </pre></blockquote>
 This method treats the incidental
 <code>white space</code> as indentation to be
 stripped, producing a string that preserves the relative indentation of
 the content. Using | to visualize the start of each line of the string:
 <blockquote><pre>
 |&lt;html&gt;
 |    &lt;body&gt;
 |        &lt;p&gt;Hello, world&lt;/p&gt;
 |    &lt;/body&gt;
 |&lt;/html&gt;
 </pre></blockquote>
 First, the individual lines of this string are extracted. A <i>line</i>
 is a sequence of zero or more characters followed by either a line
 terminator or the end of the string.
 If the string has at least one line terminator, the last line consists
 of the characters between the last terminator and the end of the string.
 Otherwise, if the string has no terminators, the last line is the start
 of the string to the end of the string, in other words, the entire
 string.
 A line does not include the line terminator.
 <p>
 Then, the <i>minimum indentation</i> (min) is determined as follows:
 <ul>
   <li><p>For each non-blank line (as defined by <code>String#isBlank()</code>),
   the leading <code>white space</code>
   characters are counted.</p>
   </li>
   <li><p>The leading <code>white space</code>
   characters on the last line are also counted even if
   <code>blank</code>.</p>
   </li>
 </ul>
 <p>The <i>min</i> value is the smallest of these counts.
 <p>
 For each <code>non-blank</code> line, <i>min</i> leading
 <code>white space</code> characters are
 removed, and any trailing <code>white
 space</code> characters are removed. <code>Blank</code> lines
 are replaced with the empty string.

 <p>
 Finally, the lines are joined into a new string, using the LF character
 <code>"\n"</code> (U+000A) to separate lines.

**Returns:** string with incidental indentation removed and line
         terminators normalized

</details>
<details>
<summary><code>String stripLeading()</code></summary>

Returns a string whose value is this string, with all leading
 <code>white space</code> removed.
 <p>
 If this <code>String</code> object represents an empty string,
 or if all code points in this string are
 <code>white space</code>, then an empty string
 is returned.
 <p>
 Otherwise, returns a substring of this string beginning with the first
 code point that is not a <code>white space</code>
 up to and including the last code point of this string.
 <p>
 This method may be used to trim
 <code>white space</code> from
 the beginning of a string.

**Returns:** a string whose value is this string, with all leading white
          space removed

</details>
<details>
<summary><code>String stripTrailing()</code></summary>

Returns a string whose value is this string, with all trailing
 <code>white space</code> removed.
 <p>
 If this <code>String</code> object represents an empty string,
 or if all characters in this string are
 <code>white space</code>, then an empty string
 is returned.
 <p>
 Otherwise, returns a substring of this string beginning with the first
 code point of this string up to and including the last code point
 that is not a <code>white space</code>.
 <p>
 This method may be used to trim
 <code>white space</code> from
 the end of a string.

**Returns:** a string whose value is this string, with all trailing white
          space removed

</details>
<details>
<summary><code>CharSequence subSequence(int beginIndex, int endIndex)</code></summary>

Returns a character sequence that is a subsequence of this sequence.

 <p> An invocation of this method of the form

 <blockquote><pre>
 str.subSequence(begin,&nbsp;end)</pre></blockquote>

 behaves in exactly the same way as the invocation

 <blockquote><pre>
 str.substring(begin,&nbsp;end)</pre></blockquote>

**Parameters:**

* `beginIndex` - the begin index, inclusive.
* `endIndex` - the end index, exclusive.

**Returns:** the specified subsequence.

</details>
<details>
<summary><code>String substring(int beginIndex)</code></summary>

Returns a string that is a substring of this string. The
 substring begins with the character at the specified index and
 extends to the end of this string. <p>
 Examples:
 <blockquote><pre>
 "unhappy".substring(2) returns "happy"
 "Harbison".substring(3) returns "bison"
 "emptiness".substring(9) returns "" (an empty string)
 </pre></blockquote>

**Parameters:**

* `beginIndex` - the beginning index, inclusive.

**Returns:** the specified substring.

</details>
<details>
<summary><code>String substring(int beginIndex, int endIndex)</code></summary>

Returns a string that is a substring of this string. The
 substring begins at the specified <code>beginIndex</code> and
 extends to the character at index <code>endIndex - 1</code>.
 Thus the length of the substring is <code>endIndex-beginIndex</code>.
 <p>
 Examples:
 <blockquote><pre>
 "hamburger".substring(4, 8) returns "urge"
 "smiles".substring(1, 5) returns "mile"
 </pre></blockquote>

**Parameters:**

* `beginIndex` - the beginning index, inclusive.
* `endIndex` - the ending index, exclusive.

**Returns:** the specified substring.

</details>
<details>
<summary><code>char[] toCharArray()</code></summary>

Converts this string to a new character array.

**Returns:** a newly allocated character array whose length is the length
          of this string and whose contents are initialized to contain
          the character sequence represented by this string.

</details>
<details>
<summary><code>String toLowerCase()</code></summary>

Converts all of the characters in this <code>String</code> to lower
 case using the rules of the default locale. This method is equivalent to
 <code>toLowerCase(Locale.getDefault())</code>.

**Returns:** the <code>String</code>, converted to lowercase.

</details>
<details>
<summary><code>String toLowerCase(Locale locale)</code></summary>

Converts all of the characters in this <code>String</code> to lower
 case using the rules of the given <code>Locale</code>.  Case mapping is based
 on the Unicode Standard version specified by the <code>Character</code>
 class. Since case mappings are not always 1:1 char mappings, the resulting <code>String</code>
 and this <code>String</code> may differ in length.
 <p>
 Examples of lowercase mappings are in the following table:
 <table class="plain">
 <caption style="display:none">Lowercase mapping examples showing language code of locale, upper case, lower case, and description</caption>
 <thead>
 <tr>
   <th scope="col">Language Code of Locale</th>
   <th scope="col">Upper Case</th>
   <th scope="col">Lower Case</th>
   <th scope="col">Description</th>
 </tr>
 </thead>
 <tbody>
 <tr>
   <td>tr (Turkish)</td>
   <th scope="row" style="font-weight:normal; text-align:left">&#92;u0130</th>
   <td>&#92;u0069</td>
   <td>capital letter I with dot above -&gt; small letter i</td>
 </tr>
 <tr>
   <td>tr (Turkish)</td>
   <th scope="row" style="font-weight:normal; text-align:left">&#92;u0049</th>
   <td>&#92;u0131</td>
   <td>capital letter I -&gt; small letter dotless i </td>
 </tr>
 <tr>
   <td>(all)</td>
   <th scope="row" style="font-weight:normal; text-align:left">French Fries</th>
   <td>french fries</td>
   <td>lowercased all chars in String</td>
 </tr>
 <tr>
   <td>(all)</td>
   <th scope="row" style="font-weight:normal; text-align:left">
       &Iota;&Chi;&Theta;&Upsilon;&Sigma;</th>
   <td>&iota;&chi;&theta;&upsilon;&sigma;</td>
   <td>lowercased all chars in String</td>
 </tr>
 </tbody>
 </table>

**Parameters:**

* `locale` - use the case transformation rules for this locale

**Returns:** the <code>String</code>, converted to lowercase.

</details>
<details>
<summary><code>String toString()</code></summary>

This object (which is already a string!) is itself returned.

**Returns:** the string itself.

</details>
<details>
<summary><code>String toUpperCase()</code></summary>

Converts all of the characters in this <code>String</code> to upper
 case using the rules of the default locale. This method is equivalent to
 <code>toUpperCase(Locale.getDefault())</code>.

**Returns:** the <code>String</code>, converted to uppercase.

</details>
<details>
<summary><code>String toUpperCase(Locale locale)</code></summary>

Converts all of the characters in this <code>String</code> to upper
 case using the rules of the given <code>Locale</code>. Case mapping is based
 on the Unicode Standard version specified by the <code>Character</code>
 class. Since case mappings are not always 1:1 char mappings, the resulting <code>String</code>
 and this <code>String</code> may differ in length.
 <p>
 Examples of locale-sensitive and 1:M case mappings are in the following table:
 <table class="plain">
 <caption style="display:none">Examples of locale-sensitive and 1:M case mappings. Shows Language code of locale, lower case, upper case, and description.</caption>
 <thead>
 <tr>
   <th scope="col">Language Code of Locale</th>
   <th scope="col">Lower Case</th>
   <th scope="col">Upper Case</th>
   <th scope="col">Description</th>
 </tr>
 </thead>
 <tbody>
 <tr>
   <td>tr (Turkish)</td>
   <th scope="row" style="font-weight:normal; text-align:left">&#92;u0069</th>
   <td>&#92;u0130</td>
   <td>small letter i -&gt; capital letter I with dot above</td>
 </tr>
 <tr>
   <td>tr (Turkish)</td>
   <th scope="row" style="font-weight:normal; text-align:left">&#92;u0131</th>
   <td>&#92;u0049</td>
   <td>small letter dotless i -&gt; capital letter I</td>
 </tr>
 <tr>
   <td>(all)</td>
   <th scope="row" style="font-weight:normal; text-align:left">&#92;u00df</th>
   <td>&#92;u0053 &#92;u0053</td>
   <td>small letter sharp s -&gt; two letters: SS</td>
 </tr>
 <tr>
   <td>(all)</td>
   <th scope="row" style="font-weight:normal; text-align:left">Fahrvergn&uuml;gen</th>
   <td>FAHRVERGN&Uuml;GEN</td>
   <td></td>
 </tr>
 </tbody>
 </table>

**Parameters:**

* `locale` - use the case transformation rules for this locale

**Returns:** the <code>String</code>, converted to uppercase.

</details>
<details>
<summary><code>&lt;R&gt; R transform(Function&lt;? super String, ? extends R&gt; f)</code></summary>

This method allows the application of a function to <code>this</code>
 string. The function should expect a single String argument
 and produce an <code>R</code> result.
 <p>
 Any exception thrown by <code>f.apply()</code> will be propagated to the
 caller.

**Parameters:**

* `f` - a function to apply

**Returns:** the result of applying the function to this string

</details>
<details>
<summary><code>String translateEscapes()</code></summary>

Returns a string whose value is this string, with escape sequences
 translated as if in a string literal.
 <p>
 Escape sequences are translated as follows;
 <table class="striped">
   <caption style="display:none">Translation</caption>
   <thead>
   <tr>
     <th scope="col">Escape</th>
     <th scope="col">Name</th>
     <th scope="col">Translation</th>
   </tr>
   </thead>
   <tbody>
   <tr>
     <th scope="row"><code>\b</code></th>
     <td>backspace</td>
     <td><code>U+0008</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\t</code></th>
     <td>horizontal tab</td>
     <td><code>U+0009</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\n</code></th>
     <td>line feed</td>
     <td><code>U+000A</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\f</code></th>
     <td>form feed</td>
     <td><code>U+000C</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\r</code></th>
     <td>carriage return</td>
     <td><code>U+000D</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\s</code></th>
     <td>space</td>
     <td><code>U+0020</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\"</code></th>
     <td>double quote</td>
     <td><code>U+0022</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\'</code></th>
     <td>single quote</td>
     <td><code>U+0027</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\\</code></th>
     <td>backslash</td>
     <td><code>U+005C</code></td>
   </tr>
   <tr>
     <th scope="row"><code>\0 - \377</code></th>
     <td>octal escape</td>
     <td>code point equivalents</td>
   </tr>
   <tr>
     <th scope="row"><code>\&lt;line-terminator&gt;</code></th>
     <td>continuation</td>
     <td>discard</td>
   </tr>
   </tbody>
 </table>

**Returns:** String with escape sequences translated.

</details>
<details>
<summary><code>static String valueOf(Object obj)</code></summary>

Returns the string representation of the <code>Object</code> argument.

**Parameters:**

* `obj` - an <code>Object</code>.

**Returns:** if the argument is <code>null</code>, then a string equal to
          <code>"null"</code>; otherwise, the value of
          <code>obj.toString()</code> is returned.

</details>
<details>
<summary><code>static String valueOf(boolean b)</code></summary>

Returns the string representation of the <code>boolean</code> argument.

**Parameters:**

* `b` - a <code>boolean</code>.

**Returns:** if the argument is <code>true</code>, a string equal to
          <code>"true"</code> is returned; otherwise, a string equal to
          <code>"false"</code> is returned.

</details>
<details>
<summary><code>static String valueOf(char c)</code></summary>

Returns the string representation of the <code>char</code>
 argument.

**Parameters:**

* `c` - a <code>char</code>.

**Returns:** a string of length <code>1</code> containing
          as its single character the argument <code>c</code>.

</details>
<details>
<summary><code>static String valueOf(char[] data)</code></summary>

Returns the string representation of the <code>char</code> array
 argument. The contents of the character array are copied; subsequent
 modification of the character array does not affect the returned
 string.

**Parameters:**

* `data` - the character array.

**Returns:** a <code>String</code> that contains the characters of the
          character array.

</details>
<details>
<summary><code>static String valueOf(char[] data, int offset, int count)</code></summary>

Returns the string representation of a specific subarray of the
 <code>char</code> array argument.
 <p>
 The <code>offset</code> argument is the index of the first
 character of the subarray. The <code>count</code> argument
 specifies the length of the subarray. The contents of the subarray
 are copied; subsequent modification of the character array does not
 affect the returned string.

**Parameters:**

* `data` - the character array.
* `offset` - initial offset of the subarray.
* `count` - length of the subarray.

**Returns:** a <code>String</code> that contains the characters of the
          specified subarray of the character array.

</details>
<details>
<summary><code>static String valueOf(double d)</code></summary>

Returns the string representation of the <code>double</code> argument.
 <p>
 The representation is exactly the one returned by the
 <code>Double.toString</code> method of one argument.

**Parameters:**

* `d` - a <code>double</code>.

**Returns:** a  string representation of the <code>double</code> argument.

</details>
<details>
<summary><code>static String valueOf(float f)</code></summary>

Returns the string representation of the <code>float</code> argument.
 <p>
 The representation is exactly the one returned by the
 <code>Float.toString</code> method of one argument.

**Parameters:**

* `f` - a <code>float</code>.

**Returns:** a string representation of the <code>float</code> argument.

</details>
<details>
<summary><code>static String valueOf(int i)</code></summary>

Returns the string representation of the <code>int</code> argument.
 <p>
 The representation is exactly the one returned by the
 <code>Integer.toString</code> method of one argument.

**Parameters:**

* `i` - an <code>int</code>.

**Returns:** a string representation of the <code>int</code> argument.

</details>
<details>
<summary><code>static String valueOf(long l)</code></summary>

Returns the string representation of the <code>long</code> argument.
 <p>
 The representation is exactly the one returned by the
 <code>Long.toString</code> method of one argument.

**Parameters:**

* `l` - a <code>long</code>.

**Returns:** a string representation of the <code>long</code> argument.

</details>




