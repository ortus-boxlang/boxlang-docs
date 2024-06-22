[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Decrypt`

Decrypts a provided encoded encrypted string using the specified algorithm and key

## Method Signature

```
Decrypt(string=[string], key=[string], algorithm=[string], encoding=[string], IVorSalt=[any], iterations=[integer], precise=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The encrypted string to decrypt |  |
| `key` | `string` | `true` | The string representation of the secret key to use for encryption ( see generateSecretKey() ) |  |
| `algorithm` | `string` | `false` | The algorithm to use for encryption. Default is AES |  |
| `encoding` | `string` | `false` | The encoding type to use for encoding the encrypted data. Default is Base64 | `UU` |
| `IVorSalt` | `any` | `false` | The initialization vector or salt to use for encryption. |  |
| `iterations` | `integer` | `false` | The number of iterations to use for encryption. Default is 1000 | `1000` |
| `precise` | `boolean` | `false` | If set to true, the string and key will be validated before encryption to ensure conformity to the algorithm. Default is false | `false` |

## Examples



## Related

  * [Encrypt](./Encrypt.md)
  * [EncryptBinary](./EncryptBinary.md)
  * [GeneratePDBKDFKey](./GeneratePDBKDFKey.md)
  * [GenerateSecretKey](./GenerateSecretKey.md)
  * [Hash](./Hash.md)
  * [Hash40](./Hash40.md)
  * [Hmac](./Hmac.md)
