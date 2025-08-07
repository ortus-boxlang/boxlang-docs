[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSafeHTML`

Verifies if the HTML is safe using antisamy policy rules.

If no policy is provided, the default policy is used which is the eBay policy.
 <p>
 Available policies are:
 <ul>
 <li>anythinggoes</li>
 <li>ebay</li>
 <li>myspace</li>
 <li>slashdot</li>
 <li>tinymce</li>
 </ul>
 <p>
 If a policy is not one of the above, it is assumed to be an absolute path to a custom policy file.

## Method Signature

```
IsSafeHTML(string=[string], policy=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The HTML to sanitize |  |
| `policy` | `string` | `false` | The policy to use for sanitization |  |

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
  * [SanitizeHTML](./SanitizeHTML.md)
