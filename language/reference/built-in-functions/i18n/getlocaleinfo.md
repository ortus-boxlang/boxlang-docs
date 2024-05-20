# GetLocaleInfo

Retrieves a struct containin info on a locale, with an optional display locale

## Method Signature

```
GetLocaleInfo(locale=[string], dspLocale=[string])
```

### Arguments

| Argument    | Type     | Required   | Description                                                                                           | Default   |
| ----------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------- | --------- |
| `locale`    | `string` | `false`    | Optional locale to retrieve information on - either a common format ( "German" ), or an ISO Directive |           |
| `dspLocale` | `string` | `false`    | Optional display language locale                                                                      |           |
| ----------  | ------   | ---------- | -------------                                                                                         | --------- |

## Examples

```
GetLocaleInfo(locale=[string], dspLocale=[string])
```

## Related

* [GetLocale](getlocale.md)
* [GetLocaleDisplayName](getlocaledisplayname.md)
* [LSCurrencyFormat](lscurrencyformat.md)
* [LSIsCurrency](lsiscurrency.md)
* [LSIsNumeric](lsisnumeric.md)
* [LSNumberFormat](lsnumberformat.md)
* [LSParseCurrency](lsparsecurrency.md)
* [LSParseNumber](lsparsenumber.md)
* [SetLocale](setlocale.md)
