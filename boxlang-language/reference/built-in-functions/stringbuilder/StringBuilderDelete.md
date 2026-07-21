[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderDelete`

Removes characters from start to end, both 1-based and inclusive.

## Method Signature

```
StringBuilderDelete(stringBuilder=[stringBuilder], start=[integer], end=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to delete from. |  |
| `start` | `integer` | `true` | The 1-based start position (inclusive). |  |
| `end` | `integer` | `true` | The 1-based end position (inclusive). |  |

## Examples

### Delete a range with stringBuilderDelete()

Removes characters using 1-based, inclusive start and end positions.

```java
sb = sb{'Hello World'};
stringBuilderDelete( sb, 6, 11 );
writeOutput( sb.toString() );
```

Result: Hello

### Member usage

```java
sb = sb{'Hello World'};
sb.delete( 6, 11 );
writeOutput( sb.toString() );
```

Result: Hello

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderEndsWith](./StringBuilderEndsWith.md)
  * [StringBuilderFind](./StringBuilderFind.md)
  * [StringBuilderInsert](./StringBuilderInsert.md)
  * [StringBuilderLeft](./StringBuilderLeft.md)
  * [StringBuilderMid](./StringBuilderMid.md)
  * [StringBuilderNew](./StringBuilderNew.md)
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
