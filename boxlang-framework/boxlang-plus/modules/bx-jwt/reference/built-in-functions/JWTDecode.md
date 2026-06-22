# JWTDecode

Decodes a JWS token **without verifying the signature**. Returns the header and payload so you can inspect the `kid`, `alg`, or any claim before deciding which key to verify with.

{% hint style="warning" %}
Never trust the contents returned by `jwtDecode()` for authorization decisions — always follow up with `jwtVerify()` (or `jwtValidate()`) before honoring any claim.
{% endhint %}

## Method Signature

```
JWTDecode( token )
```

### Arguments

| Argument | Type     | Required | Description                         | Default |
| -------- | -------- | -------- | ----------------------------------- | ------- |
| `token`  | `string` | Yes      | Compact JWS token string to decode. |         |

### Returns

A `struct` with two keys:

* `header` — the JOSE header struct (e.g. `{ alg: "RS256", kid: "v2", typ: "JWT" }`)
* `payload` — the claims struct

## Examples

```javascript
decoded = jwtDecode( token );
kid     = decoded.header.kid;     // e.g. "v2"
alg     = decoded.header.alg;     // e.g. "RS256"
sub     = decoded.payload.sub;    // claims are readable without verification

// Typical kid-dispatch pattern
decoded = jwtDecode( token );
key     = getKeyById( decoded.header.kid );
payload = jwtVerify( token, key, decoded.header.alg );
```

## Related

* [JWTVerify()](JWTVerify.md) — verify the token before trusting it
* [Key Rotation Guide](../../key-rotation.md) — kid-based dispatch patterns
