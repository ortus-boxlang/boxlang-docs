
# Component: `search`

Executes a full-text search against a collection and places the results in a
 CFML-compatible {@link Query} object.

## Component Signature

```
<bx:search collection=[string]
name=[string]
criteria=[string]
type=[string]
maxrows=[integer]
startrow=[integer]
language=[string]
suggestions=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `collection` | `string` | `true` | Required: bare collection name to search. |  |
| `name` | `string` | `true` | Required: variable name that receives the result Query. |  |
| `criteria` | `string` | `false` | Search expression / query string. Defaults to match-all when omitted. |  |
| `type` | `string` | `false` | Search type: {@code simple} (default) | {@code explicit}.<br>                 Currently both map to a multi-match query across all fields. | `simple` |
| `maxrows` | `integer` | `false` | Maximum number of rows to return (default: 50). | `50` |
| `startrow` | `integer` | `false` | 1-based offset for pagination (default: 1). | `1` |
| `language` | `string` | `false` | Language hint (stored in query metadata; reserved for future analyzer use). |  |
| `suggestions` | `string` | `false` | Ignored \u2014 accepted for CFML compatibility. |  |

## Examples

### Script Syntax

Execute a full-text search against a collection and place the results into a named `Query`:

```boxlang
<bx:search collection="products"
           criteria="BoxLang"
           name="searchResults"
           maxrows="20"
           startrow="1" />

<bx:output query="searchResults">
    #searchResults.rank# — #searchResults.title# (#searchResults.score#)
</bx:output>
```
