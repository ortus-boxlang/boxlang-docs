# ListMap

This BIF will iterate over each item in the delimited list and invoke the callback function for each item so\
you can do any operation on the item and return a new value that will be set at the same index in a new list.

The callback function will be passed the item as a string, the current index (0-based), and the original list.

* If the callback requires strict arguments, it will only receive the item as a string.
* If the callback does not require strict arguments, it will receive the item as a string, the index (0-based), and the original list.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
ListMap(list=[string], callback=[function:Function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument             | Type                | Required | Description                                                                                                                                                                                                       | Default |
| -------------------- | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `list`               | `string`            | `true`   | The delimited list to perform operations on                                                                                                                                                                       |         |
| `callback`           | `function:Function` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Function which will only receive the 1st arg.                   |         |
| `delimiter`          | `string`            | `false`  | string the list delimiter                                                                                                                                                                                         | `,`     |
| `includeEmptyFields` | `boolean`           | `false`  | boolean whether to include empty fields in the returned result                                                                                                                                                    | `false` |
| `parallel`           | `boolean`           | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads`         | `integer`           | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### Script Syntax

[Run Example](https://try.boxlang.io/?code=eJxdT8FKw0AQPe9%2BxdBcEgj9gJYKEfdQTCukoRXEw4iDXRI3YZpkFem%2FO2trGz0sM%2FPmzXtvC7TupfGwgMluT9ykcI%2BMFUpt%2FB5tmCtkW4XOVg2je5O2RI%2BdvBRW6MPdZK7poyN2WOf20AU9gZgG4gMVF5NaditsY%2BATlEIMmfuEIf0p9lRqSGBxA19aDcjgyG%2Bx7iloRjaaRcP0rBsnkZiof8bjcRoMs7Yl9xpfhRI5Yup6dhdsro8B9mw7uuvfJeGTVhJAFdlyffuwg9lvZK2O6XlltqbYmBHjz3evRPNYmmKd5flyUwptHFBI%2Bjk4fwPtEnrw)

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

[Run Example](https://try.boxlang.io/?code=eJxljVsKwjAQRb%2FNKi75kBayg1LBBQhuYaBTCYwxTBIfiHtv2og%2F%2Fh2453JmLT4njLAUo7CLTOpuSuHCdjAP9Zmnco0d5ib2g2l0lqIk9Sg%2B5RP9DIcOx%2FDCnaSw29CHiZ8NVxk9xgPeZqeci4ZmYg%2BbavGzFv6y31idFrkIOmQ%3D)

```java
fruits = "apple,pear,orange";
writedump( fruits );
fruitsPlural = listMap( fruits, ( Any value, Any index, Any list ) => {
	return value & "s";
} );
writedump( fruitsPlural );

```

## Related

* [GetToken](GetToken.md)
* [ListAppend](ListAppend.md)
* [ListAvg](ListAvg.md)
* [ListChangeDelims](ListChangeDelims.md)
* [ListCompact](ListCompact.md)
* [ListContains](ListContains.md)
* [ListContainsNoCase](ListContainsNoCase.md)
* [ListDeleteAt](ListDeleteAt.md)
* [ListEach](ListEach.md)
* [ListEvery](ListEvery.md)
* [ListFilter](ListFilter.md)
* [ListFind](ListFind.md)
* [ListFindNoCase](ListFindNoCase.md)
* [ListFirst](ListFirst.md)
* [ListGetAt](ListGetAt.md)
* [ListIndexExists](ListIndexExists.md)
* [ListInsertAt](ListInsertAt.md)
* [ListItemTrim](ListItemTrim.md)
* [ListLast](ListLast.md)
* [ListLen](ListLen.md)
* [ListNone](ListNone.md)
* [ListPrepend](ListPrepend.md)
* [ListQualify](ListQualify.md)
* [ListReduceRight](ListReduceRight.md)
* [ListRemoveDuplicates](ListRemoveDuplicates.md)
* [ListRest](ListRest.md)
* [ListSetAt](ListSetAt.md)
* [ListSome](ListSome.md)
* [ListSort](ListSort.md)
* [ListToArray](ListToArray.md)
* [ListTrim](ListTrim.md)
* [ListValueCount](ListValueCount.md)
* [ListValueCountNoCase](ListValueCountNoCase.md)
