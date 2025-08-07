
# Component: `Mail`

This component wraps an encompassing mail message and sends it to the specified recipients

## Component Signature

```
<bx:Mail from=[string]
to=[string]
subject=[string]
bcc=[string]
cc=[string]
charset=[string]
debug=[boolean]
failTo=[string]
mailerid=[string]
mimeAttach=[string]
password=[string]
port=[integer]
priority=[string]
remove=[boolean]
replyTo=[string]
server=[string]
spoolEnable=[boolean]
timeout=[string]
type=[string]
username=[string]
useSSL=[string]
useTLS=[string]
wrapText=[string]
sign=[boolean]
keystore=[string]
keystorePassword=[string]
keyAlias=[string]
keyPassword=[string]
encrypt=[boolean]
recipientCert=[string]
encryptionAlgorithm=[string]
iDNAVersion=[integer]
query=[any]
group=[string]
groupCaseSensitive=[boolean]
startRow=[integer]
maxRows=[integer]
messageVariable=[any]
messageIdentifier=[any] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `from` | `string` | `true` | Sender email address |  |
| `to` | `string` | `true` | Comma-delimited list of recipient email addresses |  |
| `subject` | `string` | `true` | The email subject |  |
| `bcc` | `string` | `false` |  |  |
| `cc` | `string` | `false` |  |  |
| `charset` | `string` | `false` | The character encoding of the email | `utf-8` |
| `debug` | `boolean` | `false` | true|false Whether to enable debug logging output | `false` |
| `failTo` | `string` | `false` |  |  |
| `mailerid` | `string` | `false` | The header ID of the mailer |  |
| `mimeAttach` | `string` | `false` | path of file to attach |  |
| `password` | `string` | `false` | Optional SMTP password |  |
| `port` | `integer` | `false` | Optional SMTP server port |  |
| `priority` | `string` | `false` |  |  |
| `remove` | `boolean` | `false` |  | `false` |
| `replyTo` | `string` | `false` |  |  |
| `server` | `string` | `false` | Optional SMTP server address |  |
| `spoolEnable` | `boolean` | `false` |  | `false` |
| `timeout` | `string` | `false` |  |  |
| `type` | `string` | `false` | MIME type of the email |  |
| `username` | `string` | `false` | Optional SMTP username |  |
| `useSSL` | `string` | `false` | Optional true|false for SMTP Connection |  |
| `useTLS` | `string` | `false` | true|false for SMTP TLS Connection |  |
| `wrapText` | `string` | `false` | Wrap text after a certain number of characters has been reached |  |
| `sign` | `boolean` | `false` | true|false Whether to sign the mail message - requires keystore, keystorePassword, keyAlias, keyPassword |  |
| `keystore` | `string` | `false` | The location of the keystore (Used when signing) |  |
| `keystorePassword` | `string` | `false` | The password of the keystore (Used when signing) |  |
| `keyAlias` | `string` | `false` | The alias of the private key to use for signing (Used when signing) |  |
| `keyPassword` | `string` | `false` | The password for the private key within the keystore (Used when signing) |  |
| `encrypt` | `boolean` | `false` | true|false Whether to encrypt the mail message - requires recipientCert, encryptionAlgorithm | `false` |
| `recipientCert` | `string` | `false` | The path to the public key certificate of the recipient (Used when encrypting) |  |
| `encryptionAlgorithm` | `string` | `false` | The encryption algorithm to use (Used when encrypting). One of DES_EDE3_CBC, RC2_CBC, AES128_CBC, AES192_CBC,<br>                                AES256_CBC | `AES256_CBC` |
| `iDNAVersion` | `integer` | `false` |  |  |
| `query` | `any` | `false` |  |  |
| `group` | `string` | `false` |  |  |
| `groupCaseSensitive` | `boolean` | `false` |  |  |
| `startRow` | `integer` | `false` |  | `1` |
| `maxRows` | `integer` | `false` |  |  |
| `messageVariable` | `any` | `false` |  |  |
| `messageIdentifier` | `any` | `false` |  |  |

## Examples

### Simple Email Example ( Script syntax )

```javascript
bx:mail
    from="jclausen@ortussolutions.com"
    to="jclausen@ortussolutions.com"
    subject="Hello from BoxLang Mail!"
{
    writeOutput( "Hello world!" );
}
```

### Email with a single file attachment ( Templating syntax )

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

### MultiPart with text and html parts, with an attachment ( Templating syntax )

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
