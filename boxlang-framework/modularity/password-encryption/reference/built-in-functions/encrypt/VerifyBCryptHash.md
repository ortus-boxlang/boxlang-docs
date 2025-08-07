[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `VerifyBCryptHash`

Verifies a BCrypt hash against a plaintext string.

## Method Signature

```
VerifyBCryptHash(string=[string], hashed=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The plaintext string to verify against the hashed value. |  |
| `hashed` | `string` | `true` | The BCrypt hashed value to verify against. |  |

## Examples



## Related

  * [Argon2CheckHash](./Argon2CheckHash.md)
  * [ArgonHash](./ArgonHash.md)
  * [ArgonVerify](./ArgonVerify.md)
  * [BCryptHash](./BCryptHash.md)
  * [BCryptVerify](./BCryptVerify.md)
  * [GenerateArgon2Hash](./GenerateArgon2Hash.md)
  * [GenerateBCryptHash](./GenerateBCryptHash.md)
  * [GenerateSCryptHash](./GenerateSCryptHash.md)
  * [SCryptHash](./SCryptHash.md)
  * [SCryptVerify](./SCryptVerify.md)
  * [VerifySCryptHash](./VerifySCryptHash.md)
