[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Find`

Finds the first occurrence of a substring in a string, from a specified start position.

## Method Signature

```
Find(substring=[string], string=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The string you are looking for. |  |
| `string` | `string` | `true` | The string to search in. |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io?code=eJxLy8xL8ct3TixO1VBQKlbSUVBKyq%2FIScxL18svKiktTsrPzy7WS87PBcoYKGhaAwB9TA9L" target="_blank">Run Example</a>

```java
findNoCase( "s", "boxlang.ortusbooks.com", 0 );

```

Result: 13

### Additional Examples

<a href="https://try.boxlang.io?code=eJxNjbEKwkAQRPv7imGrBILRTghWFmKhFvoDF7PRg%2BRWLnuen%2B8lINgMzDAzLwWnfIn6ilqgd747y95OXIBugZkq0CFIgj4ZmoMKV%2FvmxSYJQ0coUTaoa2zWJuuJx5YD%2Bujv6sSbSQN2oCMGybNWPoP1D2pM%2Bsfm0mpGZ%2Bivsdya%2BXdrvvX3Mv4%3D" target="_blank">Run Example</a>

```java
writeOutput( findNoCase( "Tree", "Grow the tree, Save the world" ) ); // 10
// Member function
str = "I love boxlang";
writeOutput( str.find( "boxlang" ) );
 // 8

```

## Related

  * [SpanIncluding](./SpanIncluding.md)
  * [ReFind](./ReFind.md)
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
