[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StripCR`

Deletes return characters from a string.

## Method Signature

```
StripCR(string=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string or variable that contains the text. |  |

## Examples

### Removing carriage returns (cr) from a string

<a href="https://try.boxlang.io/?code=eJyrULBVUHJUUlBTSM5ILNJQMDRW0ARylJxQhay5KoEKi0uKMguSgUIVIJHyosyS1PzSkoLSEg0FJf%2BizPTMvMQcKwWQzgqQGQo%2BqXnpJRlWCso5qXlgTco2SUV2Spiag0EGF6SmQDRXYtFcCdQM1ggAdOswPQ%3D%3D" target="_blank">Run Example</a>

```java
x = "A" & char( 13 ) & "B" & char( 13 );
y = stripcr( x );
writeoutput( "Original: " & x & " Length: #len( x )#<br>" );
writeoutput( "Stripped: " & y & " Length: #len( y )#" );

```

### Additional Examples

<a href="https://try.boxlang.io?code=eJwrLilSsFVQ8lTIyS9LVUjKr8hJzEtXUlBTSM5ILNJQMDRW0LTmKkotBioqLinKLHAGCgIZINHyosySVJfS3AINBZACVJGc1DyoQmwSYPVACQCfTCao" target="_blank">Run Example</a>

```java
str = "I love boxlang" & char( 13 );
res = stripCr( str );
writeDump( res );
writeDump( len( str ) );
writeDump( len( res ) );

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
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [Trim](./Trim.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
