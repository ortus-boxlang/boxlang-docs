---
name: boxlang-core-dev-component-development
description: "Use this skill when creating custom BoxLang components (tags): component file structure, attribute declarations, body/output handling, registering component paths in modules, the difference between components and classes, and testing custom components."
---

# BoxLang Component Development

## Overview

BoxLang **components** (also called "custom tags") are reusable markup-oriented
units invoked with tag-like syntax in `.bxm` templates. Unlike classes, components
are designed for output generation and template composition. They live in the
`components/` directory of a module and are registered globally when the module loads.

## BoxLang Component Syntax — NOT CFML

All built-in and custom components in BoxLang use the `bx:` prefix.
**Never use `cf`-prefixed functions or tags** — those are CFML, not BoxLang.

```boxlang
// CORRECT BoxLang component syntax
bx:header name="Content-Type" value="application/json";
bx:location url="/dashboard" addToken=false;
bx:abort;
bx:include template="partials/nav.bxm";

// Paired component with body
bx:transaction {
    // body
}

// WRONG \u2014 these are CFML, not BoxLang
cfheader( name="Content-Type", value="application/json" )   // \u274c CFML function
<cfabort>                                                    // \u274c CFML tag
<cflocation url="/dashboard">                               // \u274c CFML tag
```

### Calling Components in Script

Self-closing components end with a **semicolon** to terminate the invocation:

```boxlang
// Self-closing \u2014 semicolon required in script
bx:header name="X-Custom" value="hello";
bx:setting showdebugoutput=false;

// Paired \u2014 body in braces (no trailing semicolon on the closing brace)
bx:savecontent variable="local.output" {
    writeOutput( "captured content" )
}
```

### Property Declarations (class body)

In a class or component body, `bx:property` declarations also end with a semicolon:

```boxlang
class {
    bx:property name="title"  type="string"  default="";
    bx:property name="count"  type="numeric" default=0;
    bx:property name="active" type="boolean" default=true;
}
```

## Component vs Class

| | Component (`.bx` in `components/`) | Class (`.bx` anywhere) |
|---|---|---|
| **Invocation** | `<bx:myTag attr="val">` | `new MyClass()` |
| **Purpose** | Output/template composition | Logic, services, models |
| **Body** | Can have child content | N/A |
| **Use in** | `.bxm` templates | Anywhere |

## Basic Component Structure

```boxlang
// components/Alert.bx
// Invoked as: <bx:alert type="warning" message="Something happened!" />

class {

    // Declare accepted attributes
    property name="type"    type="string"  default="info"
    property name="message" type="string"  required="true"
    property name="closable" type="boolean" default="true"

    /**
     * Called when the opening tag is encountered.
     * Return false to suppress body execution.
     */
    boolean function onStartTag( struct attributes, struct caller ) {
        // Normalize attributes
        if ( !listFindNoCase("info,success,warning,danger", attributes.type) ) {
            attributes.type = "info"
        }
        return true  // true = execute body (if any)
    }

    /**
     * Called after the body content (for paired tags) or after the tag (for self-closing).
     * Use this to render output.
     */
    void function onEndTag( struct attributes, struct caller, string generatedContent ) {

        // Render the component HTML
        writeOutput( '<div class="alert alert-#attributes.type#">' )

        if ( attributes.closable ) {
            writeOutput( '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' )
        }

        writeOutput( attributes.message )

        // Include any child body content
        if ( len( trim(generatedContent) ) ) {
            writeOutput( generatedContent )
        }

        writeOutput( '</div>' )
    }

}
```

### Usage in a Template

```boxlang
// Simple self-closing
<bx:alert type="success" message="Record saved successfully!" />

// With body content
<bx:alert type="warning">
    <strong>Please note:</strong> Your session will expire in 5 minutes.
</bx:alert>
```

## Component with Full Output Control

```boxlang
// components/DataTable.bx
class {

    property name="query"      required="true"
    property name="columns"    type="array"     default="#[]#"
    property name="cssClass"   type="string"    default="table"
    property name="caption"    type="string"    default=""

    boolean function onStartTag( struct attributes, struct caller ) {
        return true
    }

    void function onEndTag( struct attributes, struct caller, string generatedContent ) {
        var qry     = attributes.query
        var cols    = attributes.columns.len() ? attributes.columns : listToArray( qry.columnList )
        var cssClass = attributes.cssClass

        savecontent variable="local.tableHtml" {
            writeOutput( '<table class="#cssClass#">' )

            if ( len(attributes.caption) ) {
                writeOutput( '<caption>#encodeForHTML(attributes.caption)#</caption>' )
            }

            // Header row
            writeOutput( '<thead><tr>' )
            cols.each( (col) -> writeOutput('<th>#encodeForHTML(col)#</th>') )
            writeOutput( '</tr></thead>' )

            // Data rows
            writeOutput( '<tbody>' )
            for ( var i = 1; i <= qry.recordCount; i++ ) {
                writeOutput( '<tr>' )
                cols.each( (col) -> {
                    var cellVal = qry[col][i] ?: ""
                    writeOutput( '<td>#encodeForHTML(cellVal.toString())#</td>' )
                })
                writeOutput( '</tr>' )
            }
            writeOutput( '</tbody></table>' )
        }

        writeOutput( local.tableHtml )
    }

}
```

