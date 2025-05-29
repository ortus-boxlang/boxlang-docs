[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetLocaleDisplayName`

Returns the {@link java.util.Locale} display name with an optional display language/locale

## Method Signature

```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `locale` | `string` | `false` | Optional locale to target - either a common format ( "German" ), or an ISO Directive |  |
| `dspLocale` | `string` | `false` | Optional display language locale |  |

## Examples

### Output current Locale's display name than set it to swiss locale




```java
writeOutput( getLocaleDisplayName() );
writeOutput( " → " );
setLocale( "de_ch" );
writeOutput( getLocaleDisplayName() );

```

Result: English (United States) → Deutsch (Schweiz)

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUEhPLfHJT07MSXXJLC7ISaz0S8xN1dBU0LTmAgAJfgzQ" target="_blank">Run Example</a>

```java
writeDump( getLocaleDisplayName() );

```



## Related

  * [GetLocale](./GetLocale.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [SetLocale](./SetLocale.md)
  * [ParseCurrency](./ParseCurrency.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [ClearLocale](./ClearLocale.md)
  * [CurrencyFormat](./CurrencyFormat.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [IsCurrency](./IsCurrency.md)
  * [LSIsCurrency](./LSIsCurrency.md)
