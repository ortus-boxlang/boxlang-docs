[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListFilter`

Filters a delimted list and returns the values from the callback test

## Method Signature

```
ListFilter(list=[string], filter=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `filter` | `function:Predicate` | `true` | function closure filter test. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |
| `parallel` | `boolean` | `false` | boolean whether to execute the filter in parallel | `false` |
| `maxThreads` | `integer` | `false` | number the maximum number of threads to use in the parallel filter |  |

## Examples

### Example using a simple numeric comparison

Take list and use List Filter to return items that are 3 and higher.

<a href="https://try.boxlang.io/?code=eJzLK81NSi3yySwuUbBVUDLUMdIx1jHRMdUxU7LmKskoSk31L%2FLNL0oFSuYA1bhl5pSkFmko5MF16ShoKDjmVSpklqTmKmgq2NopVHNxFqWWlBblQcTsbBWMrblqFTStucqLgCIppbkFGgrIRgNlAO%2BmKaI%3D" target="_blank">Run Example</a>

```java
numberList = "1,2,3,4,5,6";
threeOrMore = listFilter( numberList, ( Any item ) => {
	return item >= 3;
} );
writedump( threeOrMore );

```

Result: A List with the values '3,4,5,6'

### Example using a member function

This is the same example as above, but using a member function on the list instead of a standalone function.

<a href="https://try.boxlang.io/?code=eJzLK81NSi3yySwuUbBVUDLUMdIx1jHRMdUxU7LmKskoSk31L%2FLNL0oFSubBVerlAAm3zJyS1CINBQ0Fx7xKhcyS1FwFTQVbO4VqLs6i1JLSojyImJ2tgrE1V62CpjVXeRFQJKU0t0BDAdlkoAwA1gUphA%3D%3D" target="_blank">Run Example</a>

```java
numberList = "1,2,3,4,5,6";
threeOrMore = numberList.listFilter( ( Any item ) => {
	return item >= 3;
} );
writedump( threeOrMore );

```

Result: A List with the values '3,4,5,6'

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyNj0FrwzAMhc%2Fxr9BySsGsPyB0MCi9FcYG29lb5dVgK0WRm5Wl%2F31yaNnWXnrUe096%2BtIhhl5gAfWL2%2BP45gR5fIqOZPxkRKpb40NU8Rn7HEuw5FeT1ECati008EgHwIgJSccyhM0XzGDxAN%2BmCr45m3CnVUNpqdVWr2KUzATCGVtTHc1Z8C72qhwt1KNmWzNwEFzmtGvg30tqzeewxvSODKtMHxI6MuWxVxcLWUdoZeisbJXI%2Bi6z9WGPisbYn4g0ev%2BX7JfohEObK5yJZTp6K8sFRqlX5QcTI3x6" target="_blank">Run Example</a>

```java
mylist = "Save|Water|Plant|green";
filterResult = listFilter( mylist, ( Any element, Any idx ) => {
	if( element != "water" ) {
		return true;
	}
	return false;
}, "|" );
writeDump( filterResult );
// Member Function
listVal = "one,two,three,four,five";
res = listVal.listFilter( ( Any elem, Any ind ) => {
	if( elem != "three" ) {
		return true;
	}
	return false;
} );
writeDump( res );

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
  * [ListMap](./ListMap.md)
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
  * [GetToken](./GetToken.md)
  * [ListItemTrim](./ListItemTrim.md)
