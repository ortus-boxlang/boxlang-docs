[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSIsCurrency`

Determines whether a value can be parsed to numeric in the given or default locale

## Method Signature
```
LSIsCurrency(number=[any], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `any` | `true` | The value to be parsed |  |
| `locale` | `string` | `false` | The locale to apply to parsing - uses the context config value if not specified |  |

## Examples

```
LSIsCurrency(number=[any], locale=[string])
```

## Related
  * [GetLocale](./GetLocale.md)
  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [LSNumberFormat](./LSNumberFormat.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [SetLocale](./SetLocale.md)
