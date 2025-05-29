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

### Validate against an XML Schema

Validates that note.xml is valid according to the schema note.xsd. 

<a href="https://try.boxlang.io/?code=eJyryM0JS8zJTEksSdVQUMooKSkottLXLy8v1ys3Lk7OyM%2FPKdZLzs%2FVr8jN0c%2FLL0nVAzKUdIhTWZyipKCpFxziGBIabM0FAPhjJN4%3D" target="_blank">Run Example</a>

```java
xmlValidate( "https://www.w3schools.com/xml/note.xml", "https://www.w3schools.com/xml/note.xsd" ).STATUS;

```

Result: false

### Additional Examples


```java
validator = "
		<?xml version=""1.0""?>
		<xs:schema xmlns:xs=""http://www.w3.org/2001/XMLSchema"">
			<xs:element name=""note"">
				<xs:complexType>
					<xs:sequence>
						<xs:element name=""to"" type=""xs:string""/>
						<xs:element name=""from"" type=""xs:string""/>
						<xs:element name=""heading"" type=""xs:string""/>
						<xs:element name=""body"" type=""xs:string""/>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:schema>
		";
xml_stream = "
			<?xml version=""1.0"" encoding=""UTF-8""?>
			<note>
				<to>Alice</to>
				<from>Bob</from>
				<heading>Reminder</heading>
				<body>Here is the message you requested.</body>
			</note>";
xml_document = XmlParse( xml_stream );
dump( xmlValidate( xml_document, validator ) );

```



## Related

  * [XMLElemNew](./XMLElemNew.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLNew](./XMLNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLChildPos](./XMLChildPos.md)
  * [XMLParse](./XMLParse.md)
