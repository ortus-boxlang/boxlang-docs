---
description: Real-world examples of Word document generation with BoxLang
icon: lightbulb
---

# 💡 Examples

Real-world patterns and scenarios for the BoxLang Word Module.

---

## 1. Sales Report

Generate a formatted sales report from query data:

```js
salesData = queryExecute( "
    SELECT product_name, units_sold, unit_price,
           (units_sold * unit_price) as revenue
    FROM sales
    WHERE quarter = 'Q4'
    ORDER BY revenue DESC
" )

word( "sales-report.docx" )
    .margins( 1.5, 1.5, 1.5, 1.5 )
    .setTitle( "Q4 Sales Report" )
    .setAuthor( "Sales Department" )
    .setSubject( "Quarterly sales summary" )
    .header( "ACME Corp — Q4 2024 Sales Report" )
    .addHeading( "Q4 2024 Sales Report", 1 )
    .addParagraph( "Generated on " & dateTimeFormat( now(), "yyyy-mm-dd HH:nn" ), {
        italic: true,
        size: 10,
        color: "808080"
    } )
    .addParagraph( "The following report summarizes sales performance for Q4 2024.", {
        spacingAfter: 240
    } )
    .addTable( salesData )
    .addPageBreak()
    .addHeading( "Summary", 2 )
    .addParagraph( "All products met or exceeded quarterly targets.", { bold: true } )
    .save()
```

---

## 2. Contract Generation from Template

Batch-generate contracts using a template with placeholders:

```js
clients = [
    { name: "Acme Corp", date: "2024-01-15", value: "$150,000" },
    { name: "Globex Inc", date: "2024-01-20", value: "$200,000" },
    { name: "Initech", date: "2024-02-01", value: "$75,000" }
]

clients.each( ( client ) => {
    word( "/templates/contract-template.docx" )
        .populate( {
            clientName: client.name,
            signDate: client.date,
            contractValue: client.value
        } )
        .save( "/output/contract_#client.name#.docx" )
} )
```

---

## 3. Invoice Builder

Create a professional invoice with calculated totals:

```js
lineItems = [
    [ "Item", "Qty", "Rate", "Amount" ],
    [ "Consulting", "40", "$150/hr", "$6,000.00" ],
    [ "Development", "80", "$125/hr", "$10,000.00" ],
    [ "Testing", "20", "$100/hr", "$2,000.00" ],
    [ "", "", "Total", "$18,000.00" ]
]

word( "invoice-2024-001.docx" )
    .margins( 2.0, 2.0, 2.5, 2.5 )
    .addParagraph( "INVOICE", {
        bold: true,
        size: 24,
        color: "2C3E50",
        alignment: "CENTER",
        spacingAfter: 480
    } )
    .addParagraph( "Invoice #: INV-2024-001", { bold: true, spacingAfter: 120 } )
    .addParagraph( "Date: " & dateTimeFormat( now(), "yyyy-mm-dd" ), { spacingAfter: 120 } )
    .addParagraph( "Due Date: " & dateTimeFormat( dateAdd( "d", 30, now() ), "yyyy-mm-dd" ), { spacingAfter: 360 } )
    .addTable( lineItems )
    .newLine()
    .addParagraph( "Payment Terms: Net 30", { italic: true, color: "808080" } )
    .addParagraph( "Thank you for your business!", { bold: true, alignment: "CENTER", spacingBefore: 240 } )
    .save()
```

---

## 4. Meeting Minutes with Nested Lists

Document meeting notes with structured lists:

```js
word( "meeting-minutes.docx" )
    .setTitle( "Project Kickoff Meeting Minutes" )
    .setAuthor( "Project Manager" )
    .header( "ACME Corp — Project Kickoff — " & dateTimeFormat( now(), "yyyy-mm-dd" ) )
    .addHeading( "Project Kickoff Meeting", 1 )
    .addParagraph( "Date: " & dateTimeFormat( now(), "yyyy-mm-dd" ), { spacingAfter: 120 } )
    .addParagraph( "Attendees: Alice, Bob, Charlie, Diana", { spacingAfter: 240 } )

    .addHeading( "Agenda", 2 )
    .addOrderedList( [
        "Project Overview",
        "Timeline & Milestones",
        { text: "Technical Architecture", items: [
            "Database Design",
            "API Contracts",
            "Frontend Framework Selection"
        ] },
        "Risk Assessment",
        "Next Steps"
    ] )

    .addHeading( "Action Items", 2 )
    .addUnorderedList( [
        "Alice: Set up project repository by Friday",
        "Bob: Draft API specification by next Wednesday",
        "Charlie: Prepare database migration plan",
        "Diana: Schedule follow-up meeting"
    ] )

    .addPageBreak()
    .addHeading( "Decisions Made", 2 )
    .addOrderedList( [
        "Use PostgreSQL for primary data store",
        "Adopt REST API with OpenAPI documentation",
        "Choose Vue.js for the frontend framework"
    ] )
    .save()
```

---

## 5. Employee Handbook with TOC

Create a structured handbook with auto-generated table of contents:

