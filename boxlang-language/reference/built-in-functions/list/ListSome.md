[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListSome`

Tests whether any item in a list meets the specified callback

## Method Signature

```
ListSome(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |
| `parallel` | `boolean` | `false` | boolean whether to execute the filter in parallel | `false` |
| `maxThreads` | `integer` | `false` | number the maximum number of threads to use in the parallel filter |  |

## Examples

### List contains some.

Take a string list and see if some elements match a given predicate.


```java
var fruitList = arrayToList( [ 
	"apple",
	"mango",
	"orange",
	"pear"
], "," );
writeOutput( listSome( fruitList, ( Any fruit ) => {
	return findNoCase( "n", fruit );
}, "," ) );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyljUsKwkAQRNfOKYpZTaAgBwgjCC7deYKJdCAwiTIfg4p3t5UsdeWmqS6K9%2BKYCzwsGcieJ1I42M60LfqQBUVyMUmybg46PZ4ncYiaCIfdfMM1xCpo4Ld4mE2SUtO8ll65QVlPKt8SQ4hZiJLqetF0ZkljkX2dLg5vjTZ%2F2O6%2FbJ%2Fnu%2B4Fi7lMtw%3D%3D" target="_blank">Run Example</a>

```java
list = ",,a,,b,c,,e,f";
// base test
res = ListSome( list, ( Any value ) => {
	return value == "a";
}, ",", false, true, true );
writeDump( res );
res = ListSome( list, ( Any value ) => {
	return value == "z";
}, ",", false, true, false );
writeDump( res );

```



## Related

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
  * [ListFilter](./ListFilter.md)
  * [GetToken](./GetToken.md)
  * [ListItemTrim](./ListItemTrim.md)
