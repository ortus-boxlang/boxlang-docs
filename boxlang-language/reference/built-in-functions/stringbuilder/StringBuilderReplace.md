[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderReplace`

Replaces characters from start to end (1-based, inclusive) with value.

## Method Signature

```
StringBuilderReplace(stringBuilder=[stringBuilder], start=[integer], end=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to modify. |  |
| `start` | `integer` | `true` | The 1-based start position (inclusive). |  |
| `end` | `integer` | `true` | The 1-based end position (inclusive). |  |
| `value` | `any` | `true` | The replacement text. Coerced to string. |  |

## Examples

### Replace a range with stringBuilderReplace()

Replaces characters using 1-based, inclusive start and end positions.

```java
sb = sb{'Hello World'};
stringBuilderReplace( sb, 7, 11, 'BoxLang' );
writeOutput( sb.toString() );
```

Result: Hello BoxLang

### Member usage

```java
sb = sb{'Hello World'};
sb.replace( 7, 11, 'BoxLang' );
writeOutput( sb.toString() );
```

Result: Hello BoxLang

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderDelete](./StringBuilderDelete.md)
  * [StringBuilderEndsWith](./StringBuilderEndsWith.md)
  * [StringBuilderFind](./StringBuilderFind.md)
  * [StringBuilderInsert](./StringBuilderInsert.md)
  * [StringBuilderLeft](./StringBuilderLeft.md)
  * [StringBuilderMid](./StringBuilderMid.md)
  * [StringBuilderNew](./StringBuilderNew.md)
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
