[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CSRFHiddenField`

Generates a random token and stores it in the session cache to protect against Cross-Site Request Forgery (CSRF) attacks.

<p>
 However, this method returns a hidden input field named "csrf"

 <pre>
 #CSRFHiddenField()#
 </pre>

## Method Signature

```
CSRFHiddenField(key=[string], forceNew=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `string` | `false` | The key to store the token under in the cache. Defaults to "default". | `default` |
| `forceNew` | `boolean` | `false` | If true, a new token will be generated and stored in the cache. Defaults to false. | `false` |

## Examples



## Related

  * [CSRFGenerateToken](./CSRFGenerateToken.md)
  * [CSRFRotate](./CSRFRotate.md)
  * [CSRFVerifyToken](./CSRFVerifyToken.md)
