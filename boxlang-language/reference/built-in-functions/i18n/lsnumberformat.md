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
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleDisplayName](boxlang-language/reference/built-in-functions/GetLocaleDisplayName.md)
  * [GetLocaleInfo](boxlang-language/reference/built-in-functions/GetLocaleInfo.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsCurrency](boxlang-language/reference/built-in-functions/LSIsCurrency.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSParseCurrency](boxlang-language/reference/built-in-functions/LSParseCurrency.md)
  * [LSParseNumber](boxlang-language/reference/built-in-functions/LSParseNumber.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)
