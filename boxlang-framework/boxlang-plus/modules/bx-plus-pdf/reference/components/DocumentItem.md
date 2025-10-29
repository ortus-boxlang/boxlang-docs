
# Component: `DocumentItem`

Component which specifies header, footer, and pagebreaks within a document body


This component is available in the free-tier functionality of this module

## Component Signature

```
<bx:DocumentItem type=[string]
evalAtPrint=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | string pagebreak|header|footer |  |
| `evalAtPrint` | `string` | `false` | A boolean which determines if the contents of the cfdocumentitem tag body has to be evaluated at the time of printing the document.  This attribute is deprecated as all content is evaluated at print time. | `true` |

## Examples

### Document Header

```html
<bx:document format="pdf" filename="header-example.pdf">
    <!-- Global Header -->
    <bx:documentitem type="header">
        <div style="text-align: center; border-bottom: 2px solid #333; padding: 10px;">
            <h2>Company Annual Report</h2>
            <p>Confidential - Internal Use Only</p>
        </div>
    </bx:documentitem>

    <h1>Document Content</h1>
    <p>This content will appear on every page with the header above.</p>
</bx:document>
```

### Document Footer

```html
<bx:document format="pdf" filename="footer-example.pdf">
    <bx:documentitem type="footer">
        <div style="text-align: center; font-size: 10px; padding: 10px; border-top: 1px solid #ccc;">
            <p>Page #bxdocument.currentpagenumber# of #bxdocument.totalpages#</p>
            <p>© 2024 Your Company Name. All rights reserved.</p>
        </div>
    </bx:documentitem>

    <h1>Document Content</h1>
    <p>This content will appear on every page with the footer below.</p>
</bx:document>
```

### Page Break

```html
<bx:document format="pdf" filename="pagebreak-example.pdf">
    <h1>Section 1</h1>
    <p>Content for the first page...</p>

    <!-- Force a page break -->
    <bx:documentitem type="pagebreak" />

    <h1>Section 2</h1>
    <p>This content will start on a new page...</p>
</bx:document>
```

### Combined Header, Footer, and Page Breaks

```html
<bx:document format="pdf" filename="complete-example.pdf">
    <!-- Global Header -->
    <bx:documentitem type="header">
        <div style="text-align: center; background: #f0f0f0; padding: 5px;">
            <strong>Document Title</strong>
        </div>
    </bx:documentitem>

    <!-- Global Footer -->
    <bx:documentitem type="footer">
        <div style="text-align: center; font-size: 8px;">
            Page #bxdocument.currentpagenumber# | Generated on #dateFormat(now(), "mm/dd/yyyy")#
        </div>
    </bx:documentitem>

    <h1>Chapter 1</h1>
    <p>First chapter content...</p>

    <bx:documentitem type="pagebreak" />

    <h1>Chapter 2</h1>
    <p>Second chapter content...</p>
</bx:document>
```

## Built-in Variables

When using DocumentItem components, BoxLang provides special variables:

- `#bxdocument.currentpagenumber#` - Current page number
- `#bxdocument.totalpages#` - Total number of pages in the document

## Related Components

- [Document](Document.md) - Main component for PDF generation
- [DocumentSection](DocumentSection.md) - Divides documents into sections


