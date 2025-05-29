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
