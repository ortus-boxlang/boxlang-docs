[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `JSONSerialize`

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string.

## Method Signature

```
JSONSerialize(data=[any], queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `data` | `any` | `true` | The variable to convert to a JSON string. |  |
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. | `row` |
| `useSecureJSONPrefix` | `string` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not used) |  |

## Examples



## Related

  * [ToNumeric](./ToNumeric.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [ToScript](./ToScript.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)
  * [ToBase64](./ToBase64.md)
  * [DataNavigate](./DataNavigate.md)
  * [ParseNumber](./ParseNumber.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToString](./ToString.md)
