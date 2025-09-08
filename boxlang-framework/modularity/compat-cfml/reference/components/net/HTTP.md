
# Component: `HTTP`

Overload to the core component to supply compatibility

## Component Signature

```
<bx:HTTP URL=[string]
port=[numeric]
method=[string]
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
file=[string]
multipart=[boolean]
multipartType=[string]
clientCertPassword=[string]
path=[string]
clientCert=[string]
compression=[string]
authType=[string]
cachedWithin=[string]
encodeUrl=[boolean]
proxyServer=[string]
proxyPort=[integer]
proxyUser=[string]
proxyPassword=[string]
name=[string]
delimiter=[string]
columns=[string]
firstRowAsHeaders=[boolean]
textQualifier=[string]
domain=[string]
workstation=[string]
httpVersion=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `URL` | `string` | `true` |  |  |
| `port` | `numeric` | `false` |  |  |
| `method` | `string` | `true` |  | `GET` |
| `username` | `string` | `false` |  |  |
| `password` | `string` | `false` |  |  |
| `userAgent` | `string` | `false` |  | `BoxLang` |
| `charset` | `string` | `false` |  | `UTF-8` |
| `resolveUrl` | `boolean` | `false` |  | `false` |
| `throwOnError` | `boolean` | `false` |  | `true` |
| `redirect` | `boolean` | `false` |  | `true` |
| `timeout` | `numeric` | `false` |  |  |
| `getAsBinary` | `string` | `true` |  | `auto` |
| `result` | `string` | `true` |  | `bxhttp` |
| `file` | `string` | `false` |  |  |
| `multipart` | `boolean` | `false` |  | `false` |
| `multipartType` | `string` | `true` |  | `form-data` |
| `clientCertPassword` | `string` | `false` |  |  |
| `path` | `string` | `false` |  |  |
| `clientCert` | `string` | `false` |  |  |
| `compression` | `string` | `false` |  |  |
| `authType` | `string` | `true` |  | `BASIC` |
| `cachedWithin` | `string` | `false` |  |  |
| `encodeUrl` | `boolean` | `false` |  | `true` |
| `proxyServer` | `string` | `false` |  |  |
| `proxyPort` | `integer` | `false` |  |  |
| `proxyUser` | `string` | `false` |  |  |
| `proxyPassword` | `string` | `false` |  |  |
| `name` | `string` | `false` |  |  |
| `delimiter` | `string` | `false` |  |  |
| `columns` | `string` | `false` |  |  |
| `firstRowAsHeaders` | `boolean` | `false` |  |  |
| `textQualifier` | `string` | `false` |  |  |
| `domain` | `string` | `false` |  |  |
| `workstation` | `string` | `false` |  |  |
| `httpVersion` | `string` | `false` |  | `HTTP/2` |

## Examples


