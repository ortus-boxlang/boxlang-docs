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
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [TrueFalseFormat](./TrueFalseFormat.md)
  * [UCase](./UCase.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
