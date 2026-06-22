[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTGenerateSecret`

Generates a cryptographically random HMAC secret and returns it Base64-encoded. Use this to create RFC 7518–compliant keys for HS256/384/512.

## Method Signature

```
JWTGenerateSecret( [bits] )
```

### Arguments

| Argument | Type      | Required | Description                                                                | Default |
| -------- | --------- | -------- | -------------------------------------------------------------------------- | ------- |
| `bits`   | `numeric` | No       | Key length in bits. Must be ≥ 128 and a multiple of 8.                     | `256`   |

### Returns

A Base64-encoded `string` of `bits / 8` random bytes.

## Examples

```javascript
secret256 = jwtGenerateSecret();       // 256-bit, suitable for HS256
secret384 = jwtGenerateSecret( 384 );  // 384-bit, suitable for HS384
secret512 = jwtGenerateSecret( 512 );  // 512-bit, suitable for HS512

// Save to an environment variable / secret manager
writeOutput( "JWT_HMAC_SECRET=" & secret256 );
```

## Related

* [JWTGenerateKeyPair()](JWTGenerateKeyPair.md) — asymmetric key pairs
* [Key Management Guide](../../key-management.md)
* [Security Best Practices](../../security-best-practices.md)
