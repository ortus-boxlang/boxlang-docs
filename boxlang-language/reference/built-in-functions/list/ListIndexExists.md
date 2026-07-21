[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListIndexExists`

Checks if a list has a given index

## Method Signature

```
ListIndexExists(list=[string], index=[integer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to check for an index |  |
| `index` | `integer` | `true` | numeric The index to check for |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Simple listIndexExists

Check whether the index is exists or not in list


```java
<bx:set list = "Apple,Orange,Banana,Graphs" >
<bx:if listIndexExists( list, 2 ) >
	<bx:set list = listsetAt( list, 2, "Goa" ) >
</bx:if>
<bx:output>#list#</bx:output>
```

Result: Apple,Goa,Banana,Graphs

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljbEKwjAYhPc8xZGphR8zCC7FQbBCobr0CWr9hUCblOSP9vGNVienO4777oxBZ6d5ZNRL%2F1b1DFbYJ5mTFBhtlMbdeKmX7GIB3aVoqT10RGMamIlIOIombFGirJQxOPN05YBTcoNY71SU0GYae2hqMucf%2FIN1tf4d0zQX%2BBY3f6%2B7dRt5%2FOIF%2FIkJgSUFF3Hvx8jqBcsbQqE%3D" target="_blank">Run Example</a>

```java
// Simple Example
writeoutput( listIndexExists( "Susi,LAS,,boxlang,,,test", 3 ) );
// Member Function
strList = ",I,,love,boxlang,,";
writeDump( strList.listIndexExists( 6 ) );
 // Not exists, returns false

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
  * [ListGetAt](./ListGetAt.md)
  * [ListGetEndings](./ListGetEndings.md)
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
