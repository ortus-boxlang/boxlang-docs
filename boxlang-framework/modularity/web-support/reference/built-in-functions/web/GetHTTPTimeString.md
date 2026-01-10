[comment]: # (Note: This documentation is generated dy[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetHTTPTimestring`

Returns the legacy HTTP TimeString as specified for the now-obsolete RFC 1123/RCF 822.

Example: `Sat, 10 Jan 2026 17:09:26 GMT`

This method should be used for legacy compatibility with older CFML engines and is not recommended for new code.
The updated specification, [RFC 2822](https://www.rfc-editor.org/rfc/rfc2822) should be used for new implemenations. ( e.g. `Sat, 10 Jan 2026 17:09:26 -0000`)



## Method Signature

```
GetHTTPTimeString(date=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `false` |  |  |

## Examples



## Related

  * [FileUpload](./FileUpload.md)
  * [FileUploadAll](./FileUploadAll.md)
  * [Forward](./Forward.md)
  * [GetHTTPRequestData](./GetHTTPRequestData.md)
  * [GetPageContext](./GetPageContext.md)
  * [HtmlFooter](./HtmlFooter.md)
  * [HtmlHead](./HtmlHead.md)
  * [Location](./Location.md)
  * [SetEncoding](./SetEncoding.md)
