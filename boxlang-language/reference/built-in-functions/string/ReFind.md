[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ReFind`

Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

The search is case-sensitive.
 It will return numeric if returnsubexpressions is false and a struct of arrays named "len", "match" and "pos" when returnsubexpressions is true.

## Method Signature

```
ReFind(reg_expression=[string], string=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `reg_expression` | `string` | `true` | The regular expression to search for |  |
| `string` | `string` | `true` | The string to serach in |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |
| `returnSubExpressions` | `boolean` | `false` | True: if the regular expression is found, the first array element contains the length and position, respectively, of<br>                                the first match. If the regular expression contains parentheses that group subexpressions, each subsequent array<br>                                element contains the length and position, respectively, of the first occurrence of each group. If the regular<br>                                expression is not found, the arrays each contain one element with the value 0. False: the function returns the<br>                                position in the string where the match begins. Default. | `false` |
| `scope` | `string` | `false` | "one": returns the first value that matches the regex. "all": returns all values that match the regex. | `one` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJwrSnXLzEvxy3dOLE7VUFByVdJRUCpJLS5RMDQyVlRS0LTmAgC4MAkY" target="_blank">Run Example</a>

```java
reFindNoCase( "E", "test 123!" );

```

Result: 2

### Script Syntax

CF2016+ example with all optional arguments

<a href="https://try.boxlang.io/?code=eJzzCvb3C04tykzMyaxK1VAoSnXLzEvxy3dOLAbylFyVdBSUSlKLSxQMjYwVgRxDHYWSotJUoKijj4%2BSgqaCpjUXAMLsEn0%3D" target="_blank">Run Example</a>

```java
JSONSerialize( reFindNoCase( "E", "test 123!", 1, true, "ALL" ) );

```

Result: [{"len":[1],"pos":[2],"match":["e"]}]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyNjsFLwzAYxe%2F7Kz5z2Fo7Bs30siEj1HkSD2OCkOXwNY22uKYlyZj%2B937ZPGyCOkjII7z3fm%2FvmmDud22fwGr50NjqqSvQmwQYZjpjY3pLjVgUVcUghXQ%2B2P%2BVuI4JQQmhL0nIzWKonOnhDmKQVOfCRL%2B2i%2BNnzqc3wx2J2wvgsaFERPGvd3KY%2BW0LxgcfXGPf8jhjXRvQGKCxEEjWJOPV2BooUb9fsfnAh2g9llJdIkdyhtu%2BxpkaqSyVoLJkk6cEOSkfAx22Xj0v2Y91VCeBbY1loCRMQZ3P4nGWEOKFrjjQ%2BSn94wzDf8egc%2Fj5aGwEcgL2nWeRFW1fc4uWkg%3D%3D" target="_blank">Run Example</a>

```java
writeDump( REFindNoCase( "a+c+", "abcaaCCdd" ) );
writeDump( REFindNoCase( "a+c*", "AbcaAcCdd" ) );
writeDump( REFindNoCase( "[\?&]rep = ", "report.bxm?rep = 1234&u = 5" ) );
writeDump( REFindNoCase( "a+", "baaaA" ) );
writeDump( REFindNoCase( ".*", "" ) );
teststring1 = "The cat in the hat hat came back!";
st1 = REFind( "(['[:alpha:]']+)[ ]+(\1)", teststring1, 1, "TRUE" );
writeDump( st1[ "len" ][ 3 ] );
teststring2 = "AAAXAAAA";
st2 = REFind( "x", teststring2, 1, "TRUE" );
writeDump( arrayLen( st2[ "pos" ] ) );

```



## Related

  * [SpanIncluding](./SpanIncluding.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [KebabCase](./KebabCase.md)
  * [Ascii](./Ascii.md)
  * [Val](./Val.md)
  * [StringFilter](./StringFilter.md)
  * [Compare](./Compare.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
  * [ReReplace](./ReReplace.md)
  * [reReplaceNoCase](./reReplaceNoCase.md)
  * [StripCR](./StripCR.md)
  * [Insert](./Insert.md)
  * [CamelCase](./CamelCase.md)
  * [StringBind](./StringBind.md)
  * [SnakeCase](./SnakeCase.md)
  * [Right](./Right.md)
  * [FindOneOf](./FindOneOf.md)
  * [ReEscape](./ReEscape.md)
  * [SpanExcluding](./SpanExcluding.md)
  * [CompareNoCase](./CompareNoCase.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [Reverse](./Reverse.md)
  * [Replace](./Replace.md)
  * [ReplaceList](./ReplaceList.md)
  * [ReplaceListNoCase](./ReplaceListNoCase.md)
  * [StringReduce](./StringReduce.md)
  * [Slugify](./Slugify.md)
  * [Wrap](./Wrap.md)
  * [PascalCase](./PascalCase.md)
  * [StringSort](./StringSort.md)
  * [StringEach](./StringEach.md)
  * [Trim](./Trim.md)
  * [LTrim](./LTrim.md)
  * [UCFirst](./UCFirst.md)
  * [Find](./Find.md)
  * [FindNoCase](./FindNoCase.md)
  * [ReMatch](./ReMatch.md)
  * [reMatchNoCase](./reMatchNoCase.md)
  * [LJustify](./LJustify.md)
  * [RJustify](./RJustify.md)
  * [CharsetEncode](./CharsetEncode.md)
  * [StringEvery](./StringEvery.md)
  * [Left](./Left.md)
  * [UCase](./UCase.md)
  * [ListReduce](./ListReduce.md)
  * [YesNoFormat](./YesNoFormat.md)
  * [Char](./Char.md)
  * [ReplaceNoCase](./ReplaceNoCase.md)
  * [RemoveChars](./RemoveChars.md)
  * [RTrim](./RTrim.md)
  * [JSStringFormat](./JSStringFormat.md)
  * [RepeatString](./RepeatString.md)
  * [CharsetDecode](./CharsetDecode.md)
  * [StringSome](./StringSome.md)
  * [SQLPrettify](./SQLPrettify.md)
  * [StringMap](./StringMap.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
