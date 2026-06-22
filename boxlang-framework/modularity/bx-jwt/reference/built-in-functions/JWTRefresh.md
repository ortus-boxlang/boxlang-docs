[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTRefresh`

Verifies an existing JWT and re-issues it with fresh `iat`, `jti`, and optionally a new `exp`. All application claims (`sub`, `iss`, `aud`, custom claims) are preserved.

## Method Signature

```
JWTRefresh( token, [key], [algorithm], [options] )
```

### Arguments

| Argument    | Type     | Required | Description                                                                                          | Default |
| ----------- | -------- | -------- | ---------------------------------------------------------------------------------------------------- | ------- |
| `token`     | `string` | Yes      | Existing compact JWS token to refresh.                                                                |         |
| `key`       | `any`    | No       | Signing/verification key. Optional when defaults are configured.                                      | `null`  |
| `algorithm` | `string` | No       | Algorithm to use for the new token.                                                                   | `null`  |
| `options`   | `struct` | No       | See options table below.                                                                              | `{}`    |

#### Options

| Option         | Type      | Description                                                                                              | Default |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------- | ------- |
| `allowExpired` | `boolean` | Allow refreshing an expired token. The signature is still verified.                                       | `false` |
| `expireIn`     | `numeric` | Seconds until the refreshed token expires.                                                                | `null`  |
| `headers`      | `struct`  | JOSE headers to include in the new token (overrides originals).                                           | `{}`    |
| `claims`       | `struct`  | Optional claim assertions to enforce during verification before refreshing.                               | `{}`    |

### Returns

A new compact JWS string with refreshed time claims.

## Examples

```javascript
// Standard refresh — token must still be valid
newToken = jwtRefresh( oldToken, secret, "HS256" );

// Refresh with a new 1-hour expiration
newToken = jwtRefresh( oldToken, secret, "HS256", { expireIn: 3600 } );

// Allow refreshing an expired token (grace period)
newToken = jwtRefresh( oldToken, secret, "HS256", {
    allowExpired : true,
    expireIn     : 3600
} );
```

## Related

* [JWTVerify()](JWTVerify.md)
* [JWTCreate()](JWTCreate.md)
* [Signing (JWS) Guide](../../signing-jws.md)
