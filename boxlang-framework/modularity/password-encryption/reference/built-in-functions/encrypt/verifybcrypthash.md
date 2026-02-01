# VerifyBCryptHash

Verifies a BCrypt hash against a plaintext string.

## Method Signature

```
VerifyBCryptHash(string=[string], hashed=[string])
```

### Arguments

| Argument | Type     | Required | Description                                              | Default |
| -------- | -------- | -------- | -------------------------------------------------------- | ------- |
| `string` | `string` | `true`   | The plaintext string to verify against the hashed value. |         |
| `hashed` | `string` | `true`   | The BCrypt hashed value to verify against.               |         |

## Examples

## Related

* [Argon2CheckHash](argon2checkhash.md)
* [ArgonHash](argonhash.md)
* [ArgonVerify](argonverify.md)
* [BCryptHash](bcrypthash.md)
* [BCryptVerify](bcryptverify.md)
* [GenerateArgon2Hash](generateargon2hash.md)
* [GenerateBCryptHash](generatebcrypthash.md)
* [GenerateSCryptHash](generatescrypthash.md)
* [SCryptHash](scrypthash.md)
* [SCryptVerify](scryptverify.md)
* [VerifySCryptHash](verifyscrypthash.md)
