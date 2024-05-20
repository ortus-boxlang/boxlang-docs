# XMLChildPos

Gets the position of a child element within an XML document object.

## Method Signature

```
XMLChildPos(elem=[XML], childname=[string], n=[integer])
```

### Arguments

| Argument    | Type      | Required   | Description                                 | Default   |
| ----------- | --------- | ---------- | ------------------------------------------- | --------- |
| `elem`      | `XML`     | `true`     | The XML DOM object.                         |           |
| `childname` | `string`  | `true`     | The name of the child element.              |           |
| `n`         | `integer` | `true`     | The position of the child element. 1-based. |           |
| ----------  | ------    | ---------- | -------------                               | --------- |

## Examples

```
XMLChildPos(elem=[XML], childname=[string], n=[integer])
```

## Related

* [XMLElemNew](xmlelemnew.md)
* [XMLFormat](xmlformat.md)
* [XMLGetNodeType](xmlgetnodetype.md)
* [XMLNew](xmlnew.md)
* [XMLParse](xmlparse.md)
* [XMLSearch](xmlsearch.md)
* [XMLTransform](xmltransform.md)
* [XMLValidate](xmlvalidate.md)
