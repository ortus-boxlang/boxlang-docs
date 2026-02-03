[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Numeric`



## Numeric Methods

<details>
<summary><code>sqr()</code></summary>

Returns the square root of a number
</details>
<details>
<summary><code>asin()</code></summary>

Returns the arcsine (inverse sine) of a number
</details>
<details>
<summary><code>sgn()</code></summary>

Determine the sign of a number
</details>
<details>
<summary><code>decrementValue()</code></summary>

Decrement the integer part of a number
</details>
<details>
<summary><code>round(precision=[integer])</code></summary>

Rounds a number to the closest integer.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `precision` | `integer` | `false` | `0` |

</details>
<details>
<summary><code>cos()</code></summary>

Returns the cosine of an angle entered in radians
</details>
<details>
<summary><code>int()</code></summary>

Returns the closest integer that is smaller than the number
</details>
<details>
<summary><code>exp()</code></summary>

Calculates the exponent whose base is e that represents a number.
</details>
<details>
<summary><code>ceiling()</code></summary>

Determines the closest integer that is greater than a specified floating point number.
</details>
<details>
<summary><code>atn()</code></summary>

Returns the arc tangent (inverse tangent) of a number
</details>
<details>
<summary><code>fix()</code></summary>

Converts a real number to an integer
</details>
<details>
<summary><code>max(number2=[numeric])</code></summary>

Return larger of two numbers

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `number2` | `numeric` | `true` | `null` |

</details>
<details>
<summary><code>min(number2=[numeric])</code></summary>

Return larger of two numbers

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `number2` | `numeric` | `true` | `null` |

</details>
<details>
<summary><code>abs()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>log()</code></summary>

Returns the natural logarithm of a number.
</details>
<details>
<summary><code>log10()</code></summary>

No description available
</details>
<details>
<summary><code>acos()</code></summary>

Returns the arccosine (inverse cosine) of a number
</details>
<details>
<summary><code>floor()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>formatBaseN(radix=[integerTruncate])</code></summary>

Converts a number to a string representation in the specified base.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `radix` | `integerTruncate` | `true` | `null` |

</details>
<details>
<summary><code>tan()</code></summary>

Returns the tangent of an angle that is entered in radians.
</details>
<details>
<summary><code>sin()</code></summary>

Returns the sine of a number
</details>
<details>
<summary><code>incrementValue()</code></summary>

Increment the integer part of a number
</details>
<details>
<summary><code>bxDump(label=[string], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>,
 The available ,<code>,output,</code>, locations are:
 - ,<strong>,buffer,</strong>,: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - ,<strong>,console,</strong>,: The output is printed to the System console.
 - ,<strong>,Absolute File Path,</strong>, The output is written to a file with the specified absolute file path.
 ,</p>,
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `label` | `string` | `false` | `null` |
| `top` | `numeric` | `false` | `null` |
| `expand` | `boolean` | `false` | `true` |
| `abort` | `boolean` | `false` | `false` |
| `output` | `string` | `false` | `null` |
| `format` | `string` | `false` | `null` |
| `showUDFs` | `boolean` | `false` | `true` |

</details>
<details>
<summary><code>decimalFormat(length=[integer])</code></summary>

Converts a number to a decimal-formatted string.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `length` | `integer` | `false` | `2` |

</details>
<details>
<summary><code>booleanFormat()</code></summary>

Returns the value formatted as a boolean string
</details>
<details>
<summary><code>numberFormat(mask=[string], locale=[string])</code></summary>

Formats a number with an optional format mask

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `null` |
| `locale` | `string` | `false` | `null` |

</details>
<details>
<summary><code>currencyFormat(type=[string], locale=[string])</code></summary>

nullArguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `type` | `string` | `false` | `local` |
| `locale` | `string` | `false` | `null` |

</details>


## Examples
