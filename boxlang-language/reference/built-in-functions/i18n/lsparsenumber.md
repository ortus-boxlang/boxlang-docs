[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSParseNumber`

Converts a string that is a valid numeric representation in the current locale into a formatted number.

## Method Signature
```
LSParseNumber(number=[string], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `string` | `true` | The number to parse. |  |
| `locale` | `string` | `false` | The locale to use when parsing the number. If not provided, the system or application-configured locale is used. |  |

## Examples

```
LSParseNumber(number=[string], locale=[string])
```

## Related
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleDisplayName](boxlang-language/reference/built-in-functions/GetLocaleDisplayName.md)
  * [GetLocaleInfo](boxlang-language/reference/built-in-functions/GetLocaleInfo.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsCurrency](boxlang-language/reference/built-in-functions/LSIsCurrency.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSNumberFormat](boxlang-language/reference/built-in-functions/LSNumberFormat.md)
  * [LSParseCurrency](boxlang-language/reference/built-in-functions/LSParseCurrency.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)
