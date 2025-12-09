---
description: >-
  Core subscription bootstrap module enabling licensing utilities, and shared
  helpers for premium BoxLang+ modules.
icon: key
---

# Plus Core

The `bx-plus` module is the enterprise licensing and feature management module that unlocks the full potential of BoxLang+ and BoxLang++ subscription plans. This module provides the essential licensing infrastructure, validation, and activation services that enable access to premium enterprise features and functionality across all BoxLang+ and BoxLang++ modules.

## What This Module Enables

The **bx-plus** module serves as the foundation for enterprise BoxLang subscriptions by providing:

* **License Activation & Validation** - Secure JWT-based license management with automatic token refresh
* **Trial Mode Management** - 60-day trial period tracking for evaluation purposes
* **Enterprise Feature Gating** - Controls access to premium modules and functionality based on subscription level
* **Subscription Status Monitoring** - Real-time validation of license status and subscription benefits
* **Multi-Environment Support** - License binding and validation across development, staging, and production environments

## Premium Features Unlocked

With an active BoxLang+ or BoxLang++ subscription and this module, you gain access to enterprise-grade capabilities such as:

* **Advanced Caching & NoSQL** - Redis, Couchbase, MongoDB, and other distributed caching solutions
* **Enhanced Communication Services** - Enterprise messaging and notification systems ( Redis and Couchbase modules )
* **Premium CommandBox Features** - Multi-site management, advanced deployment tools, and professional server features
* **Priority Support & SLAs** - Business-grade support with guaranteed response times
* **Professional Tooling** - Enhanced development and debugging tools for enterprise workflows
* **Custom Language Parsers** - Support for additional language syntaxes and compatibility modules

## 📦 Installation

### Via CommandBox

```bash
box install bx-plus
```

### Via BoxLang

```bash
install-bx-module bx-plus
```

For a complete list of features and benefits, visit the [BoxLang Plans](https://boxlang.io/plans) page.

* `bx` - The BoxLang test code
* `java` - Java test code
* `resources` - Resources for testing
  * `libs` - BoxLang binary goes here for now.

## Getting Started

### License Activation

To activate your BoxLang+ or BoxLang++ subscription and enable enterprise features:

```javascript
// Activate your license using the provided BIF
boxlangLicenseActivate(
    email = "your-email@company.com",
    licenseKey = "your-license-key",
    serverType = "server" // or "cloud"
);
```

### Refreshing License Token

To refresh your license token and ensure continued access to enterprise features:

```javascript
// Refresh the current license token
refreshResult = boxlangLicenseRefresh();
writeOutput( "License refreshed successfully" );
writeOutput( "Updated license info: " & serializeJSON( refreshResult ) );
```

This function will attempt to refresh your existing license token using the stored refresh token. It's useful for:

* Extending license validity before expiration
* Updating license information after subscription changes
* Ensuring continued access to enterprise features

### Checking License Status

You can programmatically check your license status and available features:

```javascript
// Get current license information
licenseInfo = boxlangLicenseInfo();
writeOutput( "License Status: " & licenseInfo.status );
writeOutput( "Trial Mode: " & licenseInfo.isTrialMode );
```

## CLI Methods

In addition to the built-in functions (BIFs), the bx-plus module provides command-line interface methods for license management.

### Available CLI Commands

#### `activate`

Activates your BoxLang+ or BoxLang++ license from the command line.

<pre class="language-bash"><code class="lang-bash"><strong>boxlang module:plus activate --email your-email@company.com --licenseKey your-license-key --serverType server
</strong></code></pre>

**Required Options:**

* `--email` - The email address associated with your license
* `--licenseKey` - Your BoxLang+ or BoxLang++ license key

**Optional Options:**

* `--serverType` - The type of server deployment (default: "Production")

#### `refresh`

Refreshes the current license token to ensure continued access to enterprise features.

```bash
boxlang module:plus refresh
```

This command will attempt to refresh your existing license token and display the updated license information.

#### `info`

Displays detailed information about your current license status and subscription.

```bash
boxlang module:plus info
```

Returns information including:

* License status (active, expired, trial, etc.)
* Subscription type (BoxLang+, BoxLang++, trial)
* License expiration date
* Available features and modules

#### `help`

Shows usage information and available commands.

```bash
boxlang module:plus help
```

### CommandBox CLI Usage

If you are using CommandBox, and wish to activate a server, without installing the core BoxLang binary, you can also use the CLI activation commands.   This is especially useful in activating licenses when building Docker images for deployment.

```shellscript
box boxlang cli module:bx-plus activate --email=$BX_LICENSE_EMAIL --licenseKey=$BX_LICENSE_KEY --serverType=Development|Staging|Production
```

All of the commands listed above in the CLI section are available by simply using `boxlang cli`  in place of just `boxlang` . &#x20;



For example, to build and register a licensed Docker image

```docker
FROM ortussolutions/commandbox

ARG BX_LICENSE_EMAIL
ARG BX_LICENSE_KEY
ARG BX_SERVER_TYPE=Production

ENV BOX_SERVER_APP_CFENGINE=boxlang

RUN ${BUILD_DIR}/util/warmup-server.sh

RUN box boxlang cli module:bx-plus activate --email=$BX_LICENSE_EMAIL --licenseKey=$BX_LICENSE_KEY --serverType=$BX_SERVER_TYPE

```

### Enterprise Support

This module is part of the BoxLang+ and BoxLang++ enterprise subscription offerings. For enterprise support, license questions, or to purchase a subscription:

* **Visit**: [BoxLang Plans](https://boxlang.io/plans)
* **Email**: [boxlang@ortussolutions.com](mailto:boxlang@ortussolutions.com)
* **Phone**: 1-888-557-8057

***

Next: Explore data caching with the [`bx-redis` module](broken-reference/).
