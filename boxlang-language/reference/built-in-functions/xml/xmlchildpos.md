[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLChildPos`

Gets the position of a child element within an XML document object.

## Method Signature
```
XMLChildPos(elem=[XML], childname=[string], n=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `elem` | `XML` | `true` | The XML DOM object. |  |
| `childname` | `string` | `true` | The name of the child element. |  |
| `n` | `integer` | `true` | The position of the child element. 1-based. |  |

## Examples

```
XMLChildPos(elem=[XML], childname=[string], n=[integer])
```

## Related
  * [XMLElemNew](boxlang-language/reference/built-in-functions/XMLElemNew.md)
  * [XMLFormat](boxlang-language/reference/built-in-functions/XMLFormat.md)
  * [XMLGetNodeType](boxlang-language/reference/built-in-functions/XMLGetNodeType.md)
  * [XMLNew](boxlang-language/reference/built-in-functions/XMLNew.md)
  * [XMLParse](boxlang-language/reference/built-in-functions/XMLParse.md)
  * [XMLSearch](boxlang-language/reference/built-in-functions/XMLSearch.md)
  * [XMLTransform](boxlang-language/reference/built-in-functions/XMLTransform.md)
  * [XMLValidate](boxlang-language/reference/built-in-functions/XMLValidate.md)
