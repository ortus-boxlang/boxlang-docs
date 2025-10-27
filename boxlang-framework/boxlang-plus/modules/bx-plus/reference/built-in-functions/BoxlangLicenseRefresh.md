[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxlangLicenseRefresh`

Refreshes an existing BoxLang license token. This function uses the stored refresh token to obtain a new access token from the licensing server, extending the validity of the license without requiring manual re-activation.

## Method Signature

```
BoxlangLicenseRefresh()
```

### Arguments

No arguments. This function uses the stored refresh token from the active license.

### Return Value

Returns a `STRUCT` with the following keys:

- `success` (BOOLEAN) - Whether the refresh was successful
- `message` (STRING) - Status message or error description
- `isValidLicense` (BOOLEAN) - Whether the license is now valid
- `isTrialMode` (BOOLEAN) - Whether the system is in trial mode
- `expirationDate` (STRING) - New license expiration date
- `licenseType` (STRING) - Type of license: `BoxLang+` or `BoxLang++`

## Examples

### Template Syntax

```js
// Refresh the active license token
<bx:script>
    try {
        result = boxlangLicenseRefresh();

        if ( result.success ) {
            writeOutput( "License token refreshed successfully!" );
            writeOutput( "New Expiration: " & result.expirationDate );
        } else {
            writeOutput( "Refresh failed: " & result.message );
        }
    } catch ( Exception e ) {
        writeOutput( "Error refreshing license: " & e.message );
    }
</bx:script>
```

### Script Syntax

```js
// Refresh license with error handling
try {
    refreshResult = boxlangLicenseRefresh();

    if ( refreshResult.success ) {
        systemOutput( "✓ License refreshed successfully" );
        systemOutput( "Expiration: " & refreshResult.expirationDate );
    } else {
        systemOutput( "✗ Refresh failed: " & refreshResult.message );
        throw new Exception( refreshResult.message );
    }
} catch ( Exception e ) {
    systemOutput( "Exception: " & e.message );
}
```

### Scheduled Refresh Example

```js
// Scheduled task to refresh license weekly
scheduledTask = {
    name = "RefreshBoxLangLicense",
    task = () => {
        licenseInfo = boxlangLicenseInfo();

        // Only refresh if license is active
        if ( licenseInfo.isValidLicense ) {
            try {
                result = boxlangLicenseRefresh();
                systemOutput( "[" & now() & "] License refresh: " & result.message );
            } catch ( Exception e ) {
                systemOutput( "[ERROR] License refresh failed: " & e.message );
            }
        }
    },
    // Run every Monday at 2:00 AM
    schedule = "0 2 ? * MON"
};
```

### Combined License Management Example

```js
// Complete license management workflow
function manageLicense() {
    licenseInfo = boxlangLicenseInfo();

    // Check license status
    if ( licenseInfo.isValidLicense ) {
        systemOutput( "License Status: Active" );

        // Attempt to refresh token proactively
        try {
            refreshResult = boxlangLicenseRefresh();
            if ( refreshResult.success ) {
                systemOutput( "License token refreshed" );
            }
        } catch ( Exception e ) {
            systemOutput( "License refresh failed: " & e.message );

            // If refresh fails, may need reactivation
            systemOutput( "Please contact Ortus Support" );
        }
    } else if ( licenseInfo.isTrialMode ) {
        systemOutput( "Trial Mode Active - activation required" );
    } else {
        systemOutput( "No valid license - activation required" );
    }
}
```

## Related

- [`BoxlangLicenseInfo()`](BoxlangLicenseInfo.md) - Get current license status and information
- [`BoxlangLicenseActivate()`](BoxlangLicenseActivate.md) - Activate a new license with email and key
