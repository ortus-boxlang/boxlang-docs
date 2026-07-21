[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderInsert`

Inserts value at the given 1-based position in the StringBuilder buffer.

## Method Signature

```
StringBuilderInsert(stringBuilder=[stringBuilder], position=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `stringBuilder` | `stringBuilder` | `true` | The StringBuilder to insert into. |  |
| `position` | `integer` | `true` | The 1-based character position at which to insert. |  |
| `value` | `any` | `true` | The value to insert. Coerced to string. |  |

## Examples

### Insert text with stringBuilderInsert()

Inserts text at a 1-based position.

```java
sb = sb{'Hello World'};
stringBuilderInsert( sb, 7, 'Beautiful ' );
writeOutput( sb.toString() );
```

Result: Hello Beautiful World

### Member usage

```java
sb = sb{'HelloWorld'};
sb.insert( 6, ' ' );
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
  * [StringBuilderLeft](./StringBuilderLeft.md)
  * [StringBuilderMid](./StringBuilderMid.md)
  * [StringBuilderNew](./StringBuilderNew.md)
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
