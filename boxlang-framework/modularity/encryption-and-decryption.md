---
description: >-
  The password encryption module provides password encryption and hashing
  functionality to Boxlang.
icon: binary-lock
---

# Password Encryption

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-password-encrypt

# Using CommandBox to install for web servers.
box install bx-password-encrypt
```

The password encryption module ( `bx-password-encrypt` ) provides password encryption and hashing functionality to Boxlang.

It contributes the following Built-in-Functions to the language:

* `ArgonHash`: Returns a secure input hash of the given string using the Argon2 hashing algorithm. ( Alias: `GenerateArgon2Hash` )
* `ArgonVerify`: Performs a Argon2 verification on the given string against the hashed value. ( Alias: `Argon2CheckHash` )
* `BCryptHash`: Returns a secure input hash of the given string using the BCrypt hashing algorithm.( Alias: `GenerateBCryptHash` )
* `BCryptVerify`: Performs a BCrypt verification on the given string against the hashed value. ( Alias: `BCryptCheckHash` )
* `SCryptHash`: Returns a secure input hash of the given string using the SCrypt hashing algorithm.( Alias: `GenerateSCryptHash` )
* `SCryptVerify`: Performs a SCrypt verification on the given string against the hashed value. ( Alias: `SCryptCheckHash` )
* `GeneratePBKDFKey`: Generates a PDFK key from the given password and salt.

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-password-encrypt) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27019\&issuetype=1).
