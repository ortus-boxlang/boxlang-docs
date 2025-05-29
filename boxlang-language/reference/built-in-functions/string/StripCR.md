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
