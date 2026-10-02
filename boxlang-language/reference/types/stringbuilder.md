
# Type: `StringBuilder`

BoxLang first-class <code>StringBuilder</code> type.

<p>
 Wraps <code>java.lang.StringBuilder</code> and exposes a fluent, mutable string-buffer API
 to BoxLang code. All positional parameters are <em>1-based</em> (BoxLang convention);
 the wrapper subtracts/adds 1 before delegating to the underlying buffer.

 <p>
 A <code>BoxStringBuilder</code> silently casts to <code>String</code> anywhere the runtime needs
 a string — via <code>ortus.boxlang.runtime.dynamic.casters.StringCasterStrict</code>. This
 allows all existing string BIFs and member methods to operate on an <code>sb</code> value
 without any explicit conversion.

 <p>
 Create instances via:
 <ul>
 <li>Literal: <code>sb{"initial value"</code>} or <code>stringbuilder{"initial value"</code>} (Box parser only)</li>
 <li>BIF: <code>stringBuilderNew()</code> or <code>stringBuilderNew("initial", 128)</code></li>
 </ul>

## StringBuilder Methods

<details>
<summary><code>append(value=[any])</code></summary>

Appends the string representation of value to the end of the StringBuilder buffer.

### Method Signature

```
append(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to append. Coerced to string. |  |
</details>
<details>
<summary><code>clear()</code></summary>

Resets the StringBuilder buffer to empty.

### Method Signature

```
clear()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>contains(substring=[string])</code></summary>

No description available

### Method Signature

