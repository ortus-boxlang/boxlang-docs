[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArgonHash`

Returns a secure input hash of the given string using the Argon2 hashing algorithm.

## Method Signature

```
ArgonHash(input=[string], variant=[string], parallelism=[integer], memory=[integer], iterations=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `input` | `string` | `true` | The string to perform secure hashing upon. |  |
| `variant` | `string` | `false` | The Argon2 variant to use. Defaults to "ARGON2i". | `ARGON2i` |
| `parallelism` | `integer` | `false` | The number of threads to use in the hashing algorithm. Must be between 1 and 10. | `1` |
| `memory` | `integer` | `false` | The amount of memory to use in the hashing algorithm. Must be between 8 and 100000. | `8` |
| `iterations` | `integer` | `false` | The number of iterations to use in the hashing algorithm. Must be between 1 and 20. | `8` |

## Examples



## Related

  * [Argon2CheckHash](./Argon2CheckHash.md)
  * [ArgonVerify](./ArgonVerify.md)
  * [BCryptHash](./BCryptHash.md)
  * [BCryptVerify](./BCryptVerify.md)
  * [GenerateArgon2Hash](./GenerateArgon2Hash.md)
  * [GenerateBCryptHash](./GenerateBCryptHash.md)
  * [GenerateSCryptHash](./GenerateSCryptHash.md)
  * [SCryptHash](./SCryptHash.md)
  * [SCryptVerify](./SCryptVerify.md)
  * [VerifyBCryptHash](./VerifyBCryptHash.md)
  * [VerifySCryptHash](./VerifySCryptHash.md)
