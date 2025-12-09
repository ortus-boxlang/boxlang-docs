---
icon: soap
description: Consume SOAP web services with BoxLang's fluent SOAP client
---

# 🧼 SOAP Web Services

**New in BoxLang 1.8.0** - BoxLang provides a powerful, fluent SOAP client for consuming SOAP 1.1 and SOAP 1.2 web services. The `soap()` BIF automatically parses WSDL documents, discovers available operations, and provides intelligent type conversion between SOAP XML and BoxLang types.

## 🚀 Quick Start

```js
// Create SOAP client from WSDL
ws = soap( "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL" );

// Invoke operations directly as methods
countries = ws.ListOfContinentsByName();
dump( countries );

// Pass arguments
countryInfo = ws.CountryISOCode( { sCountryName: "United States" } );
dump( countryInfo );
```

## 📋 Key Features

- 🔍 **Automatic WSDL Parsing** - Discovers operations, parameters, and types from WSDL
- 🎯 **Fluent API** - Call SOAP operations as native BoxLang methods
- 🔄 **Automatic Type Conversion** - Converts SOAP XML types to BoxLang types automatically
- 📦 **Smart Response Unwrapping** - Automatically unwraps single-property SOAP responses
- 🔒 **Authentication Support** - HTTP Basic Auth for secured services
- ⏱️ **Configurable Timeouts** - Control request timeouts
- 📊 **SOAP 1.1 & 1.2** - Supports both SOAP versions with automatic detection
- 🔧 **Custom Headers** - Add custom HTTP headers as needed
- 📈 **Statistics Tracking** - Monitor invocations, successes, and failures

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Key Features](#key-features)
- [The soap() BIF](#the-soap-bif)
- [Configuration Methods](#configuration-methods)
- [Invoking SOAP Operations](#invoking-soap-operations)
- [Real-World Examples](#real-world-examples)
- [Client Information Methods](#client-information-methods)
- [Automatic Type Conversion](#automatic-type-conversion)
- [WSDL Discovery](#wsdl-discovery)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)
- [Advanced Usage](#advanced-usage)
- [SOAP vs REST](#soap-vs-rest)
- [Summary](#summary)

## 🎯 The `soap()` BIF

The `soap()` BIF creates a fluent SOAP client from a WSDL URL. The client automatically discovers available operations and allows you to invoke them as native BoxLang methods.

### Basic Syntax

```js
soapClient = soap( wsdlUrl );
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `wsdlUrl` | string | Yes | The URL to the WSDL document describing the web service |

### Return Value

Returns a `BoxSoapClient` instance configured with all operations discovered from the WSDL.

---

## 🔧 Configuration Methods

The SOAP client provides fluent configuration methods that can be chained:

### `timeout( seconds )`

Set the request timeout in seconds.

```js
ws = soap( "http://example.com/service.wsdl" )
    .timeout( 60 ); // 60 second timeout
```

### `withBasicAuth( username, password )`

Configure HTTP Basic Authentication for secured services.

```js
ws = soap( "http://example.com/service.wsdl" )
    .withBasicAuth( "myuser", "mypassword" );
```

### `header( name, value )`

Add a custom HTTP header to all requests.

```js
ws = soap( "http://example.com/service.wsdl" )
    .header( "X-API-Key", "your-api-key" )
    .header( "X-Client-Version", "1.0" );
```

### `soapVersion( version )`

Override the SOAP version (normally auto-detected from WSDL).

```js
ws = soap( "http://example.com/service.wsdl" )
    .soapVersion( "1.2" ); // Force SOAP 1.2
```

**Valid values:** `"1.1"` or `"1.2"`

### Chaining Configuration

All configuration methods return the client instance for fluent chaining:

```js
ws = soap( "http://example.com/service.wsdl" )
    .timeout( 30 )
    .withBasicAuth( "user", "pass" )
    .header( "X-Custom", "value" )
    .soapVersion( "1.2" );

// Now invoke operations
result = ws.myOperation( args );
```

---

## 🎬 Invoking SOAP Operations

Once you have a SOAP client, invoke operations directly as methods:

### Direct Method Invocation

```js
// No arguments
result = ws.operationName();

// With struct of named arguments
result = ws.operationName( { arg1: "value1", arg2: "value2" } );

// With array of positional arguments
result = ws.operationName( [ "value1", "value2" ] );
```

### Using the `invoke()` Method

You can also use the `invoke()` method explicitly:

```js
result = ws.invoke( "operationName", { arg1: "value1" } );
```

---

## 🌍 Real-World Examples

### Example 1: Country Information Service

```js
// Create client from public WSDL
ws = soap( "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL" );

// Get list of continents
continents = ws.ListOfContinentsByName();
dump( continents );

// Get country info by ISO code
countryInfo = ws.CountryISOCode( { sCountryName: "United States" } );
println( "ISO Code: " & countryInfo );

// Get capital city
capital = ws.CapitalCity( { sCountryISOCode: "US" } );
println( "Capital: " & capital );

// Get country currency
currency = ws.CountryCurrency( { sCountryISOCode: "US" } );
dump( currency );
```

### Example 2: Weather Service

```js
// Weather service with authentication
ws = soap( "http://example.com/weather.wsdl" )
    .withBasicAuth( "apiuser", "apipass" )
    .timeout( 30 );

// Get weather by zip code
weather = ws.GetWeatherByZipCode( { zipCode: "90210" } );

println( "Temperature: " & weather.temperature & "°F" );
println( "Conditions: " & weather.conditions );
println( "Humidity: " & weather.humidity & "%" );
```

### Example 3: Payment Gateway

```js
// Secure payment service
ws = soap( "https://secure.paymentgateway.com/api/v1?wsdl" )
    .withBasicAuth( "merchant_id", "api_secret" )
    .header( "X-Client-ID", "your-client-id" )
    .timeout( 45 );

// Process payment
result = ws.ProcessPayment( {
    amount: 99.99,
    currency: "USD",
    cardNumber: "4111111111111111",
    expiryMonth: 12,
    expiryYear: 2025,
    cvv: "123",
    billingAddress: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        zip: "12345"
    }
} );

if ( result.approved ) {
    println( "Payment approved! Transaction ID: " & result.transactionId );
} else {
    println( "Payment declined: " & result.declineReason );
}
```

### Example 4: CRM Integration

```js
// Salesforce SOAP API example
ws = soap( "https://login.salesforce.com/services/Soap/u/58.0" )
    .timeout( 60 )
    .header( "X-SFDC-Session", sessionId );

// Query accounts
accounts = ws.query( {
    queryString: "SELECT Id, Name, Industry FROM Account WHERE Industry = 'Technology' LIMIT 10"
} );

// Create new contact
newContact = ws.create( {
    sObjectType: "Contact",
    FirstName: "John",
    LastName: "Doe",
    Email: "john.doe@example.com",
    AccountId: "001XX000003DHJ0"
} );

println( "Created contact with ID: " & newContact.id );
```

### Example 5: Shipping Service

```js
// UPS/FedEx-style shipping service
ws = soap( "https://shipping.example.com/ShipService?wsdl" )
    .withBasicAuth( "account_number", "api_key" )
    .timeout( 30 );

// Get shipping rates
rates = ws.GetShippingRates( {
    origin: {
        address: "123 Warehouse Rd",
        city: "Los Angeles",
        state: "CA",
        zip: "90001"
    },
    destination: {
        address: "456 Customer St",
        city: "New York",
        state: "NY",
        zip: "10001"
    },
    package: {
        weight: 5.5,
        length: 12,
        width: 10,
        height: 8,
        units: "inches"
    }
} );

// Display rates
rates.each( ( rate ) => {
    println( "#rate.service#: $#rate.cost# (#rate.deliveryDays# days)" );
} );

// Create shipment
shipment = ws.CreateShipment( {
    service: "GROUND",
    origin: originAddress,
    destination: destAddress,
    package: packageDetails
} );

println( "Tracking number: " & shipment.trackingNumber );
```

---

## 📊 Client Information Methods

The SOAP client provides several methods to inspect and understand the web service:

### `getOperationNames()`

Returns an array of all available operation names.

```js
ws = soap( "http://example.com/service.wsdl" );
operations = ws.getOperationNames();
dump( operations );
// Output: ["operationOne", "operationTwo", "operationThree"]
```

### `hasOperation( operationName )`

Check if a specific operation exists.

```js
if ( ws.hasOperation( "GetCustomer" ) ) {
    customer = ws.GetCustomer( { customerId: 123 } );
}
```

### `getOperationInfo( operationName )`

Get detailed information about a specific operation.

```js
info = ws.getOperationInfo( "GetCustomer" );
dump( info );
// Output:
// {
//     name: "GetCustomer",
//     soapAction: "http://example.com/GetCustomer",
//     inputMessage: "GetCustomerRequest",
//     outputMessage: "GetCustomerResponse",
//     inputParameters: [
//         { name: "customerId", type: "int", namespace: "http://www.w3.org/2001/XMLSchema" }
//     ],
//     outputParameters: [
//         { name: "customer", type: "Customer", namespace: "http://example.com/types" }
//     ]
// }
```

### `getStatistics()`

Get client usage statistics.

```js
stats = ws.getStatistics();
dump( stats );
// Output:
// {
//     totalInvocations: 42,
//     successfulInvocations: 40,
//     failedInvocations: 2,
//     wsdlUrl: "http://example.com/service.wsdl",
//     serviceEndpoint: "http://example.com/service",
//     operationCount: 15,
//     createdAt: "2024-12-05T10:30:00Z"
// }
```

### `toStruct()`

Convert the entire client to a struct representation.

```js
clientInfo = ws.toStruct();
dump( clientInfo );
// Output:
// {
//     wsdlUrl: "http://example.com/service.wsdl",
//     serviceEndpoint: "http://example.com/service",
//     serviceName: "MyService",
//     targetNamespace: "http://example.com/",
//     bindingStyle: "document",
//     operations: [...],
//     soapVersion: "1.1",
//     timeout: 30,
//     statistics: {...}
// }
```

---

## 🔄 Automatic Type Conversion

One of the most powerful features of BoxLang's SOAP client is **automatic type conversion** between SOAP XML types and BoxLang types.

### XML Schema Types to BoxLang

BoxLang automatically converts XML Schema types to appropriate BoxLang types:

| XML Schema Type | BoxLang Type | Example |
|----------------|--------------|---------|
| `xsd:string` | String | `"hello"` |
| `xsd:int`, `xsd:integer` | Integer | `42` |
| `xsd:long` | Long | `9223372036854775807` |
| `xsd:float`, `xsd:double`, `xsd:decimal` | Double | `3.14159` |
| `xsd:boolean` | Boolean | `true`, `false` |
| `xsd:date`, `xsd:dateTime` | DateTime | `now()` |
| `xsd:base64Binary` | ByteArray | Binary data |
| Complex types | Struct | `{ field1: "value", field2: 123 }` |
| Arrays/Lists | Array | `["item1", "item2", "item3"]` |

### Intelligent Casting

When `xsi:type` information is present in the SOAP response, BoxLang uses it to cast values accurately:

```xml
<!-- SOAP Response -->
<result xsi:type="xsd:int">42</result>
```

```js
// BoxLang automatically converts to integer
result = ws.myOperation(); // result = 42 (integer, not "42" string)
```

Without `xsi:type`, BoxLang attempts intelligent casting:

```js
// "123" → 123 (integer)
// "3.14" → 3.14 (double)
// "true" → true (boolean)
// "2024-12-05T10:30:00Z" → DateTime object
// "hello" → "hello" (string - no casting needed)
```

### Complex Type Conversion

SOAP complex types are automatically converted to BoxLang structs:

```xml
<!-- SOAP Response -->
<Customer>
    <Id>12345</Id>
    <Name>John Doe</Name>
    <Email>john@example.com</Email>
    <Active>true</Active>
    <Balance>1234.56</Balance>
</Customer>
```

```js
// Automatically becomes:
customer = {
    Id: 12345,              // Integer
    Name: "John Doe",       // String
    Email: "john@example.com", // String
    Active: true,           // Boolean
    Balance: 1234.56        // Double
};
```

### Array Conversion

SOAP arrays are automatically converted to BoxLang arrays:

```xml
<!-- SOAP Response -->
<ArrayOfString>
    <string>Apple</string>
    <string>Banana</string>
    <string>Cherry</string>
</ArrayOfString>
```

```js
// Automatically becomes:
fruits = [ "Apple", "Banana", "Cherry" ];
```

### Response Unwrapping

Many SOAP services wrap the actual result in a container element. BoxLang automatically unwraps single-property structs:

```xml
<!-- SOAP Response -->
<GetCustomerResponse>
    <GetCustomerResult>
        <Customer>
            <Id>12345</Id>
            <Name>John Doe</Name>
        </Customer>
    </GetCustomerResult>
</GetCustomerResponse>
```

```js
// Without unwrapping, you'd get:
// { GetCustomerResult: { Customer: { Id: 12345, Name: "John Doe" } } }

// With automatic unwrapping (default), you get:
// { Customer: { Id: 12345, Name: "John Doe" } }

// Or even further unwrapped to:
// { Id: 12345, Name: "John Doe" }
```

This makes working with SOAP responses much more intuitive!

---

## 🔍 WSDL Discovery

BoxLang automatically parses WSDL documents and discovers:

- **Service endpoint** - Where to send SOAP requests
- **Operations** - Available methods you can call
- **Input parameters** - Required and optional arguments for each operation
- **Output types** - Return types and structure
- **SOAP version** - 1.1 or 1.2 (auto-detected from binding)
- **Binding style** - Document/literal, RPC/encoded, etc.

### Example: Inspecting a Service

```js
ws = soap( "http://example.com/service.wsdl" );

// Get service info
info = ws.toStruct();
println( "Service: " & info.serviceName );
println( "Endpoint: " & info.serviceEndpoint );
println( "SOAP Version: " & info.soapVersion );
println( "Operations: " & info.operations.len() );

// List all operations
operations = ws.getOperationNames();
operations.each( ( op ) => {
    opInfo = ws.getOperationInfo( op );
    println( "\n#op#:" );
    println( "  Input: #opInfo.inputParameters.len()# parameters" );
    opInfo.inputParameters.each( ( param ) => {
        println( "    - #param.name# (#param.type#)" );
    } );
} );
```

---

## ⚠️ Error Handling

SOAP faults are automatically converted to BoxLang exceptions:

```js
try {
    result = ws.ProcessPayment( {
        amount: 99.99,
        cardNumber: "invalid"
    } );
} catch ( any e ) {
    // SOAP Fault becomes BoxLang exception
    println( "SOAP Error: " & e.message );
    // Output: "SOAP Fault: [Client.InvalidCardNumber] Invalid credit card number - Card validation failed"

    // Access fault details
    println( "Type: " & e.type );
    println( "Detail: " & e.detail );
}
```

### SOAP Fault Structure

SOAP faults contain:
- **Fault Code** - Standard SOAP fault code (Client, Server, etc.)
- **Fault String** - Human-readable error message
- **Fault Detail** - Additional error details from the service

BoxLang combines these into a single exception message for easy handling.

---

## 💡 Best Practices

{% hint style="success" %}
**SOAP Client Best Practices:**

1. **Cache clients** - Create SOAP clients once and reuse them (WSDL parsing is expensive)
2. **Set appropriate timeouts** - SOAP calls can be slow, adjust timeouts accordingly
3. **Handle faults gracefully** - Always wrap SOAP calls in try-catch blocks
4. **Inspect operations first** - Use `getOperationNames()` to see what's available
5. **Check operation info** - Use `getOperationInfo()` to understand parameters before calling
6. **Use named arguments** - Struct arguments are clearer than positional arrays
7. **Monitor statistics** - Track invocations and failures with `getStatistics()`
8. **Secure credentials** - Never hardcode passwords, use environment variables or config files
9. **Test with public WSDLs** - Start with known working services for testing
10. **Log SOAP requests** - Enable debug logging to see raw SOAP XML for troubleshooting
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

- WSDL parsing happens once per client creation
- Clients are automatically cached by the HttpService
- Reuse clients across multiple invocations for best performance
- Consider connection pooling for high-volume SOAP calls
{% endhint %}

{% hint style="warning" %}
**Common Gotchas:**

- **Case sensitivity** - SOAP operation names are case-sensitive, match them exactly
- **Null values** - Some SOAP services don't handle null/empty values well
- **Namespace issues** - If operations aren't discovered, check WSDL namespace definitions
- **Authentication** - Some services require API keys in headers, not just basic auth
- **SOAP version** - Mismatched SOAP versions cause cryptic errors
- **Timeout defaults** - Default timeout is 30 seconds, increase for slow services
{% endhint %}

---

## 🔧 Advanced Usage

### Programmatic Operation Discovery

Build dynamic SOAP integrations by discovering operations at runtime:

```js
function callSoapOperation( wsdlUrl, operationName, args = {} ) {
    ws = soap( wsdlUrl );

    if ( !ws.hasOperation( operationName ) ) {
        throw( type="InvalidOperation", message="Operation '#operationName#' not found" );
    }

    opInfo = ws.getOperationInfo( operationName );

    // Log what we're about to call
    logger.info( "Calling #operationName# with #args.keyArray().len()# arguments" );

    try {
        result = ws.invoke( operationName, args );
        logger.info( "Success: #operationName#" );
        return result;
    } catch ( any e ) {
        logger.error( "SOAP fault in #operationName#: #e.message#" );
        rethrow;
    }
}

// Use it
result = callSoapOperation(
    "http://example.com/service.wsdl",
    "GetCustomer",
    { customerId: 123 }
);
```

### Building a SOAP Service Wrapper

Create a reusable service class:

```js
class WeatherService {
    property name="client";
    property name="logger";

    function init( apiKey ) {
        variables.logger = getLogger();
        variables.client = soap( "http://api.weather.com/service.wsdl" )
            .withBasicAuth( "api", apiKey )
            .timeout( 30 );

        logger.info( "WeatherService initialized with #client.getOperationNames().len()# operations" );

        return this;
    }

    function getCurrentWeather( zipCode ) {
        try {
            return client.GetCurrentWeather( { zipCode: zipCode } );
        } catch ( any e ) {
            logger.error( "Failed to get weather for #zipCode#: #e.message#" );
            // Return default/cached data or rethrow
            throw( type="WeatherServiceError", message="Unable to retrieve weather data" );
        }
    }

    function getForecast( zipCode, days = 5 ) {
        return client.GetForecast( {
            zipCode: zipCode,
            days: days
        } );
    }

    function getStatistics() {
        return client.getStatistics();
    }
}

// Use it
weatherService = new WeatherService( "your-api-key" );
current = weatherService.getCurrentWeather( "90210" );
forecast = weatherService.getForecast( "90210", 7 );
```

### Handling Multiple Services

Manage multiple SOAP services efficiently:

```js
class SoapServiceManager {
    property name="services" type="struct";

    function init() {
        variables.services = {};
        return this;
    }

    function registerService( name, wsdlUrl, config = {} ) {
        client = soap( wsdlUrl );

        if ( structKeyExists( config, "username" ) && structKeyExists( config, "password" ) ) {
            client.withBasicAuth( config.username, config.password );
        }

        if ( structKeyExists( config, "timeout" ) ) {
            client.timeout( config.timeout );
        }

        if ( structKeyExists( config, "headers" ) ) {
            config.headers.each( ( name, value ) => {
                client.header( name, value );
            } );
        }

        variables.services[ name ] = client;
        return this;
    }

    function getService( name ) {
        if ( !structKeyExists( variables.services, name ) ) {
            throw( type="ServiceNotFound", message="Service '#name#' not registered" );
        }
        return variables.services[ name ];
    }

    function getAllStatistics() {
        stats = {};
        variables.services.each( ( name, client ) => {
            stats[ name ] = client.getStatistics();
        } );
        return stats;
    }
}

// Use it
manager = new SoapServiceManager()
    .registerService( "weather", "http://api.weather.com/service.wsdl", {
        username: "api",
        password: "key123",
        timeout: 30
    } )
    .registerService( "shipping", "http://shipping.example.com/service.wsdl", {
        username: "account",
        password: "secret",
        timeout: 45,
        headers: { "X-API-Version": "2.0" }
    } );

// Call services
weather = manager.getService( "weather" ).GetCurrentWeather( { zipCode: "90210" } );
rates = manager.getService( "shipping" ).GetShippingRates( shippingDetails );

// Monitor all services
dump( manager.getAllStatistics() );
```

---

## 📚 SOAP vs REST

While BoxLang excels at both SOAP and REST APIs, here's when to choose each:

### Use SOAP When:

- ✅ Working with legacy enterprise systems
- ✅ Need WS-Security, WS-ReliableMessaging, or other WS-* standards
- ✅ Strict contracts and type safety required
- ✅ WSDL-based service discovery is beneficial
- ✅ Working with financial, healthcare, or government systems

### Use REST (http() BIF) When:

- ✅ Building modern web APIs
- ✅ Need lightweight, fast communication
- ✅ JSON is preferred over XML
- ✅ Stateless operations are sufficient
- ✅ HTTP caching and standard methods are beneficial

{% hint style="info" %}

BoxLang provides excellent support for both! Use:

- `soap()` BIF for SOAP web services
- `http()` BIF for RESTful APIs
- Both support authentication, timeouts, and error handling
{% endhint %}

---

## 🎯 Summary

BoxLang's SOAP support provides:

- 🔍 **Automatic WSDL discovery** - Parse and understand services automatically
- 🎯 **Fluent invocation** - Call SOAP operations like native BoxLang methods
- 🔄 **Intelligent type conversion** - SOAP XML types automatically become BoxLang types
- 📦 **Smart unwrapping** - Clean, intuitive response structures
- 🔒 **Authentication support** - HTTP Basic Auth built-in
- ⏱️ **Configurable behavior** - Timeouts, headers, SOAP versions
- 📊 **Service inspection** - Discover operations and parameters programmatically
- ⚠️ **Error handling** - SOAP faults become BoxLang exceptions
- 📈 **Statistics tracking** - Monitor usage and performance

Whether you're integrating with legacy enterprise systems, consuming third-party SOAP APIs, or building service-oriented architectures, BoxLang's SOAP client makes it simple and elegant.

```js
// It's this easy:
ws = soap( "http://example.com/service.wsdl" );
result = ws.myOperation( args );
```
