[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListReduceRight`

Run the provided udf over a reversed delimited list to reduce the values to a single output

## Method Signature

```
ListReduceRight(list=[string], callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java BiFunction which will only receive the first 2 args. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

### Simple listReduceRight Example

Demonstrate how the function works from right to left.

<a href="https://try.boxlang.io/?code=eJw1jUEKwjAQRdfmFJ8sJIW5Qajg3lVvUJtBAyaUMbUt0rt3SHX1H58HL623%2BC5oYXu600DBepN5%2Fp0vnY7DNHAXH8%2FikKpOcLjmFaPwhyplXspBMSwH9CJo0F7wNSfhMkmuPs5V1lHTm41gLRpvZolFS2l0%2BPf13QHc5DHQ" target="_blank">Run Example</a>

```java
myList = "a,b,c,d";
newList = listReduceRight( myList, ( Any prev, Any next, Any idx, Any arr ) => {
	return prev & next & idx;
}, "" );
writedump( newList );

```

Result: d4c3b2a1

### listReduceRight as a Member Function

Demonstrate the member function.

<a href="https://try.boxlang.io/?code=eJw1jU0KwjAQhdfmFI8sJIXgBUIF9656g9oMGjChjNM%2FxLs7pLqZ%2BXjvg5e3a3oJWtje3%2Fzgow2m0PILc21PTz0dxWmgLt0f4uBwKRtGptlXKrTKTimuO%2FTMaNCe8TYHJpm4VB%2FHKutTM5iPh7Voglk4iS7k0eE%2Fr%2BkXv84xsg%3D%3D" target="_blank">Run Example</a>

```java
myList = "a,b,c,d";
newList = myList.listReduceRight( ( Any prev, Any next, Any idx, Any arr ) => {
	return prev & next & idx;
}, "" );
writedump( newList );

```

Result: d4c3b2a1

### Empty Elements

Demonstrate the behavior when there is an empty element.

<a href="https://try.boxlang.io/?code=eJzLrfTJLC5RsFVQStQBgSQgTgbiFCVrrrzUcqhkLliVXg6QCEpNKU1ODcpMzyjRUNBQcMyrVCgoSi3TAbPyUitKIKzMlAoFTQVbO4VqLs6i1JLSojywMgU1sBogBVRgzVWro6CkpKBpzVVelFkCNDi3QEMBZitQFADheTA5" target="_blank">Run Example</a>

```java
myList = "a,,,,,b,,,c,,,d";
newList = myList.listReduceRight( ( Any prev, Any next, Any idx ) => {
	return prev & next & idx;
}, "" );
writedump( newList );

```

Result: d4c3b2a1


## Related

  * [ListSome](./ListSome.md)
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
