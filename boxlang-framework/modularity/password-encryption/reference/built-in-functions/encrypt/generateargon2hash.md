# GenerateArgon2Hash

Returns a secure input hash of the given string using the Argon2 hashing algorithm.

## Method Signature

```
GenerateArgon2Hash(input=[string], variant=[string], parallelism=[integer], memory=[integer], iterations=[integer])
```

### Arguments

| Argument      | Type      | Required | Description                                                                         | Default   |
| ------------- | --------- | -------- | ----------------------------------------------------------------------------------- | --------- |
| `input`       | `string`  | `true`   | The string to perform secure hashing upon.                                          |           |
| `variant`     | `string`  | `false`  | The Argon2 variant to use. Defaults to "ARGON2i".                                   | `ARGON2i` |
| `parallelism` | `integer` | `false`  | The number of threads to use in the hashing algorithm. Must be between 1 and 10.    | `1`       |
| `memory`      | `integer` | `false`  | The amount of memory to use in the hashing algorithm. Must be between 8 and 100000. | `8`       |
| `iterations`  | `integer` | `false`  | The number of iterations to use in the hashing algorithm. Must be between 1 and 20. | `8`       |

## Examples

## Related

* [Argon2CheckHash](argon2checkhash.md)
* [ArgonHash](argonhash.md)
* [ArgonVerify](argonverify.md)
* [BCryptHash](bcrypthash.md)
* [BCryptVerify](bcryptverify.md)
* [GenerateBCryptHash](generatebcrypthash.md)
* [GenerateSCryptHash](generatescrypthash.md)
* [SCryptHash](scrypthash.md)
* [SCryptVerify](scryptverify.md)
* [VerifyBCryptHash](verifybcrypthash.md)
* [VerifySCryptHash](verifyscrypthash.md)
