[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SanitizeHTML`

Sanitizes unsafe HTML to protect against XSS attacks using the OWASP Java HTML Sanitizer.

<p>
 The policy can be one of the following:
 <ul>
 <li>blocks</li>
 <li>formatting</li>
 <li>images</li>
 <li>links</li>
 <li>styles</li>
 <li>tables</li>
 </ul>
 <p>
 If no policy is provided, all policies are used.
 <p>
 You can also provide a OWASP {@link PolicyFactory} object to use a custom policy.

## Method Signature

```
SanitizeHTML(string=[string], policy=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to sanitize. |  |
| `policy` | `any` | `false` | The policy to use for sanitization. If not provided, all policies are used. This can also be a ${link PolicyFactory} object. |  |

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
  * [esapiDecode](./esapiDecode.md)
  * [esapiEncode](./esapiEncode.md)
  * [GetSafeHTML](./GetSafeHTML.md)
  * [IsSafeHTML](./IsSafeHTML.md)
