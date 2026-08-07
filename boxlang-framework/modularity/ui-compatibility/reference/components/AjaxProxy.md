# Component: `AjaxProxy`

Creates an AJAX proxy for client-server communication, allowing JavaScript to call server-side functions asynchronously.

## Syntax

```boxlang
<bx:ajaxproxy 
    cfc="string"
    jsclassname="string"
    bind="string"
    onError="string"
    onSuccess="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `cfc` | `string` | No* | The CFC for which to create a proxy (dot-delimited path) | `""` |
| `jsclassname` | `string` | No | Name for the JavaScript proxy class (defaults to CFC name) | `""` |
| `bind` | `string` | No* | Bind expression for CFC method, JavaScript function, or URL | `""` |
| `onError` | `string` | No | JavaScript function to execute if bind fails | `""` |
| `onSuccess` | `string` | No | JavaScript function to execute if bind succeeds | `""` |

**Note:** Either `cfc` or `bind` is required.

## Examples

### CFC-based proxy

```boxlang
<bx:ajaxproxy cfc="UserService" jsclassname="UserProxy" />
```

### Bind-based proxy

```boxlang
<bx:ajaxproxy bind="cfc:UserService.getUser" jsclassname="UserProxy" />
```

### With callbacks

```boxlang
<bx:ajaxproxy bind="cfc:myComponent.getData()" onSuccess="handleSuccess" onError="handleError" />
```

## Related Components

- [AjaxImport](AjaxImport.md) - Import required AJAX files
