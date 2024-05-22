[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLSearch`

Get XML values according to given xPath query

## Method Signature
```
XMLSearch(XMLNode=[XML], xpath=[String], params=[Struct])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XMLNode` | `XML` | `true` | The XML node to search |  |
| `xpath` | `String` | `true` | The xpath query to search for |  |
| `params` | `Struct` | `false` | The parameters to pass to the xpath query | `{}` |

## Examples

```
XMLSearch(XMLNode=[XML], xpath=[String], params=[Struct])
```

## Related
  * [XMLChildPos](boxlang-language/reference/built-in-functions/XMLChildPos.md)
  * [XMLElemNew](boxlang-language/reference/built-in-functions/XMLElemNew.md)
  * [XMLFormat](boxlang-language/reference/built-in-functions/XMLFormat.md)
  * [XMLGetNodeType](boxlang-language/reference/built-in-functions/XMLGetNodeType.md)
  * [XMLNew](boxlang-language/reference/built-in-functions/XMLNew.md)
  * [XMLParse](boxlang-language/reference/built-in-functions/XMLParse.md)
  * [XMLTransform](boxlang-language/reference/built-in-functions/XMLTransform.md)
  * [XMLValidate](boxlang-language/reference/built-in-functions/XMLValidate.md)
