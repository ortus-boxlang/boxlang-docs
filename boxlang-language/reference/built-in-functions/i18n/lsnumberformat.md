[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSNumberFormat`

Localized Number formatting

## Method Signature
```
LSNumberFormat(number=[any], mask=[string], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `any` | `true` | The number to be formatted |  |
| `mask` | `string` | `false` | The formatting mask to apply |  |
| `locale` | `string` | `false` | The locale string to apply to the format |  |

## Examples

```
LSNumberFormat(number=[any], mask=[string], locale=[string])
```

## Related
  * [GetLocale](GetLocale.md)
  * [GetLocaleDisplayName](GetLocaleDisplayName.md)
  * [GetLocaleInfo](GetLocaleInfo.md)
  * [LSCurrencyFormat](LSCurrencyFormat.md)
  * [LSIsCurrency](LSIsCurrency.md)
  * [LSIsNumeric](LSIsNumeric.md)
  * [LSParseCurrency](LSParseCurrency.md)
  * [LSParseNumber](LSParseNumber.md)
  * [SetLocale](SetLocale.md)
