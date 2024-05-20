# GetLocaleDisplayName

Returns the ,{@link java.util.Locale}, display name with an optional display language/locale

## Method Signature

```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```

### Arguments

| Argument    | Type     | Required   | Description                                                                          | Default   |
| ----------- | -------- | ---------- | ------------------------------------------------------------------------------------ | --------- |
| `locale`    | `string` | `false`    | Optional locale to target - either a common format ( "German" ), or an ISO Directive |           |
| `dspLocale` | `string` | `false`    | Optional display language locale                                                     |           |
| ----------  | ------   | ---------- | -------------                                                                        | --------- |

## Examples

```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```

## Related

* [GetLocale](getlocale.md)
* [GetLocaleInfo](getlocaleinfo.md)
* [LSCurrencyFormat](lscurrencyformat.md)
* [LSIsCurrency](lsiscurrency.md)
* [LSIsNumeric](lsisnumeric.md)
* [LSNumberFormat](lsnumberformat.md)
* [LSParseCurrency](lsparsecurrency.md)
* [LSParseNumber](lsparsenumber.md)
* [SetLocale](setlocale.md)
