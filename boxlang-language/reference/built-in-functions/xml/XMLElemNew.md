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

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLParse](./XMLParse.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLValidate](./XMLValidate.md)
