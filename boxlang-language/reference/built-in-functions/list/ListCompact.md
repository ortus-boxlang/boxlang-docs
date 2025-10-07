[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListCompact`

Compacts a list by removing empty items from the start and end of the list

## Method Signature

```
ListCompact(list=[string], delimiter=[string], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to compact |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Trims first and last comma from list string



<a href="https://try.boxlang.io/?code=eJzLySwucc7PLUhMLtFQUNJJTU8v1snNzMnWSSpKTUzRScvJLy3SUVLQtOYCAEI9DfM%3D" target="_blank">Run Example</a>

```java
listCompact( ",eggs,milk,bread,flour," );

```

Result: eggs,milk,bread,flour

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVjssKwjAQRff9iiGrlhkMPnbFlS4VBb8g1tEG8iKZ2N%2B3UBG8uwuXc4%2FWcLM%2BOYZnDYPYGJopW%2BFLlVSlBWeLHKJPZpiLIqKrM0HolZkDFfNmYpNlJFLQQdc3WsOZ%2FZ3zjweTlRGGWiR6eLCzfsbnpkg%2BFYE9KERc4wa3uMMlql8cjtWnFpbh6l8Ev3cf5Ps80Q%3D%3D" target="_blank">Run Example</a>

```java
// Simple function
writeOutput( listCompact( ",,,Plant,green,save,earth,," ) );
// Member function with custom delimiter
strLst = "+++1+2+3+4+++++++";
writeDump( strLst.listCompact( "+" ) );

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
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
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
