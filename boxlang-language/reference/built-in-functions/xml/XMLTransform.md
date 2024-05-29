[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLTransform`

Get XML values according to given xPath query

## Method Signature

```
XMLTransform(XML=[any], XSL=[String], parameters=[Struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XML` | `any` | `true` | The XML to transform |  |
| `XSL` | `String` | `true` | The XSL to use for the transformation |  |
| `parameters` | `Struct` | `false` | The parameters to pass to the xsl transformation | `{}` |

## Examples

```
XMLTransform(XML=[any], XSL=[String], parameters=[Struct])
```

## Related

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLElemNew](./XMLElemNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLParse](./XMLParse.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLValidate](./XMLValidate.md)
