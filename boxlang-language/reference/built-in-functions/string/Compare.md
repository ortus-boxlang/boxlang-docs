# Compare

Performs a case-sensitive comparison of two strings.

-1, if string1 is less than string2\
0, if string1 is equal to string2\
1, if string1 is greater than string2

## Method Signature

```
Compare(string1=[any], string2=[any])
```

### Arguments

| Argument  | Type  | Required | Description                  | Default |
| --------- | ----- | -------- | ---------------------------- | ------- |
| `string1` | `any` | `true`   | The first string to compare  |         |
| `string2` | `any` | `true`   | The second string to compare |         |

## Examples

### Tag Syntax

[Run Example](https://try.boxlang.io/?code=eJxLSEjgskmqsCpOLVFIzs8tSCzKLM7PU7CFclI1FJSc8ityEvPSlXQUlJKgTAVNBTuwtpTS3AKFssQiWyVlhG5lJX07BRDgSkhIAAAqGR6x)

```java
<bx:set comparison = compare( "Boxlang", "boxlang" ) >
<bx:dump var="#comparison#"/>     
```

Result: -1

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxLKc0t0FBwzs8tSCxK1VBQMjQwUPBNzMxTCC7RU9JRUDIzN1VwTSwuUXAsS80rTVVS0FTQtFbQ11fQNeRKQdNriqbXUMG5tCC1qCQzL18hPLESoZewVhQ%2BWB8XSKMBFwC5nC4y)

```java
dump( Compare( "100 Main St.", "675 East Avenue" ) ); // -1
dump( Compare( "500 Main St.", "1 Cupertino Way" ) ); // 1
dump( Compare( "500 Main St.", "500 Main St." ) );
 // 0

```

## Related

* [Ascii](Ascii.md)
* [CamelCase](CamelCase.md)
* [Char](Char.md)
* [CharsetDecode](CharsetDecode.md)
* [CharsetEncode](CharsetEncode.md)
* [CompareNoCase](CompareNoCase.md)
* [Find](Find.md)
* [FindNoCase](FindNoCase.md)
* [FindOneOf](FindOneOf.md)
* [Insert](Insert.md)
* [JSStringFormat](JSStringFormat.md)
* [KebabCase](KebabCase.md)
* [LCase](LCase.md)
* [Left](Left.md)
* [ListReduce](ListReduce.md)
* [LJustify](LJustify.md)
* [LTrim](LTrim.md)
* [Mid](Mid.md)
* [ParagraphFormat](ParagraphFormat.md)
* [PascalCase](PascalCase.md)
* [QueryStringToStruct](QueryStringToStruct.md)
* [ReEscape](ReEscape.md)
* [ReFind](ReFind.md)
* [reFindNoCase](reFindNoCase.md)
* [ReMatch](ReMatch.md)
* [reMatchNoCase](reMatchNoCase.md)
* [RemoveChars](RemoveChars.md)
* [RepeatString](RepeatString.md)
* [Replace](Replace.md)
* [ReplaceList](ReplaceList.md)
* [ReplaceListNoCase](ReplaceListNoCase.md)
* [ReplaceNoCase](ReplaceNoCase.md)
* [ReReplace](ReReplace.md)
* [reReplaceNoCase](reReplaceNoCase.md)
* [Reverse](Reverse.md)
* [Right](Right.md)
* [RJustify](RJustify.md)
* [RTrim](RTrim.md)
* [Slugify](Slugify.md)
* [SnakeCase](SnakeCase.md)
* [SpanExcluding](SpanExcluding.md)
* [SpanIncluding](SpanIncluding.md)
* [SQLPrettify](SQLPrettify.md)
* [StringBind](StringBind.md)
* [StringEach](StringEach.md)
* [StringEvery](StringEvery.md)
* [StringFilter](StringFilter.md)
* [StringMap](StringMap.md)
* [StringReduce](StringReduce.md)
* [StringReduceRight](StringReduceRight.md)
* [StringSome](StringSome.md)
* [StringSort](StringSort.md)
* [StripCR](StripCR.md)
* [Trim](Trim.md)
* [TrueFalseFormat](TrueFalseFormat.md)
* [UCase](UCase.md)
* [UCFirst](UCFirst.md)
* [Val](Val.md)
* [Wrap](Wrap.md)
* [YesNoFormat](YesNoFormat.md)
