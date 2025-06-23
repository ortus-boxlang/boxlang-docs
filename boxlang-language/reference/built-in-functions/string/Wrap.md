[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Wrap`

Wraps a string at the specified limit, breaking at the last space within the limit.

## Method Signature

```
Wrap(string=[string], limit=[integer], strip=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to wrap. |  |
| `limit` | `integer` | `true` | The character limit at which to wrap the string. |  |
| `strip` | `boolean` | `false` | If true, replaces all line endings with spaces before wrapping. Default is false. | `false` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJwrTs0rSc1LTlWwVVAKycgsVgCiRIXiksS8lMSiFIViqLSekjVXeVFiQUFqSjBCB0hEA65GR8FcQROkLLMk1b%2B0pKC0REMBXQ9QHgDmUSdM" target="_blank">Run Example</a>

```java
sentence = "This is a standard sentence.";
wrappedSentence = wrap( sentence, 7 );
writeOutput( wrappedSentence );

```

Result: This is a standar d senten ce.

### Tag Syntax




```java
<bx:set sentence = "This is a standard sentence." >
<bx:set wrappedSentence = wrap( sentence, 7 ) >
<bx:output>#wrappedSentence#</bx:output>
```

Result: This is a standar d senten ce.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxFjksLwjAQhO%2F%2BiiEHacEXXn2AV8GrV0nbNVnYJiFZLf33tnrwNMyDj5EY3KNo5uBwgrlA2HldDzQLujHYnluUNnPSeSM2uJd1hGfMUE%2B43m%2BTWgUF2wiVb5ht4g4dvUli6iko4hOF%2ByQEjfATXEaUmDwX5dYqdRiogU1JZssxlI05LKj1sYI5pkxngyWGCVxB%2Fp9X2O9QT405bn%2Bj%2BrD4AN3XSNI%3D" target="_blank">Run Example</a>

```java
long_string = "A light-weight dynamic scripting language for the JVM that enables the rapid development of simple to highly sophisticated web applications.";
echo( "<pre>" & wrap( long_string, 20 ) & "</pre>" );

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
  * [YesNoFormat](./YesNoFormat.md)
