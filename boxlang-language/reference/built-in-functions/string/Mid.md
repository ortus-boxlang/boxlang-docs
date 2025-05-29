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
| `count` | `integer` | `true` | The number of characters to retrieve. |  |

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
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
