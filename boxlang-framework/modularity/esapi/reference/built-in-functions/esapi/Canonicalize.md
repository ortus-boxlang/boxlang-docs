[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Canonicalize`

Canonicalize or decode the input string.

Canonicalization is simply the operation of reducing a possibly encoded string down to its simplest form.
 This is important because attackers frequently use encoding to change their input in a way that will bypass validation filters,
 but still be interpreted properly by the target of the attack.
 <p>
 Note that data encoded more than once is not something that a normal user would generate and should be regarded as an attack.

## Method Signature

```
Canonicalize(input=[string], restrictMultiple=[boolean], restrictMixed=[boolean], throwOnError=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `input` | `string` | `true` | The input string to be canonicalized. |  |
| `restrictMultiple` | `boolean` | `true` | If set to true, multiple encoding is restricted. This argument can be set to true to restrict the input if multiple or<br>                            nested encoding is detected. If this argument is set to true, and the given input is multiple or nested encoded using<br>                            one encoding scheme an error will be thrown. |  |
| `restrictMixed` | `boolean` | `true` | If set to true, mixed encoding is restricted. This argument can be set to true to restrict the input if mixed encoding is |  |
| `throwOnError` | `boolean` | `false` | If set to true, an error will be thrown if the input is not valid. If set to false, the input will be returned as is. | `false` |

## Examples



## Related

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
  * [SanitizeHTML](./SanitizeHTML.md)
