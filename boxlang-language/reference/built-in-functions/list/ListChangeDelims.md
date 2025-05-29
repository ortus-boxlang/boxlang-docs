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

  * [ListSome](./ListSome.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListFirst](./ListFirst.md)
  * [ListLast](./ListLast.md)
  * [ListIndexExists](./ListIndexExists.md)
  * [ListInsertAt](./ListInsertAt.md)
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
