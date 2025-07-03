# Encrypt

Encrypts an object using the specified algorithm and key

## Method Signature

```
Encrypt(object=[any], key=[string], algorithm=[string], encoding=[string], IVorSalt=[any], iterations=[integer], precise=[boolean])
```

### Arguments

| Argument     | Type      | Required | Description                                                                                                                       | Default |
| ------------ | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `object`     | `any`     | `false`  | The object to encrypt. If the object is not a string or binary data, the object must implement the java.io.Serializable interface |         |
| `key`        | `string`  | `true`   | The string representation of the secret key to use for encryption ( see generateSecretKey() )                                     |         |
| `algorithm`  | `string`  | `false`  | The algorithm to use for encryption. Default is AES                                                                               |         |
| `encoding`   | `string`  | `false`  | The encoding type to use for encoding the encrypted data. Default is Base64                                                       | `UU`    |
| `IVorSalt`   | `any`     | `false`  | The initialization vector or salt to use for encryption.                                                                          |         |
| `iterations` | `integer` | `false`  | The number of iterations to use for encryption. Default is 1000                                                                   | `1000`  |
| `precise`    | `boolean` | `false`  | If set to true, the string and key will be validated before encryption to ensure conformity to the algorithm. Default is false    | `true`  |

## Examples

### Encrypt using AES Encryption in ECB Mode

The key must be generated using the generateSecretKey("AES") function.

[Run Example](https://try.boxlang.io/?code=eJxLzUsuqiwo0VBQKskvUChOTS5KLVHSUVAKDym0qIpMjkpLDA8r881Lzkz3KCwPtLUFyTm6BoMop8TiVDMTJQVNay4APgQVPg%3D%3D)

```java
encrypt( "top secret", "WTq8zYcZfaWVvMncigHqwQ==", "AES", "Base64" );

```

Result: keciULin7bxOWvN/BOarWw==

### Encrypt using AES Cipher Block Chaining (CBC) mode

By default encrypt() uses the Electronic Code Book (ECB) mode for encryption.\
For increased security you should specify the mode and padding to use. In this example we will use CBC mode and PKCS5Padding. The value of the encrypted string will be different every time it runs because the IV is generated at random.

[Run Example](https://try.boxlang.io/?code=eJzLLU5XsFVQSkksSVQoyVdIzUsuqiwoUbLmyk6tBEqkp%2BalFiWWpAanJhellninVmooKDm6BispaFpzAdX6gnVDNWko5Ban6ygANeqAFek7OznrB3g7B5sGJKakZOalKwHFPVwjwJrLizJLUv1LSwpKgfqgJgGFAcD1LEQ%3D)

```java
msg = "data to encrypt";
key = generateSecretKey( "AES" );
encMsg = encrypt( msg, key, "AES/CBC/PKCS5Padding", "HEX" );
writeOutput( encMsg );

```

### Encrypt using AES Galois/Counter Mode (GCM)

```java
msg = "data to encrypt";
key = generateSecretKey( "AES" );
encMsg = encrypt( msg, key, "AES/GCM/NoPadding", "Base64" );
writeOutput( encMsg );

```

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJzLTq1UsFVIT81LLUosSQ1OTS5KLfFOrdRQUHJ0DVZS0LTmKkktLnHNSy6qLCgBqkyFsIDyxYlpqfmlRSVFqalKOgrZqZU6ED1AKimxONXMBKy7vCizJNWlNLdAQwHZIKAMAKC9J0k%3D)

```java
key = generateSecretKey( "AES" );
testEncrypt = encrypt( "safeourtree", key, "AES", "base64" );
writeDump( testEncrypt );

```

## Related

* [Decrypt](Decrypt.md)
* [DecryptBinary](DecryptBinary.md)
* [EncryptBinary](EncryptBinary.md)
* [GeneratePBKDFKey](GeneratePBKDFKey.md)
* [GenerateSecretKey](GenerateSecretKey.md)
* [Hash](Hash.md)
* [Hash40](Hash40.md)
* [Hmac](Hmac.md)
