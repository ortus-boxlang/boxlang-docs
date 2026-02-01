# GenerateBCryptHash

Performs a BCrypt hash on the given string.

## Method Signature

```
GenerateBCryptHash(input=[string], iterations=[integer])
```

### Arguments

| Argument     | Type      | Required | Description                                                                                                                                                                                | Default |
| ------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `input`      | `string`  | `true`   | The string to perform secure hashing upon.                                                                                                                                                 |         |
| `iterations` | `integer` | `false`  | <p>The number of iterations to use in the hashing algorithm. Must be a multiple of 2 and between 2 and 30.<br>Note that a high number of iterations can take <em>days</em> to complete</p> |         |

## Examples

## Related

* [Argon2CheckHash](argon2checkhash.md)
* [ArgonHash](argonhash.md)
* [ArgonVerify](argonverify.md)
* [BCryptHash](bcrypthash.md)
* [BCryptVerify](bcryptverify.md)
* [GenerateArgon2Hash](generateargon2hash.md)
* [GenerateSCryptHash](generatescrypthash.md)
* [SCryptHash](scrypthash.md)
* [SCryptVerify](scryptverify.md)
* [VerifyBCryptHash](verifybcrypthash.md)
* [VerifySCryptHash](verifyscrypthash.md)
