[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `EncodeFor`

Encodes a given string for safe output in the specified context.

The encoding is meant to mitigate Cross Site Scripting (XSS) attacks.

## Method Signature

```
EncodeFor(type=[string], value=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The type of encoding to use. Valid values are: "css", "dn", "html", "htmlAttribute", "javascript", "ldap", "sql", "url", "xml",<br>                "xmlAttribute", "xpath". | `ortus.boxlang.runtime.validation.dynamic.ValueOneOf@4c7a078` |
| `value` | `string` | `false` | The string to encode. |  |

## Examples



## Related

  * [Canonicalize](./Canonicalize.md)
  * [DecodeFor](./DecodeFor.md)
  * [DecodeForBase64](./DecodeForBase64.md)
  * [DecodeForHTML](./DecodeForHTML.md)
  * [DecodeForJson](./DecodeForJson.md)
  * [DecodeFromURL](./DecodeFromURL.md)
  * [encodeForCSS](./encodeForCSS.md)
  * [encodeForDN](./encodeForDN.md)
  * [encodeForHTML](./encodeForHTML.md)
  * [encodeForHTMLAttribute](./encodeForHTMLAttribute.md)
  * [encodeForJavaScript](./encodeForJavaScript.md)
  * [encodeForLDAP](./encodeForLDAP.md)
  * [EncodeForSQL](./EncodeForSQL.md)
  * [encodeForURL](./encodeForURL.md)
  * [encodeForXML](./encodeForXML.md)
  * [encodeForXMLAttribute](./encodeForXMLAttribute.md)
  * [encodeForXPath](./encodeForXPath.md)
  * [esapiDecode](./esapiDecode.md)
  * [esapiEncode](./esapiEncode.md)
  * [GetSafeHTML](./GetSafeHTML.md)
  * [IsSafeHTML](./IsSafeHTML.md)
  * [SanitizeHTML](./SanitizeHTML.md)