```js
word( "employee-handbook.docx" )
    .setTitle( "Employee Handbook 2024" )
    .setAuthor( "Human Resources" )
    .header( "ACME Corp — Employee Handbook" )
    .footer( "Confidential" )

    .addHeading( "Employee Handbook", 1 )
    .addParagraph( "Welcome to ACME Corp! This handbook outlines our policies, benefits, and expectations.", {
        spacingAfter: 240
    } )

    .addTableOfContents()
    .addPageBreak()

    .addHeading( "Company Overview", 1 )
    .addParagraph( "ACME Corp was founded in 2010 with a mission to..." )
    .addHeading( "Our Mission", 2 )
    .addParagraph( "To deliver innovative solutions that..." )
    .addHeading( "Our Values", 2 )
    .addUnorderedList( [ "Integrity", "Innovation", "Collaboration", "Excellence" ] )

    .addPageBreak()
    .addHeading( "Employment Policies", 1 )
    .addHeading( "Code of Conduct", 2 )
    .addParagraph( "All employees are expected to..." )
    .addHeading( "Work Hours", 2 )
    .addParagraph( "Standard office hours are 9 AM to 5 PM, Monday through Friday." )
    .addHeading( "Remote Work", 2 )
    .addParagraph( "Employees may work remotely up to 3 days per week with manager approval." )

    .addPageBreak()
    .addHeading( "Benefits", 1 )
    .addHeading( "Health Insurance", 2 )
    .addParagraph( "Comprehensive health, dental, and vision coverage..." )
    .addHeading( "Retirement Plan", 2 )
    .addParagraph( "401(k) with 5% company match..." )
    .addHeading( "Paid Time Off", 2 )
    .addParagraph( "20 days PTO per year, plus 10 company holidays." )

    .save()
```

{% hint style="info" %}
When opened in Word, the user will be prompted to update the TOC. This auto-populates headings and page numbers.
{% endhint %}

---

## 6. Marketing Brochure with Images

Create a visually rich marketing document:

```js
word( "brochure.docx" )
    .margins( 1.5, 1.5, 2.0, 2.0 )
    .addImageFromUrl( "https://example.com/hero-banner.jpg", 18.0, 5.0 )
    .newLine()

    .addHeading( "Introducing BoxLang", 1 )
    .addParagraph( "A modern, dynamic JVM language designed for the cloud era.", {
        size: 14,
        color: "2C3E50",
        alignment: "CENTER",
        spacingAfter: 360
    } )

    .addHeading( "Key Features", 2 )
    .addUnorderedList( [
        "Multi-runtime deployment (CLI, web, lambda, Docker, WASM)",
        "100% Java interoperability",
        "Familiar syntax for CFML developers",
        "Built-in async programming with virtual threads"
    ] )

    .addHeading( "Why Choose BoxLang?", 2 )
    .addTable( [
        [ "Feature", "BoxLang", "Alternatives" ],
        [ "Performance", "⚡ JVM-native", "🐌 Interpreted" ],
        [ "Deployment", "🌐 Multi-target", "🖥️ Server-only" ],
        [ "Ecosystem", "📦 Rich module system", "📦 Limited" ],
        [ "License", "🔓 Apache 2.0", "💰 Proprietary" ]
    ] )

    .addPageBreak()
    .addHeading( "Get Started Today", 2 )
    .addHyperlink( "Download BoxLang", "https://boxlang.io/download" )
    .newLine()
    .addHyperlink( "Read the Docs", "https://boxlang.ortusbooks.com" )
    .save()
```

---

## 7. Batch Document Generation

Generate hundreds of personalized documents from a data source:

```js
employees = queryExecute( "SELECT name, department, start_date, salary FROM employees" )

for ( row in employees ) {
    word( "/templates/offer-letter.docx" )
        .populate( {
            employeeName: row.name,
            department: row.department,
            startDate: dateTimeFormat( row.start_date, "yyyy-mm-dd" ),
            salary: dollarFormat( row.salary )
        } )
        .save( "/output/offers/offer_#row.name#.docx" )
}

writeOutput( "Generated #employees.recordCount# offer letters." )
```

---

## 8. Format Conversion Pipeline

Build a document processing pipeline that converts between formats:

```js
// Step 1: Receive HTML from a web form
submittedHtml = form.content

// Step 2: Convert HTML to a styled Word document
doc = word()
    .setTitle( form.title )
    .setAuthor( form.author )
    .fromHTML( submittedHtml )

// Step 3: Save the .docx
doc.save( "/archive/#form.title#.docx" )

// Step 4: Also export to Markdown for version control
markdown = doc.toMarkdown()
fileWrite( "/archive/#form.title#.md", markdown )

// Step 5: Extract plain text for search indexing
plainText = doc.toText()
searchService.index( form.title, plainText )

doc.close()
```

---

## 📚 Related Resources

{% content-ref url="user-guide.md" %}
{% content-ref url="advanced-features.md" %}
{% content-ref url="import-export.md" %}
{% content-ref url="reference/fluent-api/README.md" %}
