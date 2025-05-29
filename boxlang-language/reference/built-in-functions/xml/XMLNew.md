[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLNew`

Creates a new empty XML Object

## Method Signature

```
XMLNew(caseSensitive=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `caseSensitive` | `boolean` | `true` | Whether the identifiers in the XML document ( e.g. dot notation ) are case sensitive | `false` |

## Examples

### The simple xmlnew example

Here, We created myXml by using xmlNew function. Then created root node(sampleXml) for myXml and set the rootnode text


```java
<bx:set myXml = xmlNew() >
<bx:set myXml.XMLROOT = xmlelemnew( myXml, "sampleXml" ) >
<bx:set myXml.SAMPLEXML.XMLTEXT = "This is root node text" >
<bx:dump var="#myXml#">
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJyryM2JT8lPLs1NzStRsFWIyM3xSy3X0LTmSinNLdBQqECWBooCAJUEEBk%3D" target="_blank">Run Example</a>

```java
xml_document = XmlNew();
dump( xml_document );

```



## Related

  * [XMLElemNew](./XMLElemNew.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLValidate](./XMLValidate.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLChildPos](./XMLChildPos.md)
  * [XMLParse](./XMLParse.md)
