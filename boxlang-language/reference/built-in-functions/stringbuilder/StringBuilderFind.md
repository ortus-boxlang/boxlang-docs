[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderFind`

No description available.

## Method Signature

```
StringBuilderFind(stringBuilder=[stringBuilder], substring=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` |  |  |
| `substring` | `string` | `true` |  |  |
| `start` | `integer` | `false` |  | `1` |

## Examples

### Find a substring position with find()

Finds the position of a substring in a StringBuilder.

```java
sb = sb{'Hello BoxLang'};
result = find( sb, 'Box' );
writeOutput( result );
```

Result: 7

### Case-insensitive find with a start position

```java
sb = sb{'Hello BoxLang Box'};
result = sb.findNoCase( 'box', 8 );
writeOutput( result );
```

Result: 15

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderDelete](./StringBuilderDelete.md)
  * [StringBuilderEndsWith](./StringBuilderEndsWith.md)
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
