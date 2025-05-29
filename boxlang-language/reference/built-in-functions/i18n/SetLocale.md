[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SetLocale`

Sets the current request-level locale.

## Method Signature

```
SetLocale(locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `locale` | `string` | `true` | The locale ISO directive, common name or alias |  |

## Examples

### Set Locale Script Example

Outputs the current locale, Sets the locale to French (Belgian) and outputs it, then puts it back to the original and outputs it


```java
<bx:script>
	currentLocale = getLocale();
	writeOutput( "Current: " );
	writeDump( currentLocale );
	writeOutput( "<br />" );
	setLocale( "French (Belgian)" );
	writeOutput( "New: " );
	writeDump( getLocale() );
	writeOutput( "<br />" );
	setLocale( currentLocale );
	writeOutput( "Original: " );
	writeDump( getLocale() );
</bx:script>

```


### Additional Examples


```java
dump( getLocale() );
setLocale( "english (australian)" );
dump( getLocale() );
dump( Server.BOXLANG.SUPPORTEDLOCALES.listToArray().sort( "text" ) );

```



## Related

  * [GetLocaleDisplayName](./GetLocaleDisplayName.md)
  * [GetLocale](./GetLocale.md)
  * [GetLocaleInfo](./GetLocaleInfo.md)
  * [ParseCurrency](./ParseCurrency.md)
  * [LSParseCurrency](./LSParseCurrency.md)
  * [ClearLocale](./ClearLocale.md)
  * [CurrencyFormat](./CurrencyFormat.md)
  * [LSCurrencyFormat](./LSCurrencyFormat.md)
  * [IsCurrency](./IsCurrency.md)
  * [LSIsCurrency](./LSIsCurrency.md)
