[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLParse`

Return new array

## Method Signature

```
XMLParse(XML=[string], caseSensitive=[boolean], validator=[any], lenient=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XML` | `string` | `false` | The XML string (or a file/URL containing XML) to parse |  |
| `caseSensitive` | `boolean` | `false` | Whether element/attribute name matching is case-sensitive | `true` |
| `validator` | `any` | `false` | Either a path/URL to an XSD schema to validate against, **or** (as of 1.17.0) a struct of XML security settings — see below |  |
| `lenient` | `boolean` | `false` | As of 1.17.0: overrides `lenientProcessing` in the effective XML security settings when explicitly passed |  |

## XML Security (1.17.0+)

By default, `xmlParse()` uses your application's `xml` config settings (see [XML Security Settings](../../../../getting-started/configuration/directives.md#xml-security-settings)) to guard against XXE (XML External Entity) attacks when parsing untrusted XML. Pass a struct as `validator` to override those defaults for a single call:

```java
xmlDoc = xmlParse(
	xml = untrustedXmlString,
	validator = {
		secureProcessing            : true,
		disallowDoctypeDeclaration  : true,
		allowExternalEntities       : false,
		lenientProcessing           : false
	}
)
```

`validator` still accepts the original XSD path/URL string for schema validation — passing a struct instead switches it to security-settings mode; the two uses are mutually exclusive per call.

## Examples

### Parse XML read from a file

Read XML from a file and use the xmlParse method to parse it into an XML data structure.


```java
<bx:file action="read" file="#tempxml#" variable="xmlString">
<bx:set myXML = xmlParse( xmlString ) >
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxFjrEOwiAURXe%2B4qVTu8gHFEl0cjRObobKtSXhFQWatH9vgyG%2B6byTO5yV%2FSPlCMN0pEbQfmoOGbrg%2FuSgT949oeROVb5iYH0Og5KFqp5grJtHfQO72SIqWU1dDMFu%2BoIIconyBGKkZEbQFhaK%2BCxIGfagZBn%2BcmTtaXphF363dGd%2FNTGhpfWf31HXiy%2FEgj49" target="_blank">Run Example</a>

```java
xml_stream = "
    <note>
      <to>Alice</to>
      <from>Bob</from>
      <heading>Reminder</heading>
      <body>Here is the message you requested.</body>
    </note>
  ";
dump( XmlParse( xml_stream ) );

```



## Related

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLElemNew](./XMLElemNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLValidate](./XMLValidate.md)
