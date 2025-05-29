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

  * [SpanIncluding](./SpanIncluding.md)
  * [ReFind](./ReFind.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [KebabCase](./KebabCase.md)
  * [Ascii](./Ascii.md)
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
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
