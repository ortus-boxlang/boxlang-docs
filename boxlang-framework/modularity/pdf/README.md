---
description: This module allows you to interact with PDF documents
icon: file-pdf
---

# PDF

This module provides PDF generation functionality to Boxlang.  In conjunction, [the BoxLang+ licensed version of the module](/boxlang-framework/boxlang-plus/modules/bx-plus-pdf.md) contributes advanced PDF functionality such as watermarking, form field completion and much more. 

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-pdf

# Using CommandBox to install for web servers.
box install bx-pdf
```

### Components

Th free tier version of this module contributes the following Components to the language:

* `document` - the wrapping component for creating PDF documents
  * The following attributes are available to the `document` component
    * `format` - The format of the document to generate. This attribute is unused and will be removed in a future release as only PDF generation is supported. Any other format requested will throw an error.
    * `encryption` - The encryption level to use for the document. Default is none. Possible values are 128-bit, 40-bit, none.
    * `localUrl` - If true, the document will be generated with local URLs. Default is false.
    * `variable` - The name of the variable to store the generated PDF binary.
    * `backgroundVisible` - If true, the background will be visible. Default is true.
    * `bookmark` - If true, bookmarks will be generated. Default is true.
    * `htmlBookmark` - If true, it is possible to convert outlines to a list of named anchors (`<a name="anchor_id">label</a>`) or a headings structure ( `<h1>... <h6>` ). Hyperlink jumps within the same document are supported as well.
    * `orientation` - The orientation of the document. Default is portrait. Possible values are portrait, landscape
    * `scale` - The percentage to scale the document. Must be less than or equal to 100.
    * `marginBottom` - The bottom margin of the document.
    * `marginLeft` - The left margin of the document.
    * `marginRight` - The right margin of the document.
    * `marginTop` - The top margin of the document.
    * `pageWidth` - The width of the page in inches.
    * `pageHeight` - The height of the page in inches.
    * `fontEmbed` - If true, fonts will be embedded in the document. Default is true.
    * `fontDirectory` - The directory where fonts are located.
    * `openpassword` - The password to open protected documents.
    * `ownerPassword` - The password to access restricted permissions.
    * `pageType` - The type of page to generate. Default is A4.
    * `pdfa` - If true, the document will be generated as a PDF/A document. Default is false.
    * `filename` - The filename to write the PDF to. If not provided and a `variable` argument is not provided, the PDF will be written to the browser (web-context only ).
    * `overwrite` - If true, the file will be overwritten if it exists. Default is false.
    * `saveAsName` - The name to save the PDF as in the browser.
    * `src` - A full URL or path relative to the web root of the source.
    * `srcfile` - The absolute path to a source file.
    * `mimeType` - The mime type of the source. Default is text/html. Possible values are text/html, text/plain, application/xml, image/jpeg, image/png, image/bmp, image/gif.
    * `unit` - The unit of measurement to use. Default is inches. Possible values are in, cm.
  * The following attributes are not currently implemented and will throw an error if used:
    * `permissions` - Granular permissability is not yet supported.
    * `permissionspassword` - Granular permissability is not yet supported.
    * `userPassword` - Granular permissability is not yet supported.
    * `authPassword` - Granular permissability is not yet supported.
    * `authUser` - Granular permissability is not yet supported.
    * `userAgent` - HTTP user agent identifier.
    * `proxyHost` - IP address or server name for proxy host.
    * `proxyPassword` - password for the proxy host.
    * `proxyPort` - port of the proxy host.
    * `proxyUser` - user name for the proxy host.
    * `tagged` - yes|no ACF OpenOffice integration not supported.
    * `formfields` - yes|no Form field attributes are not implemented in standard module.
    * `formsType` - FDF|PDF|HTML|XML Form field attributes are not implemented in standard module.
* `documentitem` - specifies header, footer, and page breaks within a document body or `documentsection.`
  * The following attributes are available to the `documentitem` component:
    * `type` A string which dictates the type of item. Accepted values are `pagebreak`|`header`|`footer.`
    * `evalAtPrint` This attribute is deprecated as all content is evaluated when the body of the tag is processed.
* `documentsection` - Divides a PDF document into sections. Used in conjunction with a `documentitem` component, each section can have unique headers, footers, and page numbers. A page break will always precede a section.
  * The following attributes are available to the `documentsection` component:
    * `marginBottom` - The bottom margin of the section in the unit specified in the `document` component.
    * `marginLeft` - The left margin of the section in the unit specified in the `document` component.
    * `marginRight` - The right margin of the section in the unit specified in the `document` component.
    * `marginTop` - The top margin of the section in the unit specified in the `document` component.
    * `mimeType` - The mime type of the content. If the content is a file, the mime type is determined by the file extension. If the content is a URL, the mime type is determined by the HTTP response.
    * `name` - The name of the section. This is used as a bookmark for the section.
    * `srcfile` - The absolute path of the file to include in the section.
    * `src` - The URL or path relative to the web root of the content to include in the section.
  * The following attributes are not currently implemented and will throw an error if used
    * `userAgent` - The HTTP user agent identifier to use when fetching the content from a URL.
    * `authPassword` - The authentication password to use when fetching the content from a URL.
    * `authUser` - The authentication user name to use when fetching the content from a URL.

### Examples

A simple example using templating syntax to generate a physical file:

```html
<bx:set testImage = "https://ortus-public.s3.amazonaws.com/logos/ortus-medium.jpg"/>
<bx:document format="pdf" filename="/path/to/mydocument.pdf">
    <!--- Header for all sections --->
    <bx:documentitem type="header">
        <h1>This is my Header</h1>
    </bx:documentitem>
    <!--- Footer for all sections --->
    <bx:documentitem type="footer">
        <h1>This is My Footer</h1>
        <bx:output><p>Page #bxdocument.currentpagenumber# of #bxdocument.totalpages#</p></bx:output>
    </bx:documentitem>
    <!--- Document section, which will be bookmarked as "Section 1" --->
    <bx:documentsection name="Section 1">
        <h1>Section 1</h1>
    </bx:documentsection>
    <!--- Document section, which will be bookmarked as "Section 2" --->
    <bx:documentsection name="Section 2">
        <h1>Section 2</h1>
    </bx:documentsection>
    <!--- Document section, which contains an image --->
    <bx:documentsection src="#testImage#">
</bx:document>
```

Example, using script syntax to create a variable containing the binary contents of the PDF, which is then written to a file

```javascript
bx:document format="pdf" variable="myPDF"{
    bx:documentsection name="Section 1"{
        writeOutput("<h1>Section 1</h1>");
        include "/path/to/section1.bxm";
    }
    bx:documentsection name="Section 2"{
        writeOutput("<h1>Section 2</h1>");
        include "/path/to/section2.bxm";
    }
}

fileWrite( "/path/to/mydocument.pdf", myPDF );
```

### Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27017\&issuetype=1).
