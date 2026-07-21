[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `RemoveChars`

Removes characters from a string.

## Method Signature

```
RemoveChars(string=[string], start=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to remove characters from. |  |
| `start` | `integer` | `true` | The one-based index position of the first character to remove. |  |
| `count` | `integer` | `true` | The number of characters to remove. |  |

## Examples

### Remove a string



<a href="https://try.boxlang.io/?code=eJwrSs3NL0t1zkgsKtZQUPJIzcnJV3B28%2FVRCM8vyklR0lEw01EwVdC05gIAIHwL%2Bw%3D%3D" target="_blank">Run Example</a>

```java
removeChars( "Hello BL World", 6, 5 );

```

Result: Hello World

### Additional Examples

<a href="https://try.boxlang.io?code=eJxtjskKwjAYhO95ijGnFkprT4rFiwvUgw%2BRNr8aaJKSJl3e3iCiCB7mNMs3k1OeTkH3CRxpO9LxIdyQgNcKTZByWWWoxUgQMKolSLHkPEO5jtoiRVqhKHCee2o9Sdjg%2B%2BB3%2BLRZdK%2BkG3K4BdN6ZQ0bvMMe%2FIIu8nCwcyfMnVds%2Bn6JkfznT5lh88Kxv7z3CHsCnS9Beg%3D%3D" target="_blank">Run Example</a>

```java
writeDump( removeChars( "Hi buddy!, Have a nice day.", 10, 18 ) ); // Expected output: Hi buddy!
// Member function
str = "I love Boxlang";
writeDump( str.removeChars( 1, 7 ) );
 // Expected output: Boxlang

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
  * [Mid](./Mid.md)
  * [ParagraphFormat](./ParagraphFormat.md)
  * [PascalCase](./PascalCase.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [ReEscape](./ReEscape.md)
  * [ReFind](./ReFind.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [ReMatch](./ReMatch.md)
  * [reMatchNoCase](./reMatchNoCase.md)
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
  * [StringEndsWith](./StringEndsWith.md)
  * [StringEndsWithNoCase](./StringEndsWithNoCase.md)
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [StringStartsWith](./StringStartsWith.md)
  * [StringStartsWithNoCase](./StringStartsWithNoCase.md)
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
