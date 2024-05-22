[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSIsNumeric`

Tests whether a value is numeric, according to a given or the default

## Method Signature
```
LSIsNumeric(number=[string], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `string` | `true` | The number to test |  |
| `locale` | `string` | `false` | Optional locale string, otherwise the context default is used |  |

## Examples

```
LSIsNumeric(number=[string], locale=[string])
```

## Related
  * [GetLocale](./GetLocale.md)
  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [LSIsCurrency](./LSIsCurrency.md)
  * [LSNumberFormat](./LSNumberFormat.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [SetLocale](./SetLocale.md)
