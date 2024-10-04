# XMLValidate

Uses a Document Type Definition (DTD) or XML Schema to validate an XML text document or an XML document object.

Returns keys status (boolean), errors (array), fatalerrors (array) and warnings (array)

## Method Signature

```
XMLValidate(XML=[any], validator=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                                                                        | Default |
| ----------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------ | ------- |
| `XML`       | `any`    | `true`   | The XML text document or XML document object to validate.                                                          |         |
| `validator` | `string` | `false`  | The DTD or XML Schema to use for validation. If not provided, the DTD declaration within the XML document is used. |         |

## Examples

## Related

* [XMLChildPos](xmlchildpos.md)
* [XMLElemNew](xmlelemnew.md)
* [XMLFormat](xmlformat.md)
* [XMLGetNodeType](xmlgetnodetype.md)
* [XMLNew](xmlnew.md)
* [XMLParse](xmlparse.md)
* [XMLSearch](xmlsearch.md)
* [XMLTransform](xmltransform.md)
