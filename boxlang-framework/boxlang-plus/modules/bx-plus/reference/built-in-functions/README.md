---
description: Built-In Functions for BoxLang+ Core Licensing Module
icon: function
---

# 📚 Built-In Functions

The bx-plus module provides three built-in functions for comprehensive license management:

## License Management Functions

### 🔑 [BoxlangLicenseActivate](BoxlangLicenseActivate.md)

Activate a new BoxLang+ or BoxLang++ license using an email address and license key.

**Usage:**

```js
result = boxlangLicenseActivate( 
    email = "admin@example.com",
    licenseKey = "XXXX-XXXX-XXXX-XXXX",
    serverType = "Production"
);
```

### ℹ️ [BoxlangLicenseInfo](BoxlangLicenseInfo.md)

Get current license status and detailed information about the active license.

**Usage:**

```js
licenseInfo = boxlangLicenseInfo();
if ( licenseInfo.isValidLicense ) {
    systemOutput( "License active until: " & licenseInfo.expirationDate );
}
```

### 🔄 [BoxlangLicenseRefresh](BoxlangLicenseRefresh.md)

Refresh an existing license token to extend its validity period.

**Usage:**

```js
try {
    result = boxlangLicenseRefresh();
    if ( result.success ) {
        systemOutput( "License refreshed successfully" );
    }
} catch ( Exception e ) {
    systemOutput( "Error: " & e.message );
}
```
