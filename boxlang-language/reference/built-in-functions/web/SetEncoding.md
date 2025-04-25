[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SetEncoding`

Sets the character encoding (character set) of Form and URL scope variable values; used when the character encoding of the input to a form, or the
 character encoding of a URL, is not in UTF-8 encoding.

## Method Signature

```
SetEncoding(scope_name=[string], charset=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `scope_name` | `string` | `true` | The name of the scope to set the character encoding for. |  |
| `charset` | `string` | `true` | The character encoding to set. |  |

## Examples



## Related

  * [HtmlHead](./HtmlHead.md)
  * [GetHTTPTimeString](./GetHTTPTimeString.md)
  * [GetHTTPRequestData](./GetHTTPRequestData.md)
  * [HtmlFooter](./HtmlFooter.md)
  * [Forward](./Forward.md)
  * [Location](./Location.md)
  * [GetPageContext](./GetPageContext.md)
  * [FileUpload](./FileUpload.md)
  * [FileUploadAll](./FileUploadAll.md)
