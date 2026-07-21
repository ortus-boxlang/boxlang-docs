[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderMid`

No description available.

## Method Signature

```
StringBuilderMid(stringBuilder=[stringBuilder], start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` |  |  |
| `start` | `integer` | `true` |  |  |
| `count` | `integer` | `false` |  |  |

## Examples

### Extract middle text with mid()

Returns a middle segment from a StringBuilder.

```java
sb = sb{'The quick brown fox'};
result = sb.mid( 5, 5 );
writeOutput( result );
```

Result: quick

### Headless usage

```java
sb = sb{'BoxLang'};
writeOutput( mid( sb, 4, 4 ) );
```

Result: Lang

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
  * [StringBuilderClear](./StringBuilderClear.md)
  * [StringBuilderContains](./StringBuilderContains.md)
  * [StringBuilderDelete](./StringBuilderDelete.md)
  * [StringBuilderEndsWith](./StringBuilderEndsWith.md)
  * [StringBuilderFind](./StringBuilderFind.md)
  * [StringBuilderInsert](./StringBuilderInsert.md)
  * [StringBuilderLeft](./StringBuilderLeft.md)
  * [StringBuilderNew](./StringBuilderNew.md)
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
