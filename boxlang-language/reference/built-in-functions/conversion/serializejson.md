[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `serializeJSON`

Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

## Method Signature
```
serializeJSON(var=[any], queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `var` | `any` | `true` | The variable to convert to a JSON string. |  |
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not used) |  |

## Examples

```
serializeJSON(var=[any], queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])
```

## Related
  * [DataNavigate](DataNavigate.md)
  * [JSONDeserialize](JSONDeserialize.md)
  * [JSONSerialize](JSONSerialize.md)
  * [ParseNumber](ParseNumber.md)
  * [ToBase64](ToBase64.md)
  * [ToBinary](ToBinary.md)
  * [ToNumeric](ToNumeric.md)
  * [ToScript](ToScript.md)
  * [ToString](ToString.md)
