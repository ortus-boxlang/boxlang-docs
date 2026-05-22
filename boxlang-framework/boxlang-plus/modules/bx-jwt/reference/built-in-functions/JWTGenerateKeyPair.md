[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTGenerateKeyPair`

Generates an asymmetric key pair appropriate for the given JWS algorithm. Returns a struct with `privateKey` and `publicKey` as PEM-encoded strings.

## Method Signature

```
JWTGenerateKeyPair( [algorithm] )
```

### Arguments

| Argument    | Type     | Required | Description                                                                  | Default |
| ----------- | -------- | -------- | ---------------------------------------------------------------------------- | ------- |
| `algorithm` | `string` | No       | Target algorithm. Determines key type and size.                              | `RS256` |

### Supported Algorithms

| Algorithm           | Key Type    | Key Size  |
| ------------------- | ----------- | --------- |
| `RS256` / `RS384`   | RSA         | 2048-bit  |
| `RS512`             | RSA         | 4096-bit  |
| `ES256`             | EC (P-256)  | —         |
| `ES384`             | EC (P-384)  | —         |
| `ES512`             | EC (P-521)  | —         |

### Returns

A `struct` with:

* `privateKey` — PEM string
* `publicKey` — PEM string

## Examples

```javascript
rsaKeys = jwtGenerateKeyPair( "RS256" );
token   = jwtCreate( { sub: "u1" }, rsaKeys.privateKey, "RS256" );
payload = jwtVerify( token, rsaKeys.publicKey, "RS256" );

ecKeys  = jwtGenerateKeyPair( "ES256" );
token   = jwtCreate( { sub: "u1" }, ecKeys.privateKey, "ES256" );
payload = jwtVerify( token, ecKeys.publicKey, "ES256" );

// Persist keys for production
fileWrite( "/etc/keys/private.pem", rsaKeys.privateKey );
fileWrite( "/etc/keys/public.pem",  rsaKeys.publicKey  );
```

## Related

* [JWTGenerateSecret()](JWTGenerateSecret.md) — symmetric HMAC secret
* [Key Management Guide](../../key-management.md)
* [Algorithms](../algorithms.md)
