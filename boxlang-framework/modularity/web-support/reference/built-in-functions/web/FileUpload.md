[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileUpload`

Processes file uploads from the request

## Method Signature

```
FileUpload(destination=[string], filefield=[string], accept=[string], nameconflict=[string], strict=[boolean], allowedExtensions=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `destination` | `string` | `true` | The destination directory for the uploaded files. |  |
| `filefield` | `string` | `false` | The name of the file field to process. |  |
| `accept` | `string` | `false` | The accepted MIME types for the uploaded files. |  |
| `nameconflict` | `string` | `false` | The action to take when a file with the same name already exists in the destination directory. | `error` |
| `strict` | `boolean` | `false` | Whether to strictly enforce the system specified upload security settings. | `true` |
| `allowedExtensions` | `string` | `false` | The allowed file extensions for the uploaded files. |  |

## Examples



## Related

  * [FileUploadAll](./FileUploadAll.md)
  * [Forward](./Forward.md)
  * [GetHTTPRequestData](./GetHTTPRequestData.md)
  * [GetHTTPTimeString](./GetHTTPTimeString.md)
  * [GetPageContext](./GetPageContext.md)
  * [HtmlFooter](./HtmlFooter.md)
  * [HtmlHead](./HtmlHead.md)
  * [Location](./Location.md)
  * [SetEncoding](./SetEncoding.md)
