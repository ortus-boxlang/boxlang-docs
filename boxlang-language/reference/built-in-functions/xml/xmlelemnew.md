[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLElemNew`

Creates a new XML Element which can be appended to an XML document

## Method Signature
```
XMLElemNew(XML=[xml], childname=[string], namespace=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XML` | `xml` | `true` | The parent XML object to associate the new node to |  |
| `childname` | `string` | `true` | The XML name of the new child node |  |
| `namespace` | `string` | `false` | The XML namespace to attach to the new child node |  |

## Examples

```
XMLElemNew(XML=[xml], childname=[string], namespace=[string])
```

## Related
  * [XMLChildPos](boxlang-language/reference/built-in-functions/XMLChildPos.md)
  * [XMLFormat](boxlang-language/reference/built-in-functions/XMLFormat.md)
  * [XMLGetNodeType](boxlang-language/reference/built-in-functions/XMLGetNodeType.md)
  * [XMLNew](boxlang-language/reference/built-in-functions/XMLNew.md)
  * [XMLParse](boxlang-language/reference/built-in-functions/XMLParse.md)
  * [XMLSearch](boxlang-language/reference/built-in-functions/XMLSearch.md)
  * [XMLTransform](boxlang-language/reference/built-in-functions/XMLTransform.md)
  * [XMLValidate](boxlang-language/reference/built-in-functions/XMLValidate.md)
