[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListRemoveDuplicates`

De-duplicates a delimited list - either case-sensitively or case-insenstively

## Method Signature

```
ListRemoveDuplicates(list=[string], delimiter=[string], ignoreCase=[boolean], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to deduplicate |  |
| `delimiter` | `string` | `false` | The delimiter of the list | `,` |
| `ignoreCase` | `boolean` | `false` | Whether case should be ignored or not during deduplication - defaults to false | `false` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |

## Examples

### Basic usage (case-sensitive)

Basic usage. Optional arguments left as defaults.

<a href="https://try.boxlang.io/?code=eJzLySwuCUrNzS9LdSktyMlMTixJLdZQUMrPS9UpKc%2FXKckoSk3VScsvLdJJyyxL1QGJgxlgCSUFTWsuAESpF6U%3D" target="_blank">Run Example</a>

```java
listRemoveDuplicates( "one,two,three,four,five,one,five,three" );

```

Result: one,two,three,four,five

### Optional arguments usage (ignore case = true)

Optional arguments being set. Ignore case set to true

<a href="https://try.boxlang.io/?code=eJzLySwuCUrNzS9LdSktyMlMTixJLdZQUMrPS9UpKc%2FXKckoSk3VScsvLdJJyyxL1fH3c9UJCffXCfEIcnVV0lFQ0gESJUWlqQqa1lwAH%2BQYvQ%3D%3D" target="_blank">Run Example</a>

```java
listRemoveDuplicates( "one,two,three,four,five,ONE,TWO,THREE", ",", true );

```

Result: one,two,three,four,five

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtjjEKwzAMRfecQnhqwJADJO3UsVNvUGIRG5TI2HJ9%2FSgmdAjdpPefPqIscAczf8SuXDJax4s9tpmrXViH7BFjQxqZsaspCHKRWOQGpOf9hZnJp4c58DDAhhUoqFWDeHAlUtAqzJBw5S%2B6jtoDL1XejTx%2Fyv%2F2k%2B3vsj9X" target="_blank">Run Example</a>

```java
lst = "cat,mouse,dog,cat,cow,goat,sheep,cat,dog";
writeoutput( lst );
writeoutput( "<hr>" );
// new list with duplicates removed
lst = ListRemoveDuplicates( lst );
writeoutput( lst );

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
  * [ListRest](./ListRest.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
