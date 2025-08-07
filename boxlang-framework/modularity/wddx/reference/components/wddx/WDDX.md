
# Component: `WDDX`

Serializes and de-serializes CFML data structures to the XML-based WDDX format.

## Component Signature

```
<bx:WDDX action=[string]
input=[any]
output=[string]
toplevelvariable=[string]
usetimezoneinfo=[boolean]
validate=[boolean]
xmlconform=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | The action to be performed on the input data. One of: bx2wddx, wddx2bx, bx2js, wddx2js | `bx2wddx` |
| `input` | `any` | `true` | The input data to be converted |  |
| `output` | `string` | `true` | The variable to which the converted data will be assigned |  |
| `toplevelvariable` | `string` | `false` | The name of the top-level variable to be used in the generated JavaScript code |  |
| `usetimezoneinfo` | `boolean` | `false` | Whether to use timezone information in the generated JavaScript code | `true` |
| `validate` | `boolean` | `false` | Whether to validate the input XML | `false` |
| `xmlconform` | `boolean` | `false` | Whether the WDDX input shoud conform to the WDDX DTD | `true` |

## Examples


