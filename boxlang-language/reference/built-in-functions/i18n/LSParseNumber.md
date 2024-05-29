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

  * [ClearLocale](./ClearLocale.md)
  * [GetLocale](./GetLocale.md)
  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [LSIsCurrency](./LSIsCurrency.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [LSNumberFormat](./LSNumberFormat.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [SetLocale](./SetLocale.md)
