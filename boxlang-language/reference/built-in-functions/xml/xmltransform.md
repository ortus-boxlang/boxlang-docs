# XMLTransform

Get XML values according to given xPath query

## Method Signature

```
XMLTransform(XML=[any], XSL=[String], parameters=[Struct])
```

### Arguments

| Argument     | Type     | Required | Description                                      | Default |
| ------------ | -------- | -------- | ------------------------------------------------ | ------- |
| `XML`        | `any`    | `true`   | The XML to transform                             |         |
| `XSL`        | `String` | `true`   | The XSL to use for the transformation            |         |
| `parameters` | `Struct` | `false`  | The parameters to pass to the xsl transformation | `{}`    |

## Examples

## Related

* [XMLChildPos](xmlchildpos.md)
* [XMLElemNew](xmlelemnew.md)
* [XMLFormat](xmlformat.md)
* [XMLGetNodeType](xmlgetnodetype.md)
* [XMLNew](xmlnew.md)
* [XMLParse](xmlparse.md)
* [XMLSearch](xmlsearch.md)
* [XMLValidate](xmlvalidate.md)
