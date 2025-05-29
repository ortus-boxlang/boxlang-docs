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

  * [SpanIncluding](./SpanIncluding.md)
  * [ReFind](./ReFind.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [KebabCase](./KebabCase.md)
  * [Ascii](./Ascii.md)
  * [Val](./Val.md)
  * [StringFilter](./StringFilter.md)
  * [Compare](./Compare.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
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
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
