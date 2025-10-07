[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListSort`

Sorts a delimited list and returns the result

## Method Signature

```
ListSort(list=[string], sortType=[any], sortOrder=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], localeSensitive=[boolean], callback=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to sort |  |
| `sortType` | `any` | `false` | Options are text, numeric, or textnocase |  |
| `sortOrder` | `string` | `false` | Options are asc or desc | `asc` |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |
| `localeSensitive` | `boolean` | `false` | Sort based on local rules | `false` |
| `callback` | `any` | `false` | Optional function to use for sorting - if the sort type is a closure, it will be recognized as a callback |  |

## Examples

### Simple example for listSort function

Uses the listSort() function to get the list which sorted by type text(case-sensitive)

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUHL293FxCw329PfTSc7PSUkrLc7Mz9NJTMlPStXxKU12ddUJcvT08Vey5irOLyrxgejKAVLBQK4GmKWjoBSSWlGiBKRTUouTlRQ0rbnKizJLUv1LSwpKgYrgOoESADo9JvA%3D" target="_blank">Run Example</a>

```java
list = "BOXLANG,boxlang,adobe,Boxlang,RAILO";
sortList = listSort( list, "Text", "desc" );
writeOutput( sortList );

```

Result: boxlang,adobe,RAILO,Boxlang,BOXLANG 

### Example for listSort function with delimiters

Uses the listSort() function with delimiters to get the list which sorted by type numeric

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUDI0sDYysNa1tLQ2MbM2NVCy5irOLyrxgcjmAKlgIFcDzNJRUPIrzU0tykxWAjITi8GUtZKCpjVXeVFmSap%2FaUlBKVAt3ACgBAAFZx6i" target="_blank">Run Example</a>

```java
list = "10;20;-99;46;50";
sortList = listSort( list, "Numeric", "asc", ";" );
writeOutput( sortList );

```

Result: -99;10;20;46;50

### Simple Example for listSort function using sortType(textnocase)

Uses the listSort() function with delimiters to get the list which sorted by type textnocase(case-insensitive)

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUDI0qAlydampTPXxyS%2Bv0TUyMatJL0pNzavxD0rMS09VsuYqzi8q8YGozgFSwUCuBpilo6AUklpR4pfvnFicqgTkJRYng6gaJQVNa67yosySVP%2FSkoJSoHK4GUAJAMBvJ%2Bs%3D" target="_blank">Run Example</a>

```java
list = "10|RED|yeLLow|-246|green|ORange";
sortList = listSort( list, "TextNoCase", "asc", "|" );
writeOutput( sortList );

```

Result: -246|10|green|ORange|RED|yeLLow

### Additional Examples

<a href="https://try.boxlang.io/?code=eJylkMsKwjAQRfd%2BxZCVwmiIWF34AB8IQtVF8QPadIRC20ge6OebWEVRBMFFkgvhzrl3ysLYnatIFxKmwAbYFUPso4iwG%2BEIhWDj1lkXlvbOnpxtQ%2BkNRum7ulsRWN0o5mVqJIMOdN6cbJLpWTjs4%2Bs5lM1zlRGXqsyPzhSq5rGTRFxEPJ4nYbqliw1vTuZG43%2By8MnCMrBC%2BRdWrWRq6OdenMOWqow0HF0trZ%2FaMlbHHhr2eyuDS09cN0QPwuSQbNBnWdBj2StXndrgfSFsL1xJk%2FhboCvvopB%2F" target="_blank">Run Example</a>

```java
listNumeric = "4,-16,2,15,-5,7,11";
writeOutput( listsort( listNumeric, "numeric", "asc" ) );
writeOutput( "<br><br>" );
writeOutput( listsort( "Adobe/boxlang/Boxlang/15/LAS", "text", "desc", "/" ) );
writeOutput( "<br><br>" );
writeOutput( listsort( "Adobe,boxlang,boxlang,15,LAS", "textnocase", "asc" ) );
writeOutput( "<br><br>" );
// Member function
strList = "Boxlang,Boxlang,LAS,SUSI,AdoBe";
writeDump( strlist.listSort( "textnocase", "asc" ) );

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
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
