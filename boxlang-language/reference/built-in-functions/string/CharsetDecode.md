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

  * [Ascii](./Ascii.md)
  * [CamelCase](./CamelCase.md)
  * [Char](./Char.md)
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
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
