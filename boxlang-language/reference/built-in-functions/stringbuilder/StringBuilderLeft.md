[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderLeft`

No description available.

## Method Signature

```
StringBuilderLeft(stringBuilder=[stringBuilder], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` |  |  |
| `count` | `integer` | `true` |  |  |

## Examples

### Get left characters with left()

Returns the leftmost characters from a StringBuilder.

```java
sb = sb{'The quick brown fox'};
result = sb.left( 9 );
writeOutput( result );
```

Result: The quick

### Headless usage

```java
sb = sb{'BoxLang'};
writeOutput( left( sb, 3 ) );
```

Result: Box

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderDelete](./StringBuilderDelete.md)
  * [StringBuilderEndsWith](./StringBuilderEndsWith.md)
  * [StringBuilderFind](./StringBuilderFind.md)
  * [StringBuilderInsert](./StringBuilderInsert.md)
  * [StringBuilderMid](./StringBuilderMid.md)
  * [StringBuilderNew](./StringBuilderNew.md)
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
