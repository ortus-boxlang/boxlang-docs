[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListChangeDelims`

Converts the delimiters of a list to the new delimiter.

## Method Signature

```
ListChangeDelims(list=[string], newDelimiter=[string], delimiter=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to convert the delimiters. |  |
| `newDelimiter` | `string` | `true` | string the new list delimiter |  |
| `delimiter` | `string` | `false` | string the old list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |

## Examples

### Simple Example

Changes the delimiters in the list

<a href="https://try.boxlang.io/?code=eJzLySwucc5IzEtPdUnNycwt1lBQSsvP10lKLNLJyS9KzdXJLCguzVXSUVCqUVLQtOYCAKkAD9E%3D" target="_blank">Run Example</a>

```java
listChangeDelims( "foo,bar,lorem,ipsum", "|" );

```

Result: foo|bar|lorem|ipsum

### Example with Custom Delimiter

Changes the delimiters in the list using a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLySwucc5IzEtPdUnNycwt1lBQSsvP10lKLKrJyS9KzdXJLCguza3JTa0pzs9NLcnIzEtX0lFQqgMRNUoKmtZcADvdFsc%3D" target="_blank">Run Example</a>

```java
listChangeDelims( "foo,bar|lorem,ipsum|me|something", "~", "|" );

```

Result: foo,bar~lorem,ipsum~me~something

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxlzssKwjAUhOF9n2LIqiXB4GVXBMEuKwo%2BQaxHG0jSkpzY19dSceN64P9Ga1ytHx3hkUPHdgjFFC3TOfOYuURrEx97E57UkLM%2BlRAXZwKrZyQKKpkXKTKRe6EgDgIVqrrQGifyN4q%2FKCbLPbqcePC4z6WPEYvEsU2MPcRabuRW7kS98E32Y4llXrn%2FD3rm5Jd7A5D0P3A%3D" target="_blank">Run Example</a>

```java
// Simple function
writeOutput( ListChangeDelims( "Plant,green,save,earth", "@" ) );
// Member function with custom delimiter
strLst = "1+2+3+4";
writeDump( strLst.listChangeDelims( "/", "+" ) );

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAppend](./ListAppend.md)
  * [ListAvg](./ListAvg.md)
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
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
