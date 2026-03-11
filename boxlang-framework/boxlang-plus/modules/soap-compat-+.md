---
description: >-
  Premium SOAP webservices compatibility module for high-performance parsing and
  generation of delimited datasets in BoxLang+ applications.
icon: file-xml
---

# SOAP Compat +

{% include "../../../.gitbook/includes/this-component-is-only-avai....md" %}

The `bx-compat-soap` module provides comprehensive SOAP (Simple Object Access Protocol) web services functionality for BoxLang applications. It provides Compatibility for existing CFML Axis-based web services functionality. This module enables you to create and manage SOAP-based web services with automatic WSDL generation, request/response handling, and full support for complex data types.

### Features

* 🌐 **Automatic WSDL Generation** - Generate standards-compliant WSDL documents from BoxLang classes
* 🔄 **SOAP Request/Response Handling** - Parse and process SOAP envelopes with namespace support
* 🎯 **Type Coercion** - Automatic type conversion between SOAP XML types and BoxLang types
* 📋 **Metadata Extraction** - Extract function metadata for WSDL operation definitions
* 🚀 **Web Context Support** - Full integration with BoxLang web request/response cycle
* ⚡ **SOAPAction Routing** - Automatic routing based on SOAPAction headers or XML body

### Installation

Install the module using CommandBox:

```bash
box install bx-compat-soap
```

### Usage

#### Creating a SOAP Web Service

To create a SOAP web service, simply create a BoxLang class with `remote` methods:

```javascript
/**
 * Calculator Web Service
 */
class {
    
    /**
     * Add two numbers
     * @a First number
     * @b Second number
     * @return The sum
     */
    remote numeric function add( required numeric a, required numeric b ) {
        return arguments.a + arguments.b;
    }
    
    /**
     * Get user information
     * @userId The user ID to lookup
     * @return User struct
     */
    remote struct function getUser( required string userId ) {
        return {
            id: arguments.userId,
            name: "John Doe",
            email: "john@example.com"
        };
    }
    
    /**
     * Get list of users
     * @limit Maximum number of users to return
     * @return Array of user structs
     */
    remote array function getUsers( numeric limit = 10 ) {
        var users = [];
        for( var i = 1; i <= arguments.limit; i++ ) {
            users.append({
                id: i,
                name: "User #i#"
            });
        }
        return users;
    }
    
    /**
     * This method is NOT accessible via SOAP (not marked as remote)
     */
    public numeric function multiply( required numeric a, required numeric b ) {
        return arguments.a * arguments.b;
    }
}
```

#### Accessing the WSDL

The WSDL is automatically generated and accessible via the `?wsdl` parameter:

```
http://yourserver/path/to/Calculator.bx?wsdl
```

#### SOAP XML Request Format

Send SOAP requests to your service endpoint using standard SOAP envelope format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soapenv:Body>
        <ns1:add soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
            xmlns:ns1="http://DefaultNamespace">
            <a xsi:type="xsd:double">5.0</a>
            <b xsi:type="xsd:double">10.0</b>
        </ns1:add>
    </soapenv:Body>
</soapenv:Envelope>
```

#### SOAP Response Format

The service returns standard SOAP responses:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soap:Body>
        <addResponse xmlns="http://boxlang.ortussolutions.com/soap/">
            <return>15.0</return>
        </addResponse>
    </soap:Body>
</soap:Envelope>
```

#### Error Handling (SOAP Faults)

Errors are returned as standard SOAP faults:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultcode>Server</faultcode>
            <faultstring>Method not found or not accessible: multiply</faultstring>
            <detail>Only methods with access="remote" can be invoked via SOAP</detail>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>
```

### Consuming SOAP Web Services

#### Using createObject()

The easiest way to consume a SOAP web service is using BoxLang's `createObject()` function:

```javascript
// Create a SOAP web service instance
ws = createObject( "webservice", "http://example.com/Calculator.bx?wsdl" );

// Call methods directly on the web service object
result = ws.add( 5, 10 );
writeOutput( "5 + 10 = #result#" );

// Call methods with named arguments
user = ws.getUser( userId = "123" );
writeOutput( "User: #user.name# (#user.email#)" );

// Get multiple results
users = ws.getUsers( limit = 5 );
for( user in users ) {
    writeOutput( "#user.id#: #user.name#<br>" );
}
```

#### Advanced SOAP Client Usage

For more control over the SOAP request, you can configure the web service instance:

```javascript
// Create web service with custom configuration
ws = createObject( 
    "webservice", 
    "http://example.com/Calculator.bx?wsdl",
    {
        timeout: 30,
        username: "admin",
        password: "secret"
    }
);

// Call methods
result = ws.complexCalculation( 
    operation = "multiply",
    values = [1, 2, 3, 4, 5]
);
```

#### Handling SOAP Faults

SOAP faults are automatically converted to BoxLang exceptions:

```javascript
try {
    ws = createObject( "webservice", "http://example.com/Calculator.bx?wsdl" );
    
    // Try to call a non-remote method (will throw exception)
    result = ws.multiply( 5, 10 );
    
} catch( any e ) {
    writeOutput( "SOAP Error: #e.message#" );
    writeOutput( "Detail: #e.detail#" );
}
```



### Supported Data Types

#### Simple Types

* `string` → `xsd:string`
* `numeric` → `xsd:double`
* `boolean` → `xsd:boolean`
* `date` → `xsd:dateTime`

#### Complex Types

* `binary` → `xsd:base64Binary`
* `struct` → `apachesoap:map`  or `xsd:complexType`&#x20;
* `array` → Array type with sequential items
* `any` → `xsd:anyType`

