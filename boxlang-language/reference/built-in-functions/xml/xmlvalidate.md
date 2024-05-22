[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLValidate`

Uses a Document Type Definition (DTD) or XML Schema to validate an XML text document or an XML document object.

## Method Signature
```
XMLValidate(XML=[any], validator=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XML` | `any` | `true` | The XML text document or XML document object to validate. |  |
| `validator` | `string` | `false` | The DTD or XML Schema to use for validation. If not provided, the DTD declaration within the XML document is used. |  |

## Examples

```
XMLValidate(XML=[any], validator=[string])
```

## Related
  * [XMLChildPos](boxlang-language/reference/built-in-functions/XMLChildPos.md)
  * [XMLElemNew](boxlang-language/reference/built-in-functions/XMLElemNew.md)
  * [XMLFormat](boxlang-language/reference/built-in-functions/XMLFormat.md)
  * [XMLGetNodeType](boxlang-language/reference/built-in-functions/XMLGetNodeType.md)
  * [XMLNew](boxlang-language/reference/built-in-functions/XMLNew.md)
  * [XMLParse](boxlang-language/reference/built-in-functions/XMLParse.md)
  * [XMLSearch](boxlang-language/reference/built-in-functions/XMLSearch.md)
  * [XMLTransform](boxlang-language/reference/built-in-functions/XMLTransform.md)
