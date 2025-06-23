[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListValueCount`

returns a count of the number of occurrences of a value in a list

## Method Signature

```
ListValueCount(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to be searched. |  |
| `value` | `string` | `true` | The value to locale |  |
| `delimiter` | `string` | `false` | The list delimiter(s) | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the search | `false` |

## Examples

### Simple Example

Counts instances of 'foo' in the list, ignoring case

<a href="https://try.boxlang.io/?code=eJzLySwuCUvMKU11zi%2FNK%2FHLd04sTtVQUErLz9dJSizSyckvSs3VcQPyMguKS3OVdMBSSgqa1lwAcZoThA%3D%3D" target="_blank">Run Example</a>

```java
listValueCountNoCase( "foo,bar,lorem,Foo,ipsum", "foo" );

```

Result: 2

### Example with Custom Delimiter

Counts instances of 'foo' in the list with a custom delimiter, ignoring case

<a href="https://try.boxlang.io/?code=eJzLySwuCUvMKU11zi%2FNK%2FHLd04sTtVQUEpKLKpxy8%2BvyckvSs3VySwoLs2tyU2tScvP1ynOz00tycjMSwfxatz8%2FZV0FJSATBBVo6Sgac0FAFkAHeg%3D" target="_blank">Run Example</a>

```java
listValueCountNoCase( "bar|Foo|lorem,ipsum|me|foo,something|foo|FOO", "foo", "|" );

```

Result: 3

### Additional Examples

<a href="https://try.boxlang.io?code=eJyVj0ELgkAQRu%2F%2BisFLCguCVwnWzEKQukR4XWWIBVtjd7b8%2BU2U5SWo07y5PL5Xa0ewhLAdxl6Zk8iLjXhxOdKEApCf1b6p8922bA5hFtysJlz78yWCmh1H1XssBm8ogp5%2F8VaGEEOcQZJARWCRvDULB%2BnvAt7xxQEtdso7BE3QKb6VcWicJn3F4CFNZ2mS0%2BRHOaHkMvlPWTpLY5TPbXc%2BE2xh" target="_blank">Run Example</a>

```java
List = "boxlang,ACF,boxlangExt,boxlang, ext,BOXLANGEXT";
writeDump( ListValueCount( list, "boxlang" ) ); // It return's 2
writeDump( ListValueCount( list, "boxlangExt" ) ); // It return's 2 because it case Insensitive
List2 = "boxlang@ACF@boxlangExt@boxlang@ext@BOXLANGEXT";
writeDump( ListValueCount( list2, "boxlang", "@" ) );

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
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
