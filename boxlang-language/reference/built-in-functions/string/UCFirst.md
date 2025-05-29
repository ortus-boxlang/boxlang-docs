[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `UCFirst`

Transform the first letter of a string to uppercase or the first letter of each word, and optionally lowercase uppercase characters.

## Method Signature

```
UCFirst(string=[string], doAll=[boolean], doLowerIfAllUppercase=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to transform. |  |
| `doAll` | `boolean` | `false` | Boolean flag indicating whether to transform the first letter of each word. | `false` |
| `doLowerIfAllUppercase` | `boolean` | `false` | Boolean flag indicating whether to lowercase uppercase characters. | `false` |

## Examples

### Basic usage

Capitalizes the first character of the first word only.

<a href="https://try.boxlang.io/?code=eJwrTXbLLCou0VBQykjNyclXKM8vyklRVFLQtOYCAIPJCHg%3D" target="_blank">Run Example</a>

```java
ucFirst( "hello world!" );

```

Result: Hello world!

### Capitalize all the words in string

Using the optional doAll parameter capitalizes the first character of all words. Word separators are: whitespace, period, parenthesis, or dash.

```java
ucFirst( "boxlang.ortusbooks.com is your (everyone's) resource for BX-related documentation!", true );

```

Result: boxlang.ortusbooks.com Is Your (everyone's) Resource For BX-related Documentation!

### Handling of strings in all uppercase

Using the optional doLowerIfAllUppercase parameter allows for intelligent capitalization of words in all caps.


```java
ucFirst( "boxlang.ortusbooks.com YOUR (EVERYONE'S) RESOURCE FOR BX-related DOCUMENTATION!", true, true );

```

Result: boxlang.ortusbooks.com Your (everyone's) Resource For BX-related Documentation!

### Additional Examples

```java
string = "submitting bugs and feature requests via our online system";
dump( UcFirst( string, false, false ) );
dump( UcFirst( string, true, false ) );

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