```boxlang
// Usage
<bx:dataTable
    query="#userQuery#"
    columns="#['name','email','status']#"
    cssClass="table table-striped"
    caption="Active Users"
/>
```

## Component with Body Processing

```boxlang
// components/Cache.bx
// Similar to <bx:cache> — caches child content

class {

    property name="key"       required="true"
    property name="timespan"  required="true"
    property name="cacheName" default="default"

    variables.cachedContent = ""
    variables.useCache      = false

    boolean function onStartTag( struct attributes, struct caller ) {
        // Check if we have a cached version
        var cached = cacheGet( attributes.key, false, attributes.cacheName )
        if ( !isNull(cached) ) {
            writeOutput( cached )
            variables.useCache = true
            return false  // false = skip executing the body
        }
        return true  // true = execute body and capture it in generatedContent
    }

    void function onEndTag( struct attributes, struct caller, string generatedContent ) {
        if ( !variables.useCache ) {
            // Cache the generated body content
            cachePut(
                attributes.key,
                generatedContent,
                attributes.timespan,
                "",
                attributes.cacheName
            )
            writeOutput( generatedContent )
        }
    }

}
```

## Accessing Caller Scope

The `caller` argument gives access to the calling template's scope:

```boxlang
void function onEndTag( struct attributes, struct caller, string generatedContent ) {
    // Read a variable from the calling template
    var userId = caller.userId ?: ""

    // Set a variable in the calling template
    caller.componentResult = processData( attributes.data )
}
```

## Attribute Validation

```boxlang
boolean function onStartTag( struct attributes, struct caller ) {
    // Required attribute check
    if ( !structKeyExists(attributes, "query") || isNull(attributes.query) ) {
        throw(
            message = "The 'query' attribute is required for <bx:dataTable>",
            type    = "MyModule.MissingAttributeError"
        )
    }

    // Type coercion
    if ( structKeyExists(attributes, "maxRows") ) {
        attributes.maxRows = val( attributes.maxRows )
        if ( attributes.maxRows < 1 ) attributes.maxRows = 100
    }

    return true
}
```

## Registering Component Paths in a Module

In `ModuleConfig.bx`:

```boxlang
class {

    // Register the module's components/ directory
    this.componentPaths = [
        "#moduleRecord.physicalPath#/components"
    ]

    // Or register a specific namespace
    this.componentNamespace = "mymodule"
    // Usage: <bx:mymodule:alert type="info" message="Hello!" />

}
```

After registration, components are available globally in all templates:

```boxlang
// Available after module loads (no imports needed):
<bx:alert type="info" message="Hello from my module!" />
<bx:dataTable query="#qry#" />
<bx:cache key="homePage" timespan="#createTimeSpan(0,1,0,0)#">
    <!-- expensive content here -->
</bx:cache>
```

## Self-Closing vs Paired Tags

BoxLang handles both automatically:

```boxlang
// Self-closing — onStartTag + onEndTag called with empty generatedContent
<bx:myTag attr="val" />

// Paired — body is executed and passed as generatedContent to onEndTag
<bx:myTag attr="val">
    body content here
</bx:myTag>
```

## Component Output Buffering

```boxlang
// Capture component output into a variable instead of writing to response
savecontent variable="myOutput" {
    // <bx:myTag ...> goes here in markup files
    // In script: invoke the component
    include template="components/Alert.bx"
        attributes={ type: "info", message: "Test" }
}
writeOutput( myOutput )
```

## Testing Custom Components

```boxlang
// tests/specs/AlertComponentTest.bx
class extends="testbox.system.BaseSpec" {

    function run() {
        describe( "Alert Component", function() {

            it( "should render an info alert", function() {
                savecontent variable="local.output" {
                    include template="#expandPath('./../../components/Alert.bx')#"
                        attributes={ type: "info", message: "Test message" }
                }
                expect( local.output ).toInclude( 'class="alert alert-info"' )
                expect( local.output ).toInclude( "Test message" )
            })

            it( "should default to info type when invalid type given", function() {
                savecontent variable="local.output" {
                    include template="#expandPath('./../../components/Alert.bx')#"
                        attributes={ type: "invalid", message: "Hello" }
                }
                expect( local.output ).toInclude( 'alert-info' )
            })

        })
    }

}
```

## CFML Compatibility Note

BoxLang components map to CFML custom tags (`<cf_myTag>`) when the
`bx-compat-cfml` module is enabled. Existing CFML custom tags work without modification.

## References

- [Components](https://boxlang.ortusbooks.com/boxlang-language/components)
- [Custom Tags / CFML Compat](https://boxlang.ortusbooks.com/boxlang-framework/boxlang-plus/modules/bx-compat-cfml)
- [Module Development](https://boxlang.ortusbooks.com/boxlang-framework/modularity)
- [Module Template](https://github.com/ortus-boxlang/boxlang-module-template)
