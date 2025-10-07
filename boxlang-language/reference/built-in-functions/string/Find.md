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

  * [Ascii](./Ascii.md)
  * [CamelCase](./CamelCase.md)
  * [Char](./Char.md)
  * [CharsetDecode](./CharsetDecode.md)
  * [CharsetEncode](./CharsetEncode.md)
  * [Compare](./Compare.md)
  * [CompareNoCase](./CompareNoCase.md)
  * [FindNoCase](./FindNoCase.md)
  * [FindOneOf](./FindOneOf.md)
  * [Insert](./Insert.md)
  * [JSStringFormat](./JSStringFormat.md)
  * [Justify](./Justify.md)
  * [KebabCase](./KebabCase.md)
  * [LCase](./LCase.md)
  * [Left](./Left.md)
  * [ListReduce](./ListReduce.md)
  * [LJustify](./LJustify.md)
  * [LTrim](./LTrim.md)
  * [Mid](./Mid.md)
  * [ParagraphFormat](./ParagraphFormat.md)
  * [PascalCase](./PascalCase.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [ReEscape](./ReEscape.md)
  * [ReFind](./ReFind.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [ReMatch](./ReMatch.md)
  * [reMatchNoCase](./reMatchNoCase.md)
  * [RemoveChars](./RemoveChars.md)
  * [RepeatString](./RepeatString.md)
  * [Replace](./Replace.md)
  * [ReplaceList](./ReplaceList.md)
  * [ReplaceListNoCase](./ReplaceListNoCase.md)
  * [ReplaceNoCase](./ReplaceNoCase.md)
  * [ReReplace](./ReReplace.md)
  * [reReplaceNoCase](./reReplaceNoCase.md)
  * [Reverse](./Reverse.md)
  * [Right](./Right.md)
  * [RJustify](./RJustify.md)
  * [RTrim](./RTrim.md)
  * [Slugify](./Slugify.md)
  * [SnakeCase](./SnakeCase.md)
  * [SpanExcluding](./SpanExcluding.md)
  * [SpanIncluding](./SpanIncluding.md)
  * [SQLPrettify](./SQLPrettify.md)
  * [StringBind](./StringBind.md)
  * [StringEach](./StringEach.md)
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
