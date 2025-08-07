[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Location`

Relocates to a different pages.

## Method Signature

```
Location(URL=[string], addToken=[boolean], statusCode=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` | The URL of web page to open. |  |
| `addToken` | `boolean` | `false` | clientManagement must be enabled. |  |
| `statusCode` | `integer` | `false` | The HTTP status code.<br>                      Values:<br>                      - 300<br>                      - 301<br>                      - 302<br>                      - 303<br>                      - 304<br>                      - 305<br>                      - 306<br>                      - 307 | `302` |

## Examples



## Related

  * [FileUpload](./FileUpload.md)
  * [FileUploadAll](./FileUploadAll.md)
  * [Forward](./Forward.md)
  * [GetHTTPRequestData](./GetHTTPRequestData.md)
  * [GetHTTPTimeString](./GetHTTPTimeString.md)
  * [GetPageContext](./GetPageContext.md)
  * [HtmlFooter](./HtmlFooter.md)
  * [HtmlHead](./HtmlHead.md)
  * [SetEncoding](./SetEncoding.md)
