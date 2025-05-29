[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListMap`

Used to iterate over a delimited list and run the function closure for each item in the list and create a new list from the returned values.

## Method Signature

```
ListMap(list=[string], callback=[function:Function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Function which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxdT8FKw0AQPe9%2BxdBcEgj9gJYKEfdQTCukoRXEw4iDXRI3YZpkFem%2FO2trGz0sM%2FPmzXtvC7TupfGwgMluT9ykcI%2BMFUpt%2FB5tmCtkW4XOVg2je5O2RI%2BdvBRW6MPdZK7poyN2WOf20AU9gZgG4gMVF5NaditsY%2BATlEIMmfuEIf0p9lRqSGBxA19aDcjgyG%2Bx7iloRjaaRcP0rBsnkZiof8bjcRoMs7Yl9xpfhRI5Yup6dhdsro8B9mw7uuvfJeGTVhJAFdlyffuwg9lvZK2O6XlltqbYmBHjz3evRPNYmmKd5flyUwptHFBI%2Bjk4fwPtEnrw" target="_blank">Run Example</a>

```java
Rainbow = "Whero, Karaka, Kowhai, Kakariki, Kikorangi, Tawatawa, Mawhero";
externalList = "";
reverseRainbow = listMap( rainbow, ( Any v, Any i, Any l ) => {
	var newValue = "#i#:#v.reverse()#";
	externalList = externalList.listAppend( newValue );
	return newValue;
} );
writeDump( [
	{
		RAINBOW : rainbow
	},
	{
		REVERSERAINBOW : reverseRainbow
	},
	{
		EXTERNALLIST : externalList
	}
] );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljVsKwjAQRb%2FNKi75kBayg1LBBQhuYaBTCYwxTBIfiHtv2og%2F%2Fh2453JmLT4njLAUo7CLTOpuSuHCdjAP9Zmnco0d5ib2g2l0lqIk9Sg%2B5RP9DIcOx%2FDCnaSw29CHiZ8NVxk9xgPeZqeci4ZmYg%2BbavGzFv6y31idFrkIOmQ%3D" target="_blank">Run Example</a>

```java
fruits = "apple,pear,orange";
writedump( fruits );
fruitsPlural = listMap( fruits, ( Any value, Any index, Any list ) => {
	return value & "s";
} );
writedump( fruitsPlural );

```



## Related

  * [ListSome](./ListSome.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListFirst](./ListFirst.md)
  * [ListLast](./ListLast.md)
  * [ListIndexExists](./ListIndexExists.md)
  * [ListInsertAt](./ListInsertAt.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListCompact](./ListCompact.md)
  * [ListTrim](./ListTrim.md)
  * [ListDeleteAt](./ListDeleteAt.md)
  * [ListRemoveDuplicates](./ListRemoveDuplicates.md)
  * [ListToArray](./ListToArray.md)
  * [ListQualify](./ListQualify.md)
  * [ListAppend](./ListAppend.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
  * [ListAvg](./ListAvg.md)
  * [ListLen](./ListLen.md)
  * [ListRest](./ListRest.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListEvery](./ListEvery.md)
  * [ListEach](./ListEach.md)
  * [ListSort](./ListSort.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListFilter](./ListFilter.md)
  * [GetToken](./GetToken.md)
  * [ListItemTrim](./ListItemTrim.md)
