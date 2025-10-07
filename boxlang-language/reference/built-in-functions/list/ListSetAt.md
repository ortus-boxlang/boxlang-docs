[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListSetAt`

Retrieves an item in to a delimited list at the specified position

## Method Signature

```
ListSetAt(list=[string], position=[integer], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `position` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `value` | `string` | `true` | string the value to set at the specified position |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Simple Example

Replaces the 2nd list element with 'foo'

<a href="https://try.boxlang.io/?code=eJzLySwuCU4tcSzRUFBKSizSyckvSs3VySwoLs1V0lEw0lFQSsvPV1LQtOYCADQuDOQ%3D" target="_blank">Run Example</a>

```java
listSetAt( "bar,lorem,ipsum", 2, "foo" );

```

Result: bar,foo,ipsum

### Example with Custom Delimiter

Inserts 'foo' into the list with a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwuCU4tcSzRUFBKSiyqyckvSs3VySwoLs2tyU2tKc7PTS3JyMxLV9JRMNJRUErLzweylGqUFDStuQCfNhPY" target="_blank">Run Example</a>

```java
listSetAt( "bar|lorem,ipsum|me|something", 2, "foo", "|" );

```

Result: bar|foo|me|something

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyNjjELwjAQhff8iiOThcPS1q04KOLm5NRubXJCIK2lTQThfryprVoHweVx3N1737NmcAlsQWKFNSrUSDIXB990K7Dhdia3c9OYIMhUBiklRBDlYlymk5e5ZlbMmvmnP%2F34gzAvUrL%2FGmRfCRjE9Z6eMRDHsCdV%2BYHAODCtsl7TANR07g4XQ1bDrbLhG8sXRgTPiZqa%2BqNvlTPXVug3Nlkv4HIzAou58ciayxYh5QGgO1x8" target="_blank">Run Example</a>

```java
list1 = ",a,b,c,d,e";
Dump( listSetAt( list1, "2", "Z" ) );
list2 = ",a||b||c||d||e";
Dump( listSetAt( list2, "2", "Z", "||" ) );
list3 = ",a,b,c,d,e";
Dump( listSetAt( list3, "2", "Z", ",", true ) ); // Because it includes empty field value ,Z,b,c,d,e
// MemberFunction
dump( list1.listSetAt( "4", "Y" ) );
 // ,a,b,c,Y,e

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
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
