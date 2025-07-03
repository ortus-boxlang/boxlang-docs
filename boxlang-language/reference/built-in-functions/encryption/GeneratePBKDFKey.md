# GeneratePBKDFKey

Generates an encoded encryption key using the specified algorithm and key\
size

## Method Signature

```
GeneratePBKDFKey(algorithm=[string], passphrase=[string], salt=[string], iterations=[numeric], keySize=[numeric])
```

### Arguments

| Argument     | Type      | Required | Description                                                                                                                                                                       | Default |
| ------------ | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `algorithm`  | `string`  | `true`   | The algorithm to use for generating the key. Algorithms supported are: PBKDF2WithHmacSHA1, PBKDF2WithHmacSHA224, PBKDF2WithHmacSHA256, PBKDF2WithHmacSHA384, PBKDF2WithHmacSHA512 | `AES`   |
| `passphrase` | `string`  | `true`   | The passphrase to use for generating the key. This is                                                                                                                             |         |
| `salt`       | `string`  | `true`   | The salt to use for generating the key. This is a random string                                                                                                                   |         |
| `iterations` | `numeric` | `false`  | The number of iterations to use for generating the key.                                                                                                                           |         |
| `keySize`    | `numeric` | `false`  | <p>The optional size of the key to generate. If not provided<br>the default key size for the algorithm will be used</p>                                                           |         |

## Examples

### Example PBKDF2 With HMAC SHA1

The `PBKDF2WithHmacSHA1` algorithm will work on older JVMs, or older versions of CF

[Run Example](https://try.boxlang.io/?code=eJxLT81LLUosSQ1w8nZx806t1FBQAjONwjNLMjxyE5ODPRwNlXQUlIpTk4tSS8CsxJySSiDD1MDAQEfB0MhCQdOaCwA5uBR8)

```java
generatePBKDFKey( "PBKDF2WithHmacSHA1", "secret", "salty", 5000, 128 );

```

Result: Y0MCpCe3zb0CNJvyXNUWEQ==

### More complex encryption example

```java
// some variables
password = "top_secret";
dataToEncrypt = "the most closely guarded secret";
encryptionAlgorithm = "AES";
keysize = 128;
algorithmVersion = 512;
PBKDFalgorithm = "PBKDF2WithHmacSHA" & algorithmVersion;
// Generate key as recommended in docs
length = keysize / 8;
multiplicator = 10 ^ length;
salt = Round( Randomize( 5, "SHA1PRNG" ) * multiplicator );
// The magic happens here
PBKDFKey = GeneratePBKDFKey( PBKDFalgorithm, password, salt, algorithmVersion, keysize );
encryptedData = encrypt( dataToEncrypt, PBKDFKey, encryptionAlgorithm, "BASE64" );
decryptedData = decrypt( encryptedData, PBKDFKey, encryptionAlgorithm, "BASE64" );
// Output
writeOutput( "<b>Generated PBKDFKey (Base 64)</b>: " & PBKDFKey );
writeOutput( "<br /><b>Data After Encryption</b>: " & encryptedData );
writeOutput( "<br /><b>Data After Decryption</b>: " & decryptedData );

```

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxLKc0t0FBIT81LLUosSQ1w8nZx806t1FBQAjONwjNLMjxyE5ODPRwNlXQUlIpTk4tSS8CsxJySSiDD1MDAQEfB0MhCQVNB05pLQV9fIdLA17nAOdW4KsnA2c%2BrrDLCLzTcNdDWlgsACv4fBw%3D%3D)

```java
dump( generatePBKDFKey( "PBKDF2WithHmacSHA1", "secret", "salty", 5000, 128 ) );
 // Y0MCpCe3zb0CNJvyXNUWEQ==

```

## Related

* [Decrypt](Decrypt.md)
* [DecryptBinary](DecryptBinary.md)
* [Encrypt](Encrypt.md)
* [EncryptBinary](EncryptBinary.md)
* [GenerateSecretKey](GenerateSecretKey.md)
* [Hash](Hash.md)
* [Hash40](Hash40.md)
* [Hmac](Hmac.md)
