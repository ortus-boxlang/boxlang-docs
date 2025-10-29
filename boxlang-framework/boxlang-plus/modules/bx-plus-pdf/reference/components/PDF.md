# PDF

The PDF component is used to manipulate existing PDF documents or create new ones.

{% include "../../../../../../.gitbook/includes/bx-plus-functionality-notice.md" %}

## Component Signature

```
<bx:PDF action=[string]
ascending=[boolean]
type=[string]
ddxfile=[string]
destination=[string]
directory=[string]
encrypt=[string]
flatten=[boolean]
image=[any]
filter=[string]
info=[struct]
inputfiles=[struct]
keepbookmark=[boolean]
name=[string]
opacity=[double]
order=[string]
outputfiles=[struct]
overwrite=[boolean]
pages=[string]
newOwnerPassword=[string]
newUserPassword=[string]
password=[string]
permissions=[string]
saveoption=[string]
showonprint=[boolean]
source=[any]
stoponerror=[boolean]
version=[double]
text=[string]
numberformat=[string]
align=[string]
leftmargin=[numeric]
rightmargin=[numeric]
topmargin=[numeric]
bottommargin=[numeric]
format=[string]
imageprefix=[string]
resolution=[string]
transparent=[boolean]
overridepage=[boolean]
hires=[boolean]
scale=[double]
position=[double]
rotation=[double]
hscale=[double]
vscale=[double]
foreground=[boolean]
isbase64=[boolean]
copyfrom=[any]
exportTo=[string]
importFrom=[string]
encodeall=[boolean] />
```

### Attributes

