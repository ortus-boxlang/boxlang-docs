---
description: This module provides mail sending functionality to BoxLang.
icon: envelope-open
---

# Mail

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-mail

# Using CommandBox to install for web servers.
box install bx-mail
```

### Components

This module contributes the following Components to the language:

* `mail` - the wrapping component for a mail operation
  * The following attributes are available to the `mail` component
    * `from` - Sender email address
    * `to` - Comma-delimited list of recipient email addresses
    * `charset` - The character encoding of the email
    * `subject` - The email subject
    * `server` - Optional SMTP server address
    * `port` - Optional SMTP server port
    * `username` - Optional SMTP username
    * `password` - Optional SMTP password
    * `useSSL` - Optional true|false for SMTP Connection
    * `useTLS` - true|false for SMTP TLS Connection
    * `mailerid` - The header ID of the mailer
    * `mimeAttach` - path of file to attach
    * `type` - MIME type of the email
    * `wrapText` - Wrap text after a certain number of characters has been reached
    * `sign` - true|false Whether to sign the mail message - requires keystore, keystorePassword, keyAlias, keyPassword
    * `keystore` - The location of the keystore (Used when signing)
    * `keystorePassword` - The password of the keystore (Used when signing)
    * `keyAlias` - The alias of the private key to use for signing (Used when signing)
    * `keyPassword` The password for the private key within the keystore (Used when signing)
    * `encrypt` - true|false Whether to encrypt the mail message - requires recipientCert, encryptionAlgorithm
    * `recipientCert` - The path to the public key certificate of the recipient (Used when encrypting)
    * `encryptionAlgorithm` - The encryption algorithm to use (Used when encrypting). One of DES\_EDE3\_CBC, RC2\_CBC, AES128\_CBC, AES192\_CBC, AES256\_CBC
    * `debug` - true|false Whether to enable debug logging output
* `mailparam` - the component which supplies a mail parameter to the operation, such as headers or files
  * The following attributes are available to the `mailparam` component
    * `name` - The header name ( if applicable )
    * `value` - The header value ( if applicable )
    * `contentID` - The content ID ( optional content id)
    * `disposition` - The disposition type ( `inline` or `attachment` - if applicable )
    * `file` - The file path of an attachment ( if applicable )
    * `fileName` - An optional name of the file to be sent as an attachment ( if applicable )
    * `type` - The media type ( if applicable )
* `mailpart` - the component which supplies a message part ( e.g. "text", "html", etc ) to the mail operation
  * The following attributes are available to the `mailpart` component
    * `type` - The mime type of the mail part
    * `charset` - The character encoding of the mail part
    * `wrapText` - The number of characters to wrap the mail part at

### Examples

#### Simple Email Example ( Script syntax )

```javascript
bx:mail
    from="jclausen@ortussolutions.com"
    to="jclausen@ortussolutions.com"
    subject="Hello from BoxLang Mail!"
{
    writeOutput( "Hello world!" );
}
```

#### Email with a single file attachment ( Templating syntax )

```javascript
<bx:mail
    from="jclausen@ortussolutions.com"
    to="jclausen@ortussolutions.com"
    subject="File For You"
    mimeAttach="/path/to/my/file.pdf"
>
Here's a PDF for you!
</bx:mail>
```

#### MultiPart with text and html parts, with an attachment ( Templating syntax )

```javascript
<bx:mail
	from="jclausen@ortussolutions.com"
	to="jclausen@ortussolutions.com"
	subject="Mail In Parts"
>

<bx:mailpart type="text">
Hello mail!
</bx:mailpart>

<bx:mailpart type="html">
<h1>Hello mail!</h1>
</bx:mailpart>

<bx:mailparam file="/path/to/my/file.pdf" fileName="PDFForYou.pdf" type="application/x-pdf" />

</bx:mail>
```

### Configuration

Mail server connectivity may be provided either via runtime configuration ( e.g. `.boxlang.json` ) or via the attributes allowed by the mail component ( see above ). An example configuration is provided below:

```json
{
	"modules": {

		"mail": {
			// An array of mail servers
			"mailServers" : [
				{
					// The SMTP Server
					"smtp": "127.0.0.1",
					// The SMTP Port
					"port": "25",
					// The SMTP Username
					"username": "",
					// The SMTP Password
					"password": "",
					// Whether to use SSL in connection to the SMTP server
					"ssl": false,
					// Whether to use TLS in connection to the SMTP server
					"tls": false,
					// The idle timeout, in milliseconds, for connection to the mail server
					"idleTimeout": "10000",
					// The timeout, in milliseconds before giving up on attempts to connect
					"lifeTimeout": "60000"
				}
			],
			// The default encoding to use for outbound email
			"defaultEncoding" : "utf-8",
			// Whether to enable spooling of mail - when false, mail will be sent immediately
			"spoolEnable" : true,
			// The interval in fractions of seconds to process the spool
			"spoolInterval" : .50,
			// The connection timeout - defaults to null, meaning no connection timeout attempting to connect to the mail server
			"connectionTimeout" : null,
			// The following attributes are used for signing of all outbound emails
			"signMesssage" : false,
			// The signature keystore
			"signKeystore" : null,
			// The signature keystore password
			"signKeystorePassword" : null,
			// The private key alias within the keystore
			"signKeyAlias" : null,
			// The Key password within the keystore
			"signKeyPassword" : null,
			// Whether to enable mail logging
			"logEnabled" : true,
			// The severity level for logging
			"logSeverity" : "ERROR",
			// The time in minutes retain a message in the spool before the message is discarded - defaults to infinite
			"spoolTimeout" : 0,
			//  The time in minutes to try resending email before it is considered bounced - defaults to infinite
			"bounceTimeout" : 0,
			// Optional directory settings for the spool ( Defaults to BoxLang runtime home )
			"spoolDirectory" : "/usr/local/boxlang/mail/unsent",
			"bounceDirectory" : "/usr/local/mail/bounced"
		}
	}
}
```
