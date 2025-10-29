
# Component: `DocumentSection`

Divides a PDF document into sections.

This component is available in the free-tier functionality of this module

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

### Named Sections with Bookmarks

```html
<bx:document format="pdf" filename="sections-example.pdf" bookmark="true">
    <!-- Executive Summary Section -->
    <bx:documentsection name="Executive Summary">
        <h1>Executive Summary</h1>
        <p>This section provides an overview of our quarterly performance...</p>
        <ul>
            <li>Revenue increased by 15%</li>
            <li>Customer satisfaction up 8%</li>
            <li>Market expansion into 3 new regions</li>
        </ul>
    </bx:documentsection>

    <!-- Financial Details Section -->
    <bx:documentsection name="Financial Details">
        <h1>Financial Performance</h1>
        <p>Detailed breakdown of financial metrics...</p>
        <table border="1">
            <tr><th>Quarter</th><th>Revenue</th><th>Profit</th></tr>
            <tr><td>Q1</td><td>$1.2M</td><td>$150K</td></tr>
            <tr><td>Q2</td><td>$1.4M</td><td>$175K</td></tr>
        </table>
    </bx:documentsection>
</bx:document>
```

### External Content Sections

```html
<bx:set testImage = "https://ortus-public.s3.amazonaws.com/logos/ortus-medium.jpg"/>

<bx:document format="pdf" filename="external-sections.pdf">
    <!-- Content from external file -->
    <bx:documentsection name="Terms and Conditions" 
                        srcfile="/templates/terms-template.html" />

    <!-- Content from image URL -->
    <bx:documentsection name="Company Logo" 
                        src="#testImage#" />

    <!-- Content from web URL -->
    <bx:documentsection name="Current News" 
                        src="https://example.com/news-feed" />
</bx:document>
```

### Custom Section Margins

```html
<bx:document format="pdf" filename="custom-margins.pdf" unit="in">
    <!-- Section with custom margins -->
    <bx:documentsection name="Indented Content"
                        marginTop="1.0"
                        marginBottom="0.5"
                        marginLeft="1.5"
                        marginRight="0.75">
        <h2>This Section Has Custom Margins</h2>
        <p>The margins for this section are different from the document defaults.</p>
        <p>This creates visual separation and emphasis for important content.</p>
    </bx:documentsection>

    <!-- Regular section with document margins -->
    <bx:documentsection name="Regular Content">
        <h2>Standard Margins</h2>
        <p>This section uses the document's default margin settings.</p>
    </bx:documentsection>
</bx:document>
```

### Mixed Content Types

```html
<bx:document format="pdf" filename="mixed-content.pdf">
    <!-- HTML content section -->
    <bx:documentsection name="Introduction">
        <h1>Project Overview</h1>
        <p>This document contains various types of content...</p>
    </bx:documentsection>

    <!-- Image section -->
    <bx:documentsection name="Diagrams" 
                        src="https://example.com/architecture-diagram.png"
                        mimeType="image/png" />

    <!-- External HTML section -->
    <bx:documentsection name="Technical Specs" 
                        srcfile="/data/specifications.html"
                        mimeType="text/html" />
</bx:document>
```

## Section Bookmarks

When the `name` attribute is specified and the document has `bookmark="true"`, sections automatically create PDF bookmarks for easy navigation. The bookmark hierarchy follows the order of sections in the document.

## Related Components

- [Document](Document.md) - Main component for PDF generation
- [DocumentItem](DocumentItem.md) - Specifies headers, footers, and page breaks


