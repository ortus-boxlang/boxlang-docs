[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Query`

No description available.

## Component Signature

```
<bx:Query name=[string]
datasource=[string]
timezone=[string]
dbtype=[string]
username=[string]
password=[string]
maxRows=[numeric]
blockfactor=[numeric]
fetchsize=[numeric]
timeout=[numeric]
cachedAfter=[date]
cachedWithin=[numeric]
debug=[boolean]
result=[string]
ormoptions=[struct]
cacheID=[string]
cacheRegion=[string]
clientInfo=[struct]
fetchClientInfo=[boolean]
lazy=[boolean]
psq=[boolean]
returnType=[string]
columnKey=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` |  |  |
| `datasource` | `string` | `false` |  |  |
| `timezone` | `string` | `false` |  |  |
| `dbtype` | `string` | `false` |  |  |
| `username` | `string` | `false` |  |  |
| `password` | `string` | `false` |  |  |
| `maxRows` | `numeric` | `false` |  | `-1` |
| `blockfactor` | `numeric` | `false` |  | `[ortus.boxlang.runtime.validation.dynamic.Max@204a02a4, ortus.boxlang.runtime.validation.dynamic.Min@4777f71e]` |
| `fetchsize` | `numeric` | `false` |  |  |
| `timeout` | `numeric` | `false` |  |  |
| `cachedAfter` | `date` | `false` |  |  |
| `cachedWithin` | `numeric` | `false` |  |  |
| `debug` | `boolean` | `false` |  | `false` |
| `result` | `string` | `false` |  |  |
| `ormoptions` | `struct` | `false` |  |  |
| `cacheID` | `string` | `false` |  |  |
| `cacheRegion` | `string` | `false` |  |  |
| `clientInfo` | `struct` | `false` |  |  |
| `fetchClientInfo` | `boolean` | `false` |  | `false` |
| `lazy` | `boolean` | `false` |  | `false` |
| `psq` | `boolean` | `false` |  | `false` |
| `returnType` | `string` | `false` |  | `query` |
| `columnKey` | `string` | `false` |  |  |

## Examples

```
<bx:Query name=[string]
datasource=[string]
timezone=[string]
dbtype=[string]
username=[string]
password=[string]
maxRows=[numeric]
blockfactor=[numeric]
fetchsize=[numeric]
timeout=[numeric]
cachedAfter=[date]
cachedWithin=[numeric]
debug=[boolean]
result=[string]
ormoptions=[struct]
cacheID=[string]
cacheRegion=[string]
clientInfo=[struct]
fetchClientInfo=[boolean]
lazy=[boolean]
psq=[boolean]
returnType=[string]
columnKey=[string] />
```
