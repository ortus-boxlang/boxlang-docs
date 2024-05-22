[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `JSONDeserialize`

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

## Method Signature
```
JSONDeserialize(json=[string], strictMapping=[boolean], useCustomSerializer=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `json` | `string` | `true` | The JSON string to convert to data. |  |
| `strictMapping` | `boolean` | `false` | A Boolean value that specifies whether to convert the JSON strictly. If true, everything becomes structures. | `true` |
| `useCustomSerializer` | `string` | `false` | A string that specifies the name of a custom serializer to use. (Not used) |  |

## Examples

```
JSONDeserialize(json=[string], strictMapping=[boolean], useCustomSerializer=[string])
```

## Related
  * [DataNavigate](boxlang-language/reference/built-in-functions/DataNavigate.md)
  * [JSONSerialize](boxlang-language/reference/built-in-functions/JSONSerialize.md)
  * [ParseNumber](boxlang-language/reference/built-in-functions/ParseNumber.md)
  * [serializeJSON](boxlang-language/reference/built-in-functions/serializeJSON.md)
  * [ToBase64](boxlang-language/reference/built-in-functions/ToBase64.md)
  * [ToBinary](boxlang-language/reference/built-in-functions/ToBinary.md)
  * [ToNumeric](boxlang-language/reference/built-in-functions/ToNumeric.md)
  * [ToScript](boxlang-language/reference/built-in-functions/ToScript.md)
  * [ToString](boxlang-language/reference/built-in-functions/ToString.md)
