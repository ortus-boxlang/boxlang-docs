[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTValidate`

Verifies a JWS signature and claims, returning `true` or `false` instead of throwing. Useful for simple conditional checks where you don't need the exception detail.

## Method Signature

```
JWTValidate( token, [key], [algorithm], [options] )
```

### Arguments

| Argument    | Type     | Required | Description                                                                                  | Default |
| ----------- | -------- | -------- | -------------------------------------------------------------------------------------------- | ------- |
| `token`     | `string` | Yes      | Compact JWS token string.                                                                    |         |
| `key`       | `any`    | No       | Verification key. Optional when `defaultVerifyKey` is configured.                            | `null`  |
| `algorithm` | `string` | No       | Expected algorithm.                                                                          | `null`  |
| `options`   | `struct` | No       | `claims` (expected claim values), `clockSkew` (seconds tolerance for `exp`/`nbf`).           | `{}`    |

### Returns

`boolean` — `true` if the signature is valid and all claim constraints pass, `false` otherwise.

## Examples

```javascript
if ( jwtValidate( token, secret, "HS256" ) ) {
    payload = jwtVerify( token, secret, "HS256" );
    // proceed with authenticated request
} else {
    // redirect to login / return 401
}
```

## Related

* [JWTVerify()](JWTVerify.md) — throwing counterpart that returns the claims struct
* [JWTDecode()](JWTDecode.md) — inspect a token without verifying
* [Security Best Practices](../../security-best-practices.md)
