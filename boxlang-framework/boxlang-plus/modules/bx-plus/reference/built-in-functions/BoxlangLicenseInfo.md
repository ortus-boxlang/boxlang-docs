[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxlangLicenseInfo`

Retrieves the current BoxLang license status and information. This function returns details about the active license, including validity status, trial mode information, and license attributes.

## Method Signature

```
BoxlangLicenseInfo()
```

### Arguments

No arguments.

### Return Value

Returns a `STRUCT` with the following keys:

- `isValidLicense` (BOOLEAN) - Whether a valid license is currently active
- `isTrialMode` (BOOLEAN) - Whether the system is running in 60-day trial mode
- `email` (STRING) - Email address associated with the license (if activated)
- `serverType` (STRING) - Server environment type: `Production`, `Staging`, or `Development`
- `expirationDate` (STRING) - License expiration date in ISO format (if available)
- `licenseType` (STRING) - Type of license: `BoxLang+` or `BoxLang++`
- `message` (STRING) - Status message describing the current license state

## Examples

### Template Syntax

```js
// Check current license status
<bx:script>
    licenseInfo = boxlangLicenseInfo();

    if ( licenseInfo.isValidLicense ) {
        writeOutput( "✓ BoxLang+ License Active" );
        writeOutput( "Email: " & licenseInfo.email );
        writeOutput( "Server Type: " & licenseInfo.serverType );
        writeOutput( "Expires: " & licenseInfo.expirationDate );
    } else if ( licenseInfo.isTrialMode ) {
        writeOutput( "Currently in 60-day trial mode" );
    } else {
        writeOutput( "No valid license detected" );
    }
</bx:script>
```

### Script Syntax

```js
// Display detailed license information
licenseInfo = boxlangLicenseInfo();

systemOutput( "=== BoxLang License Status ===" );
systemOutput( "Valid License: " & ( licenseInfo.isValidLicense ? "Yes" : "No" ) );
systemOutput( "Trial Mode: " & ( licenseInfo.isTrialMode ? "Yes" : "No" ) );

if ( licenseInfo.isValidLicense ) {
    systemOutput( "Email: " & licenseInfo.email );
    systemOutput( "Type: " & licenseInfo.licenseType );
    systemOutput( "Server: " & licenseInfo.serverType );
    systemOutput( "Expires: " & licenseInfo.expirationDate );
}
```

### Conditional Logic Example

```js
licenseInfo = boxlangLicenseInfo();

// Enable premium features based on license type
if ( licenseInfo.isValidLicense && licenseInfo.licenseType == "BoxLang++" ) {
    enableAdvancedFeatures = true;
    enablePDF = true;
    enableSpreadsheet = true;
} else if ( licenseInfo.isValidLicense && licenseInfo.licenseType == "BoxLang+" ) {
    enableAdvancedFeatures = true;
    enablePDF = false;
    enableSpreadsheet = true;
} else if ( licenseInfo.isTrialMode ) {
    systemOutput( "Trial mode - limited features available" );
} else {
    systemOutput( "Please activate a BoxLang license to continue" );
}
```

## Related

- [`BoxlangLicenseActivate()`](BoxlangLicenseActivate.md) - Activate a new license with email and key
- [`BoxlangLicenseRefresh()`](BoxlangLicenseRefresh.md) - Refresh an existing license token
