[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderEndsWith`

No description available.

## Method Signature

```
StringBuilderEndsWith(stringBuilder=[stringBuilder], substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` |  |  |
| `substring` | `string` | `true` |  |  |

## Examples

### Check suffix with endsWith()

Tests whether a StringBuilder ends with a given substring.

```java
sb = sb{'Hello BoxLang'};
result = endsWith( sb, 'Lang' );
writeOutput( result );
```

Result: true

### Member usage

```java
sb = sb{'Hello BoxLang'};
result = sb.endsWith( 'Box' );
writeOutput( result );
```

Result: false

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderDelete](./StringBuilderDelete.md)
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
