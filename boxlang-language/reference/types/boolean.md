
# Type: `Boolean`

In BoxLang, the `boolean` type is represented by the native Java class `java.lang.Boolean`. The member functions below are provided by the BoxLang runtime and can be called directly on the value, in addition to the methods of the underlying Java class.

The Boolean class wraps a value of the primitive type
 <code>boolean</code> in an object.

## Boolean Methods

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


## Java Methods

> **Use at your own risk:** These are the public methods of the native Java class `java.lang.Boolean`, documented from the JDK 21 javadocs. They are not part of the BoxLang API, are not tested or supported by BoxLang, and may change between Java versions.

<details>
<summary><code>boolean booleanValue()</code></summary>

Returns the value of this <code>Boolean</code> object as a boolean
 primitive.

**Returns:** the primitive <code>boolean</code> value of this object.

</details>
<details>
<summary><code>static int compare(boolean x, boolean y)</code></summary>

Compares two <code>boolean</code> values.
 The value returned is identical to what would be returned by:
 <pre>
    Boolean.valueOf(x).compareTo(Boolean.valueOf(y))
 </pre>

**Parameters:**

* `x` - the first <code>boolean</code> to compare
* `y` - the second <code>boolean</code> to compare

**Returns:** the value <code>0</code> if <code>x == y</code>;
         a value less than <code>0</code> if <code>!x &amp;&amp; y</code>; and
         a value greater than <code>0</code> if <code>x &amp;&amp; !y</code>

</details>
<details>
<summary><code>int compareTo(Boolean b)</code></summary>

Compares this <code>Boolean</code> instance with another.

**Parameters:**

* `b` - the <code>Boolean</code> instance to be compared

**Returns:** zero if this object represents the same boolean value as the
          argument; a positive value if this object represents true
          and the argument represents false; and a negative value if
          this object represents false and the argument represents true

</details>
<details>
<summary><code>Optional&lt;DynamicConstantDesc&lt;Boolean&gt;&gt; describeConstable()</code></summary>

Returns an <code>Optional</code> containing the nominal descriptor for this
 instance.

**Returns:** an <code>Optional</code> describing the <code>Boolean</code> instance

</details>
<details>
<summary><code>boolean equals(Object obj)</code></summary>

Returns <code>true</code> if and only if the argument is not
 <code>null</code> and is a <code>Boolean</code> object that
 represents the same <code>boolean</code> value as this object.

**Parameters:**

* `obj` - the object to compare with.

**Returns:** <code>true</code> if the Boolean objects represent the
          same value; <code>false</code> otherwise.

</details>
<details>
<summary><code>static boolean getBoolean(String name)</code></summary>

Returns <code>true</code> if and only if the system property named
 by the argument exists and is equal to, ignoring case, the
 string <code>"true"</code>.
 A system property is accessible through <code>getProperty</code>, a
 method defined by the <code>System</code> class.  <p> If there is no
 property with the specified name, or if the specified name is
 empty or null, then <code>false</code> is returned.

**Parameters:**

* `name` - the system property name.

**Returns:** the <code>boolean</code> value of the system property.

</details>
<details>
<summary><code>int hashCode()</code></summary>

Returns a hash code for this <code>Boolean</code> object.

**Returns:** the integer <code>1231</code> if this object represents
 <code>true</code>; returns the integer <code>1237</code> if this
 object represents <code>false</code>.

</details>
<details>
<summary><code>static int hashCode(boolean value)</code></summary>

Returns a hash code for a <code>boolean</code> value; compatible with
 <code>Boolean.hashCode()</code>.

**Parameters:**

* `value` - the value to hash

**Returns:** a hash code value for a <code>boolean</code> value.

</details>
<details>
<summary><code>static boolean logicalAnd(boolean a, boolean b)</code></summary>

Returns the result of applying the logical AND operator to the
 specified <code>boolean</code> operands.

**Parameters:**

* `a` - the first operand
* `b` - the second operand

**Returns:** the logical AND of <code>a</code> and <code>b</code>

</details>
<details>
<summary><code>static boolean logicalOr(boolean a, boolean b)</code></summary>

Returns the result of applying the logical OR operator to the
 specified <code>boolean</code> operands.

**Parameters:**

* `a` - the first operand
* `b` - the second operand

**Returns:** the logical OR of <code>a</code> and <code>b</code>

</details>
<details>
<summary><code>static boolean logicalXor(boolean a, boolean b)</code></summary>

Returns the result of applying the logical XOR operator to the
 specified <code>boolean</code> operands.

**Parameters:**

* `a` - the first operand
* `b` - the second operand

**Returns:** the logical XOR of <code>a</code> and <code>b</code>

</details>
<details>
<summary><code>static boolean parseBoolean(String s)</code></summary>

Parses the string argument as a boolean.  The <code>boolean</code>
 returned represents the value <code>true</code> if the string argument
 is not <code>null</code> and is equal, ignoring case, to the string
 <code>"true"</code>.
 Otherwise, a false value is returned, including for a null
 argument.<p>
 Example: <code>Boolean.parseBoolean("True")</code> returns <code>true</code>.<br>
 Example: <code>Boolean.parseBoolean("yes")</code> returns <code>false</code>.

**Parameters:**

* `s` - the <code>String</code> containing the boolean
                 representation to be parsed

**Returns:** the boolean represented by the string argument

</details>
<details>
<summary><code>String toString()</code></summary>

Returns a <code>String</code> object representing this Boolean's
 value.  If this object represents the value <code>true</code>,
 a string equal to <code>"true"</code> is returned. Otherwise, a
 string equal to <code>"false"</code> is returned.

**Returns:** a string representation of this object.

</details>
<details>
<summary><code>static String toString(boolean b)</code></summary>

Returns a <code>String</code> object representing the specified
 boolean.  If the specified boolean is <code>true</code>, then
 the string <code>"true"</code> will be returned, otherwise the
 string <code>"false"</code> will be returned.

**Parameters:**

* `b` - the boolean to be converted

**Returns:** the string representation of the specified <code>boolean</code>

</details>
<details>
<summary><code>static Boolean valueOf(String s)</code></summary>

Returns a <code>Boolean</code> with a value represented by the
 specified string.  The <code>Boolean</code> returned represents a
 true value if the string argument is not <code>null</code>
 and is equal, ignoring case, to the string <code>"true"</code>.
 Otherwise, a false value is returned, including for a null
 argument.

**Parameters:**

* `s` - a string.

**Returns:** the <code>Boolean</code> value represented by the string.

</details>
<details>
<summary><code>static Boolean valueOf(boolean b)</code></summary>

Returns a <code>Boolean</code> instance representing the specified
 <code>boolean</code> value.  If the specified <code>boolean</code> value
 is <code>true</code>, this method returns <code>Boolean.TRUE</code>;
 if it is <code>false</code>, this method returns <code>Boolean.FALSE</code>.
 If a new <code>Boolean</code> instance is not required, this method
 should generally be used in preference to the constructor
 <code>#Boolean(boolean)</code>, as this method is likely to yield
 significantly better space and time performance.

**Parameters:**

* `b` - a boolean value.

**Returns:** a <code>Boolean</code> instance representing <code>b</code>.

</details>


## Examples


