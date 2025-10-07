[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListGetEndings`

Returns the first or last item in a delimited list, according to the specified function name

## Method Signature

```
ListGetEndings(list=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `false` |

## Examples

### Simple listLast Example

A very basic listLast example

<a href="https://try.boxlang.io/?code=eJzLySwu8UksLtFQUMrPS9UpKc%2FXKckoSk3VScsvLVJS0LTmAgDV5gtf" target="_blank">Run Example</a>

```java
listLast( "one,two,three,four" );

```

Result: four

### listLast Example with multiple delimiters

A more advanced listLast example

<a href="https://try.boxlang.io/?code=eJzLySwu8UksLtFQUMrPS9UvKc%2BPKckoSk3VT8svLVLSUVCK0VdS0LTmAgAjqQyw" target="_blank">Run Example</a>

```java
listLast( "one/two\three/four", "\/" );

```

Result: four

### Additional Examples

<a href="https://try.boxlang.io/?code=eJw9jTsKwzAQRHudYlFlwxIdwKQIJIGAUukEjtlCIFlCu%2Bvk%2BFG%2B1Uwxb55zEGKuieD0mF9p7i0KFZWqMkCKLH7m3mxQjoD%2BEBCTLkSIKMRiYYRxMs7BlfKNGpx1XSSW1bA033HYg8VLh8pGP9JOH81Rcx3gO9z9Ze%2FHJ1DsMeE%3D" target="_blank">Run Example</a>

```java
// Simple Example
writeoutput( listLast( "Susi ,LAS,,boxlang,,,test" ) );
// Member Function
strList = ",I,,love,boxlang,,";
writeDump( strList.listLast() );

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
