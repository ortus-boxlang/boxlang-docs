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
| `elem` | `XML` | `true` | The XML DOM object. | |
| `childname` | `string` | `true` | The name of the child element. | |
| `n` | `integer` | `true` | The position of the child element. 1-based. | |
|----------|------|----------|-------------|---------|



## Examples

```
XMLChildPos(elem=[XML], childname=[string], n=[integer])
```

## Related
  * [XMLElemNew](XMLElemNew.md)
  * [XMLFormat](XMLFormat.md)
  * [XMLGetNodeType](XMLGetNodeType.md)
  * [XMLNew](XMLNew.md)
  * [XMLParse](XMLParse.md)
  * [XMLSearch](XMLSearch.md)
  * [XMLTransform](XMLTransform.md)
  * [XMLValidate](XMLValidate.md)
