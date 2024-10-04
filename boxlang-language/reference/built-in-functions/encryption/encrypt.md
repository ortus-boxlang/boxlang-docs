# Encrypt

Encrypts an object using the specified algorithm and key

## Method Signature

```
Encrypt(object=[any], key=[string], algorithm=[string], encoding=[string], IVorSalt=[any], iterations=[integer], precise=[boolean])
```

### Arguments

| Argument     | Type      | Required | Description                                                                                                                       | Default |
| ------------ | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `object`     | `any`     | `true`   | The object to encrypt. If the object is not a string or binary data, the object must implement the java.io.Serializable interface |         |
| `key`        | `string`  | `true`   | The string representation of the secret key to use for encryption ( see generateSecretKey() )                                     |         |
| `algorithm`  | `string`  | `false`  | The algorithm to use for encryption. Default is AES                                                                               |         |
| `encoding`   | `string`  | `false`  | The encoding type to use for encoding the encrypted data. Default is Base64                                                       | `UU`    |
| `IVorSalt`   | `any`     | `false`  | The initialization vector or salt to use for encryption.                                                                          |         |
| `iterations` | `integer` | `false`  | The number of iterations to use for encryption. Default is 1000                                                                   | `1000`  |
| `precise`    | `boolean` | `false`  | If set to true, the string and key will be validated before encryption to ensure conformity to the algorithm. Default is false    | `true`  |

## Examples

## Related

* [Decrypt](decrypt.md)
* [EncryptBinary](encryptbinary.md)
* [GeneratePDBKDFKey](generatepdbkdfkey.md)
* [GenerateSecretKey](generatesecretkey.md)
* [Hash](hash.md)
* [Hash40](hash40.md)
* [Hmac](hmac.md)
