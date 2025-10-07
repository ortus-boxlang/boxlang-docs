[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CharsetEncode`

Encodes a binary string representation to an encoded string

## Method Signature

```
CharsetEncode(binary=[byte[]], encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `binary` | `byte[]` | `true` | The binary data to encode to a string |  |
| `encoding` | `string` | `false` | The charset encoding to use (default: utf-8 ) | `utf-8` |

## Examples

### Encode a string using utf-8 back into binary encoding of the string

Use charsetEncode to Encode with utf-8

<a href="https://try.boxlang.io/?code=eJwrVrBVSM5ILCpOLXFJTc5PSdVQUCouKcrMS1fSUVAqLUnTtVBS0LTmgqpxzYOoKUaRBAAFghTZ" target="_blank">Run Example</a>

```java
s = charsetDecode( "string", "utf-8" );
charsetEncode( s, "utf-8" );

```

Result: string

### Encode a string using us-ascii back into binary encoding of the string

Use charsetEncode to Encode with us-ascii

<a href="https://try.boxlang.io/?code=eJwrVrBVSM5ILCpOLXFJTc5PSdVQUCouKcrMS1fSUVAqLdZNLE7OzFRS0LTmgipzzYMoK0aXBwClexet" target="_blank">Run Example</a>

```java
s = charsetDecode( "string", "us-ascii" );
charsetEncode( s, "us-ascii" );

```

Result: string

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLSU3OT0lNUbBVcM5ILCpOLXEBC2goKHkqJOYqJCoUlxRl5qXrKekoKJWWpOlaKCloWnOllOYWaMB0uOZBdKRAjEJSCFKqoK%2BPZpYSFwBvKCLr" target="_blank">Run Example</a>

```java
decoded = CharsetDecode( "I am a string.", "utf-8" );
dump( CharsetEncode( decoded, "utf-8" ) );
 // "I am a string"

```



## Related

  * [Ascii](./Ascii.md)
  * [CamelCase](./CamelCase.md)
  * [Char](./Char.md)
  * [CharsetDecode](./CharsetDecode.md)
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
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
