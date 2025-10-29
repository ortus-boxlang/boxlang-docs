
# Component: `PDFForm`

--------------------------------------------------------------------------
 _invoke()
 --------------------------------------------------------------------------
 Manipulates existing forms created in Adobe Acrobat and Adobe LiveCycle Designer.

 {% hint style="danger" %}
This component is only available to [Boxlang+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](https://forgebox.io/view/bx-plus) with a limited trial.
{% endhint %}

## Component Signature

```
<bx:PDFForm action=[string]
source=[any]
destination=[string]
overwrite=[boolean]
overwriteData=[boolean]
XMLdata=[string]
fdf=[boolean]
fdfdata=[string]
result=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | String - The action to perform on the PDF form.<br>                   Valid values: "populate", "read"<br>                   Required. |  |
| `source` | `any` | `true` | Any - The source PDF document to operate on. Can be a file path,<br>                   byte array, or PDF document variable.<br>                   Required. |  |
| `destination` | `string` | `false` | String - The output file pathname for populate action.<br>                        File extension determines format (PDF or XDP for LiveCycle forms).<br>                        If not specified, form is displayed in browser. |  |
| `overwrite` | `boolean` | `false` | Boolean - Whether to overwrite the destination file.<br>                      Default: false | `false` |
| `overwriteData` | `boolean` | `false` | Boolean - Whether to overwrite existing data in form fields<br>                          with data from the data source (populate action only).<br>                          Default: false | `false` |
| `XMLdata` | `string` | `false` | String - XML data file pathname, XML object, or XML string.<br>                    For populate: data to populate form fields.<br>                    For read: variable name to store extracted XML data. |  |
| `fdf` | `boolean` | `false` | Boolean - If true, creates FDF format instead of XML (populate action).<br>                Default: false | `false` |
| `fdfdata` | `string` | `false` | String - FDF data file pathname.<br>                    For populate: file to import FDF data from.<br>                    For read: file to export FDF data to. |  |
| `result` | `string` | `false` | String - ColdFusion structure variable name to contain form field values<br>                   (read action). Either result or XMLdata must be specified for read action. |  |

## Examples

### Populating Form Fields with Data

```js
<!-- Create form data structure -->
<bx:set formData = {
    "employeeName": "John Doe",
    "employeeID": "12345",
    "department": "Engineering",
    "startDate": "2024-01-15",
    "salary": 75000
} />

<!-- Convert to XML for population -->
<bx:set xmlData = serializeXML(formData) />

<!-- Populate the PDF form -->
<bx:pdfform action="populate"
            source="employee-form-template.pdf"
            destination="completed-employee-form.pdf"
            xmldata="#xmlData#"
            overwrite="true" />
```

### Reading Form Field Values

```js
<!-- Read form data into a structure -->
<bx:pdfform action="read"
            source="submitted-form.pdf"
            result="formFields" />

<!-- Display the extracted data -->
<bx:output>
<h3>Form Data Extracted:</h3>
<ul>
<bx:loop collection="#formFields#" item="fieldName">
    <li><strong>#fieldName#:</strong> #formFields[fieldName]#</li>
</bx:loop>
</ul>
</bx:output>
```

### Using XML Data File

```js
<!-- Populate form from XML file -->
<bx:pdfform action="populate"
            source="contract-template.pdf"
            destination="personalized-contract.pdf"
            xmldata="/data/client-info.xml"
            overwrite="true" />

<!-- Read form data to XML file -->
<bx:pdfform action="read"
            source="signed-contract.pdf"
            xmldata="/exports/contract-data.xml" />
```

### FDF Data Handling

```js
<!-- Populate form using FDF data -->
<bx:pdfform action="populate"
            source="registration-form.pdf"
            destination="completed-registration.pdf"
            fdfdata="/imports/registration-data.fdf"
            overwrite="true" />

<!-- Export form data as FDF -->
<bx:pdfform action="read"
            source="filled-form.pdf"
            fdfdata="/exports/form-data.fdf"
            fdf="true" />
```

### Multiple Form Fields with XML

```xml
<!-- Example XML data file (client-data.xml) -->
<?xml version="1.0" encoding="UTF-8"?>
<form>
    <firstName>Jane</firstName>
    <lastName>Smith</lastName>
    <email>jane.smith@example.com</email>
    <phone>555-0123</phone>
    <address>
        <street>123 Main St</street>
        <city>Anytown</city>
        <state>CA</state>
        <zip>90210</zip>
    </address>
    <preferences>
        <newsletter>true</newsletter>
        <notifications>false</notifications>
    </preferences>
</form>
```

```js
<!-- Use the XML file to populate form -->
<bx:pdfform action="populate"
            source="customer-profile-form.pdf"
            destination="jane-smith-profile.pdf"
            xmldata="/data/client-data.xml"
            overwriteData="true"
            overwrite="true" />
```

### Complex Form Processing Workflow

```js
<bx:try>
    <!-- Step 1: Read existing form data -->
    <bx:pdfform action="read"
                source="partial-application.pdf"
                result="existingData" />
    
    <!-- Step 2: Merge with new data -->
    <bx:set updatedData = structCopy(existingData) />
    <bx:set updatedData.reviewDate = dateFormat(now(), "yyyy-mm-dd") />
    <bx:set updatedData.reviewedBy = "Manager" />
    <bx:set updatedData.status = "Approved" />
    
    <!-- Step 3: Convert to XML -->
    <bx:set xmlData = serializeXML(updatedData) />
    
    <!-- Step 4: Populate final form -->
    <bx:pdfform action="populate"
                source="application-template.pdf"
                destination="approved-application.pdf"
                xmldata="#xmlData#"
                overwriteData="true"
                overwrite="true" />
    
    <p>Application processed and approved successfully!</p>
    
<bx:catch type="any">
    <p>Error processing form: #cfcatch.message#</p>
</bx:catch>
</bx:try>
```

### Conditional Field Population

```js
<bx:set clientType = "premium" />

<!-- Create conditional data based on client type -->
<bx:if clientType eq "premium">
    <bx:set formData = {
        "clientName": "Premium Client Corp",
        "tier": "Premium",
        "discount": "15%",
        "supportLevel": "24/7 Priority",
        "accountManager": "Senior Account Manager"
    } />
<bx:else>
    <bx:set formData = {
        "clientName": "Standard Client Inc",
        "tier": "Standard", 
        "discount": "5%",
        "supportLevel": "Business Hours",
        "accountManager": "Account Representative"
    } />
</bx:if>

<!-- Populate appropriate form template -->
<bx:pdfform action="populate"
            source="service-agreement-template.pdf"
            destination="client-service-agreement.pdf"
            xmldata="#serializeXML(formData)#"
            overwrite="true" />
```

## Form Field Types Supported

The PDFForm component supports all standard PDF form field types:

- **Text Fields** - Single and multi-line text input
- **Checkboxes** - Boolean values (true/false)
- **Radio Buttons** - Single selection from options
- **Dropdown Lists** - Selection from predefined options
- **Signature Fields** - Digital signature areas
- **Date Fields** - Date picker controls

## Data Format Requirements

When populating forms, ensure your data structure matches the field names in the PDF form. Field names are case-sensitive and must match exactly.

## Related Components

- [PDF](PDF.md) - Main PDF manipulation component
- [PDFFormParam](PDFFormParam.md) - Specify individual form field parameters


