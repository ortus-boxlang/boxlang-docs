[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListInsertAt`

Filters a delimted list and returns the values from the callback test

## Method Signature

```
ListInsertAt(list=[string], position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `position` | `integer` | `true` |  |  |
| `value` | `string` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

### Simple Example

Inserts 'foo' into the list at position 2

<a href="https://try.boxlang.io/?code=eJzLySwu8cwrTi0qcSzRUFBKSizSyckvSs3VySwoLs1V0lEw0lFQSsvPV1LQtOYCAGxYDi0%3D" target="_blank">Run Example</a>

```java
listInsertAt( "bar,lorem,ipsum", 2, "foo" );

```

Result: bar,foo,lorem,ipsum

### Example with Custom Delimiter

Inserts 'foo' into the list with a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwu8cwrTi0qcSzRUFBKSiyqyckvSs3VySwoLs2tyU2tKc7PTS3JyMxLV9JRMNJRUErLzweylGqUFDStuQDughUh" target="_blank">Run Example</a>

```java
listInsertAt( "bar|lorem,ipsum|me|something", 2, "foo", "|" );

```

Result: bar|foo|lorem,ipsum|me|something

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVzcEKwjAQhOF7nmLYUwvBIh6LEEEEQfEZTLpgoE1LsiGv7wq9eBwG%2Fq%2FlKPyqslXpMMci91Q4y0UXva31NliyOFrQmpjQox%2FNMODJi%2BeMW01B4prQonzgMPEcFw1mUyQ%2FtIazZpx3E42m%2FahrXbYO%2B3v4B0%2BqBNXI7dAXidwwnQ%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( listInsertAt( "a,,b,c,", 1, "one" ) );
// Member Function with @ delimiter
strList = "a@b@d";
writeDump( strList.listInsertAt( 3, "c", "@" ) );

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
