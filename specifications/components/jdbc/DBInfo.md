[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `DBInfo`

Retrieve database metadata for a given datasource.

## Component Signature
```
<bx:DBInfo type=[string]
name=[string]
datasource=[string]
table=[string]
pattern=[string]
dbname=[string]
username=[string]
password=[string]
filter=[filter] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | Type of metadata to retrieve. One of: `columns`, `dbnames`, `tables`, `foreignkeys`, `index`, `procedures`, or `version`. | ``|
| `name` | `string` | `true` | Name of the variable to which the result will be assigned. Required. | ``|
| `datasource` | `string` | `false` | Name of the datasource to check metadata on. If not provided, the default datasource will be used. | ``|
| `table` | `string` | `false` | Table name for which to retrieve metadata. Required for `columns`, `foreignkeys`, and `index` types. | ``|
| `pattern` | `string` | `false` |  | ``|
| `dbname` | `string` | `false` |  | ``|
| `username` | `string` | `false` | Not currently implemented. | ``|
| `password` | `string` | `false` | Not currently implemented. | ``|
| `filter` | `filter` | `false` | A lucee-only attribute to perform additional filtering on <code>type="tables"</code> results. Not currently implemented, as this
                   should be performed by a queryFilter() call. | ``|
|----------|------|----------|-------------|---------|



## Examples

```
<bx:DBInfo type=[string]
name=[string]
datasource=[string]
table=[string]
pattern=[string]
dbname=[string]
username=[string]
password=[string]
filter=[filter] />
```
