
# Component: `Document`

Component to generate PDF documents from HTML content

## Component Signature

```
<bx:Document format=[string]
encryption=[string]
localUrl=[boolean]
variable=[string]
backgroundVisible=[boolean]
bookmark=[boolean]
htmlBookmark=[boolean]
orientation=[string]
scale=[integer]
marginBottom=[double]
marginLeft=[double]
marginRight=[double]
marginTop=[double]
pageWidth=[double]
pageHeight=[double]
fontEmbed=[boolean]
fontDirectory=[string]
openpassword=[string]
ownerPassword=[string]
pageType=[string]
pdfa=[string]
filename=[string]
overwrite=[string]
saveAsName=[string]
src=[string]
srcfile=[string]
mimeType=[string]
unit=[string]
permissions=[string]
permissionspassword=[string]
userPassword=[string]
authPassword=[string]
authUser=[string]
userAgent=[string]
proxyHost=[string]
proxyPassword=[string]
proxyPort=[string]
proxyUser=[string]
tagged=[string]
formfields=[string]
formsType=[string]
name=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `false` | [Deprecated] The format of the document to generate. This attribute is deprecated and will be removed in a future release as only PDF generation is supported | `pdf` |
| `encryption` | `string` | `false` | The encryption level to use for the document. Default is none. Possible values are 128-bit, 40-bit, none | `none` |
| `localUrl` | `boolean` | `false` | If true, the document will be generated with local URLs. Default is false | `false` |
| `variable` | `string` | `false` | The name of the variable to store the generated PDF binary |  |
| `backgroundVisible` | `boolean` | `false` | If true, the background will be visible. Default is true | `true` |
| `bookmark` | `boolean` | `false` | If true, bookmarks will be generated. Default is true | `true` |
| `htmlBookmark` | `boolean` | `false` | If true, it is possible to convert outlines to a list of named anchors (<a name="anchor_id">label</a>) or a headings structure ( <h1>... <h6>). Transforming of HTML hyperlinks to PDF hyperlinks (if not explicitly disabled). Hyperlink jumps within the same document are supported as well | `false` |
| `orientation` | `string` | `false` | The orientation of the document. Default is portrait. Possible values are portrait, landscape | `portrait` |
| `scale` | `integer` | `false` | The percentage to scale the document. Must be less than 100 |  |
| `marginBottom` | `double` | `false` | The bottom margin of the document |  |
| `marginLeft` | `double` | `false` | The left margin of the document |  |
| `marginRight` | `double` | `false` | The right margin of the document |  |
| `marginTop` | `double` | `false` | The top margin of the document |  |
| `pageWidth` | `double` | `false` | The width of the page in inches |  |
| `pageHeight` | `double` | `false` | The height of the page in inches |  |
| `fontEmbed` | `boolean` | `false` | If true, fonts will be embedded in the document. Default is true | `true` |
| `fontDirectory` | `string` | `false` | The directory where fonts are located |  |
| `openpassword` | `string` | `false` | The password to open protected documents |  |
| `ownerPassword` | `string` | `false` | The password to access restricted permissions |  |
| `pageType` | `string` | `false` | The type of page to generate. Default is A4. |  |
| `pdfa` | `string` | `false` | If true, the document will be generated as a PDF/A document. Default is false | `false` |
| `filename` | `string` | `false` | The filename to write the PDF to |  |
| `overwrite` | `string` | `false` | If true, the file will be overwritten if it exists. Default is false | `false` |
| `saveAsName` | `string` | `false` | The name to save the PDF as in the browser |  |
| `src` | `string` | `false` | A full URL or path relative to the web root of the source |  |
| `srcfile` | `string` | `false` | The absolute path to a source file |  |
| `mimeType` | `string` | `false` | The mime type of the source. Default is text/html. Possible values are text/html, text/plain, application/xml, image/jpeg, image/png, image/bmp, image/gif | `text/html` |
| `unit` | `string` | `false` | The unit of measurement to use. Default is inches. Possible values are in, cm | `in` |
| `permissions` | `string` | `false` |  |  |
| `permissionspassword` | `string` | `false` |  |  |
| `userPassword` | `string` | `false` |  |  |
| `authPassword` | `string` | `false` |  |  |
| `authUser` | `string` | `false` |  |  |
| `userAgent` | `string` | `false` |  |  |
| `proxyHost` | `string` | `false` |  |  |
| `proxyPassword` | `string` | `false` |  |  |
| `proxyPort` | `string` | `false` |  |  |
| `proxyUser` | `string` | `false` |  |  |
| `tagged` | `string` | `false` |  |  |
| `formfields` | `string` | `false` |  |  |
| `formsType` | `string` | `false` |  |  |
| `name` | `string` | `false` |  |  |

## Examples


