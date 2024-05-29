[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `HTTP`

I make an HTTP call

## Component Signature

```
<bx:HTTP URL=[string]
port=[numeric]
method=[string]
proxyServer=[string]
proxyPort=[string]
proxyUser=[string]
proxyPassword=[string]
username=[string]
password=[string]
userAgent=[string]
charset=[string]
resolveUrl=[boolean]
throwOnError=[boolean]
redirect=[boolean]
timeout=[numeric]
getAsBinary=[string]
result=[string]
delimiter=[string]
name=[string]
columns=[string]
firstRowAsHeaders=[boolean]
textQualifier=[string]
file=[string]
multipart=[boolean]
multipartType=[string]
clientCertPassword=[string]
path=[string]
clientCert=[string]
compression=[string]
authType=[string]
domain=[string]
workstation=[string]
cachedWithin=[string]
encodeUrl=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` |  |  |
| `port` | `numeric` | `false` |  |  |
| `method` | `string` | `true` |  | `GET` |
| `proxyServer` | `string` | `false` |  |  |
| `proxyPort` | `string` | `false` |  |  |
| `proxyUser` | `string` | `false` |  |  |
| `proxyPassword` | `string` | `false` |  |  |
| `username` | `string` | `false` |  |  |
| `password` | `string` | `false` |  |  |
| `userAgent` | `string` | `false` |  | `BoxLang` |
| `charset` | `string` | `false` |  | `UTF-8` |
| `resolveUrl` | `boolean` | `false` |  | `false` |
| `throwOnError` | `boolean` | `false` |  | `true` |
| `redirect` | `boolean` | `false` |  | `true` |
| `timeout` | `numeric` | `false` |  |  |
| `getAsBinary` | `string` | `true` |  | `auto` |
| `result` | `string` | `true` |  | `cfhttp` |
| `delimiter` | `string` | `false` |  |  |
| `name` | `string` | `false` |  |  |
| `columns` | `string` | `false` |  |  |
| `firstRowAsHeaders` | `boolean` | `false` |  |  |
| `textQualifier` | `string` | `false` |  |  |
| `file` | `string` | `false` |  |  |
| `multipart` | `boolean` | `false` |  | `false` |
| `multipartType` | `string` | `true` |  | `form-data` |
| `clientCertPassword` | `string` | `false` |  |  |
| `path` | `string` | `false` |  |  |
| `clientCert` | `string` | `false` |  |  |
| `compression` | `string` | `false` |  |  |
| `authType` | `string` | `true` |  | `BASIC` |
| `domain` | `string` | `false` |  |  |
| `workstation` | `string` | `false` |  |  |
| `cachedWithin` | `string` | `false` |  |  |
| `encodeUrl` | `boolean` | `false` |  | `true` |

## Examples

```
<bx:HTTP URL=[string]
port=[numeric]
method=[string]
proxyServer=[string]
proxyPort=[string]
proxyUser=[string]
proxyPassword=[string]
username=[string]
password=[string]
userAgent=[string]
charset=[string]
resolveUrl=[boolean]
throwOnError=[boolean]
redirect=[boolean]
timeout=[numeric]
getAsBinary=[string]
result=[string]
delimiter=[string]
name=[string]
columns=[string]
firstRowAsHeaders=[boolean]
textQualifier=[string]
file=[string]
multipart=[boolean]
multipartType=[string]
clientCertPassword=[string]
path=[string]
clientCert=[string]
compression=[string]
authType=[string]
domain=[string]
workstation=[string]
cachedWithin=[string]
encodeUrl=[boolean] />
```
