# GenerateSCryptHash

Returns a secure input hash of the given string using the Argon2 hashing algorithm.

## Method Signature

```
GenerateSCryptHash(input=[string], saltLength=[integer], parallelism=[integer], keySize=[integer], memory=[integer], cpuCost=[integer])
```

### Arguments

| Argument      | Type      | Required | Description                                                                               | Default |
| ------------- | --------- | -------- | ----------------------------------------------------------------------------------------- | ------- |
| `input`       | `string`  | `true`   | The string to perform secure hashing upon.                                                |         |
| `saltLength`  | `integer` | `false`  | The length of the salt to use in the hashing algorithm. Must be greated than 8.           | `8`     |
| `parallelism` | `integer` | `false`  | The number of threads to use in the hashing algorithm. Must be between 1 and 10.          | `1`     |
| `keySize`     | `integer` | `false`  | The size of the key to use in the hashing algorithm. Must be greater than 32.             | `32`    |
| `memory`      | `integer` | `false`  | The amount of memory to use in the hashing algorithm. Must be between 8 and 100000.       | `8`     |
| `cpuCost`     | `integer` | `false`  | The CPU cost to use in the hashing algorithm. Must be greater than 2 and be a power off 2 | `16384` |

## Examples

## Related

* [Argon2CheckHash](argon2checkhash.md)
* [ArgonHash](argonhash.md)
* [ArgonVerify](argonverify.md)
* [BCryptHash](bcrypthash.md)
* [BCryptVerify](bcryptverify.md)
* [GenerateArgon2Hash](generateargon2hash.md)
* [GenerateBCryptHash](generatebcrypthash.md)
* [SCryptHash](scrypthash.md)
* [SCryptVerify](scryptverify.md)
* [VerifyBCryptHash](verifybcrypthash.md)
* [VerifySCryptHash](verifyscrypthash.md)
