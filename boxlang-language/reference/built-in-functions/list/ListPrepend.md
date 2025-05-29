[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListPrepend`

Filters a delimted list and returns the values from the callback test

## Method Signature

```
ListPrepend(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `value` | `string` | `true` |  |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

### Prepend to a List using the List member function



<a href="https://try.boxlang.io/?code=eJwrTs3MS0vNSfHJLC5RsFVQcs7JL05VCEnMyU4t0gnOLy1Q8EusylSy5ipGVYjM1csBEgFFqQWpeSkaCkoBpWlplQrBGZlFJUoKmtZc5UWZJan%2BpSUFpSUaKPpAkgBktCyy" target="_blank">Run Example</a>

```java
seinfeldList = "Close Talker,Soup Nazi";
seinfeldList = seinfeldList.listPrepend( "Puffy Shirt" );
writeOutput( seinfeldList );

```

Result: "Puffy Shirt,Close Talker,Soup Nazi"

### Prepend to a List using a dash delimiter



<a href="https://try.boxlang.io/?code=eJwrzs9N9cksLlGwVVAy1DXSNdY1UbLmKkaI5gCpgKLUgtS8FA0FmLiOgpKBEpDQVVLQtOYqL8osSfUvLSkoLUEoAUkAADlxHIQ%3D" target="_blank">Run Example</a>

```java
someList = "1-2-3-4";
someList = listPrepend( someList, "0", "-" );
writeOutput( someList );

```

Result: "0-1-2-3-4"

### Prepend to a List with Empty Fields On

CF2018+

<a href="https://try.boxlang.io/?code=eJwrzs9N9cksLlGwVVByS03S8U0s0nEsKFKy5ipGyOQAqYCi1ILUvBQNBZi4joKSjo5XYp4SiAEkSopKUxU0rbnKizJLUv1LSwpKSxCKQRIAUHoiJw%3D%3D" target="_blank">Run Example</a>

```java
someList = "Feb,Mar,Apr";
someList = listPrepend( someList, ",,Jan", ",", true );
writeOutput( someList );

```

Result: ",,Jan,Feb,Mar,Apr"

### Prepend to a List with Empty Fields Off

CF2018+

<a href="https://try.boxlang.io/?code=eJwrzs9N9cksLlGwVVByS03S8U0s0nEsKFKy5ipGyOQAqYCi1ILUvBQNBZi4joKSjo5XYp6OjhKICSTSEnOKUxU0rbnKizJLUv1LSwpKSxDqQRIArBoiyg%3D%3D" target="_blank">Run Example</a>

```java
someList = "Feb,Mar,Apr";
someList = listPrepend( someList, ",,Jan,,", ",", false );
writeOutput( someList );

```

Result: "Jan,Feb,Mar,Apr"

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVzU0KwjAQhuF9TjHMKoXBHKC4ELRQqCDkBNrOIpA%2Fkkn1%2BFaqC1ff5uN5jQHrQvYMl9f9s%2BpZnHBqkpto8K7KrXDmuGhA26qj6WSJfJuZiUi4ChLgGCsX4QWhg65XxsCVw4MLDC3O4lJUVcq0YXAEpHED0so%2FBfs9em4ha%2FgeD%2F%2FpwZWttOtvId86jw%3D%3D" target="_blank">Run Example</a>

```java
// Simple Example
writeoutput( listPrepend( "Susi,LAS,,boxlang,,,test", "Inserted" ) );
// Member Function
strList = ",I,,love,boxlang,,";
writeDump( strList.listPrepend( "First" ) );

```



## Related

  * [ListSome](./ListSome.md)
  * [ListReduceRight](./ListReduceRight.md)
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
