[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ReFind`

Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

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

```
ReFind(reg_expression=[string], string=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
```

## Related
  * [Ascii](boxlang-language/reference/built-in-functions/Ascii.md)
  * [Char](boxlang-language/reference/built-in-functions/Char.md)
  * [CharsetDecode](boxlang-language/reference/built-in-functions/CharsetDecode.md)
  * [CharsetEncode](boxlang-language/reference/built-in-functions/CharsetEncode.md)
  * [Compare](boxlang-language/reference/built-in-functions/Compare.md)
  * [CompareNoCase](boxlang-language/reference/built-in-functions/CompareNoCase.md)
  * [Find](boxlang-language/reference/built-in-functions/Find.md)
  * [FindNoCase](boxlang-language/reference/built-in-functions/FindNoCase.md)
  * [FindOneOf](boxlang-language/reference/built-in-functions/FindOneOf.md)
  * [Insert](boxlang-language/reference/built-in-functions/Insert.md)
  * [LCase](boxlang-language/reference/built-in-functions/LCase.md)
  * [Left](boxlang-language/reference/built-in-functions/Left.md)
  * [ListReduce](boxlang-language/reference/built-in-functions/ListReduce.md)
  * [LJustify](boxlang-language/reference/built-in-functions/LJustify.md)
  * [LTrim](boxlang-language/reference/built-in-functions/LTrim.md)
  * [Mid](boxlang-language/reference/built-in-functions/Mid.md)
  * [ParagraphFormat](boxlang-language/reference/built-in-functions/ParagraphFormat.md)
  * [QueryStringToStruct](boxlang-language/reference/built-in-functions/QueryStringToStruct.md)
  * [reFindNoCase](boxlang-language/reference/built-in-functions/reFindNoCase.md)
  * [ReMatch](boxlang-language/reference/built-in-functions/ReMatch.md)
  * [reMatchNoCase](boxlang-language/reference/built-in-functions/reMatchNoCase.md)
  * [RemoveChars](boxlang-language/reference/built-in-functions/RemoveChars.md)
  * [RepeatString](boxlang-language/reference/built-in-functions/RepeatString.md)
  * [Replace](boxlang-language/reference/built-in-functions/Replace.md)
  * [ReplaceList](boxlang-language/reference/built-in-functions/ReplaceList.md)
  * [ReplaceListNoCase](boxlang-language/reference/built-in-functions/ReplaceListNoCase.md)
  * [ReplaceNoCase](boxlang-language/reference/built-in-functions/ReplaceNoCase.md)
  * [ReReplace](boxlang-language/reference/built-in-functions/ReReplace.md)
  * [reReplaceNoCase](boxlang-language/reference/built-in-functions/reReplaceNoCase.md)
  * [Reverse](boxlang-language/reference/built-in-functions/Reverse.md)
  * [Right](boxlang-language/reference/built-in-functions/Right.md)
  * [RJustify](boxlang-language/reference/built-in-functions/RJustify.md)
  * [RTrim](boxlang-language/reference/built-in-functions/RTrim.md)
  * [SpanExcluding](boxlang-language/reference/built-in-functions/SpanExcluding.md)
  * [SpanIncluding](boxlang-language/reference/built-in-functions/SpanIncluding.md)
  * [StringEach](boxlang-language/reference/built-in-functions/StringEach.md)
  * [StringEvery](boxlang-language/reference/built-in-functions/StringEvery.md)
  * [StringFilter](boxlang-language/reference/built-in-functions/StringFilter.md)
  * [StringMap](boxlang-language/reference/built-in-functions/StringMap.md)
  * [StringReduce](boxlang-language/reference/built-in-functions/StringReduce.md)
  * [StringReduceRight](boxlang-language/reference/built-in-functions/StringReduceRight.md)
  * [StringSome](boxlang-language/reference/built-in-functions/StringSome.md)
  * [StringSort](boxlang-language/reference/built-in-functions/StringSort.md)
  * [StripCR](boxlang-language/reference/built-in-functions/StripCR.md)
  * [Trim](boxlang-language/reference/built-in-functions/Trim.md)
  * [TrueFalseFormat](boxlang-language/reference/built-in-functions/TrueFalseFormat.md)
  * [UCase](boxlang-language/reference/built-in-functions/UCase.md)
  * [UCFirst](boxlang-language/reference/built-in-functions/UCFirst.md)
  * [Val](boxlang-language/reference/built-in-functions/Val.md)
  * [Wrap](boxlang-language/reference/built-in-functions/Wrap.md)
  * [YesNoFormat](boxlang-language/reference/built-in-functions/YesNoFormat.md)
