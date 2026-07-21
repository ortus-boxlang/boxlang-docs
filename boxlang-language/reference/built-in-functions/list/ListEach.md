[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListEach`

Used to iterate over a delimited list and run the function closure for each item in the list.

This BIF is similar to the ArrayEach BIF, but operates on a delimited list instead of an array.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
ListEach(list=[string], callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Consumer which will only receive the 1st arg. |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | Whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### List Loop using listEach

Using a semicolon delimiter.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUEq0TrJOVrLmygHyXROTMzQUQCwdBQ0Fx7xKhdSc1NzUPCAXxMnMS0mtgDBBahQ0FWztFKq5OMuLMktS%2FUtLCkpLNBSUlMHKlK2UoXqVrZUUNK25anUUlCAsACwvJJM%3D" target="_blank">Run Example</a>

```java
list = "a;b;c";
listEach( list, ( Any element, Any index, Any list ) => {
	writeOutput( "#index#:#element#;" );
}, ";" );

```

Result: 1:a;2:b;3:c;

### Member Function Example

List Loop list.listEach()

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUEq0TrJOVrLmygHy9UCEa2JyhoaChoJjXqVCak5qbmpeiQ6Yk5mXkloBYYLUKWgq2NopVHNxlhdllqT6l5YUlJZoKCgpg5UpWylD9SpbKyloWnPV6igoQVgAGaQkdQ%3D%3D" target="_blank">Run Example</a>

```java
list = "a;b;c";
list.listEach( ( Any element, Any index, Any list ) => {
	writeOutput( "#index#:#element#;" );
}, ";" );

```

Result: 1:a;2:b;3:c;

### Example using a Closure

Example 1

<a href="https://try.boxlang.io/?code=eJxVjcEOgjAMhs%2F0KZodGCR7AokHDl7l4NF4GFjDDGxkbBFifHe3oSae%2Brf9%2BpXGqbZWrrjHM0LG7qbXTIQwkaMUWtMyuFQwqNmdAsZ4ZLhAHpFYA8FZBTJ6DrLrC6SPVeDSDWb2lrDcDNs%2Buf6XcPO6c8ro37TAWq9RpeVIIjVKX2nBEp%2BQPaxy1Hg3eZf%2BHQOEOTKUbsN2Ieffiwpe8AbgiEjb" target="_blank">Run Example</a>

```java
empArray = [ 
	"john",
	"pete",
	"bob"
];
listS = "'john', 'pete', 'bob'";
arrayEach( empArray, xclosure );
listEach( listS, xclosure );

function xclosure( Any empname, Any index ) {
	writeOutput( empName & " at index: " & index );
}

```

Result: john at index: 1pete at index: 2bob at index: 3'john' at index: 1 'pete' at index: 2 'bob' at index: 3

### Another Closure Example

Example 2

<a href="https://try.boxlang.io/?code=eJxFTksKwjAUXJtTDFlIhJzA4qq4qygW3McQ0wc1LckLUsS7mxTB3fyYGUu8dJQYB8gLMad7jn7QuJrRUQUnMk%2FS6EzCzXmTZCPEIwfLNAXMkQK3pUKh54I9bCHY4S02r0jszpnnzAqyzTG6wKu%2Fh8T2l2zER4xl%2F2jsoFatvtH%2F5hr5AiovNyw%3D" target="_blank">Run Example</a>

```java
cityList = "Pittsburgh, Raleigh, Miami, Las Vegas";

function printCity( String city ) {
	writeOutput( "Current city: " & city );
}
listEach( cityList, printCity );

```

Result: Current city: PittsburghCurrent city: RaleighCurrent city: MiamiCurrent city: Las Vegas

### Additional Examples

<a href="https://try.boxlang.io/?code=eJy1j0sKwjAURcd2FZd0Ummwc2sLDnSk6Bb6edpAmkr6ahVx7%2Fan4gKchBvePQeuVjUjgjjqxLA8WyIj6%2BRKkhLLhQgd3RU2SVZ46JOEh7W5gzSV1AHDR5mcbmPsO5gjivFwZq1VTIeGLw17EO5Qc5fuxLrhKrWxwDx0nv0TBNhTmZLFqTEZq8qgVVwga2quSuSkVdn5rPOr7SUTt524j7dmuxvnVYZ8biufi26heF8W33F%2FmSUh%2FCG9AMg6c50%3D" target="_blank">Run Example</a>

```java
list = "Plant,green,save,earth";
listEach( list, ( Any element, Any index, Any list ) => {
	writeOutput( "#index#:#element#;<br>" );
} );
// Member function with custom delimiter
writeOutput( "<br>Member Function<br>" );
strLst = "one+two+three";
strLst.listEach( ( Any element, Any index, Any list ) => {
	writeOutput( "#index#:#element#;<br>" );
}, "+" );

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListDeleteAt](./ListDeleteAt.md)
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
