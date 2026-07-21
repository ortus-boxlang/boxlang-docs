[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Trim`

Trim whitespace from the beginning and end of a string.

If chars is provided, each character in the string is treated as a character to trim instead of whitespace.

## Method Signature

```
Trim(string=[string], chars=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to trim |  |
| `chars` | `string` | `false` | An optional string of characters to trim. Each character is treated individually. |  |

## Examples

### Trim



<a href="https://try.boxlang.io/?code=eJxTslNSUFMoKcrM1VBQUgACZzeX%2FORiEEtJQRMopWSjZM0FAKIqB7c%3D" target="_blank">Run Example</a>

```java
">" & trim( "    BLDocs    " ) & "<";

```

Result: >BLDocs<

### Additional Examples

<a href="https://try.boxlang.io/?code=eJx9jrEOwjAMRPd%2BxZGhageUD0BsDHwAErNpXRopbSrHafl8SAYYQGznO93zWYtOmJSxkji6ecbmdAQhqrj5jjBA%2BaHQkRQjRXimPgc091Ah5%2FMRF%2Bo4VkMIOMLgzN4HXIP4fgeYQ2UtQtIl6ftNtYlTPqVpaWD2BjVyuS66%2FVUou17e3wFf0Iu4qSno9gN%2FAm76TtY%3D" target="_blank">Run Example</a>

```java
// create variable with a string of text that has leading and trailing spaces
foo = " Hello World!  ";
// output variable
writeDump( "-" & foo & "-" );
// output variable without leading and trailing spaces
writeDump( "-" & Trim( foo ) & "-" );

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
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
