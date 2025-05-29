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