| Atrribute          | Type      | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        | Default   |
| ------------------ | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `action`           | `string`  | `false`  | <p>String - The action to perform on the PDF document.<br>Supported values: addheader, addfooter, addwatermark, deletepages,<br>export, extracttext, extractimage, getinfo, import, merge, protect,<br>read, removepassword, removewatermark, removeheaderfooter,<br>sanitize, setinfo, sign, thumbnail, transform, unsign,<br>validatesignature, write.<br>NOTE: Some actions are not yet implemented and will throw a NOT_IMPLEMENTED error.</p> | `open`    |
| `ascending`        | `boolean` | `false`  | Boolean - Sort order for operations. Default: true.                                                                                                                                                                                                                                                                                                                                                                                                | `true`    |
| `type`             | `string`  | `false`  | <p>String - The type of operation or format. Used with export/import<br>actions to specify the data format (e.g., "fdf", "xfdf").</p>                                                                                                                                                                                                                                                                                                              |           |
| `ddxfile`          | `string`  | `false`  | <p>String - DDX file path for processddx operations.<br>NOTE: processddx action is not yet implemented.</p>                                                                                                                                                                                                                                                                                                                                        |           |
| `destination`      | `string`  | `false`  | <p>String - The destination file path for output operations.<br>Used with actions like extracttext, write, and export.</p>                                                                                                                                                                                                                                                                                                                         |           |
| `directory`        | `string`  | `false`  | <p>String - The directory path for operations that create multiple files,<br>such as thumbnail generation or image extraction.</p>                                                                                                                                                                                                                                                                                                                 |           |
| `encrypt`          | `string`  | `false`  | String - Encryption settings for PDF operations.                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| `flatten`          | `boolean` | `false`  | Boolean - Whether to flatten form fields. Default: false.                                                                                                                                                                                                                                                                                                                                                                                          | `false`   |
| `image`            | `any`     | `false`  | Any - Image data or file path for watermark operations.                                                                                                                                                                                                                                                                                                                                                                                            |           |
| `filter`           | `string`  | `false`  | String - Filter criteria for extraction operations.                                                                                                                                                                                                                                                                                                                                                                                                |           |
| `info`             | `struct`  | `false`  | Struct - Document information structure for setinfo operations.                                                                                                                                                                                                                                                                                                                                                                                    |           |
| `inputfiles`       | `struct`  | `false`  | Struct - Input file mappings for batch operations.                                                                                                                                                                                                                                                                                                                                                                                                 |           |
| `keepbookmark`     | `boolean` | `false`  | Boolean - Whether to preserve bookmarks during operations.                                                                                                                                                                                                                                                                                                                                                                                         |           |
| `name`             | `string`  | `false`  | <p>String - The name of the variable to store the result in.<br>Alternative to destination for storing output in memory.</p>                                                                                                                                                                                                                                                                                                                       |           |
| `opacity`          | `double`  | `false`  | Double - Opacity level for watermarks (0.0 to 1.0). Default: 0.5.                                                                                                                                                                                                                                                                                                                                                                                  | `0.5`     |
| `order`            | `string`  | `false`  | String - Ordering specification for merge operations.                                                                                                                                                                                                                                                                                                                                                                                              |           |
| `outputfiles`      | `struct`  | `false`  | Struct - Output file mappings for batch operations.                                                                                                                                                                                                                                                                                                                                                                                                |           |
| `overwrite`        | `boolean` | `false`  | Boolean - Whether to overwrite existing files. Default: false.                                                                                                                                                                                                                                                                                                                                                                                     | `false`   |
| `pages`            | `string`  | `false`  | <p>String - Specifies which pages to operate on. Can be page ranges<br>like "1-5", individual pages like "1,3,5", or "*" for all pages.<br>Required for addheader, addfooter, and deletepages actions.</p>                                                                                                                                                                                                                                         |           |
| `newOwnerPassword` | `string`  | `false`  | <p>String - The new owner password when protecting a PDF.<br>Required for the protect action.</p>                                                                                                                                                                                                                                                                                                                                                  |           |
| `newUserPassword`  | `string`  | `false`  | String - The new user password when protecting a PDF.                                                                                                                                                                                                                                                                                                                                                                                              |           |
| `password`         | `string`  | `false`  | String - The password for encrypted PDF documents.                                                                                                                                                                                                                                                                                                                                                                                                 |           |
| `permissions`      | `string`  | `false`  | String - The permissions to set when protecting a PDF document.                                                                                                                                                                                                                                                                                                                                                                                    |           |
| `saveoption`       | `string`  | `false`  | String - Save options for write operations.                                                                                                                                                                                                                                                                                                                                                                                                        |           |
| `showonprint`      | `boolean` | `false`  | Boolean - Whether watermark shows when printing.                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| `source`           | `any`     | `false`  | <p>Any - The source PDF document(s) to operate on. Can be a file path,<br>binary data, or PDF document variable.</p>                                                                                                                                                                                                                                                                                                                               |           |
| `stoponerror`      | `boolean` | `false`  | Boolean - Whether to stop processing on first error.                                                                                                                                                                                                                                                                                                                                                                                               |           |
| `version`          | `double`  | `false`  | Double - PDF version to use for output documents.                                                                                                                                                                                                                                                                                                                                                                                                  |           |
| `text`             | `string`  | `false`  | String - Text content for header/footer operations.                                                                                                                                                                                                                                                                                                                                                                                                |           |
| `numberformat`     | `string`  | `false`  | <p>String - Number format for page numbering in headers/footers.<br>Valid values: "numeric", "lowercaseroman", "uppercaseroman".<br>Default: "numeric".</p>                                                                                                                                                                                                                                                                                        | `numeric` |
| `align`            | `string`  | `false`  | <p>String - Text alignment for header/footer text.<br>Valid values: "left", "right", "center". Default: "left".</p>                                                                                                                                                                                                                                                                                                                                | `left`    |
| `leftmargin`       | `numeric` | `false`  | Numeric - Left margin in points for header/footer positioning.                                                                                                                                                                                                                                                                                                                                                                                     |           |
| `rightmargin`      | `numeric` | `false`  | Numeric - Right margin in points for header/footer positioning.                                                                                                                                                                                                                                                                                                                                                                                    |           |
| `topmargin`        | `numeric` | `false`  | Numeric - Top margin in points for header positioning.                                                                                                                                                                                                                                                                                                                                                                                             |           |
| `bottommargin`     | `numeric` | `false`  | Numeric - Bottom margin in points for footer positioning.                                                                                                                                                                                                                                                                                                                                                                                          |           |
| `format`           | `string`  | `false`  | String - Output format for thumbnail generation. Default: "jpeg".                                                                                                                                                                                                                                                                                                                                                                                  | `jpeg`    |
| `imageprefix`      | `string`  | `false`  | String - Prefix for generated image filenames. Default: "".                                                                                                                                                                                                                                                                                                                                                                                        |           |
| `resolution`       | `string`  | `false`  | <p>String - Resolution quality for thumbnails.<br>Valid values: "low", "medium", "high". Default: "high".</p>                                                                                                                                                                                                                                                                                                                                      | `high`    |
| `transparent`      | `boolean` | `false`  | Boolean - Whether thumbnail background is transparent. Default: false.                                                                                                                                                                                                                                                                                                                                                                             | `false`   |
| `overridepage`     | `boolean` | `false`  | Boolean - Whether to override existing pages. Default: false.                                                                                                                                                                                                                                                                                                                                                                                      | `false`   |
| `hires`            | `boolean` | `false`  | <p>Boolean - High resolution mode for operations.<br>NOTE: This attribute is not yet implemented.</p>                                                                                                                                                                                                                                                                                                                                              |           |
| `scale`            | `double`  | `false`  | Double - Scale factor for thumbnails and watermarks. Default: 100.0.                                                                                                                                                                                                                                                                                                                                                                               | `100.0`   |
| `position`         | `double`  | `false`  | Double - Position for watermark or signature placement.                                                                                                                                                                                                                                                                                                                                                                                            |           |
| `rotation`         | `double`  | `false`  | Double - Rotation angle in degrees for watermarks or signatures.                                                                                                                                                                                                                                                                                                                                                                                   |           |
| `hscale`           | `double`  | `false`  | Double - Horizontal scale factor for watermarks. Default: 1.0.                                                                                                                                                                                                                                                                                                                                                                                     | `1.0`     |
| `vscale`           | `double`  | `false`  | Double - Vertical scale factor for watermarks. Default: 1.0.                                                                                                                                                                                                                                                                                                                                                                                       | `1.0`     |
| `foreground`       | `boolean` | `false`  | Boolean - Whether watermark appears in foreground. Default: false.                                                                                                                                                                                                                                                                                                                                                                                 | `false`   |
| `isbase64`         | `boolean` | `false`  | Boolean - Whether input data is base64 encoded. Default: false.                                                                                                                                                                                                                                                                                                                                                                                    | `false`   |
| `copyfrom`         | `any`     | `false`  | Any - Source document to copy pages from.                                                                                                                                                                                                                                                                                                                                                                                                          |           |
| `exportTo`         | `string`  | `false`  | String - Target file path for export operations.                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| `importFrom`       | `string`  | `false`  | String - Source file path for import operations.                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| `encodeall`        | `boolean` | `false`  | <p>Boolean - Whether to encode all content.<br>NOTE: This attribute is not yet implemented.</p>                                                                                                                                                                                                                                                                                                                                                    |           |

