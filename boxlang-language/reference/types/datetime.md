
# Type: `Datetime`

The primary DateTime class that represents a date and time object in BoxLang

 All temporal methods in BoxLang operate on this class and all castable date/time representations are cast to this class

## Datetime Methods

<details>
<summary><code>add(datepart=[string], number=[number])</code></summary>

Modifies a date object by date part and integer time unit

### Method Signature

```
add(datepart=[string], number=[number])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `datepart` | `string` | `true` | The date part to modify |  |
| `number` | `number` | `true` | The number of units to modify by |  |
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
<summary><code>clone()</code></summary>

No description available

### Method Signature

```
clone()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>compare(date2=[any], datepart=[string])</code></summary>

Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

### Method Signature

```
compare(date2=[any], datepart=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date2` | `any` | `true` | The date which to compare against date1 |  |
| `datepart` | `string` | `false` | The precision to compare down to. Accepts y, yyyy, m, d, h, n, s (default). |  |
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
<summary><code>diff(datepart=[string], date2=[any])</code></summary>

Returns the numeric difference in the requested date part between two dates

### Method Signature

```
diff(datepart=[string], date2=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `datepart` | `string` | `true` | The datepart code in which to express the difference (yyyy, q, m, d, y, w, ww, wd, h, n, s, l). |  |
| `date2` | `any` | `true` | The date which to compare against date1 |  |
</details>
<details>
<summary><code>duplicate(deep=[boolean])</code></summary>

Duplicates an object - either shallow or deep

### Method Signature

```
duplicate(deep=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `deep` | `boolean` | `false` | Whether to deep copy the object or make a shallow copy (e.g. only the top level keys in a struct) | `true` |
</details>
<details>
<summary><code>equals(obj=[any])</code></summary>

Indicates whether some other object is "equal to" this one.

### Method Signature

```
equals(obj=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `obj` | `any` | `true` |  |  |
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
<summary><code>format(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

### Method Signature

```
format(mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |
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
<summary><code>getTime()</code></summary>

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT represented by this Date object.

### Method Signature

```
getTime()
```

### Arguments

This function does not accept any arguments
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
<summary><code>setDay(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setDay(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
</details>
<details>
<summary><code>setHour(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setHour(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
</details>
<details>
<summary><code>setMinute(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setMinute(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
</details>
<details>
<summary><code>setMonth(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setMonth(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
</details>
<details>
<summary><code>setSecond(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setSecond(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
</details>
<details>
<summary><code>setYear(value=[integer])</code></summary>

Sets a single date/time unit on a date object, mutating it in place and returning it.

Out-of-range values roll over (e.g. <code>setDay( 50 )</code> advances into following months) while
 zero/negative values clamp to the first valid unit (e.g. <code>setDay( 0 )</code> becomes day 1).

### Method Signature

```
setYear(value=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `integer` | `true` | The value to set for the given date/time unit |  |
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
<summary><code>toEpoch()</code></summary>

Returns this date time in epoch time ( seconds )

### Method Signature

```
toEpoch()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toEpochMillis()</code></summary>

Returns this date time in epoch milliseconds

### Method Signature

```
toEpochMillis()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toEpochSecond()</code></summary>

No description available

### Method Signature

```
toEpochSecond()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toISOString()</code></summary>

Returns the date time representation as a string in the specified format mask

### Method Signature

```
toISOString()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toODBCDate(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

### Method Signature

```
toODBCDate(timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone to apply |  |
</details>
<details>
<summary><code>toODBCDateTime(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

### Method Signature

```
toODBCDateTime(timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone to apply |  |
</details>
<details>
<summary><code>toODBCTime(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

### Method Signature

```
toODBCTime(timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | An optional timezone to apply |  |
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






