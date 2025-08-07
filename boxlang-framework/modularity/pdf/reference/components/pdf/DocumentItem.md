
# Component: `DocumentItem`

Component which specifies header, footer, and pagebreaks within a document body

## Component Signature

```
<bx:DocumentItem type=[string]
evalAtPrint=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | string pagebreak|header|footer |  |
| `evalAtPrint` | `string` | `false` | A boolean which determines if the contents of the cfdocumentitem tag body has to be evaluated at the time of printing the document.  This attribute is deprecated as all content is evaluated at print time. | `true` |

## Examples


