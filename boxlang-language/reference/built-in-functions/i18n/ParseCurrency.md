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

### lsParseCurrency Example

LSParseCurrency converts a locale-specific currency string to a number.

<a href="https://try.boxlang.io/?code=eJzLKQ5ILCpOdS4tKkrNS67UUFBSMTQy0DM1UFLQtOYCAKArCIo%3D" target="_blank">Run Example</a>

```java
lsParseCurrency( "$120.50" );

```

Result: 120.5

### Additional Examples


```java
<bx:output>
	#LSParseCurrency( 4.5 )#<br>
	#LSParseCurrency( "$4.50" )#<br>
	#LSParseCurrency( "£4.50", "English (UK)" )#
</bx:output>
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
