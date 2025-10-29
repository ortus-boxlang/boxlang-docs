# PDFParam

Component which specifies header, footer, and pagebreaks within a document body

{% include "../../../../../../.gitbook/includes/this-component-is-only-avai....md" %}

## Component Signature

```
<bx:PDFParam source=[string]
filename=[string]
encoding=[string]
mimeType=[string]
description=[string]
password=[string]
iconname=[string]
coordinates=[string]
note=[string] />
```

### Attributes

| Atrribute     | Type     | Required | Description | Default |
| ------------- | -------- | -------- | ----------- | ------- |
| `source`      | `string` | `false`  |             |         |
| `filename`    | `string` | `false`  |             |         |
| `encoding`    | `string` | `false`  |             | `UTF-8` |
| `mimeType`    | `string` | `false`  |             |         |
| `description` | `string` | `false`  |             |         |
| `password`    | `string` | `false`  |             |         |
| `iconname`    | `string` | `false`  |             | `Draft` |
| `coordinates` | `string` | `false`  |             |         |
| `note`        | `string` | `false`  |             |         |

## Examples

### Basic PDF Merging

```js
<bx:pdf action="merge" destination="combined-report.pdf" overwrite="true">
    <bx:pdfparam source="executive-summary.pdf" />
    <bx:pdfparam source="financial-data.pdf" />
    <bx:pdfparam source="charts-graphs.pdf" />
    <bx:pdfparam source="appendix.pdf" />
</bx:pdf>
```

### Password-Protected Source Files

```js
<bx:pdf action="merge" destination="secure-documents.pdf" overwrite="true">
    <bx:pdfparam source="public-info.pdf" />
    <bx:pdfparam source="confidential-data.pdf" password="secret123" />
    <bx:pdfparam source="financial-report.pdf" password="finance456" />
</bx:pdf>
```

### Merging with File Descriptions

```js
<bx:pdf action="merge" destination="project-documentation.pdf" overwrite="true">
    <bx:pdfparam source="requirements.pdf" 
                 description="Project Requirements and Specifications" />
    <bx:pdfparam source="design.pdf" 
                 description="System Design and Architecture" />
    <bx:pdfparam source="testing.pdf" 
                 description="Test Plans and Results" />
    <bx:pdfparam source="deployment.pdf" 
                 description="Deployment Guide and Procedures" />
</bx:pdf>
```

### Custom File Encoding

```js
<bx:pdf action="merge" destination="international-docs.pdf" overwrite="true">
    <bx:pdfparam source="english-doc.pdf" encoding="UTF-8" />
    <bx:pdfparam source="french-doc.pdf" encoding="UTF-8" />
    <bx:pdfparam source="japanese-doc.pdf" encoding="UTF-8" />
</bx:pdf>
```

### Specifying MIME Types

```js
<bx:pdf action="merge" destination="mixed-media.pdf" overwrite="true">
    <bx:pdfparam source="document1.pdf" mimeType="application/pdf" />
    <bx:pdfparam source="document2.pdf" mimeType="application/pdf" />
    <bx:pdfparam source="report.pdf" mimeType="application/pdf" />
</bx:pdf>
```

### Complex Merge with Metadata

```js
<bx:pdf action="merge" destination="comprehensive-report.pdf" overwrite="true">
    <bx:pdfparam source="/reports/q1/summary.pdf" 
                 description="Q1 Executive Summary"
                 filename="Q1-Executive-Summary.pdf" />
    
    <bx:pdfparam source="/reports/q1/financials.pdf" 
                 password="q1finance"
                 description="Q1 Financial Analysis"
                 filename="Q1-Financial-Data.pdf" />
    
    <bx:pdfparam source="/reports/q1/operations.pdf" 
                 description="Q1 Operations Report"
                 filename="Q1-Operations.pdf"
                 encoding="UTF-8" />
    
    <bx:pdfparam source="/reports/q1/forecasts.pdf" 
                 description="Q2 Forecasts and Projections"
                 filename="Q2-Forecasts.pdf" />
</bx:pdf>
```

### Variable-Based Sources

```js
<bx:set reportFiles = [
    {source: "intro.pdf", desc: "Introduction"},
    {source: "methodology.pdf", desc: "Research Methodology", password: "research123"},
    {source: "findings.pdf", desc: "Key Findings and Results"},
    {source: "conclusions.pdf", desc: "Conclusions and Recommendations"}
] />

<bx:pdf action="merge" destination="research-report.pdf" overwrite="true">
    <bx:loop array="#reportFiles#" item="file">
        <bx:pdfparam source="#file.source#" 
                     description="#file.desc#"
                     <bx:if structKeyExists(file, "password")>
                         password="#file.password#"
                     </bx:if> />
    </bx:loop>
</bx:pdf>
```

### Conditional PDF Inclusion

```js
<bx:set includeFinancials = true />
<bx:set includeConfidential = false />

<bx:pdf action="merge" destination="custom-report.pdf" overwrite="true">
    <!-- Always include executive summary -->
    <bx:pdfparam source="executive-summary.pdf" 
                 description="Executive Summary" />
    
    <!-- Conditionally include financial data -->
    <bx:if includeFinancials>
        <bx:pdfparam source="financial-data.pdf" 
                     description="Financial Analysis"
                     password="finance2024" />
    </bx:if>
    
    <!-- Always include operations data -->
    <bx:pdfparam source="operations-report.pdf" 
                 description="Operations Report" />
    
    <!-- Conditionally include confidential information -->
    <bx:if includeConfidential>
        <bx:pdfparam source="confidential-data.pdf" 
                     description="Confidential Information"
                     password="confidential123" />
    </bx:if>
</bx:pdf>
```

### Error Handling with Try/Catch

```js
<bx:try>
    <bx:pdf action="merge" destination="safe-merge.pdf" overwrite="true">
        <bx:pdfparam source="document1.pdf" description="Primary Document" />
        <bx:pdfparam source="document2.pdf" 
                     description="Secondary Document"
                     password="doc2pass" />
        <bx:pdfparam source="document3.pdf" description="Supporting Data" />
    </bx:pdf>
    
    <p>PDF merge completed successfully!</p>
    
<bx:catch type="any">
    <p>Error merging PDFs: #cfcatch.message#</p>
    <p>Please check that all source files exist and passwords are correct.</p>
</bx:catch>
</bx:try>
```

## Common Use Cases

* **Document Assembly** - Combining multiple PDF sections into complete reports
* **Archive Creation** - Merging related documents for storage
* **Report Generation** - Assembling dynamic reports from template pieces
* **Workflow Processing** - Combining documents at different workflow stages

## Best Practices

* Always specify meaningful descriptions for merged sections
* Use consistent encoding (UTF-8) for international content
* Store passwords securely, not in plain text code
* Test merge operations with sample documents first
* Handle password-protected sources with appropriate error handling

## Related Components

* [PDF](PDF.md) - Main PDF manipulation component
* [PDFForm](PDFForm.md) - PDF form field manipulation
