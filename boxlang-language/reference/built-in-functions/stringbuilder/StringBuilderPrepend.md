[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderPrepend`

Inserts the string representation of value at the beginning (position 1) of the buffer.

## Method Signature

```
StringBuilderPrepend(stringBuilder=[stringBuilder], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to prepend to. |  |
| `value` | `any` | `true` | The value to insert at the start. Coerced to string. |  |

## Examples

### Prepend text with stringBuilderPrepend()

Adds text to the beginning of a StringBuilder and returns the same instance.

```java
sb = sb{'World'};
stringBuilderPrepend( sb, 'Hello ' );
writeOutput( sb.toString() );
```

Result: Hello World

### Member usage

```java
sb = sb{'World'};
sb.prepend( 'Hello ' );
writeOutput( sb.toString() );
```

Result: Hello World

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
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
