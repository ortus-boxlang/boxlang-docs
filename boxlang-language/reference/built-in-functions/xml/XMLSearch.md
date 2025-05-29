[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLSearch`

Get XML values according to given xPath query

## Method Signature

```
XMLSearch(XMLNode=[XML], xpath=[String], params=[Struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XMLNode` | `XML` | `true` | The XML node to search |  |
| `xpath` | `String` | `true` | The xpath query to search for |  |
| `params` | `Struct` | `false` | The parameters to pass to the xpath query | `{}` |

## Examples

### Read specific properties from XML collection

XPath extracts 'name' property from every user given in the XML collection


```java
<bx:savecontent variable="xmlstring">
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <users>
        <user id="1">
            <name>Me</name>
        </user>
        <user id="2">
            <name>You</name>
            <address>
                <street>Long Road</street>
            </address>
        </user>
    </users>
</bx:savecontent>
<bx:script>
	xml = XMLParse( xmlstring );
	result = xmlSearch( xml, "users//name" );
	userlist = "";
	for( i = 1; i <= ArrayLen( result ); i++ ) {
		userlist = ListAppend( userlist, result[ i ].XMLTEXT );
	}
	writeOutput( userlist );
</bx:script>

```

Result: Me,You

### Additional Examples


```java
xml_stream = "
			<?xml version=""1.0"" encoding=""UTF-8""?>
			<notes>
				<note>
					<to>Alice</to>
					<from>Bob</from>
					<heading>Reminder</heading>
					<body>Here is the message you requested.</body>
				</note>
				<note>
					<to>Bob</to>
					<from>Alice</from>
					<heading>Your request</heading>
					<body>I got your message; all is well.</body>
				</note>
			</notes>";
xml_document = XmlParse( xml_stream );
dump( XmlSearch( xml_document, "/notes/note[last()]/body" ) );
 // I got your message; all is well.

```



## Related

  * [XMLElemNew](./XMLElemNew.md)
  * [XMLValidate](./XMLValidate.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLNew](./XMLNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLChildPos](./XMLChildPos.md)
  * [XMLParse](./XMLParse.md)
