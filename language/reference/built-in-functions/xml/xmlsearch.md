# XMLSearch

Get XML values according to given xPath query

## Method Signature

```
XMLSearch(XMLNode=[XML], xpath=[String], params=[Struct])
```

### Arguments

| Argument   | Type     | Required   | Description                               | Default   |
| ---------- | -------- | ---------- | ----------------------------------------- | --------- |
| `XMLNode`  | `XML`    | `true`     | The XML node to search                    |           |
| `xpath`    | `String` | `true`     | The xpath query to search for             |           |
| `params`   | `Struct` | `false`    | The parameters to pass to the xpath query | {}        |
| ---------- | ------   | ---------- | -------------                             | --------- |

## Examples

```
XMLSearch(XMLNode=[XML], xpath=[String], params=[Struct])
```

## Related

* [XMLChildPos](xmlchildpos.md)
* [XMLElemNew](xmlelemnew.md)
* [XMLFormat](xmlformat.md)
* [XMLGetNodeType](xmlgetnodetype.md)
* [XMLNew](xmlnew.md)
* [XMLParse](xmlparse.md)
* [XMLTransform](xmltransform.md)
* [XMLValidate](xmlvalidate.md)
