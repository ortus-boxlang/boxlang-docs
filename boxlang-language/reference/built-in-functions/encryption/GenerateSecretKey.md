# GenerateSecretKey

Generates an encoded encryption key using the specified algorithm and key\
size

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

### Generate an AES 128 bit Key

Generate an AES key and use it to encrypt and decrypt a secret.

[Run Example](https://try.boxlang.io/?code=eJxLrVCwVaiuteZKrdDzdo0EctJT81KLEktSg1OTi1JLvFMrNRSUHF2DlRQ0wYqCXZ2DXEOA6pRK8gsUisGKlMAyrn7OQZEBIa4uQMnUvOSiyoISDQW4Dh0FiA06ENOAlFNicaqZCcxcF1eE7pRUhG64qXgNKC%2FKLEl1Kc0tAOkBCQAA8t497g%3D%3D)

```java
ex = {};
ex.KEY = generateSecretKey( "AES" );
ex.SECRET = "top secret";
ex.ENCRYPTED = encrypt( ex.SECRET, ex.KEY, "AES", "Base64" );
ex.DECRYPTED = decrypt( ex.ENCRYPTED, ex.KEY, "AES", "Base64" );
writeDump( ex );

```

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxLrVCwVaiuteZKrdBz9HH3B%2FKUgpxNlMACYY4%2Boa4gEVNTE0MjI4igt2skUMg9NS%2B1KLEkNTg1uSi1xDu1UkMBZoImWJmrnzNQmWteclFlQQlYEmyajgLECB005S6uIOUuqQjlQAOwKk4pzS0AKQCxAaeBNOk%3D)

```java
ex = {};
ex.ALGO = "RC4";
ex.VALUE = "554122";
ex.KEY = GenerateSecretKey( ex.ALGO );
ex.ENC = Encrypt( ex.VALUE, ex.KEY, ex.ALGO );
ex.DEC = Decrypt( ex.ENC, ex.KEY, ex.ALGO );
dump( ex );

```

## Related

* [Decrypt](Decrypt.md)
* [DecryptBinary](DecryptBinary.md)
* [Encrypt](Encrypt.md)
* [EncryptBinary](EncryptBinary.md)
* [GeneratePBKDFKey](GeneratePBKDFKey.md)
* [Hash](Hash.md)
* [Hash40](Hash40.md)
* [Hmac](Hmac.md)
