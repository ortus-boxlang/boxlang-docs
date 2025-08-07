
# Component: `MailPart`

Processes a mail part within the body of a mail component

## Component Signature

```
<bx:MailPart type=[string]
charset=[string]
wrapText=[integer] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The mime type of the mail part |  |
| `charset` | `string` | `false` | The character encoding of the mail part | `utf-8` |
| `wrapText` | `integer` | `false` | The number of characters to wrap the mail part at |  |

## Examples


