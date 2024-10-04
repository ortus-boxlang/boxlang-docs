# GenerateSecretKey

Generates an encoded encryption key using the specified algorithm and key size

## Method Signature

```
GenerateSecretKey(algorithm=[string], keySize=[numeric])
```

### Arguments

| Argument    | Type      | Required | Description                                                                                                                                                                | Default |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `algorithm` | `string`  | `false`  | <p>The algorithm to use for generating the key. The default<br>is AES. Example values are: AES, DES, DESede, Blowfish,<br>HmacSHA1, HmacSHA256, HmacSHA384, HmacSHA512</p> | `AES`   |
| `keySize`   | `numeric` | `false`  | <p>The optional size of the key to generate. If not provided<br>the default key size for the algorithm will be used</p>                                                    |         |

## Examples

## Related

* [Decrypt](decrypt.md)
* [Encrypt](encrypt.md)
* [EncryptBinary](encryptbinary.md)
* [GeneratePDBKDFKey](generatepdbkdfkey.md)
* [Hash](hash.md)
* [Hash40](hash40.md)
* [Hmac](hmac.md)
