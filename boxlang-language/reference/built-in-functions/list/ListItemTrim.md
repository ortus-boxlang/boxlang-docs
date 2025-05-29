[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListItemTrim`

Trims each item in the list.

## Method Signature

```
ListItemTrim(list=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to trim each item |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |

## Examples

### Simple Example

Trims each item in the list.

<a href="https://try.boxlang.io/?code=eJxLrUjMLchJ9cksLlGwVVDKSM3JyddRKM8vyklR0CnJyCzWUcgsVkjUUdBJhahUsuYqL8osSfUvLSkoLdFQyAHq9CxJzQ0pyszVUIAqAgkqaCpoWnMBAFBFINo%3D" target="_blank">Run Example</a>

```java
exampleList = "hello, world ,this, is a, ,example";
writeOutput( listItemTrim( examplelist ) );

```

Result: hello,world,this,is a,,example

### Using as member function

Trims each item in the list.

<a href="https://try.boxlang.io/?code=eJxLrUjMLchJ9cksLlGwVVDKSM3JyddRKM8vyklR0CnJyCzWUcgsVkjUUdBJhahUsuZKRdGDxNPLARKeJam5IUWZuRqa1lzlRZklqf6lJQWlJRowhSA1CkA5ADH%2BKpo%3D" target="_blank">Run Example</a>

```java
exampleList = "hello, world ,this, is a, ,example";
exampleList = exampleList.listItemTrim();
writeOutput( examplelist );

```

Result: hello,world,this,is a,,example

### Keep empty items in the list

Trims each item in the list and keep empty items.

<a href="https://try.boxlang.io/?code=eJwty8EJgDAQRNG7VQw5RZgOxAIEwYsNCC64sEFJNmj5Knr9vC%2FXkg6TUYujR9jEbCfOPdsK%2BqaF0IKFACmfDV1zZnWZqh%2FVI%2Bx5B5c0Z00RP3ojERgIz1XQou2aG%2F08I%2B4%3D" target="_blank">Run Example</a>

```java
exampleList = "hello, world ,this, is a,  ,,example";
writeOutput( listItemTrim( examplelist, ",", true ) );

```

Result: hello,world,this,is a,,,example

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVzUEKwjAUBNB9TjFklcLHHKC4EFQo1FW8gJa%2FCCRNSH6qx9e2bpzNrOaNtXA%2B5sC4vB9rq1fxwqlJbmIQfJVBON6LjwbatepBGE8OIAptYiYi4SpEGh26XlmLG8cnF1zbPIlPs6pSxq%2BDIzQNhC2EkBbeidXS%2FX58bjEb%2FBaHv%2FuN%2FwBaHzbn" target="_blank">Run Example</a>

```java
// Simple Example
writeoutput( listItemTrim( "Susi , LAS  ,,boxlang,,,test,," ) );
// Member Function
strList = ",I,      , love,boxlang  ,,";
writeDump( strList.listItemTrim() );

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
  * [ListLen](./ListLen.md)
  * [ListRest](./ListRest.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListEvery](./ListEvery.md)
  * [ListEach](./ListEach.md)
  * [ListSort](./ListSort.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListFilter](./ListFilter.md)
  * [GetToken](./GetToken.md)