```
contains(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
</details>
<details>
<summary><code>containsNoCase(substring=[string])</code></summary>

No description available

### Method Signature

```
containsNoCase(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
</details>
<details>
<summary><code>delete(start=[integer], end=[integer])</code></summary>

Removes characters from start to end, both 1-based and inclusive.

### Method Signature

```
delete(start=[integer], end=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The 1-based start position (inclusive). |  |
| `end` | `integer` | `true` | The 1-based end position (inclusive). |  |
</details>
<details>
<summary><code>endsWith(substring=[string])</code></summary>

No description available

### Method Signature

```
endsWith(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
</details>
<details>
<summary><code>find(substring=[string], start=[integer])</code></summary>

No description available

### Method Signature

```
find(substring=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
| `start` | `integer` | `false` |  | `1` |
</details>
<details>
<summary><code>findNoCase(substring=[string], start=[integer])</code></summary>

No description available

### Method Signature

```
findNoCase(substring=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
| `start` | `integer` | `false` |  | `1` |
</details>
<details>
<summary><code>insert(position=[integer], value=[any])</code></summary>

Inserts value at the given 1-based position in the StringBuilder buffer.

### Method Signature

```
insert(position=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` | The 1-based character position at which to insert. |  |
| `value` | `any` | `true` | The value to insert. Coerced to string. |  |
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
<summary><code>left(count=[integer])</code></summary>

No description available

### Method Signature

```
left(count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `count` | `integer` | `true` |  |  |
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
<summary><code>mid(start=[integer], count=[integer])</code></summary>

No description available

### Method Signature

```
mid(start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` |  |  |
| `count` | `integer` | `false` |  |  |
</details>
<details>
<summary><code>prepend(value=[any])</code></summary>

Inserts the string representation of value at the beginning (position 1) of the buffer.

### Method Signature

```
prepend(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to insert at the start. Coerced to string. |  |
</details>
<details>
<summary><code>replace(start=[integer], end=[integer], value=[any])</code></summary>

Replaces characters from start to end (1-based, inclusive) with value.

### Method Signature

```
replace(start=[integer], end=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The 1-based start position (inclusive). |  |
| `end` | `integer` | `true` | The 1-based end position (inclusive). |  |
| `value` | `any` | `true` | The replacement text. Coerced to string. |  |
</details>
<details>
<summary><code>reverse()</code></summary>

Reverses the contents of the StringBuilder buffer in place.

### Method Signature

```
reverse()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>right(count=[integer])</code></summary>

No description available

### Method Signature

```
right(count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `count` | `integer` | `true` |  |  |
</details>
<details>
<summary><code>startsWith(substring=[string])</code></summary>

No description available

### Method Signature

```
startsWith(substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` |  |  |
</details>
<details>
<summary><code>trim()</code></summary>

Strips leading and trailing whitespace from the buffer in place.

### Method Signature

```
trim()
```

### Arguments

This function does not accept any arguments
</details>


## Java Methods

> **Use at your own risk:** These are the public methods of the native Java class `java.lang.StringBuilder`, documented from the JDK 21 javadocs. They are not part of the BoxLang API, are not tested or supported by BoxLang, and may change between Java versions. Java methods with the same name as one of the BoxLang member functions above are not listed, as the BoxLang member function is called instead.

<details>
<summary><code>StringBuilder appendCodePoint(int codePoint)</code></summary>



</details>
<details>
<summary><code>int compareTo(StringBuilder another)</code></summary>

Compares two <code>StringBuilder</code> instances lexicographically. This method
 follows the same rules for lexicographical comparison as defined in the
 <code>java.lang.CharSequence) CharSequence.compare(this, another)</code> method.

 <p>
 For finer-grained, locale-sensitive String comparison, refer to
 <code>java.text.Collator</code>.

**Parameters:**

* `another` - the <code>StringBuilder</code> to be compared with

**Returns:** the value <code>0</code> if this <code>StringBuilder</code> contains the same
 character sequence as that of the argument <code>StringBuilder</code>; a negative integer
 if this <code>StringBuilder</code> is lexicographically less than the
 <code>StringBuilder</code> argument; or a positive integer if this <code>StringBuilder</code>
 is lexicographically greater than the <code>StringBuilder</code> argument.

</details>
<details>
<summary><code>StringBuilder deleteCharAt(int index)</code></summary>



</details>
<details>
<summary><code>int indexOf(String str)</code></summary>

Returns the index within this string of the first occurrence of the
 specified substring.

 <p>The returned index is the smallest value <code>k</code> for which:
 <pre><code>this.toString().startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.

**Returns:** the index of the first occurrence of the specified substring,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int indexOf(String str, int fromIndex)</code></summary>

Returns the index within this string of the first occurrence of the
 specified substring, starting at the specified index.

 <p>The returned index is the smallest value <code>k</code> for which:
 <pre><code>k &gt;= Math.min(fromIndex, this.length()) &amp;&amp;
                   this.toString().startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.
* `fromIndex` - the index from which to start the search.

**Returns:** the index of the first occurrence of the specified substring,
          starting at the specified index,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>int lastIndexOf(String str)</code></summary>

Returns the index within this string of the last occurrence of the
 specified substring.  The last occurrence of the empty string "" is
 considered to occur at the index value <code>this.length()</code>.

 <p>The returned index is the largest value <code>k</code> for which:
 <pre><code>this.toString().startsWith(str, k)</code></pre>
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
                   this.toString().startsWith(str, k)</code></pre>
 If no such value of <code>k</code> exists, then <code>-1</code> is returned.

**Parameters:**

* `str` - the substring to search for.
* `fromIndex` - the index to start the search from.

**Returns:** the index of the last occurrence of the specified substring,
          searching backward from the specified index,
          or <code>-1</code> if there is no such occurrence.

</details>
<details>
<summary><code>StringBuilder repeat(CharSequence cs, int count)</code></summary>



</details>
<details>
<summary><code>StringBuilder repeat(int codePoint, int count)</code></summary>



</details>
<details>
<summary><code>String toString()</code></summary>

Returns a string representing the data in this sequence.
 A new <code>String</code> object is allocated and initialized to
 contain the character sequence currently represented by this
 object. This <code>String</code> is then returned. Subsequent
 changes to this sequence do not affect the contents of the
 <code>String</code>.

**Returns:** a string representation of this sequence of characters.

</details>


## Examples


