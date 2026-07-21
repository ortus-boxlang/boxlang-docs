[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderClear`

Resets the StringBuilder buffer to empty.

## Method Signature

```
StringBuilderClear(stringBuilder=[stringBuilder])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to clear. |  |

## Examples

### Clear a StringBuilder buffer

Removes all contents from the existing StringBuilder instance.

```java
sb = sb{'Hello'};
stringBuilderClear( sb );
writeOutput( sb.toString() );
```

Result: (empty string)

### Member usage

```java
sb = sb{'Hello'};
sb.clear();
writeOutput( sb.toString() );
```

Result: (empty string)

## Related

  * [StringBuilderAppend](./StringBuilderAppend.md)
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
