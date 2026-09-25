
# Component: `collection`

Manages full-text search collections (indices).

## Component Signature

```
<bx:collection action=[string]
collection=[string]
name=[string]
path=[string]
language=[string]
charset=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | Required action: create | delete | list | repair | map |  |
| `collection` | `string` | `false` | Bare collection name (required for create, delete, repair) |  |
| `name` | `string` | `false` | Variable name to assign the result of action="list" |  |
| `path` | `string` | `false` | Optional filesystem path stored as collection metadata (create only) |  |
| `language` | `string` | `false` | Analyzer language (create only, defaults to module setting) |  |
| `charset` | `string` | `false` | Ignored \u2014 accepted for CFML compatibility |  |

## Examples

### Create a collection

```boxlang
<bx:collection action="create" collection="products" language="english" />
```

### Delete a collection

```boxlang
<bx:collection action="delete" collection="products" />
```

### List collections

```boxlang
<bx:collection action="list" name="myCollections" />
```

### Repair a collection

```boxlang
<bx:collection action="repair" collection="products" />
```
