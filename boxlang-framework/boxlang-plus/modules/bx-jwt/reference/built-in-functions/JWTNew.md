# JWTNew

Returns a new `JwtBuilder` instance — a fluent, chainable builder for constructing signed or encrypted JWTs. Terminate the chain with `.sign()` to produce a JWS, or `.encrypt()` to produce a JWE.

## Method Signature

```
JWTNew()
```

### Arguments

This function takes no arguments.

### Returns

A `JwtBuilder` object (see [Fluent API Reference](../fluent-api/) for the full method list).

## Examples

```javascript
// HMAC-signed token
token = jwtNew()
    .subject( "user-123" )
    .issuer( "my-api" )
    .audience( "mobile-client" )
    .claim( "roles", [ "admin" ] )
    .expireIn( 3600 )
    .header( "kid", "v1" )
    .sign( secret, "HS256" );

// RSA-signed token with all standard claims
token = jwtNew()
    .subject( "svc-account" )
    .issuer( "auth-service" )
    .audience( [ "api", "analytics" ] )
    .issuedNow()
    .expireIn( 3600 )
    .jti( createUUID() )
    .sign( privateKeyPem, "RS256" );

// JWE-encrypted token
token = jwtNew()
    .subject( "patient-456" )
    .claim( "phi", { dob: "1990-01-15" } )
    .encrypt( secret, "dir", "A256GCM" );

// Use withPayload for existing structs
payload = { sub: "user-1", iss: "my-api", roles: [ "admin" ] };
token   = jwtNew().withPayload( payload ).expireIn( 3600 ).sign( secret, "HS256" );
```

## Related

* [Fluent Builder Guide](../../fluent-builder.md)
* [JwtBuilder Reference](../fluent-api/)
* [JWTCreate()](JWTCreate.md) — functional equivalent
* [JWTEncrypt()](JWTEncrypt.md) — functional equivalent for JWE
