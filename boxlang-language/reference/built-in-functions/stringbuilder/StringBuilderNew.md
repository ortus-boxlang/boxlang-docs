[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringBuilderNew`

Create a new StringBuilder instance or wrap an existing Java StringBuilder.

## Method Signature

```
StringBuilderNew(value=[any], capacity=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | Optional initial value (String) or existing Java StringBuilder to wrap. Empty if not provided. |  |
| `capacity` | `integer` | `false` | Optional initial capacity for newly created BoxStringBuilder instances. | `0` |

## Examples

### Create a StringBuilder with stringBuilderNew()

Creates a new StringBuilder instance.

```java
result = stringBuilderNew();
writeOutput( result.toString() );
```

Result: (empty string)

### Create a seeded StringBuilder

```java
result = stringBuilderNew( 'hello' );
writeOutput( result.toString() );
```

Result: hello

### Create an empty StringBuilder with explicit capacity

```java
result = stringBuilderNew( capacity = 64 );
writeOutput( result.getBuffer().capacity() );
```

Result: at least 64

### Create a seeded StringBuilder with explicit capacity

```java
result = stringBuilderNew( 'hello', 64 );
writeOutput( result.toString() );
```

Result: hello

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
  * [StringBuilderPrepend](./StringBuilderPrepend.md)
  * [StringBuilderReplace](./StringBuilderReplace.md)
  * [StringBuilderReverse](./StringBuilderReverse.md)
  * [StringBuilderRight](./StringBuilderRight.md)
  * [StringBuilderStartsWith](./StringBuilderStartsWith.md)
  * [StringBuilderTrim](./StringBuilderTrim.md)
