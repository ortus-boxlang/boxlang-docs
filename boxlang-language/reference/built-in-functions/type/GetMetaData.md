[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetMetaData`

Gets metadata (the methods, properties, and parameters of a component) associated with an object.

This only exists for backwards compat with Adobe and Lucee and this BIF should be moved to a compat module
 at a later date. In BoxLang, use the obj.$bx.meta object instead.

## Method Signature

```
GetMetaData(object=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | The object to get metadata for. |  |

## Examples

```
GetMetaData(object=[any])
```

## Related

  * [ArrayLen](./ArrayLen.md)
  * [Len](./Len.md)
  * [NullValue](./NullValue.md)
  * [StringLen](./StringLen.md)
  * [StructCount](./StructCount.md)
