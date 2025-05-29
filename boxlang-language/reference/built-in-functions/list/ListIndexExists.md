[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListIndexExists`

Checks if a list has a given index

## Method Signature

```
ListIndexExists(list=[string], index=[integer], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to check for an index |  |
| `index` | `integer` | `true` | numeric The index to check for |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |

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

  * [ListSome](./ListSome.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListFirst](./ListFirst.md)
  * [ListLast](./ListLast.md)
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
