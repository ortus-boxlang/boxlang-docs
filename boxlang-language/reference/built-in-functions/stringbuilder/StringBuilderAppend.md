[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderAppend`

Appends the string representation of value to the end of the StringBuilder buffer.

## Method Signature

```
StringBuilderAppend(stringBuilder=[stringBuilder], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to append to. |  |
| `value` | `any` | `true` | The value to append. Coerced to string. |  |

## Examples

### Append text with stringBuilderAppend()

Appends text to the end of a StringBuilder and returns the same instance.

```java
sb = sb{'Hello'};
stringBuilderAppend( sb, ' World' );
writeOutput( sb.toString() );
```

Result: Hello World

### Use append() as a member function

```java
result = sb{"foo"}
    .append( 'bar' )
    .append( 'baz' )
    .toString();
writeOutput( result );
```

Result: foobarbaz

## Related

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
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
