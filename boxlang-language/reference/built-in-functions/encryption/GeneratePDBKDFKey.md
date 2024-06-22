[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GeneratePDBKDFKey`

Generates an encoded encryption key using the specified algorithm and key
 size

## Method Signature

```
GeneratePDBKDFKey(algorithm=[string], keySize=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `algorithm` | `string` | `false` | The algorithm to use for generating the key. The default<br>                     is AES. Example values are: AES, DES, DESede, Blowfish,<br>                     HmacSHA1, HmacSHA256, HmacSHA384, HmacSHA512 | `AES` |
| `keySize` | `numeric` | `false` | The optional size of the key to generate. If not provided<br>                   the default key size for the algorithm will be used |  |

## Examples



## Related

  * [Decrypt](./Decrypt.md)
  * [Encrypt](./Encrypt.md)
  * [EncryptBinary](./EncryptBinary.md)
  * [GenerateSecretKey](./GenerateSecretKey.md)
  * [Hash](./Hash.md)
  * [Hash40](./Hash40.md)
  * [Hmac](./Hmac.md)
