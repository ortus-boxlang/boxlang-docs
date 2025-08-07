[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GenerateBCryptHash`

Performs a BCrypt hash on the given string.

## Method Signature

```
GenerateBCryptHash(input=[string], iterations=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `input` | `string` | `true` | The string to perform secure hashing upon. |  |
| `iterations` | `integer` | `false` | The number of iterations to use in the hashing algorithm. Must be a multiple of 2 and between 2 and 30.<br>                      Note that a high number of iterations can take _days_ to complete |  |

## Examples



## Related

  * [Argon2CheckHash](./Argon2CheckHash.md)
  * [ArgonHash](./ArgonHash.md)
  * [ArgonVerify](./ArgonVerify.md)
  * [BCryptHash](./BCryptHash.md)
  * [BCryptVerify](./BCryptVerify.md)
  * [GenerateArgon2Hash](./GenerateArgon2Hash.md)
  * [GenerateSCryptHash](./GenerateSCryptHash.md)
  * [SCryptHash](./SCryptHash.md)
  * [SCryptVerify](./SCryptVerify.md)
  * [VerifyBCryptHash](./VerifyBCryptHash.md)
  * [VerifySCryptHash](./VerifySCryptHash.md)
