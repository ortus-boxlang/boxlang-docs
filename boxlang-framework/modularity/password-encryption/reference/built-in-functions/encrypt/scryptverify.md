# SCryptVerify

Performs a verification of a supplied plaintext string against a hashed value.

## Method Signature

```
SCryptVerify(string=[string], hashed=[string])
```

### Arguments

| Argument | Type     | Required | Description                                              | Default |
| -------- | -------- | -------- | -------------------------------------------------------- | ------- |
| `string` | `string` | `true`   | The plaintext string to verify against the hashed value. |         |
| `hashed` | `string` | `true`   | The SCrypt hashed value to verify against.               |         |

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
* [VerifyBCryptHash](verifybcrypthash.md)
* [VerifySCryptHash](verifyscrypthash.md)
