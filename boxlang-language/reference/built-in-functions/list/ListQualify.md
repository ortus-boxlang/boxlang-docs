[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListQualify`

Inserts a string at the beginning and end of list elements.

If this BIF is being called from inside of a query component,
 and the qualifier is a single quote, any single quotes in the values will be escaped by doubling them up.
 This protects against SQL Injection attacks.

## Method Signature

```
ListQualify(list=[string], qualifier=[string], delimiter=[string], elements=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The list to qualify. |  |
| `qualifier` | `string` | `true` | The string to insert at the beginning and end of each element. |  |
| `delimiter` | `string` | `false` | The delimiter used in the list. | `,` |
| `elements` | `string` | `false` | The elements to qualify. If set to "char", only elements that are all alphabetic characters will be qualified. | `all` |
| `includeEmptyFields` | `boolean` | `false` | If true, empty fields will be qualified. | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |

## Examples

### Simple example for listQualify function with delimiter

To insert a string or character before and after the list elements.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUErOz0lJKy3OzM%2BzKkrMzMm3MjQxscopTU5NtTIxU7LmKi%2FKLEn1Ly0pKC3RUMgBagosTczJTKuEcHQUlGqUgISVkoKmgqY1FwAAjRtV" target="_blank">Run Example</a>

```java
list = "boxlang:railo:144:boxlang:46";
writeOutput( listQualify( list, "|", ":" ) );

```

Result: |boxlang|:|railo|:|144|:|boxlang|:|46|

### Example for listQualify function with elements

To insert a string or character before and after the alphabet list elements only.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUErOz0lJKy3OzM%2BzKkrMzMm3MjQxscopTU5NtTIxU7LmKi%2FKLEn1Ly0pKC3RUMgBagosTczJTKuEcHQUlGqUgIQViHD2cAxSUtBU0LTmAgDllR0D" target="_blank">Run Example</a>

```java
list = "boxlang:railo:144:boxlang:46";
writeOutput( listQualify( list, "|", ":", "CHAR" ) );

```

Result: |boxlang|:|railo|:144:|boxlang|:46

### Example for listQualify function with includeEmptyFields

If includeEmptyFields is true, empty value add in list elements.

<a href="https://try.boxlang.io/?code=eJzLySwuUbBVUErOz0lJKy3OzM%2BzKkrMzMm3MjQxsbLKKU1OTbWyMjFTsuYqL8osSfUvLSkoLdFQyAFqCyxNzMlMq4RwdBSUapSAhBWIcPZwDALSJUWlqQqaCprWXADWtx%2BD" target="_blank">Run Example</a>

```java
list = "boxlang:railo:144::boxlang::46";
writeOutput( listQualify( list, "|", ":", "CHAR", true ) );

```

Result: |boxlang|:|railo|:144:||:|boxlang|:||:46

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVjsEKwjAMhu97itCDdDDMA0wFUQRhIlK8Cs5lGmi70bUMwYc3UxA8JOQ%2F5Pt%2BRDDsekvQJn%2BL3HkYOT6g4balQD5CQ5YdRwoa82wMch1T7FPUYHmIp3S13D41qCEG9nes0o0IhzQwVmujClCXaaGCHGagFnVYTSOxzBDhQK6m8JNnQqkEC0tQH1Kx6WyzE1rnC%2BEV5mz2qvz22CbXa5CPqcj8v81r8oniDeOFSOE%3D" target="_blank">Run Example</a>

```java
// Simple function with different delimiter(/)
writeOutput( listQualify( "string/Boxlang/susi/LAS", "^", "/" ) & "<br><br>" );
// Member function
strList = "Boxlang,Boxlang,LAS,SUSI";
writeDump( strlist.listQualify( "|" ) );

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
