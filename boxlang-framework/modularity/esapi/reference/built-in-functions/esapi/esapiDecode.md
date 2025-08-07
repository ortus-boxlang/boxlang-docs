[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `esapiDecode`

Decodes a string that has been encoded with ESAPIEncode with a specified encoding type.

## Method Signature

```
esapiDecode(type=[string], value=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The type of decoding to use. Valid values are: "url", "html", "json", "base64". | `ortus.boxlang.runtime.validation.dynamic.ValueOneOf@553f3b6e` |
| `value` | `string` | `true` | The string to decode. |  |

## Examples



## Related

  * [Canonicalize](./Canonicalize.md)
  * [DecodeFor](./DecodeFor.md)
  * [DecodeForBase64](./DecodeForBase64.md)
  * [DecodeForHTML](./DecodeForHTML.md)
  * [DecodeForJson](./DecodeForJson.md)
  * [DecodeFromURL](./DecodeFromURL.md)
  * [EncodeFor](./EncodeFor.md)
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
  * [esapiEncode](./esapiEncode.md)
  * [GetSafeHTML](./GetSafeHTML.md)
  * [IsSafeHTML](./IsSafeHTML.md)
  * [SanitizeHTML](./SanitizeHTML.md)
