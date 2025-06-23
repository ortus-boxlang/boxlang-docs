[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListRest`

Returns the remainder of a list after removing the first item

## Method Signature

```
ListRest(list=[string], delimiter=[string], includeEmptyFields=[boolean], offset=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `offset` | `integer` | `false` |  | `0` |

## Examples

### Simple listRest Example

A very basic listRest example

<a href="https://try.boxlang.io/?code=eJzLySwuCUotLtFQUMrPS9UpKc%2FXKckoSk3VScsvLVJS0LTmAgDXDgtp" target="_blank">Run Example</a>

```java
listRest( "one,two,three,four" );

```

Result: two,three,four

### Combining listRest to Shorten the List

Nesting listRest shortens the list by one each time with the first element removed.

<a href="https://try.boxlang.io/?code=eJzLySwuCUotLtFQyIGzlPLzUnVKyvN1SjKKUlN10vJLi5QUNBU0rbkAh1wPVA%3D%3D" target="_blank">Run Example</a>

```java
listRest( listRest( "one,two,three,four" ) );

```

Result: three,four

### Traversing a List with listRest and listFirst

Nesting list functions lets you move through the list in pieces.

<a href="https://try.boxlang.io/?code=eJzLySwuccssKi7RUMgBMoNSUVlK%2BXmpOiXl%2BTolGUWpqTpp%2BaVFSgqaIGjNBQCDahOp" target="_blank">Run Example</a>

```java
listFirst( listRest( listRest( "one,two,three,four" ) ) );

```

Result: three

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQyMksLglKLQaylIpLijLz0nV8SpNTU3WKS4szdXwcg5UUNBXUFJRskorsQBjItebS11fwTc1NSi1SSCvNSy7JzM%2FjAur1AZqkYKugZKBjqGOkY6xjomTNVQ6yyqU0t0BDAagCZJce3EJNkFEAlXUsRQ%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( listRest( "string,Boxlang,susi,LAS" ) & "<br><br>" );
// Member function
strList = "0,1,2,3,4";
writeDump( strlist.listRest() );

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
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
