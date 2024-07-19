[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Query`

No description available.

## Component Signature

```
<bx:Query name=[string]
datasource=[string]
returnType=[string]
columnKey=[string]
maxRows=[numeric]
blockfactor=[numeric]
fetchsize=[numeric]
timeout=[numeric]
cache=[boolean]
cacheTimeout=[duration]
cacheLastAccessTimeout=[duration]
cacheKey=[string]
cacheProvider=[string]
timezone=[string]
dbtype=[string]
username=[string]
password=[string]
debug=[boolean]
result=[string]
ormoptions=[struct]
clientInfo=[struct]
fetchClientInfo=[boolean]
lazy=[boolean]
psq=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` |  |  |
| `datasource` | `string` | `false` |  |  |
| `returnType` | `string` | `false` |  | `query` |
| `columnKey` | `string` | `false` |  |  |
| `maxRows` | `numeric` | `false` |  | `-1` |
| `blockfactor` | `numeric` | `false` |  | `[ortus.boxlang.runtime.validation.dynamic.Min@674fd531, ortus.boxlang.runtime.validation.dynamic.Max@7f53b345]` |
| `fetchsize` | `numeric` | `false` |  |  |
| `timeout` | `numeric` | `false` |  |  |
| `cache` | `boolean` | `false` |  | `false` |
| `cacheTimeout` | `duration` | `false` |  |  |
| `cacheLastAccessTimeout` | `duration` | `false` |  |  |
| `cacheKey` | `string` | `false` |  |  |
| `cacheProvider` | `string` | `false` |  |  |
| `timezone` | `string` | `false` |  |  |
| `dbtype` | `string` | `false` |  |  |
| `username` | `string` | `false` |  |  |
| `password` | `string` | `false` |  |  |
| `debug` | `boolean` | `false` |  | `false` |
| `result` | `string` | `false` |  |  |
| `ormoptions` | `struct` | `false` |  |  |
| `clientInfo` | `struct` | `false` |  |  |
| `fetchClientInfo` | `boolean` | `false` |  | `false` |
| `lazy` | `boolean` | `false` |  | `false` |
| `psq` | `boolean` | `false` |  | `false` |

## Examples

```
<bx:Query name=[string]
datasource=[string]
returnType=[string]
columnKey=[string]
maxRows=[numeric]
blockfactor=[numeric]
fetchsize=[numeric]
timeout=[numeric]
cache=[boolean]
cacheTimeout=[duration]
cacheLastAccessTimeout=[duration]
cacheKey=[string]
cacheProvider=[string]
timezone=[string]
dbtype=[string]
username=[string]
password=[string]
debug=[boolean]
result=[string]
ormoptions=[struct]
clientInfo=[struct]
fetchClientInfo=[boolean]
lazy=[boolean]
psq=[boolean] />
```
