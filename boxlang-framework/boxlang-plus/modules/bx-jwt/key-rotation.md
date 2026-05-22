---
description: Rotate JWT signing keys without invalidating in-flight tokens using the kid header.
---

# Key Rotation

Rotating signing keys regularly is a security must — limits the blast radius if a key leaks, and gives you a clean break from compromised algorithms. The `kid` (key ID) JOSE header makes this safe: each token carries the ID of the key that signed it, and verifiers look up the right key dynamically.

`bx-jwt` makes this pattern straightforward by combining the [named key registry](key-management.md) with [`jwtDecode()`](reference/built-in-functions/JWTDecode.md).

## The Rotation Pattern

1. **Stamp the `kid` header** when issuing — tells consumers which key signed the token.
2. **Decode without verifying** when consuming — read the `kid` to pick the right key.
3. **Verify with the selected key** — never trust the decoded claims until verification succeeds.

```javascript
// 1. Sign with kid stamped in the header
token = jwtCreate( { sub: "u1" }, "api-signing-v2", "RS256", {
    headers: { kid: "v2" }
} );

// or with the fluent builder
token = jwtNew()
    .subject( "u1" )
    .expireIn( 3600 )
    .header( "kid", "v2" )
    .sign( "api-signing-v2", "RS256" );
```

```javascript
// 2 + 3. Verify with the right key per token
function verifyWithKeyRotation( token ) {
    var decoded = jwtDecode( token );           // header only — claims NOT trusted yet
    var kid     = decoded.header.kid ?: "default";
    return jwtVerify( token, kid, decoded.header.alg );   // looks up "kid" in the registry
}
```

## Registry-Driven Rotation

Keep multiple key versions in the registry. Active key signs new tokens; older keys remain available so existing tokens still verify until they expire.

```javascript
settings = {
    keys : {
        "api-signing-v1" : { algorithm: "RS256", privateKey: "/etc/keys/v1.pem", publicKey: "/etc/keys/v1-pub.pem" },
        "api-signing-v2" : { algorithm: "RS256", privateKey: "/etc/keys/v2.pem", publicKey: "/etc/keys/v2-pub.pem" }
    },
    defaultSigningKey : "api-signing-v2"   // new tokens signed with v2
}
```

When you cut over:

1. Add `api-signing-v2` to the registry.
2. Update `defaultSigningKey` (or the explicit name passed to `jwtCreate()`).
3. Stamp the new `kid` in the header.
4. Leave `api-signing-v1` in place until the longest-lived existing token has expired.
5. Remove `v1` from the registry.

## Verifying Tokens From External Issuers

The same pattern handles third-party tokens — register their public keys with the `kid` they advertise:

```javascript
keys : {
    "partner-2025-01" : { algorithm: "RS256", publicKey: "/etc/keys/partner-2025-01.pem" },
    "partner-2025-04" : { algorithm: "RS256", publicKey: "/etc/keys/partner-2025-04.pem" }
}
```

```javascript
function verifyPartnerToken( token ) {
    var decoded = jwtDecode( token );
    return jwtVerify( token, "partner-" & decoded.header.kid, "RS256" );
}
```

## Runtime Rotation From a KMS

If your keys come from a key-management service, register them at runtime through `JWTService`:

```javascript
jwtService = getBoxContext().getRuntime().getGlobalService( "JWTService" );

newMaterial = fetchFromVault( "api-signing-v3" );
jwtService.registerKey( "api-signing-v3", {
    algorithm  : "RS256",
    privateKey : newMaterial.private,
    publicKey  : newMaterial.public
} );
```

## Caveats

* **Always decode before verifying.** Treat `kid` as a lookup hint — never authoritatively trust anything in `jwtDecode()`'s output.
* **Constrain the algorithm.** Use [`allowedAlgorithms`](security-best-practices.md) so an attacker cannot substitute an unexpected algorithm by changing the token header.
* **Default to a safe fallback.** If `kid` is missing or unknown, reject the token — do not silently fall back to a primary key.

## Related

* [Key Management](key-management.md)
* [Security Best Practices](security-best-practices.md)
* [JWTDecode()](reference/built-in-functions/JWTDecode.md)
* [JWTVerify()](reference/built-in-functions/JWTVerify.md)
