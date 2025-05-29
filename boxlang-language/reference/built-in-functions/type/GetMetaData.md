[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetMetaData`

Gets metadata (the methods, properties, and parameters of a component) associated with an object.

This returns the <code>$bx.meta</code> object for the object.

## Method Signature

```
GetMetaData(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The object to get metadata for. |  |

## Examples

### Dump Metadata of CFC Instance

CF9+


```java
writeDump( getMetadata( new Query() ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrVLBVKCxNLar0Sy3XUFDKTNHJS8xNVdJRUMorzU0tykzWKUssSs5ILFJS0LTmSinNLdBQcE8t8U0tSUxJLEnUUChU0ATJAABTTRZo" target="_blank">Run Example</a>

```java
q = queryNew( "id,name", "numeric,varchar" );
dump( GetMetadata( q ) );

```



## Related

  * [NullValue](./NullValue.md)
  * [Len](./Len.md)
  * [StructCount](./StructCount.md)
  * [ArrayLen](./ArrayLen.md)
  * [StringLen](./StringLen.md)
