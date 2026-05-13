[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetSafeHTML`

Sanitizes HTML using antisamy policy rules.

The policy can be a string name of a built-in policy, a file path to a custom policy XML file, or a struct for programmatic policy configuration.

**Built-in policies:** `anythinggoes`, `ebay` (default), `myspace`, `slashdot`, `tinymce`

## Method Signature

```
GetSafeHTML( string, [policy], [throwOnError], [force] )
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The HTML to sanitize |  |
| `policy` | `string\|struct` | `false` | The policy to use: a string name, file path, or a struct for programmatic configuration | `""` (uses default `ebay` policy) |
| `throwOnError` | `boolean` | `false` | When `true`, throws an exception if HTML violates policy rules instead of silently returning sanitized output | `false` |
| `force` | `boolean` | `false` | When `true` and using a struct policy, evicts it from cache and rebuilds it on demand | `false` |

## Struct Policy Configuration

When passing a struct as the policy, the following keys are supported for programmatic configuration:

| Key | Type | Description |
|-----|------|-------------|
| `basePolicy` | `string` | Start from a named policy and override specific parts (e.g., `"ebay"`, `"myspace"`, `"none"` for blank) |
| `overrideMode` | `string` | `"merge"` (default) or `"override"` — controls how overrides are applied to the base policy |
| `directives` | `struct` | Struct of directive key/value pairs (e.g., `{ maxInputSize: 200000 }`) |
| `allowTags` | `array` | Array of tag names to allow with "validate" action |
| `tagRules` | `struct` | Struct of tag rules (tag name to action string or config struct) |
| `globalAttributes` | `struct` | Struct of attributes valid on all tags |
| `dynamicAttributes` | `struct` | Struct of wildcard attributes (e.g., `data-*`) |
| `cssRules` | `struct` | Struct of CSS property rules |
| `allowedEmptyTags` | `array` | Array of self-closing tag names |
| `requireClosingTags` | `array` | Array of tag names requiring end tags |
| `tagsToEncode` | `array` | Array of tag names to entity-encode |

## Examples

### Basic sanitization with default eBay policy

```js
result = getSafeHTML( "<b>Hello</b> <script>alert('xss')</script>" )
// result: "<b>Hello</b> "
```

### Using a named policy

```js
result = getSafeHTML( "<b>Hello</b>", "myspace" )
// result: "<b>Hello</b>"
```

### Custom policy via struct — merge mode with directive override

```js
result = getSafeHTML(
    "<b>" & repeatString( "x", 25000 ) & "</b>",
    {
        basePolicy: "ebay",
        overrideMode: "merge",
        directives: { maxInputSize: 50000 }
    }
)
// Returns sanitized HTML with a custom 50KB input limit
```

### Custom policy via struct — override mode (replace rules)

```js
result = getSafeHTML(
    "<b>Hello</b><em>World</em>",
    {
        basePolicy: "ebay",
        overrideMode: "override",
        allowTags: [ "b", "em" ]
    }
)
// Returns: "<b>Hello</b><em>World</em>" (only allows b and em tags)
```

### Building a policy from scratch

```js
result = getSafeHTML(
    "<b>Hello</b>",
    {
        basePolicy: "none",
        allowTags: [ "b" ],
        directives: { maxInputSize: 100000 }
    }
)
// Returns: "<b>Hello</b>" (only allows specified tags)
```

### Force cache eviction and rebuild for struct policies

```js
// First call caches the policy
result1 = getSafeHTML( "<b>test</b>", policyStruct )

// Second call uses cached policy (for performance)
result2 = getSafeHTML( "<b>test</b>", policyStruct )

// Force eviction and rebuild
result3 = getSafeHTML( "<b>test</b>", policyStruct, false, true )
```

### Throwing exceptions on policy violations

```js
try {
    result = getSafeHTML(
        "<script>alert('xss')</script>",
        "ebay",
        true  // throwOnError = true
    )
} catch ( BoxRuntimeException e ) {
    // Catches policy violations
    writeln( "Sanitization failed: " & e.message )
}
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
  * [IsSafeHTML](./IsSafeHTML.md)
  * [SanitizeHTML](./SanitizeHTML.md)
