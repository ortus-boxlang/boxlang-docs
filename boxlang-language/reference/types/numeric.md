
# Type: `Numeric`

In BoxLang, the `numeric` type is represented by the native Java class `java.lang.Number`. The member functions below are provided by the BoxLang runtime and can be called directly on the value, in addition to the methods of the underlying Java class.

The abstract class <code>Number</code> is the superclass of platform
 classes representing numeric values that are convertible to the
 primitive types <code>byte</code>, <code>double</code>, <code>float</code>, <code>int</code>, <code>long</code>, and <code>short</code>.

## Numeric Methods

<details>
<summary><code>abs()</code></summary>

Returns the absolute value of a number

### Method Signature

```
abs()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>acos()</code></summary>

Returns the arccosine (inverse cosine) of a number

### Method Signature

```
acos()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>asin()</code></summary>

Returns the arcsine (inverse sine) of a number

### Method Signature

```
asin()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>atn()</code></summary>

Returns the arc tangent (inverse tangent) of a number

### Method Signature

```
atn()
```

### Arguments

This function does not accept any arguments
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
<summary><code>ceiling()</code></summary>

Determines the closest integer that is greater than a specified floating point number.

### Method Signature

```
ceiling()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>cos()</code></summary>

Returns the cosine of an angle entered in radians

### Method Signature

```
cos()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>currencyFormat(type=[string], locale=[string])</code></summary>

No description available

### Method Signature

```
currencyFormat(type=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` |  | `local` |
| `locale` | `string` | `false` |  |  |
</details>
<details>
<summary><code>decimalFormat(length=[integer])</code></summary>

Converts a number to a decimal-formatted string.

### Method Signature

```
decimalFormat(length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `length` | `integer` | `false` | The number of decimal places to include in the formatted string. | `2` |
</details>
<details>
<summary><code>decrementValue()</code></summary>

Decrement the integer part of a number

### Method Signature

```
decrementValue()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>exp()</code></summary>

Calculates the exponent whose base is e that represents a number.

### Method Signature

```
exp()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>fix()</code></summary>

Converts a real number to an integer

### Method Signature

```
fix()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>floor()</code></summary>

Round a number down to the nearest integer

### Method Signature

```
floor()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>formatBaseN(radix=[integerTruncate])</code></summary>

Converts a number to a string representation in the specified base.

### Method Signature

```
formatBaseN(radix=[integerTruncate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `radix` | `integerTruncate` | `true` | The base to convert the number to, in the range 2-36. |  |
</details>
<details>
<summary><code>incrementValue()</code></summary>

Increment the integer part of a number

### Method Signature

```
incrementValue()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>int()</code></summary>

Returns the closest integer that is smaller than the number

### Method Signature

```
int()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>log()</code></summary>

Returns the natural logarithm of a number.

### Method Signature

```
log()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>log10()</code></summary>

No description available

### Method Signature

```
log10()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>max(number2=[numeric])</code></summary>

Return larger of two numbers

### Method Signature

```
max(number2=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number2` | `numeric` | `true` | The second number |  |
</details>
<details>
<summary><code>min(number2=[numeric])</code></summary>

Return larger of two numbers

### Method Signature

```
min(number2=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number2` | `numeric` | `true` | The second number |  |
</details>
<details>
<summary><code>numberFormat(mask=[string], locale=[string])</code></summary>

Formats a number with an optional format mask

### Method Signature

```
numberFormat(mask=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `mask` | `string` | `false` | The formatting mask to apply using the <code>java.text.DecimalFormat</code> patterns. |  |
| `locale` | `string` | `false` | An optional locale string to apply to the format |  |
</details>
<details>
<summary><code>round(precision=[integer])</code></summary>

Rounds a number to the closest integer.

### Method Signature

```
round(precision=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `precision` | `integer` | `false` | The number of decimal places to round to (default is 0). | `0` |
</details>
<details>
<summary><code>sgn()</code></summary>

Determine the sign of a number

### Method Signature

```
sgn()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>sin()</code></summary>

Returns the sine of a number

### Method Signature

```
sin()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>sqr()</code></summary>

Returns the square root of a number

### Method Signature

```
sqr()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>tan()</code></summary>

Returns the tangent of an angle that is entered in radians.

### Method Signature

```
tan()
```

### Arguments

This function does not accept any arguments
</details>


## Java Methods

> **Use at your own risk:** These are the public methods of the native Java class `java.lang.Number`, documented from the JDK 21 javadocs. They are not part of the BoxLang API, are not tested or supported by BoxLang, and may change between Java versions.

<details>
<summary><code>byte byteValue()</code></summary>

Returns the value of the specified number as a <code>byte</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>byte</code>.

</details>
<details>
<summary><code>double doubleValue()</code></summary>

Returns the value of the specified number as a <code>double</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>double</code>.

</details>
<details>
<summary><code>float floatValue()</code></summary>

Returns the value of the specified number as a <code>float</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>float</code>.

</details>
<details>
<summary><code>int intValue()</code></summary>

Returns the value of the specified number as an <code>int</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>int</code>.

</details>
<details>
<summary><code>long longValue()</code></summary>

Returns the value of the specified number as a <code>long</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>long</code>.

</details>
<details>
<summary><code>short shortValue()</code></summary>

Returns the value of the specified number as a <code>short</code>.

**Returns:** the numeric value represented by this object after conversion
          to type <code>short</code>.

</details>




