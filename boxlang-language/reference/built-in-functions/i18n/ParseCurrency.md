[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ParseCurrency`

Parses a currency value in to a numeric using the specified or context locale

## Method Signature

```
ParseCurrency(string=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | the value to be parsed |  |
| `locale` | `string` | `false` | the optional locale to apply in parsing |  |

## Examples

```
ParseCurrency(string=[string], locale=[string])
```

## Related

  * [ClearLocale](./ClearLocale.md)
  * [CurrencyFormat](./CurrencyFormat.md)
  * [GetLocale](./GetLocale.md)
  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [IsCurrency](./IsCurrency.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [LSIsCurrency](./LSIsCurrency.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [SetLocale](./SetLocale.md)
