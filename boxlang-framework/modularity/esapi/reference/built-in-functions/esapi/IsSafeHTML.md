[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSafeHTML`

Verifies if the HTML is safe using antisamy policy rules.

The policy can be a string name of a built-in policy, a file path to a custom policy XML file, or a struct for programmatic policy configuration. For full struct documentation, see [`getSafeHTML()`](./GetSafeHTML.md).

**Built-in policies:** `anythinggoes`, `ebay` (default), `myspace`, `slashdot`, `tinymce`

## Method Signature

```
IsSafeHTML( string, [policy], [force] )
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The HTML to validate |  |
| `policy` | `string\|struct` | `false` | The policy to use: a string name, file path, or a struct for programmatic configuration | `""` (uses default `ebay` policy) |
| `force` | `boolean` | `false` | When `true` and using a struct policy, evicts it from cache and rebuilds it on demand | `false` |

## Examples

### Basic safety check with default eBay policy

```js
result = isSafeHTML( "<b>Hello</b>" )
// result: true

result = isSafeHTML( "<b>Hello</b><script>alert('xss')</script>" )
// result: false (contains disallowed script tag)
```

### Using a named policy

```js
result = isSafeHTML( "<b>Hello</b><em>World</em>", "myspace" )
// result: true or false depending on whether content violates myspace policy
```

### Custom policy via struct

```js
result = isSafeHTML(
    "<b>Hello</b><em>World</em>",
    {
        basePolicy: "ebay",
        allowTags: [ "b", "em" ]
    }
)
// result: true (content only contains allowed tags)
```

### Force cache eviction for struct policies

```js
// First call caches the policy
result1 = isSafeHTML( "<b>test</b>", policyStruct )

// Second call uses cached policy (for performance)
result2 = isSafeHTML( "<b>test</b>", policyStruct )

// Force eviction and rebuild
result3 = isSafeHTML( "<b>test</b>", policyStruct, true )
```

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
