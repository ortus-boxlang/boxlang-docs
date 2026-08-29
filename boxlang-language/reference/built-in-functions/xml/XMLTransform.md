[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLTransform`

Get XML values according to given xPath query

## Method Signature

```
XMLTransform(XML=[any], XSL=[String], parameters=[Struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XML` | `any` | `true` | The XML to transform |  |
| `XSL` | `String` | `true` | The XSL to use for the transformation |  |
| `parameters` | `Struct` | `false` | The parameters to pass to the xsl transformation | `{}` |

{% hint style="info" %}
As of 1.17.0, when `XML` is passed as a raw XML string (rather than an already-parsed XML object), `xmlTransform()` automatically applies your application's [XML Security Settings](../../../../getting-started/configuration/directives.md#xml-security-settings) — the same XXE-hardening defaults used by [`xmlParse()`](./XMLParse.md).
{% endhint %}

## Examples

### Transform XML using an XSLT stylesheet

```java
xml = xmlParse( "<root><item>test</item></root>" );
xslt = '<?xml version="1.0"?><xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><xsl:template match="/"><output><xsl:value-of select="/root/item"/></output></xsl:template></xsl:stylesheet>';
result = xmlTransform( xml, xslt );
writeOutput( isString( result ) );

```

Result: true

## Related

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLElemNew](./XMLElemNew.md)
  * [XMLFormat](./XMLFormat.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLParse](./XMLParse.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLValidate](./XMLValidate.md)
