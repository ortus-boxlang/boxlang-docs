[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Hash`

Creates an algorithmic hash of an object

## Method Signature
```
Hash(input=[any], algorithm=[string], encoding=[string], numIterations=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `input` | `any` | `true` | The item to be hashed |  |
| `algorithm` | `string` | `false` | The supported {@link java.security.MessageDigest} algorithm (case-insensitive) | `MD5` |
| `encoding` | `string` | `false` | Applicable to strings ( default "utf-8" ) | `utf-8` |
| `numIterations` | `integer` | `false` |  | `1` |

## Examples

```
Hash(input=[any], algorithm=[string], encoding=[string], numIterations=[integer])
```

## Related
  * [Hash40](./Hash40.md)
  * [Hmac](./Hmac.md)
