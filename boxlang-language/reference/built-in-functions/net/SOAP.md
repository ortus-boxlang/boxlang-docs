[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SOAP`

Returns a fluent SOAP client for making SOAP web service requests.

This BIF creates a new or retrieves an existing BoxSoapClient instance based on the provided
 WSDL URL. The client can be used to fluently invoke SOAP operations discovered from the WSDL.
 The client provides fluent methods for configuring connection settings like setTimeout(),
 setAuthentication(), and addHeader().

 Example usage:

 <pre>
 // Create a SOAP client from WSDL
 ws = soap( "http://example.com/service.wsdl" )

 // Invoke a SOAP operation: methodName, passing arguments as an array
 result = ws.invoke( "methodName", [ arg1, arg2 ] )

 // With authentication and timeout configuration
 ws = soap( "http://example.com/service.wsdl" )
     .setTimeout( 60 )
     .setAuthentication( "user", "pass" )

 result = ws.invoke( "methodName", [ arg1, arg2 ] )
 </pre>

## Method Signature

```
SOAP(URL=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` | The URL to the WSDL document describing the web service |  |

## Examples



## Related

  * [HTTP](./HTTP.md)
