[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DollarFormat`

Formats a number as a U.S.

Dollar string with two decimal places, thousands separator, and a dollar sign.
 If the number is negative, the return value is enclosed in parentheses.
 If the number is an empty string, the function returns "0.00".

## Method Signature

```
DollarFormat(number=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `any` | `true` | The number to format as a U.S. Dollar string. |  |

## Examples

```
DollarFormat(number=[any])
```

## Related

  * [BooleanFormat](./BooleanFormat.md)
  * [DecimalFormat](./DecimalFormat.md)
  * [NumberFormat](./NumberFormat.md)
