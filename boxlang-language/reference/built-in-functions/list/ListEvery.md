[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListEvery`

Used to iterate over a delimited list and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the list.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large lists, especially when the test function is computationally expensive or the list is large.

## Method Signature

```
ListEvery(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to test against the callback. |  |
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | ( BoxLang only) If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |

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

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListDeleteAt](./ListDeleteAt.md)
  * [ListEach](./ListEach.md)
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
