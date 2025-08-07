[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CSRFGenerateToken`

Generates a random token and stores it in the session cache to protect against Cross-Site Request Forgery (CSRF) attacks.

<p>
 You can optionally provide a specific key to store in the cache, and optionally force the generation of a new token.

## Method Signature

```
CSRFGenerateToken(key=[string], forceNew=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `string` | `false` | The key to store the token under in the cache. Defaults to "default". | `default` |
| `forceNew` | `boolean` | `false` | If true, a new token will be generated and stored in the cache. Defaults to false. | `false` |

## Examples



## Related

  * [CSRFHiddenField](./CSRFHiddenField.md)
  * [CSRFRotate](./CSRFRotate.md)
  * [CSRFVerifyToken](./CSRFVerifyToken.md)
