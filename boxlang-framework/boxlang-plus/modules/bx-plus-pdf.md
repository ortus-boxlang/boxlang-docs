---
description: >-
  Premium PDF generation and manipulation module for BoxLang+ applications:
  build, merge, stamp, secure, and extract content programmatically.
icon: file-pdf
---

# PDF +

The Boxlang+ Licensed edition of the `bx-pdf` module equips your BoxLang+ applications with robust PDF creation and processing capabilities—ideal for invoices, reports, forms, certificates, and archival workflows.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](bx-plus.md) with a limited trial.
{% endhint %}

This module provides comprehensive PDF manipulation and generation functionality for BoxLang, including:

* **PDF Document Generation** - Create PDF documents from HTML content
* **PDF Form Manipulation** - Populate and extract data from PDF forms
* **PDF Document Processing** - Advanced PDF operations like merging, splitting, watermarking
* **Adobe ColdFusion Compatibility** - Full compatibility with ColdFusion PDF tags

## Installation

```bash
# For Operating Systems using our Quick Installer
install-bx-module bx-plus,bx-pdf

# Using CommandBox to install for web servers
box install bx-plus,bx-pdf
```

## Components

This module contributes the following components to the BoxLang runtime:

### Document Generation Components ( Free Tier )

* [`document`](bx-plus-pdf.md#document-component) - Main component for creating PDF documents from HTML
* [`documentitem`](bx-plus-pdf.md#documentitem-component) - Specifies headers, footers, and page breaks
* [`documentsection`](bx-plus-pdf.md#documentsection-component) - Divides documents into sections with unique properties

### PDF Manipulation Components ( Boxlang+ Only )

* [`pdf`](bx-plus-pdf.md#pdf-component) - Advanced PDF operations (merge, split, watermark, etc.)
* [`pdfparam`](bx-plus-pdf.md#pdfparam-component) - Parameters for PDF operations like attachments

### PDF Form Components ( Boxlang+ Only )

* [`pdfform`](bx-plus-pdf.md#pdfform-component) - Manipulate PDF forms (populate/read form fields)
* [`pdfformparam`](bx-plus-pdf.md#pdfformparam-component) - Specify individual form field values

***

## Document Component

The `document` component creates PDF documents from HTML content with extensive customization options.

### Attributes

| Attribute           | Type    | Default     | Description                                   |
| ------------------- | ------- | ----------- | --------------------------------------------- |
| `format`            | String  | "pdf"       | Document format (PDF only)                    |
| `filename`          | String  | -           | Output file path                              |
| `variable`          | String  | -           | Variable name to store PDF binary             |
| `encryption`        | String  | "none"      | Encryption level: "128-bit", "40-bit", "none" |
| `orientation`       | String  | "portrait"  | Page orientation: "portrait", "landscape"     |
| `pageType`          | String  | "A4"        | Page size (A4, LETTER, LEGAL, etc.)           |
| `pageWidth`         | Numeric | -           | Custom page width in inches                   |
| `pageHeight`        | Numeric | -           | Custom page height in inches                  |
| `marginTop`         | Numeric | -           | Top margin                                    |
| `marginBottom`      | Numeric | -           | Bottom margin                                 |
| `marginLeft`        | Numeric | -           | Left margin                                   |
| `marginRight`       | Numeric | -           | Right margin                                  |
| `scale`             | Numeric | 100         | Scaling percentage (≤100)                     |
| `backgroundVisible` | Boolean | true        | Show background elements                      |
| `bookmark`          | Boolean | true        | Generate bookmarks                            |
| `htmlBookmark`      | Boolean | false       | Convert HTML anchors to bookmarks             |
| `fontEmbed`         | Boolean | true        | Embed fonts in document                       |
| `fontDirectory`     | String  | -           | Custom font directory                         |
| `localUrl`          | Boolean | false       | Generate with local URLs                      |
| `openpassword`      | String  | -           | Password to open document                     |
| `ownerPassword`     | String  | -           | Owner password for restrictions               |
| `pdfa`              | Boolean | false       | Generate PDF/A compliant document             |
| `saveAsName`        | String  | -           | Browser save filename                         |
| `overwrite`         | Boolean | false       | Overwrite existing files                      |
| `src`               | String  | -           | URL or path to HTML content                   |
| `srcfile`           | String  | -           | Absolute path to HTML file                    |
| `mimeType`          | String  | "text/html" | Source content MIME type                      |
| `unit`              | String  | "inches"    | Measurement unit: "in", "cm"                  |

### Unsupported Attributes

The following attributes are not currently implemented and will throw an error if used:

* `permissions` - Granular permissibility is not yet supported
* `permissionspassword` - Granular permissibility is not yet supported
* `userPassword` - Granular permissibility is not yet supported
* `authPassword` - Authentication password not supported
* `authUser` - Authentication user not supported
* `userAgent` - HTTP user agent identifier not supported
* `proxyHost` - Proxy server configuration not supported
* `proxyPassword` - Proxy authentication not supported
* `proxyPort` - Proxy port configuration not supported
* `proxyUser` - Proxy user authentication not supported
* `tagged` - ACF OpenOffice integration not supported
* `formfields` - Form field attributes not implemented in standard module
* `formsType` - Form type specification not implemented in standard module

***

## DocumentItem Component

Specifies headers, footers, and page breaks within PDF documents.

### Attributes

| Attribute     | Type    | Required | Description                                |
| ------------- | ------- | -------- | ------------------------------------------ |
| `type`        | String  | Yes      | Item type: "header", "footer", "pagebreak" |
| `evalAtPrint` | Boolean | No       | ⚠️ Deprecated - content always evaluated   |

***

## DocumentSection Component

Divides PDF documents into sections with unique headers, footers, and page numbering.

### Attributes

| Attribute      | Type    | Description                       |
| -------------- | ------- | --------------------------------- |
| `name`         | String  | Section name (used for bookmarks) |
| `marginTop`    | Numeric | Section top margin                |
| `marginBottom` | Numeric | Section bottom margin             |
| `marginLeft`   | Numeric | Section left margin               |
| `marginRight`  | Numeric | Section right margin              |
| `src`          | String  | URL or relative path to content   |
| `srcfile`      | String  | Absolute path to content file     |
| `mimeType`     | String  | Content MIME type                 |

### Unsupported Attributes

The following attributes are not currently implemented and will throw an error if used:

* `userAgent` - HTTP user agent identifier for URL fetching
* `authPassword` - Authentication password for URL content
* `authUser` - Authentication username for URL content

***

## PDFForm Component

Manipulates PDF forms created in Adobe Acrobat and Adobe LiveCycle Designer. Supports both populating form fields and extracting form data.

### Actions

* **populate** - Fill form fields with data
* **read** - Extract form field data to structures or files

### Attributes

| Attribute       | Type    | Required | Description                                          |
| --------------- | ------- | -------- | ---------------------------------------------------- |
| `action`        | String  | Yes      | "populate" or "read"                                 |
| `source`        | Any     | Yes      | Source PDF form (file path, byte array, or variable) |
| `destination`   | String  | No       | Output file path (populate action)                   |
| `result`        | String  | No       | Variable name for extracted data (read action)       |
| `overwrite`     | Boolean | No       | Overwrite existing files (default: false)            |
| `overwriteData` | Boolean | No       | Overwrite existing form data (default: false)        |
| `fdfdata`       | String  | No       | FDF file path for import/export                      |
| `XMLdata`       | String  | No       | ⏳ XML data (planned feature)                         |

### Examples

#### Populating Form Fields

```html
<bx:pdfform action="populate"
            source="/forms/employee-form.pdf"
            destination="/completed/employee-123.pdf"
            overwrite="true">

    <bx:pdfformparam name="employeeId" value="EMP-123" />
    <bx:pdfformparam name="firstName" value="John" />
    <bx:pdfformparam name="lastName" value="Smith" />
    <bx:pdfformparam name="department" value="Engineering" />
    <bx:pdfformparam name="salary" value="$85,000" />
    <bx:pdfformparam name="startDate" value="2024-01-15" />

</bx:pdfform>
```

#### Reading Form Data

```html
<bx:pdfform action="read"
            source="/submitted/employee-form-filled.pdf"
            result="employeeData" />

<!-- Access extracted data -->
<bx:output>
    Employee: #employeeData.firstName# #employeeData.lastName#<br>
    ID: #employeeData.employeeId#<br>
    Department: #employeeData.department#
</bx:output>

<bx:dump var="#employeeData#" />
```

#### FDF Data Operations

```html
<!-- Export form data to FDF -->
<bx:pdfform action="read"
            source="/filled-forms/survey.pdf"
            fdfdata="/exported-data/survey-data.fdf" />

<!-- Import FDF data to populate form -->
<bx:pdfform action="populate"
            source="/templates/survey-template.pdf"
            destination="/completed/survey-filled.pdf"
            fdfdata="/data/survey-responses.fdf" />
```

***

## PDFFormParam Component

Specifies individual form field values when populating PDF forms. Must be nested within a `pdfform` component.

### Attributes

| Attribute | Type    | Required | Description                                  |
| --------- | ------- | -------- | -------------------------------------------- |
| `name`    | String  | Yes      | Form field name                              |
| `value`   | String  | Yes      | Value to assign to the field                 |
| `index`   | Integer | No       | Field index for LiveCycle forms (default: 1) |

### Usage Notes

* **Acrobat Forms**: Cannot have multiple fields with the same name, so `index` is not applicable
* **LiveCycle Forms**: Support multiple fields with the same name, use `index` to distinguish them
* **Case Sensitivity**: Field values are case-sensitive
* **Data Types**: Component handles various field types (text, checkbox, radio, dropdown, etc.)

### Example

```html
<bx:pdfform action="populate" source="registration-form.pdf" destination="completed-form.pdf">

    <!-- Text fields -->
    <bx:pdfformparam name="fullName" value="Jane Doe" />
    <bx:pdfformparam name="email" value="jane.doe@company.com" />

    <!-- Checkbox (requires specific values like "Yes"/"No" or "On"/"Off") -->
    <bx:pdfformparam name="agreeToTerms" value="Yes" />

    <!-- Dropdown selection -->
    <bx:pdfformparam name="country" value="United States" />

    <!-- Radio button -->
    <bx:pdfformparam name="gender" value="Female" />

    <!-- Date field -->
    <bx:pdfformparam name="birthDate" value="1985-03-15" />

    <!-- Numeric field -->
    <bx:pdfformparam name="yearsExperience" value="8" />

</bx:pdfform>
```

***

## PDF Component

Performs advanced PDF operations like merging, splitting, watermarking, and form manipulation.

### Supported Actions

| Action               | Description                 |
| -------------------- | --------------------------- |
| `addAttachments`     | Add file attachments to PDF |
| `addHeader`          | Add headers to pages        |
| `addFooter`          | Add footers to pages        |
| `addWatermark`       | Add watermark to pages      |
| `deletePages`        | Remove specific pages       |
| `export`             | Export form data (FDF/XFDF) |
| `extractText`        | Extract text content        |
| `extractimage`       | Extract embedded images     |
| `getInfo`            | Get PDF metadata            |
| `import`             | Import form data            |
| `merge`              | Combine multiple PDFs       |
| `protect`            | Add password protection     |
| `removePassword`     | Remove password protection  |
| `removeWatermark`    | Remove watermarks           |
| `removeHeaderFooter` | Remove headers/footers      |
| `thumbnail`          | Generate page thumbnails    |
| `transform`          | Transform/manipulate pages  |
| `unsign`             | Remove digital signatures   |
| `validatesignature`  | Validate signatures         |
| `write`              | Save PDF to file            |

### Key Attributes

| Attribute     | Type    | Description                                         |
| ------------- | ------- | --------------------------------------------------- |
| `action`      | String  | Operation to perform (see actions above)            |
| `source`      | Any     | Source PDF(s) - file path, binary data, or variable |
| `destination` | String  | Output file path                                    |
| `pages`       | String  | Page selection: "1-5", "1,3,5", "\*"                |
| `overwrite`   | Boolean | Overwrite existing files                            |
| `password`    | String  | Password for encrypted PDFs                         |

### Examples

#### Merging PDFs

```html
<bx:pdf action="merge"
        destination="/combined/merged-document.pdf"
        overwrite="true">

    <bx:pdfparam source="/docs/doc1.pdf" />
    <bx:pdfparam source="/docs/doc2.pdf" />
    <bx:pdfparam source="/docs/doc3.pdf" />

</bx:pdf>
```

#### Adding Watermarks

```html
<bx:pdf action="addWatermark"
        source="/documents/report.pdf"
        destination="/documents/watermarked-report.pdf"
        image="/images/confidential.png"
        opacity="0.3"
        position="center"
        rotation="45">
</bx:pdf>
```

#### Extracting Text

```html
<bx:pdf action="extractText"
        source="/documents/report.pdf"
        destination="/extracted/report.txt"
        pages="1-10">
</bx:pdf>
```

#### Password Protection

```html
<bx:pdf action="protect"
        source="/documents/sensitive.pdf"
        destination="/documents/protected.pdf"
        newOwnerPassword="admin123"
        newUserPassword="user123"
        permissions="print,copy">
</bx:pdf>
```

***

## PDFParam Component

Specifies parameters for PDF operations, particularly for merge and attachment operations.

### Attributes

| Attribute     | Type   | Description                    |
| ------------- | ------ | ------------------------------ |
| `source`      | String | Source file path               |
| `filename`    | String | Attachment filename            |
| `encoding`    | String | File encoding (default: UTF-8) |
| `mimeType`    | String | File MIME type                 |
| `description` | String | Attachment description         |
| `password`    | String | Password for encrypted files   |

### Example

```html
<bx:pdf action="addAttachments"
        source="/base/document.pdf"
        destination="/enhanced/document.pdf">

    <bx:pdfparam source="/files/spreadsheet.xlsx"
                 filename="data.xlsx"
                 mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 description="Supporting data analysis" />

    <bx:pdfparam source="/images/chart.png"
                 filename="sales-chart.png"
                 mimeType="image/png"
                 description="Q4 Sales Performance Chart" />

</bx:pdf>
```

***

## Advanced Examples

### Complete Document Generation

```html
<bx:set testImage = "https://ortus-public.s3.amazonaws.com/logos/ortus-medium.jpg"/>
<bx:document format="pdf"
             filename="/reports/annual-report.pdf"
             pageType="A4"
             orientation="portrait"
             encryption="128-bit"
             openpassword="company2024"
             fontEmbed="true">

    <!-- Global Header -->
    <bx:documentitem type="header">
        <div style="text-align: center; border-bottom: 2px solid #333; padding: 10px;">
            <h2>Annual Business Report 2024</h2>
        </div>
    </bx:documentitem>

    <!-- Global Footer -->
    <bx:documentitem type="footer">
        <div style="text-align: center; font-size: 10px;">
            Page #bxdocument.currentpagenumber# of #bxdocument.totalpages#
        </div>
    </bx:documentitem>

    <!-- Executive Summary Section -->
    <bx:documentsection name="Executive Summary">
        <h1>Executive Summary</h1>
        <p>This report provides an overview of our performance...</p>
    </bx:documentsection>

    <!-- Charts Section -->
    <bx:documentsection name="Performance Charts" src="#testImage#" />

</bx:document>
```

### PDF Processing Pipeline

```html
<!-- Step 1: Merge quarterly reports -->
<bx:pdf action="merge" destination="/temp/combined-quarterly.pdf">
    <bx:pdfparam source="/reports/q1-2024.pdf" />
    <bx:pdfparam source="/reports/q2-2024.pdf" />
    <bx:pdfparam source="/reports/q3-2024.pdf" />
    <bx:pdfparam source="/reports/q4-2024.pdf" />
</bx:pdf>

<!-- Step 2: Add company watermark -->
<bx:pdf action="addWatermark"
        source="/temp/combined-quarterly.pdf"
        destination="/temp/watermarked-report.pdf"
        image="/assets/company-watermark.png"
        opacity="0.2"
        pages="*">
</bx:pdf>

<!-- Step 3: Add password protection -->
<bx:pdf action="protect"
        source="/temp/watermarked-report.pdf"
        destination="/final/annual-report-protected.pdf"
        newOwnerPassword="admin2024"
        newUserPassword="view2024"
        permissions="print">
</bx:pdf>
```

### Form Processing Workflow

```html
<!-- Process submitted form data -->
<bx:pdfform action="read"
            source="/submissions/application-#url.id#.pdf"
            result="applicationData" />

<!-- Validate and process data -->
<bx:if applicationData.status eq "pending">

    <!-- Update form with approval stamp -->
    <bx:pdfform action="populate"
                source="/submissions/application-#url.id#.pdf"
                destination="/processed/approved-application-#url.id#.pdf"
                overwriteData="true">

        <bx:pdfformparam name="status" value="APPROVED" />
        <bx:pdfformparam name="approvedBy" value="#session.user.name#" />
        <bx:pdfformparam name="approvalDate" value="#dateFormat(now(), 'yyyy-mm-dd')#" />

    </bx:pdfform>

</bx:if>
```

## CFML Compatibility

This module provides full compatibility with CFML PDF tags:

* ✅ `cfdocument` → `bx:document`
* ✅ `cfdocumentitem` → `bx:documentitem`
* ✅ `cfdocumentsection` → `bx:documentsection`
* ✅ `cfpdf` → `bx:pdf`
* ✅ `cfpdfparam` → `bx:pdfparam`
* ✅ `cfpdfform` → `bx:pdfform`
* ✅ `cfpdfformparam` → `bx:pdfformparam`

Migration from ColdFusion requires only prefix changes (`cf` → `bx`).

## Technical Requirements

* **BoxLang Runtime** 1.0.0+
* **Java** 21+

## Support and Documentation

* **Issue Tracking**: [JIRA](https://ortussolutions.atlassian.net/jira/software/c/projects/BLMODULES)
* **BoxLang Information**: [https://boxlang.io](https://boxlang.io)
* **BoxLang Documentation**: [https://boxlang.ortusbooks.com](https://boxlang.ortusbooks.com)
* **Ortus Solutions**: [ortussolutions.com](https://www.ortussolutions.com)

## 📎 Related Modules

{% content-ref url="bx-spreadsheet/" %}
[bx-spreadsheet](bx-spreadsheet/)
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
[bx-plus.md](bx-plus.md)
{% endcontent-ref %}

***

Return to the [Modules Overview](./).
