[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListLen`

Calculates the length of a list separated by the specified delimiter

## Method Signature

```
ListLen(list=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to calculate the length |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |

## Examples

### Simple listLen Example

Get the number of elements in this list

<a href="https://try.boxlang.io/?code=eJzLySwu8UnN01BQSsvP10lKLAJhIx0gx0hJQdOaCwCyzQnQ" target="_blank">Run Example</a>

```java
listLen( "foo,bar,bar2,foo2" );

```

Result: 4

### listLen Example with Delimiter

Get the number of elements in this list using a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwu8UnN01BQSsvP10lKLKoBYqMaIMdISUdBqUZJQdOaCwDzEwt8" target="_blank">Run Example</a>

```java
listLen( "foo,bar|bar2|foo2", "|" );

```

Result: 3

### listLen Example with IncludeEmptyValues

Get the number of elements in this list, including empty values

<a href="https://try.boxlang.io/?code=eJzLySwu8UnN01BQSsvP10lKLNLRATKMlHQUlHRARKRrsJKCpjUXAPzbCqY%3D" target="_blank">Run Example</a>

```java
listLen( "foo,bar,,foo2", ",", "YES" );

```

Result: 4

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMjJLC7xSc3TUFAqLi3O1ClOzNXxcQzWKUktLlFS0FTQtFbQ11cw4SrHqQOsXAehtjyzJEMhNbegpFKhLDGnNLWYoF49iGYukG5jLgApey7b" target="_blank">Run Example</a>

```java
writeDump( listLen( "susi,sam,LAS,test" ) ); // 4
writeDump( listLen( "susi,,LAS,," ) ); // with empty values
writeDump( listLen( "susi,,LAS,,." ) );
 // 3

```



## Related

  * [ListSome](./ListSome.md)
  * [ListReduceRight](./ListReduceRight.md)
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
  * [ListRest](./ListRest.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListEvery](./ListEvery.md)
  * [ListEach](./ListEach.md)
  * [ListSort](./ListSort.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListFilter](./ListFilter.md)
  * [GetToken](./GetToken.md)
  * [ListItemTrim](./ListItemTrim.md)
