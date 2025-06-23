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

### Simple xmlelemnew Example

Here, we've created myXml with root and child nodes using xmlelemnew().


```java
<bx:set myXml = xmlNew() >
<bx:set myXml.XMLROOT = xmlelemnew( myXml, "sampleXml" ) >
<bx:set myXml.SAMPLEXML.XMLTEXT = "This is Root node text" >
<bx:loop from="1" to="3" index="i">
	<bx:set myXml.SAMPLEXML.XMLCHILDREN[ i ] = xmlelemnew( myXml, "childNode#i#" ) >
	<bx:set myXml.SAMPLEXML.XMLCHILDREN[ i ].XMLTEXT = "This is Child node#i# text" >
</bx:loop>
<bx:dump var="#myXml#">
```


### Additional Examples


```java
xml_document = XmlNew(); // new XML document to populate
xml_root = XmlElemNew( xml_document, "notes" );
xml_document.XMLROOT = xml_root; // set the root node of the XML document
xml_child = XmlElemNew( xml_document, "note" ); // first child node
xml_secondary_child = XmlElemNew( xml_document, "to" ); // child node for the first child node
xml_child.XMLCHILDREN.append( xml_secondary_child );
xml_root.XMLCHILDREN.append( xml_child ); // add the first child node to the XML document
dump( xml_document );

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
