[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListDeleteAt`

Deletes an element from a list.

Returns a copy of the list, without the
 specified element.

## Method Signature

```
ListDeleteAt(list=[string], position=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to delete from. |  |
| `position` | `integer` | `true` | The one-based index position of the element to delete. |  |
| `delimiter` | `string` | `false` | The delimiter used in the list. | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the list. | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | Whether the delimiter is a multi-character<br>                                   delimiter. | `false` |

## Examples

### Simple Example

Deletes 2nd item from the list

<a href="https://try.boxlang.io/?code=eJzLySwucUnNSS1JdSzRUFBKy8%2FXSUos0snJL0rN1cksKC7NVdJRMFLQtOYCAEGJDac%3D" target="_blank">Run Example</a>

```java
listDeleteAt( "foo,bar,lorem,ipsum", 2 );

```

Result: foo,lorem,ipsum

### Example with Custom Delimiter

Deletes 2nd item from the list using a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwucUnNSS1JdSzRUFBKy8%2FXSUosqsnJL0rN1cksKC7NrclNrSnOz00tycjMS1fSUTDSUVCqUVLQtOYCAKizFJs%3D" target="_blank">Run Example</a>

```java
listDeleteAt( "foo,bar|lorem,ipsum|me|something", 2, "|" );

```

Result: foo,bar|me|something

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtjsEKgkAQhu%2F7FIMnhSEPdZMOgQlC0aUXqO0PF1Zd3Nns8VutICGYyzD%2FfP83DkZwCuKCpGSNlxIWgl3ckppt%2FwDboAEWeKmMRcK0oYyygvKc9k8HLbhRPxPo90PF%2BxHtFQNVodNi%2Bk55GQ6xg7aUnBvjOc6FpXnT%2BT7hCzVOSmVoXUqf%2FGoptp771T%2BBL3XBVC%2FKX00I" target="_blank">Run Example</a>

```java
writeOutput( listDeleteAt( "I,love,boxlang,testFile", 4 ) ); // Expected output I,love,boxlang
// Member Function
strList = "This,is,a,the,test,file";
writeDump( strList.listDeleteAt( 3 ) );
 // Expected output This,is,the,test,file

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListEach](./ListEach.md)
  * [ListEvery](./ListEvery.md)
  * [ListFilter](./ListFilter.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListFirst](./ListFirst.md)
  * [ListGetAt](./ListGetAt.md)
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
