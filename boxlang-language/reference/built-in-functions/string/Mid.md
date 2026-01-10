[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Mid`

Extract a substring from a string

## Method Signature

```
Mid(string=[string], start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to extract from |  |
| `start` | `integer` | `true` | The position of the first character to retrieve. |  |
| `count` | `integer` | `false` | The number of characters to retrieve. |  |

## Examples

### Extract month from date

Grabs the month out of a raw date yyyymmdd value.

<a href="https://try.boxlang.io/?code=eJzLzUzRUFAyMjAwMDQ0MlLSUVAyBRFGSgqa1lwAXLcFZA%3D%3D" target="_blank">Run Example</a>

```java
mid( "20001122", "5", "2" );

```

Result: 11

### Additional Examples

<a href="https://try.boxlang.io/?code=eJw9zMEKgkAQBuD7PsWfJ4UlLwWBdOtgYPoMuTvBHFZldsbw7QOjvgf4sgquKO7o5pXQWSBCJllJisa9hZUG08W0ROJYIqt4XDzOqFA1rq7xoDSS4GVTUJ4nl79hyxgtxs2j50CIz%2B3wC2%2BWln067uXpv30AG6wqdQ%3D%3D" target="_blank">Run Example</a>

```java
str = "I Love Boxlang server";
writeOutput( mid( str, 8, 5 ) );
// Member function
str = "Hi buddy, Nice day!";
writeDump( str.mid( 4, 5 ) );

```



## Related

  * [Ascii](./Ascii.md)
  * [CamelCase](./CamelCase.md)
  * [Char](./Char.md)
  * [CharsetDecode](./CharsetDecode.md)
  * [CharsetEncode](./CharsetEncode.md)
  * [Compare](./Compare.md)
  * [CompareNoCase](./CompareNoCase.md)
  * [Find](./Find.md)
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
