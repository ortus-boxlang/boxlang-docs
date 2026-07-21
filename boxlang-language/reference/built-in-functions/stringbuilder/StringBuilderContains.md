[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderContains`

No description available.

## Method Signature

```
StringBuilderContains(stringBuilder=[stringBuilder], substring=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` |  |  |
| `substring` | `string` | `true` |  |  |

## Examples

### Check for a substring with stringBuilderContains()

Checks whether a StringBuilder contains a substring.

```java
sb = sb{'Hello BoxLang'};
result = stringBuilderContains( sb, 'Box' );
writeOutput( result );
```

Result: true

### Case-insensitive contains

```java
sb = sb{'Hello BoxLang'};
result = sb.containsNoCase( 'boxlang' );
writeOutput( result );
```

Result: true

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
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
