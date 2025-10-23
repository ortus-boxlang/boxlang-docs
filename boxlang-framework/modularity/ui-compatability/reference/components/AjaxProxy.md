# Component: `AjaxProxy`

Creates an AJAX proxy for client-server communication, allowing JavaScript to call server-side functions asynchronously.

## Syntax

```boxlang
<bx:ajaxproxy 
    bind="string"
    jsclassname="string"
    onError="string"
    onSuccess="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `bind` | `string` | Yes | Server-side method to bind to | |
| `jsclassname` | `string` | No | JavaScript class name | Auto-generated |
| `onError` | `string` | No | Error callback function | |
| `onSuccess` | `string` | No | Success callback function | |

## Examples

```boxlang
<bx:ajaxproxy bind="cfc:UserService.getUser" jsclassname="UserProxy" />
```

## Related Components

- [AjaxImport](AjaxImport.md) - Import required AJAX files
