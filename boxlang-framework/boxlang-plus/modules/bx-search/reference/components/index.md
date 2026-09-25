
# Component: `index`

Indexes documents into a search collection.

## Component Signature

```
<bx:index action=[string]
collection=[string]
key=[string]
type=[string]
title=[string]
body=[string]
urlpath=[string]
language=[string]
custom1=[string]
custom2=[string]
custom3=[string]
custom4=[string]
extensions=[string]
recurse=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | Required: update | delete | purge | refresh |  |
| `collection` | `string` | `true` | Required: bare collection name |  |
| `key` | `string` | `false` | Document identifier (required for update/delete; for type="file|url", this is the path/URL) |  |
| `type` | `string` | `false` | Document type: custom (default) | file | url | `custom` |
| `title` | `string` | `false` | Document title stored and returned in search results |  |
| `body` | `string` | `false` | Full-text body (used for type="custom") |  |
| `urlpath` | `string` | `false` | URL stored as the document's URL field (optional for type="url" \u2014 defaults to key) |  |
| `language` | `string` | `false` | Language/analyzer override (optional) |  |
| `custom1` | `string` | `false` | Custom metadata field 1 |  |
| `custom2` | `string` | `false` | Custom metadata field 2 |  |
| `custom3` | `string` | `false` | Custom metadata field 3 |  |
| `custom4` | `string` | `false` | Custom metadata field 4 |  |
| `extensions` | `string` | `false` | Accepted for CFML compatibility; ignored by this implementation. |  |
| `recurse` | `boolean` | `false` | Accepted for CFML compatibility; ignored by this implementation. | `false` |

## Examples

### Index a plain document

```boxlang
<bx:index action="update"
          collection="products"
          type="custom"
          key="prod-123"
          title="BoxLang"
          body="Full-text body here"
          custom1="categoryA" />
```

### Index a file attachment

```boxlang
<bx:index action="update"
          collection="docs"
          type="file"
          key="/var/docs/manual.pdf"
          title="Manual" />
```

### Index a URL

```boxlang
<bx:index action="update"
          collection="docs"
          type="url"
          key="https://example.com/page"
          urlpath="https://example.com/page" />
```

### Delete a document

```boxlang
<bx:index action="delete" collection="products" key="prod-123" />
```

### Purge all documents

```boxlang
<bx:index action="purge" collection="products" />
```
