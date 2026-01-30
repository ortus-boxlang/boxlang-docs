# ArgonVerify

Performs a Argon2 verification on the given string against the hashed value.

## Method Signature

```
ArgonVerify(input=[string], hashed=[string], variant=[string])
```

### Arguments

| Argument  | Type     | Required | Description                                                                                             | Default |
| --------- | -------- | -------- | ------------------------------------------------------------------------------------------------------- | ------- |
| `input`   | `string` | `true`   | The string to verify against the hash.                                                                  |         |
| `hashed`  | `string` | `true`   | The hashed value to verify against.                                                                     |         |
| `variant` | `string` | `false`  | The variant of Argon2 to use. If not provided the hashed value will be tested to determine the variant. |         |

## Examples

## Related

* [Argon2CheckHash](argon2checkhash.md)
* [ArgonHash](argonhash.md)
* [BCryptHash](bcrypthash.md)
* [BCryptVerify](bcryptverify.md)
* [GenerateArgon2Hash](generateargon2hash.md)
* [GenerateBCryptHash](generatebcrypthash.md)
* [GenerateSCryptHash](generatescrypthash.md)
* [SCryptHash](scrypthash.md)
* [SCryptVerify](scryptverify.md)
* [VerifyBCryptHash](verifybcrypthash.md)
* [VerifySCryptHash](verifyscrypthash.md)
