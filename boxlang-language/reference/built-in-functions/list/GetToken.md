[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetToken`

Determines whether a token of the list in the delimiters parameter is present in a string.

Returns the token found at position index of the string, as a string.
 If index is greater than the number of tokens in the string, returns an empty string.

## Method Signature

```
GetToken(string=[string], index=[integer], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | string list to filter entries from |  |
| `index` | `integer` | `true` | numeric the one-based index position to retrieve the value at |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |

## Examples

### Tag Syntax

In the following example, the function call requests element number 2 from the string, using the delimiter '[:;".' 


```java
<bx:output>
<bx:set mystring = "four," & char( 32 ) & char( 9 ) & char( 10 ) & ",five, nine,zero:;" & char( 10 ) & "nine,ten:, eleven:;twelve:;thirteen," & char( 32 ) & char( 9 ) & char( 10 ) & ",four" >
getToken(mystring, 3) is : #getToken( mystring, 3 )#
</bx:output>
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwryc9OzYsvSS0uUbBVcE8tCQHxNRSUKlNzcvLLdYpSU6x08osS89JTdZJySlOtrHVyEstS81JSi3QKMvOyrayVdBSMdBSUrJQUNK25yosyS1JdSnMLNBRKEAYDJQA3yCIW" target="_blank">Run Example</a>

```java
token_test = GetToken( "yellow,red:,orange,blue:;,lavender,pink:;", 2, ":" );
writeDump( token_test );

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
  * [ListItemTrim](./ListItemTrim.md)
