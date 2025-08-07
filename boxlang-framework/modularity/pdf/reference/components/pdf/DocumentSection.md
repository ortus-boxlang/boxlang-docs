
# Component: `DocumentSection`

Divides a PDF document into sections.

## Component Signature

```
<bx:DocumentSection marginBottom=[numeric]
marginLeft=[numeric]
marginRight=[numeric]
marginTop=[numeric]
mimeType=[string]
name=[string]
srcfile=[string]
src=[string]
userAgent=[string]
authPassword=[string]
authUser=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `marginBottom` | `numeric` | `false` | The bottom margin of the section in the unit specified in the `document` component. |  |
| `marginLeft` | `numeric` | `false` | The left margin of the section in the unit specified in the `document` component. |  |
| `marginRight` | `numeric` | `false` | The right margin of the section in the unit specified in the `document` component. |  |
| `marginTop` | `numeric` | `false` | The top margin of the section in the unit specified in the `document` component. |  |
| `mimeType` | `string` | `false` | The mime type of the content.  If the content is a file, the mime type is determined by the file extension.  If the content is a URL, the mime type is determined by the HTTP response. |  |
| `name` | `string` | `false` | The name of the section.  This is used as a bookmark for the section. |  |
| `srcfile` | `string` | `false` | The absolute path of the file to include in the section. |  |
| `src` | `string` | `false` | The URL or path relative to the web root of the content to include in the section. |  |
| `userAgent` | `string` | `false` | The HTTP user agent identifier to use when fetching the content from a URL. Not currently implemented |  |
| `authPassword` | `string` | `false` | The authentication password to use when fetching the content from a URL. Not currently implemented |  |
| `authUser` | `string` | `false` | The authentication user name to use when fetching the content from a URL. Not currently implemented |  |

## Examples


