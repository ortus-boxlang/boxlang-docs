[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSNumberFormat`

Formats a number with an optional format mask

## Method Signature

```
LSNumberFormat(number=[any], mask=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `any` | `true` | The number to be formatted, or an empty string which will be treated as 0. |  |
| `mask` | `string` | `false` | The formatting mask to apply using the {@link java.text.DecimalFormat} patterns. |  |
| `locale` | `string` | `false` | An optional locale string to apply to the format |  |

## Examples



## Related

  * [BooleanFormat](./BooleanFormat.md)
  * [DecimalFormat](./DecimalFormat.md)
  * [NumberFormat](./NumberFormat.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