## Examples

### Reading PDF Information

```js
<bx:pdf action="getinfo" source="report.pdf" name="pdfInfo" />

<bx:output>
PDF Title: #pdfInfo.Title#<br>
Author: #pdfInfo.Author#<br>
Pages: #pdfInfo.TotalPages#<br>
Created: #pdfInfo.Created#
</bx:output>
```

### Merging Multiple PDFs

```js
<bx:pdf action="merge" destination="combined-report.pdf" overwrite="true">
    <bx:pdfparam source="section1.pdf" />
    <bx:pdfparam source="section2.pdf" />
    <bx:pdfparam source="appendix.pdf" />
</bx:pdf>
```

### Extracting Text Content

```js
<bx:pdf action="extracttext" 
        source="document.pdf" 
        name="extractedText" 
        pages="1-5" />

<bx:output>
Extracted text: #extractedText#
</bx:output>
```

### Adding Watermarks

```js
<bx:pdf action="addwatermark" 
        source="original.pdf" 
        destination="watermarked.pdf"
        image="watermark.png"
        pages="*"
        opacity="0.3"
        position="5"
        overwrite="true" />
```

### Adding Headers and Footers

```js
<bx:pdf action="addheader" 
        source="document.pdf" 
        destination="document-with-header.pdf"
        text="Company Confidential"
        align="center"
        pages="*"
        overwrite="true" />

<bx:pdf action="addfooter" 
        source="document-with-header.pdf" 
        destination="final-document.pdf"
        text="Page _PAGENUMBER of _LASTPAGENUMBER"
        align="center"
        pages="*"
        numberformat="numeric"
        overwrite="true" />
```

