---
description: >-
  Compose JWTs fluently with jwtNew() — chain claim methods and terminate with
  .sign() or .encrypt().
icon: link
---

# Fluent Builder

`jwtNew()` returns a `JwtBuilder` — a chainable object that makes complex JWT construction read like an English sentence. Every claim or header method returns `this`, so calls flow naturally. Two terminal methods finish the chain:

* `.sign( [key], [algorithm] )` — produces a compact **JWS** string
* `.encrypt( [key], [keyAlgorithm], [encAlgorithm] )` — produces a compact **JWE** string

## Why Use the Builder?

| Functional BIF call                                                                | Builder equivalent                                                                      |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `jwtCreate( { sub:"u1", iss:"api", aud:"web", exp: now() + 3600 }, key, "HS256" )` | `jwtNew().subject("u1").issuer("api").audience("web").expireIn(3600).sign(key,"HS256")` |

The builder shines when you need many claims, custom headers, or want to assemble the payload conditionally.

## Anatomy of a Chain

```javascript
token = jwtNew()                          // 1. Start the chain
    .subject( "user-123" )                // 2. Standard claims
    .issuer( "my-api" )
    .audience( [ "web", "mobile" ] )
    .claim( "roles", [ "admin" ] )        // 3. Custom claim
    .expireIn( 3600 )                     // 4. Time claims
    .issuedNow()
    .jti( createUUID() )
    .header( "kid", "v2" )                // 5. JOSE headers
    .sign( secret, "HS256" );             // 6. Terminate → token string
```

## Conditional Composition

Because every method returns `this`, you can keep a reference to the builder and add claims based on logic:

```javascript
b = jwtNew().subject( user.id ).issuer( "my-api" ).expireIn( 3600 );

if ( user.isAdmin ) {
    b.claim( "scope", "admin:*" );
}
if ( user.tenant.isSet() ) {
    b.claim( "tenant", user.tenant );
}

token = b.sign( signingKey, "HS256" );
```

## Re-using an Existing Payload

Already have the claims as a struct? `.withPayload()` swaps in the whole struct at once, then you can layer additional methods on top:

```javascript
payload = { sub: "user-1", iss: "my-api", roles: [ "admin" ] };
token   = jwtNew()
    .withPayload( payload )
    .expireIn( 3600 )
    .sign( secret, "HS256" );
```

## Encrypting (JWE) Instead of Signing

Swap `.sign()` for `.encrypt()` — every other method works identically:

```javascript
token = jwtNew()
    .subject( "patient-456" )
    .claim( "phi", { dob: "1990-01-15" } )
    .expireIn( 900 )
    .encrypt( secret, "dir", "A256GCM" );
```

For asymmetric JWE just pass an RSA public key and `"RSA-OAEP-256"`:

```javascript
token = jwtNew()
    .subject( "patient-456" )
    .encrypt( publicKeyPem, "RSA-OAEP-256", "A256GCM" );
```

## Defaults Apply Here Too

If `defaultSigningKey` / `defaultAlgorithm` are set in module config, you can omit the terminal arguments entirely:

```javascript
token = jwtNew().subject( "u1" ).expireIn( 3600 ).sign();
```

## Reference Tables

The full method-by-method signatures live in the [JwtBuilder Fluent API Reference](reference/fluent-api/).

## Related

* [JWTNew()](reference/built-in-functions/JWTNew.md)
* [JwtBuilder API Reference](reference/fluent-api/)
* [Signing (JWS)](signing-jws.md)
* [Encryption (JWE)](encryption-jwe.md)
