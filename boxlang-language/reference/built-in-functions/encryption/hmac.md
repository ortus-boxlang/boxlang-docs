# Hmac

Creates an algorithmic hash of an object

## Method Signature

```
Hmac(input=[any], key=[string], algorithm=[string], encoding=[string], numIterations=[integer])
```

### Arguments

| Argument        | Type      | Required | Description                                                                    | Default   |
| --------------- | --------- | -------- | ------------------------------------------------------------------------------ | --------- |
| `input`         | `any`     | `true`   | The item to be hashed                                                          |           |
| `key`           | `string`  | `true`   |                                                                                |           |
| `algorithm`     | `string`  | `false`  | The supported {@link java.security.MessageDigest} algorithm (case-insensitive) | `HmacMD5` |
| `encoding`      | `string`  | `false`  | Applicable to strings ( default "utf-8" )                                      | `utf-8`   |
| `numIterations` | `integer` | `false`  |                                                                                | `1`       |

## Examples

## Related

* [Decrypt](decrypt.md)
* [Encrypt](encrypt.md)
* [EncryptBinary](encryptbinary.md)
* [GeneratePDBKDFKey](generatepdbkdfkey.md)
* [GenerateSecretKey](generatesecretkey.md)
* [Hash](hash.md)
* [Hash40](hash40.md)
