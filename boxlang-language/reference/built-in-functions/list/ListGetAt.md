[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListGetAt`

Retrieves an item from a delimited list at the specified position

## Method Signature

```
ListGetAt(list=[string], position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `position` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Simple Example

Returns the 2nd element in the list

<a href="https://try.boxlang.io/?code=eJzLySwucU8tcSzRUFBKy8%2FXSUos0snJL0rN1cksKC7NVdJRMFLQtOYCABBIDHQ%3D" target="_blank">Run Example</a>

```java
listGetAt( "foo,bar,lorem,ipsum", 2 );

```

Result: bar

### Example with Delimiter

Returns the 3rd element in the list using a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwucU8tcSzRUFBKy8%2FXSUosqsnJL0rN1cksKC7NrclNrSnOz00tycjMS1fSUTDWUVCqUVLQtOYCAGHmE2k%3D" target="_blank">Run Example</a>

```java
listGetAt( "foo,bar|lorem,ipsum|me|something", 3, "|" );

```

Result: me

### Example with IncludeEmptyValues

Returns the 4th element in the list, treating the empty element as a value

<a href="https://try.boxlang.io/?code=eJzLySwucU8tcSzRUFBKy8%2FXSUos0tHJyS9KzdXJLCguzVXSUTDRUVDSAdIlRaWpCprWXAC3TA9q" target="_blank">Run Example</a>

```java
listGetAt( "foo,bar,,lorem,ipsum", 4, ",", true );

```

Result: lorem

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxNzrsKwzAMBdDdX3HxkgRMNZROoUOhj6Wl0D%2BIbUENeWHLpJ9fp3TIJAkuOneJQfiZZc5Sow9JbiynsurOGGuc0QZ7A71OiZnRoGlBhBdLjmOCVeV48GA54ppHJ2EasQR5o6IKnvswFCCqJPFevuMITR2RJUfkdauW1T%2FnYa7xj%2Bw2LQ6Fpi2tVvvymdkJe0y%2F3nDqC4%2BwPHA%3D" target="_blank">Run Example</a>

```java
writeOutput( listGetAt( "a,,b,c,", 3, ",", true ) ); // Returns b
// Member Function with '/' delimiter
strList = "/a//b/c//d";
writeDump( strList.listGetAt( 5, "/", true ) );
 // Expected output c

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
  * [ListEach](./ListEach.md)
  * [ListEvery](./ListEvery.md)
  * [ListFilter](./ListFilter.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListFirst](./ListFirst.md)
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
