[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Content`

Does either or both of the following:
 - Sets the MIME content encoding header for the current page
 - Sends the contents of a file from the server as the page output

## Component Signature
```
<bx:Content type=[string]
deleteFile=[boolean]
file=[string]
variable=[any]
reset=[boolean] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` |  | ``|
| `deleteFile` | `boolean` | `false` |  | `false`|
| `file` | `string` | `false` |  | ``|
| `variable` | `any` | `false` |  | ``|
| `reset` | `boolean` | `false` |  | `true`|
|----------|------|----------|-------------|---------|



## Examples

```
<bx:Content type=[string]
deleteFile=[boolean]
file=[string]
variable=[any]
reset=[boolean] />
```
