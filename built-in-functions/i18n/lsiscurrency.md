# LSIsCurrency

Determines whether a value can be parsed to numeric in the given or default locale

## Method Signature

```
LSIsCurrency(number=[any], locale=[string])
```

### Arguments

| Argument   | Type     | Required   | Description                                                                     | Default   |
| ---------- | -------- | ---------- | ------------------------------------------------------------------------------- | --------- |
| `number`   | `any`    | `true`     | The value to be parsed                                                          |           |
| `locale`   | `string` | `false`    | The locale to apply to parsing - uses the context config value if not specified |           |
| ---------- | ------   | ---------- | -------------                                                                   | --------- |

## Examples

```
LSIsCurrency(number=[any], locale=[string])
```

## Related

* [GetLocale](getlocale.md)
* [GetLocaleDisplayName](getlocaledisplayname.md)
* [GetLocaleInfo](getlocaleinfo.md)
* [LSCurrencyFormat](lscurrencyformat.md)
* [LSIsNumeric](lsisnumeric.md)
* [LSNumberFormat](lsnumberformat.md)
* [LSParseCurrency](lsparsecurrency.md)
* [LSParseNumber](lsparsenumber.md)
* [SetLocale](setlocale.md)
