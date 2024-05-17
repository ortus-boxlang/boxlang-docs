[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSParseCurrency`

Parses a currency value in to a numeric using the specified or context locale

## Method Signature
```
LSParseCurrency(string=[string], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | the value to be parsed | |
| `locale` | `string` | `false` | the optional locale to apply in parsing | |
|----------|------|----------|-------------|---------|



## Examples

```
LSParseCurrency(string=[string], locale=[string])
```

## Related
  * [GetLocale](GetLocale.md)
  * [GetLocaleDisplayName](GetLocaleDisplayName.md)
  * [GetLocaleInfo](GetLocaleInfo.md)
  * [LSCurrencyFormat](LSCurrencyFormat.md)
  * [LSIsCurrency](LSIsCurrency.md)
  * [LSIsNumeric](LSIsNumeric.md)
  * [LSNumberFormat](LSNumberFormat.md)
  * [LSParseNumber](LSParseNumber.md)
  * [SetLocale](SetLocale.md)
