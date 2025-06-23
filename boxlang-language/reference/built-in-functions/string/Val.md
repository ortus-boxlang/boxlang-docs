[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Val`

Converts numeric characters and the first period found that occur at the beginning of a string to a number.

A period not accompianied by at least
 one numeric digit will be ignored. If no numeric digits are found at the start of the string, zero will be returned.

## Method Signature

```
Val(string=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to parse |  |

## Examples

### Numeric characters at beginning and middle of a string



<a href="https://try.boxlang.io/?code=eJwrS8zRUFAyNDIoSS0uMTQqLi4pysxLV1LQtOYCAHXFCB4%3D" target="_blank">Run Example</a>

```java
val( "120test12sstring" );

```

Result: 120

### Numeric characters only at the end of a string



<a href="https://try.boxlang.io/?code=eJwrS8zRUFAqLinKzEu3tFBS0LTmAgA9cAVm" target="_blank">Run Example</a>

```java
val( "string98" );

```

Result: 0

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FAIS8zRUFAyNDI2UfBNzMxTCC7RU1LQVNC0VtDXVwAJc6UgqYMp0QFLIRQaoKgCyumZmJqhmAMSQFGEUzOSNhSJ%2FLxUPBaGwC3kgtrIBQBiHjMQ" target="_blank">Run Example</a>

```java
dump( Val( "1234 Main St." ) ); // 1234
dump( Val( "Main St., 1234" ) ); // 0
dump( Val( "123.456" ) ); // 123.456
dump( Val( "" ) ); // 0
dump( Val( "1" ) ); // 1
dump( Val( "one" ) ); // 0
dump( Val( "123T456" ) );
 // 123

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
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
