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

### Encrypt and Decrypt a Secret

Generate an AES 128 bit key and then use it to encrypt and decrypt a secret.

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

<a href="https://try.boxlang.io/?code=eJzLTq1UsFVIT81LLUosSQ1OTS5KLfFOrdRQUHLy8Q938wz2UFLQtOYqSS0ucc1LLqosKAEqT4WwgIqKE9NS4%2FNLi%2BJLilJTlXQUslMrdZC0AtlJicWpZiZwQ1xSYYakpEINQTKbgAHlRZklqS6luQUQTTCzgDIAOTM%2FrQ%3D%3D" target="_blank">Run Example</a>

```java
key = generateSecretKey( "BLOWFISH" );
testEncrypt = encrypt( "safe_our_tree", key, "BLOWFISH", "base64" );
testDecrypt = decrypt( testEncrypt, key, "BLOWFISH", "base64" );
writeDump( testDecrypt );

```



## Related

  * [DecryptBinary](./DecryptBinary.md)
  * [Encrypt](./Encrypt.md)
  * [EncryptBinary](./EncryptBinary.md)
  * [GeneratePBKDFKey](./GeneratePBKDFKey.md)
  * [GenerateSecretKey](./GenerateSecretKey.md)
  * [Hash](./Hash.md)
  * [Hash40](./Hash40.md)
  * [Hmac](./Hmac.md)
