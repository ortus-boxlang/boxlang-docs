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
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleDisplayName](boxlang-language/reference/built-in-functions/GetLocaleDisplayName.md)
  * [GetLocaleInfo](boxlang-language/reference/built-in-functions/GetLocaleInfo.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSNumberFormat](boxlang-language/reference/built-in-functions/LSNumberFormat.md)
  * [LSParseCurrency](boxlang-language/reference/built-in-functions/LSParseCurrency.md)
  * [LSParseNumber](boxlang-language/reference/built-in-functions/LSParseNumber.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)