### Protecting PDF with Password

```js
<bx:pdf action="protect" 
        source="sensitive-data.pdf" 
        destination="protected-data.pdf"
        newOwnerPassword="admin123"
        newUserPassword="user456"
        permissions="AllowPrinting,AllowCopy"
        overwrite="true" />
```

### Removing Password Protection

```js
<bx:pdf action="removepassword" 
        source="protected-document.pdf" 
        destination="unlocked-document.pdf"
        password="user456"
        overwrite="true" />
```

### Generating Thumbnails

```js
<bx:pdf action="thumbnail" 
        source="presentation.pdf" 
        destination="thumbnails/"
        pages="1,3,5"
        format="png"
        resolution="high"
        scale="150"
        imageprefix="slide_" />
```

### Deleting Specific Pages

```js
<bx:pdf action="deletepages" 
        source="full-report.pdf" 
        destination="trimmed-report.pdf"
        pages="2,4-6,10"
        overwrite="true" />
```

### Setting Document Information

```js
<bx:set docInfo = {
    "Title": "Annual Financial Report",
    "Author": "Finance Department",
    "Subject": "2024 Financial Analysis",
    "Keywords": "finance, annual, report, 2024"
} />

<bx:pdf action="setinfo" 
        source="report.pdf" 
        destination="report-with-metadata.pdf"
        info="#docInfo#"
        overwrite="true" />
```

### Using PDF Variables

```js
<!-- Read PDF into memory -->
<bx:pdf action="read" source="input.pdf" name="pdfData" />

<!-- Process the PDF data -->
<bx:pdf action="addwatermark" 
        source="#pdfData#" 
        name="watermarkedPdf"
        text="DRAFT"
        opacity="0.5" />

<!-- Write to file -->
<bx:pdf action="write" 
        source="#watermarkedPdf#" 
        destination="output.pdf"
        overwrite="true" />
```

### Complex Multi-Action Example

```js
<bx:try>
    <!-- Step 1: Read and get info -->
    <bx:pdf action="getinfo" source="original.pdf" name="info" />
    
    <!-- Step 2: Add header and footer -->
    <bx:pdf action="addheader" 
            source="original.pdf" 
            name="withHeader"
            text="Document #info.Title#"
            align="center"
            pages="*" />
    
    <bx:pdf action="addfooter" 
            source="#withHeader#" 
            name="withFooter"
            text="Page _PAGENUMBER of _LASTPAGENUMBER | Confidential"
            align="center"
            pages="*" />
    
    <!-- Step 3: Add watermark -->
    <bx:pdf action="addwatermark" 
            source="#withFooter#" 
            name="finalPdf"
            text="INTERNAL USE ONLY"
            opacity="0.2"
            pages="*" />
    
    <!-- Step 4: Write final document -->
    <bx:pdf action="write" 
            source="#finalPdf#" 
            destination="processed-document.pdf"
            overwrite="true" />
    
    <p>PDF processing completed successfully!</p>
    
<bx:catch type="any">
    <p>Error processing PDF: #cfcatch.message#</p>
</bx:catch>
</bx:try>
```

## Supported Actions

* **addheader** - Add headers to PDF pages
* **addfooter** - Add footers to PDF pages
* **addwatermark** - Add text or image watermarks
* **deletepages** - Remove specific pages
* **extracttext** - Extract text content
* **getinfo** - Get document metadata
* **merge** - Combine multiple PDFs
* **protect** - Add password protection
* **read** - Load PDF into memory
* **removepassword** - Remove password protection
* **setinfo** - Set document metadata
* **thumbnail** - Generate page thumbnails
* **write** - Save PDF to file

## Related Components

* [PDFParam](PDFParam.md) - Specify parameters for PDF operations
* [PDFForm](PDFForm.md) - Manipulate PDF form fields
