[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GenerateSecretKey`

Generates an encoded encryption key using the specified algorithm and key
 size

## Method Signature

```
GenerateSecretKey(algorithm=[string], keySize=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `algorithm` | `string` | `false` | The algorithm to use for generating the key. The default<br>                     is AES. Example values are: AES, DES, DESede, Blowfish,<br>                     HmacSHA1, HmacSHA256, HmacSHA384, HmacSHA512 | `AES` |
| `keySize` | `numeric` | `false` | The optional size of the key to generate. If not provided<br>                   the default key size for the algorithm will be used |  |

## Examples

### Generate an AES 128 bit Key

Generate an AES key and use it to encrypt and decrypt a secret.

<a href="https://try.boxlang.io/?code=eJxLrVCwVaiuteZKrdDzdo0EctJT81KLEktSg1OTi1JLvFMrNRSUHF2DlRQ0wYqCXZ2DXEOA6pRK8gsUisGKlMAyrn7OQZEBIa4uQMnUvOSiyoISDQW4Dh0FiA06ENOAlFNicaqZCcxcF1eE7pRUhG64qXgNKC%2FKLEl1Kc0tAOkBCQAA8t497g%3D%3D" target="_blank">Run Example</a>

```java
ex = {};
ex.KEY = generateSecretKey( "AES" );
ex.SECRET = "top secret";
ex.ENCRYPTED = encrypt( ex.SECRET, ex.KEY, "AES", "Base64" );
ex.DECRYPTED = decrypt( ex.ENCRYPTED, ex.KEY, "AES", "Base64" );
writeDump( ex );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLrVCwVaiuteZKrdBz9HH3B%2FKUgpxNlMACYY4%2Boa4gEVNTE0MjI4igt2skUMg9NS%2B1KLEkNTg1uSi1xDu1UkMBZoImWJmrnzNQmWteclFlQQlYEmyajgLECB005S6uIOUuqQjlQAOwKk4pzS0AKQCxAaeBNOk%3D" target="_blank">Run Example</a>

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

  * [Decrypt](./Decrypt.md)
  * [DecryptBinary](./DecryptBinary.md)
  * [Hash](./Hash.md)
  * [Hash40](./Hash40.md)
  * [Encrypt](./Encrypt.md)
  * [EncryptBinary](./EncryptBinary.md)
  * [Hmac](./Hmac.md)
  * [GeneratePBKDFKey](./GeneratePBKDFKey.md)
