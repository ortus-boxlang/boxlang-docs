---
description: The Officially supported BoxLang modules
---

# Modules

## Core Modules

Here is the collection of modules built and supported by the BoxLang team.

### bx-compat

`Category: cfml`

This module allows your BoxLang engine to run as an Adobe CFML engine or a Lucee CFML engine. Please note that we will not offer every single feature of the Adobe engines in this single module. It can be spread out through a collection of modules.

```
install bx-compat
```

* Download: [https://forgebox.io/view/bx-compat](https://forgebox.io/view/bx-compat)
* Instructions: [https://github.com/ortus-boxlang/bx-compat](https://github.com/ortus-boxlang/bx-compat)

### bx-password-encrypt

`Category: security`

This module provides password encryption and hashing functionality to Boxlang.&#x20;

* `ArgonHash`: Returns a secure input hash of the given string using the Argon2 hashing algorithm. ( Alias: `GenerateArgon2Hash` )
* `ArgonVerify`: Performs a Argon2 verification on the given string against the hashed value. ( Alias: `Argon2CheckHash` )
* `BCryptHash`: Returns a secure input hash of the given string using the BCrypt hashing algorithm.( Alias: `GenerateBCryptHash` )
* `BCryptVerify`: Performs a BCrypt verification on the given string against the hashed value. ( Alias: `BCryptCheckHash` )
* `SCryptHash`: Returns a secure input hash of the given string using the SCrypt hashing algorithm.( Alias: `GenerateSCryptHash` )
* `SCryptVerify`: Performs a SCrypt verification on the given string against the hashed value. ( Alias: `SCryptCheckHash` )
* `GeneratePBKDFKey`: Generates a PDFK key from the given password and salt.

```
install bx-password-encrypt
```

* Download: [https://forgebox.io/view/bx-password-encrypt](https://forgebox.io/view/bx-password-encrypt)
* Instructions: [https://github.com/ortus-boxlang/bx-password-encrypt](https://github.com/ortus-boxlang/bx-password-encrypt)

### bx-esapi

`Category: Security`

Leverages ESAPI and AntiSamy to provide your BoxLang applications with security and cleaning concerns.

```
install bx-esapi
```

* Download: [https://forgebox.io/view/bx-esapi](https://forgebox.io/view/bx-esapi)
* Instructions: [https://github.com/ortus-boxlang/bx-esapi](https://github.com/ortus-boxlang/bx-esapi)

### bx-image

`Category: Image Processing`

The image module gives you tons of components and bifs that will give you a robust and extensive image manipulation library.

```
install bx-image
```

* Download: [https://forgebox.io/view/bx-image](https://forgebox.io/view/bx-image)
* Instructions: [https://github.com/ortus-boxlang/bx-image](https://github.com/ortus-boxlang/bx-image)

### bx-jython

`Category: Scripting`

This module allows you to script in Python within BoxLang.  It can also execute python scripts and modules.

```
install bx-jython
```

* Download: [https://forgebox.io/view/bx-jython](https://forgebox.io/view/bx-jython)
* Instructions: [https://github.com/ortus-boxlang/bx-jython](https://github.com/ortus-boxlang/bx-jython)

### bx-mail

`Category: Communication`

The mail module for BoxLang gives you a robust component and a collection of bifs that you can use to send mail and interact with mail services.

```
install bx-mail
```

* Download: [https://forgebox.io/view/bx-mail](https://forgebox.io/view/bx-mail)
* Instructions: [https://github.com/ortus-boxlang/bx-mail](https://github.com/ortus-boxlang/bx-mail)

### bx-pdf (Coming Soon)

`Category: Document Services`

The pdf module will give you the capabilities to create and stream PDF documents from your BoxLang server code. We also offer the enhanced version in our BoxLang +,++ subscriptions.

```
coming soon
```

* Download: [https://forgebox.io/view/bx-pdf](https://forgebox.io/view/bx-pdf)
* Instructions: [https://github.com/ortus-boxlang/bx-pdf](https://github.com/ortus-boxlang/bx-pdf)

### bx-unsafe-evaluate

`Security: Compiler`

This module will allow you to install an `evaluate()` function that can execute BoxLang and CFML expressions. Please note that this approach to coding is discouraged and unsafe.

```
install bx-unsafe-evaluate
```

* Download: [https://forgebox.io/view/bx-unsafe-evaluate](https://forgebox.io/view/bx-unsafe-evaluate)
* Instructions: [https://github.com/ortus-boxlang/bx-unsafe-evaluate](https://github.com/ortus-boxlang/bx-unsafe-evaluate)

### bx-wddx

`Security: Conversion`

The WDDX module provides the bridge between the WDDX exchange format and BoxLang. It involves reading and parsing XML, converting data types, handling errors, and ensuring performance and compatibility. The module enables the integration of legacy systems with new applications.

```
install bx-wddx
```

* Download: [https://forgebox.io/view/bx-wddx](https://forgebox.io/view/bx-wddx)
* Instructions: [https://github.com/ortus-boxlang/bx-wddx](https://github.com/ortus-boxlang/bx-wddx)

## JDBC Modules

In addition, we offer a number of JDBC modules which package the appropriate JDBC driver for your database vendor of choice. You can find all of the modules in [FORGEBOX](https://www.forgebox.io) as well as our GitHub organization: [https://github.com/ortus-boxlang/bx-{modulename}](https://github.com/ortus-boxlang)

### [Apache Derby](https://forgebox.io/view/bx-derby)

```
install bx-derby
```

### [HyperSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-hypersql/bx-hypersql-1.0.0.zip)

```
install bx-hypersql
```

### [MySQL](https://forgebox.io/view/bx-mysql)

```
install bx-mysql
```

### [MariaDB](https://forgebox.io/view/bx-mariadb)

```
install bx-mariadb
```

### [Microsoft SQL Server](https://forgebox.io/view/bx-mssql)

```
install bx-mssql
```

### [Oracle](https://forgebox.io/view/bx-oracle)

```
install bx-oracle
```

### [PostgreSQL](https://forgebox.io/view/bx-postgresql)

```
install bx-postgresql
```

## Module Installation

The fastest way to install modules is with CommandBox and the `install` command. If you used the quick installer, you can use the install-bx-module binary to download the core modules to your OS or MiniServer home.

```bash
# Install the latest version
install-bx-module bx-compat

# Install a specific version
install-bx-module bx-compat 1.0.0
```

If not, you must download the zip package manually and place it into the home folder.

### Operating System Home

Unzip the module `.zip` file into the location `.boxlang/modules/` located inside your user home directory (by default):

```bash
.boxlang/modules/bx-derby/ModuleConfig.bx ...
```

You can customize the boxlang module directory by changing the `runtime.modulesDirectory` setting in your `config/boxlang.json` file:

{% code title="boxlang.json" %}
```json
{
  "runtime" : {


    // A collection of BoxLang module directories, they must be absolute paths
    "modulesDirectory": [
      "${boxlang-home}/modules"
    ],


  }
}
```
{% endcode %}

See [Runtime Configuration](../configuration.md) for more info on using the `boxlang.json` configuration file.
