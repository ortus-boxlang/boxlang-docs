# GetLocaleInfo

Retrieves a struct containin info on a locale, with an optional display locale

## Method Signature

```
GetLocaleInfo(locale=[string], dspLocale=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                                                           | Default |
| ----------- | -------- | -------- | ----------------------------------------------------------------------------------------------------- | ------- |
| `locale`    | `string` | `false`  | Optional locale to retrieve information on - either a common format ( "German" ), or an ISO Directive |         |
| `dspLocale` | `string` | `false`  | Optional display language locale                                                                      |         |

## Examples

## Related

* [ClearLocale](clearlocale.md)
* [CurrencyFormat](currencyformat.md)
* [GetLocale](getlocale.md)
* [GetLocaleDisplayName](getlocaledisplayname.md)
* [IsCurrency](iscurrency.md)
* [LSCurrencyFormat](lscurrencyformat.md)
* [LSIsCurrency](lsiscurrency.md)
* [LSParseCurrency](lsparsecurrency.md)
* [ParseCurrency](parsecurrency.md)
* [SetLocale](setlocale.md)
