[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetLocale`

Retrieves the the string representation of the current locale

## Method Signature

```
GetLocale()
```

### Arguments

This function does not accept any arguments

## Examples

### Output current Locale than set it to swiss locale




```java
writeOutput( getlocale() );
writeOutput( " → " );
setLocale( "de_ch" );
writeOutput( getlocale() );

```

Result: english (us) → german (swiss)

### Additional Examples


```java
var n = 1234.56;
writeOutput( getlocale() );
dump( dateTimeFormat( now() ) );
dump( LSdateTimeFormat( now() ) );
dump( numberFormat( n ) );
dump( LSnumberFormat( n ) );
writeOutput( " To " );
setLocale( "french(switzerland)" );
writeOutput( getlocale() );
dump( dateTimeFormat( now() ) );
dump( LSdateTimeFormat( now() ) );
dump( numberFormat( n ) );
dump( LSnumberFormat( n ) );
writeOutput( " To " );
setLocale( "German" );
writeOutput( getlocale() );
dump( dateTimeFormat( now() ) );
dump( LSdateTimeFormat( now() ) );
dump( numberFormat( n ) );
dump( LSnumberFormat( n ) );

```



## Related

  * [ClearLocale](./ClearLocale.md)
  * [CurrencyFormat](./CurrencyFormat.md)
  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [IsCurrency](./IsCurrency.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [LSIsCurrency](./LSIsCurrency.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [ParseCurrency](./ParseCurrency.md)
  * [SetLocale](./SetLocale.md)
