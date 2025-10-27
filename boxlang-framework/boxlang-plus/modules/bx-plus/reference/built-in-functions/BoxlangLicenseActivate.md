[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxlangLicenseActivate`

Activates a BoxLang+ or BoxLang++ license using an email address and license key. This function connects to the Ortus Solutions licensing server to validate and activate your subscription license.

## Method Signature

```
BoxlangLicenseActivate( email, licenseKey [, serverType ] )
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `email` | `STRING` | `true` | The email address associated with the license account |  |
| `licenseKey` | `STRING` | `true` | The license key to activate |  |
| `serverType` | `STRING` | `false` | The server environment type: `Production`, `Staging`, or `Development` | `Production` |

### Return Value

Returns a `STRUCT` with the following keys:

- `success` (BOOLEAN) - Whether the activation was successful
- `message` (STRING) - Status message or error description
- `isValidLicense` (BOOLEAN) - Whether the license is valid
- `isTrialMode` (BOOLEAN) - Whether the system is in trial mode
- `expirationDate` (STRING) - License expiration date (if applicable)

## Examples

### Template Syntax

```js
// Activate a production license
<bx:script>
    result = boxlangLicenseActivate(
        email = "admin@example.com",
        licenseKey = "XXXX-XXXX-XXXX-XXXX",
        serverType = "Production"
    );

    if ( result.success ) {
        writeOutput( "License activated successfully!" );
    } else {
        writeOutput( "Activation failed: " & result.message );
    }
</bx:script>
```

### Script Syntax

```js
// Activate a staging license with error handling
result = boxlangLicenseActivate(
    email = "admin@staging.example.com",
    licenseKey = "XXXX-XXXX-XXXX-XXXX",
    serverType = "Staging"
);

if ( result.success ) {
    systemOutput( "✓ License activated: " & result.message );
    systemOutput( "Expiration: " & result.expirationDate );
} else {
    systemOutput( "✗ Error: " & result.message );
    throw new Exception( result.message );
}
```

### Error Handling Example

```js
try {
    result = boxlangLicenseActivate(
        email = "admin@example.com",
        licenseKey = "INVALID-KEY",
        serverType = "Production"
    );

    if ( !result.success ) {
        systemOutput( "Activation failed: " & result.message );
    }
} catch ( Exception e ) {
    systemOutput( "Exception during activation: " & e.message );
}
```

## Related

- [`BoxlangLicenseInfo()`](BoxlangLicenseInfo.md) - Get current license status and information
- [`BoxlangLicenseRefresh()`](BoxlangLicenseRefresh.md) - Refresh an existing license token
