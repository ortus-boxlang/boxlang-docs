[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListEvery`

Tests whether all items in a list meet the specified callback

## Method Signature

```
ListEvery(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
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

### Example for positive result

Checks whether all items in a list are greater than 2 and outputs true because all of them fulfill the requirement.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUDLRMdUx0zFXsuYqL8osSfUvLSkoLdFQyAFKu5alFlVCmDoKGgqOeZUKZYk5pakKmgq2dgrVXJxFqSWlRXlQQTsFI2uuWqCcpjUXAD1HG50%3D" target="_blank">Run Example</a>

```java
list = "4,5,6,7";
writeOutput( listEvery( list, ( Any value ) => {
	return value > 2;
} ) );

```

Result: true

### Example for negative result

Checks whether all items in a list are greater than 2 and outputs false because some of them do not fulfill the requirement.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUDLUMdIx1jFRsuYqL8osSfUvLSkoLdFQyAFKu5alFlVCmDoKGgqOeZUKZYk5pakKmgq2dgrVXJxFqSWlRXlQQTsFI2uuWqCcpjUXADlvG5E%3D" target="_blank">Run Example</a>

```java
list = "1,2,3,4";
writeOutput( listEvery( list, ( Any value ) => {
	return value > 2;
} ) );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxdjMEKwjAQBc%2FmKx49pZA%2FCBUEvfkTAbclEGPY7laL%2BO%2FW5FRvwzDMyBplxoAulJLIFQrsHhzyRJ031zjLZSFeLcYaOlic8oolJCVXMeYbvRqmLUeP4Yi3OTw5Cp31XmxL0PudrIt%2F2Q6bYxLlDGElbz4%2F9QXZuzbm" target="_blank">Run Example</a>

```java
fruits = "apple,pear,orange";
ListEvery( fruits, ( Any value, Any index, Any list ) => {
	writeDump( index );
	writeDump( value );
	writeDump( list );
	return true;
} );

```

Result: true


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
  * [ListEach](./ListEach.md)
  * [ListSort](./ListSort.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListFilter](./ListFilter.md)
  * [GetToken](./GetToken.md)
  * [ListItemTrim](./ListItemTrim.md)
