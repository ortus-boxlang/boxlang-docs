[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLFormat`

Formats a string so that special XML characters can be used as text in XML

## Method Signature
```
XMLFormat(string=[string], escapeChars=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to format |  |
| `escapeChars` | `boolean` | `false` | whether to escape additional characters restricted as per XML standards. For details, see<br>                       http://www.w3.org/TR/2006/REC-xml11-20060816/#NT-RestrictedChar. | `false` |

## Examples

```
XMLFormat(string=[string], escapeChars=[boolean])
```

## Related
  * [XMLChildPos](boxlang-language/reference/built-in-functions/XMLChildPos.md)
  * [XMLElemNew](boxlang-language/reference/built-in-functions/XMLElemNew.md)
  * [XMLGetNodeType](boxlang-language/reference/built-in-functions/XMLGetNodeType.md)
  * [XMLNew](boxlang-language/reference/built-in-functions/XMLNew.md)
  * [XMLParse](boxlang-language/reference/built-in-functions/XMLParse.md)
  * [XMLSearch](boxlang-language/reference/built-in-functions/XMLSearch.md)
  * [XMLTransform](boxlang-language/reference/built-in-functions/XMLTransform.md)
  * [XMLValidate](boxlang-language/reference/built-in-functions/XMLValidate.md)
