[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLValidate`

Uses a Document Type Definition (DTD) or XML Schema to validate an XML text document or an XML document object.

Returns keys status (boolean), errors (array), fatalerrors (array) and warnings (array)

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



## Related

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLElemNew](./XMLElemNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLParse](./XMLParse.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLTransform](./XMLTransform.md)
