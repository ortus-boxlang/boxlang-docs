[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CharsetDecode`

Encodes a string to a binary representation

## Method Signature

```
CharsetDecode(encoded_binary=[string], encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `encoded_binary` | `string` | `true` | The string to encode to binary |  |
| `encoding` | `string` | `false` | The charset encoding to use (default: utf-8 ) | `utf-8` |

## Examples

### Decode a string using utf-8 back into binary encoding of the string

Use charsetDecode to decode with utf-8

<a href="https://try.boxlang.io/?code=eJxLzkgsKk4tcUlNzk9J1VBQKi4pysxLV9JRUCotSdO1UFLQtOYCAOn2CyQ%3D" target="_blank">Run Example</a>

```java
charsetDecode( "string", "utf-8" );

```

Result: [B@5d9905a6

### Decode a string using us-ascii back into binary encoding of the string

Use charsetDecode to decode with us-ascii

<a href="https://try.boxlang.io/?code=eJxLzkgsKk4tcUlNzk9J1VBQKi4pysxLV9JRUCot1k0sTs7MVFLQtOYCABNqDI4%3D" target="_blank">Run Example</a>

```java
charsetDecode( "string", "us-ascii" );

```

Result: [B@8154ffd

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBwzkgsKk4tcUlNzk9J1VBQ8lRIzFVIVCguKcrMS9dT0lFQKi1J07VQUtBU0LTmAgDDLA9R" target="_blank">Run Example</a>

```java
dump( CharsetDecode( "I am a string.", "utf-8" ) );

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
  * [RemoveChars](./RemoveChars.md)
  * [RTrim](./RTrim.md)
  * [JSStringFormat](./JSStringFormat.md)
  * [RepeatString](./RepeatString.md)
  * [StringSome](./StringSome.md)
  * [SQLPrettify](./SQLPrettify.md)
  * [StringMap](./StringMap.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
