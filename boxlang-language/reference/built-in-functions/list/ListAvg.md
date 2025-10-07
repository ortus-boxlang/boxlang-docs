[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListAvg`

Gets the average of all values in a list

## Method Signature

```
ListAvg(list=[string], delimiter=[string], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to compact |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Calculate average from query columns



<a href="https://try.boxlang.io/?code=eJxlkE1Lw0AQhs%2FJrxjSgwksS1IU%2FMBDtBUqmoLtTTxskyFZyO7qfqSI%2BN%2BdpiLB3oZ35pmZ9xW%2B69Gjg1v4CGg%2FK9ynkMiGaaGQ7dD5rVSYMNK0xxYtG4StO2FZg7VUok8gu4lHtGyaF0O0%2BF3J4DWOvuIoWi3gGnJGVVU%2BL6lOSq1pJwl3y812uxrF4oKfx9E3mzDFlHk0nT5h5vzyHzOfMptwcuaKF0TEb4e391Z6XAf%2FHjyZLo9%2FnzkQA1rRIhzsgyf%2FIB3MqqB2aB%2BMVYLGe%2Bl8ObTpMbZ70welF8KLqf%2FkLz%2FIuDdPhKQZZNTIeZ6TOAOHtdGN42OMPw6cbts%3D" target="_blank">Run Example</a>

```java
athletes = queryNew( "id,name,bestTime", "integer,varchar,decimal" );
queryAddRow( athletes, [
	{
		ID : 0,
		NAME : "Anne",
		BESTTIME : 15.4
	},
	{
		ID : 1,
		NAME : "John",
		BESTTIME : 12.8
	},
	{
		ID : 2,
		NAME : "Sue",
		BESTTIME : 9.1
	}
] );
writeOutput( "Athlete's average best time is #NumberFormat( listAvg( queryColumnData( athletes, "bestTime" ).toList() ), "0.00" )# seconds." );

```

Result: Athlete's average best time is 12.43 seconds.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUPDJLC5xLEvXUFAy1DHSMVZS0FTQtFbQ11dwrShITS5JTVHILy0pKC2xUjDiAor6puYmpRYpuJXmJZdk5udx5QC1B5cUKdgqKJnomOqYKVlzlSMMB8kWlxTp5UAtAZnNhdVwUy4ANGItuQ%3D%3D" target="_blank">Run Example</a>

```java
writeDump( ListAvg( "1,2,3" ) ); // Expected output: 2
// Member Function
listStr = "4,5,6";
writeDump( liststr.listAvg() );
 // Expected output: 5

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListDeleteAt](./ListDeleteAt.md)
  * [ListEach](./ListEach.md)
  * [ListEvery](./ListEvery.md)
  * [ListFilter](./ListFilter.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListFirst](./ListFirst.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListGetEndings](./ListGetEndings.md)
  * [ListIndexExists](./ListIndexExists.md)
  * [ListInsertAt](./ListInsertAt.md)
  * [ListItemTrim](./ListItemTrim.md)
  * [ListLast](./ListLast.md)
  * [ListLen](./ListLen.md)
  * [ListMap](./ListMap.md)
  * [ListNone](./ListNone.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListQualify](./ListQualify.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListRemoveDuplicates](./ListRemoveDuplicates.md)
  * [ListRest](./ListRest.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
