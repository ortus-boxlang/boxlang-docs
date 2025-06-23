[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ReReplace`

Uses a regular expression (regex) to search a string for a string pattern and replace it with another.

The search is case-sensitive.

## Method Signature

```
ReReplace(string=[string], regex=[string], substring=[string], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to search |  |
| `regex` | `string` | `true` | The regular expression to search for |  |
| `substring` | `string` | `true` | The string to replace regex with |  |
| `scope` | `string` | `true` | The scope to search in (one, all) | `one` |

## Examples

### Strip Characters Using ReReplace

This example strips out all characters except a-z and 0-9.

<a href="https://try.boxlang.io/?code=eJwrSg1KLchJTE71y3dOLE7VUFAqSS0uUTA0MlZU0lFQio5L1K0y0LWMBXFA2NHHR0lB05oLAOdQDrs%3D" target="_blank">Run Example</a>

```java
reReplaceNoCase( "test 123!", "[^a-z0-9]", "", "ALL" );

```

Result: test123

### Extract Characters Using Back Reference

Uses a back reference: \1 to extract the pattern contained within the parenthesis.

<a href="https://try.boxlang.io/?code=eJwrSg1KLchJTE71y3dOLE7VUFAyNDJOTEo2MTVT0lFQijbQtYzV1ohO1K2K1daE8EDiMYZKCprWXAA%2B8RAd" target="_blank">Run Example</a>

```java
reReplaceNoCase( "123abc456", "[0-9]+([a-z]+)[0-9]+", "\1" );

```

Result: abc

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUAhyDUotyElMTvXLd04sTtVQUKqoSExKhhJKOgpKjk7OIColNU1JQVNB05qrHJ9uZ0cnxyDXEJAO5xonEOUONsTHhxjdyYlJiUWpJSAd0Y66UbGk6vdUyMkvS1XISvXxyUwtBmnMSs3J0aisAfI0Qdzk%2FPxskAzxZnkBDagkaBIAfCJliw%3D%3D" target="_blank">Run Example</a>

```java
writeDump( REReplaceNoCase( "xxabcxxabcxx", "ABC", "def" ) );
writeDump( REReplaceNoCase( "CABARET", "C|B", "G", "ALL" ) );
writeDump( REReplaceNoCase( "cabaret", "[A-Z]", "G", "ALL" ) );
writeDump( REReplaceNoCase( "I love jeLLies", "jell(y|ies)", "cookies" ) );
writeDump( REReplaceNoCase( "I love Jelly", "jell(y|ies)", "cookies" ) );

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
