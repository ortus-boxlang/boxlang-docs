[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Insert`

Inserts a substring into another string at a specified position.

## Method Signature

```
Insert(substring=[string], string=[string], position=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `substring` | `string` | `true` | The string to insert. |  |
| `string` | `string` | `true` |  |  |
| `position` | `integer` | `true` | The position at which to insert the string. |  |

## Examples

### Simple insert function example

To add substring on prefix of the given string

<a href="https://try.boxlang.io/?code=eJwrzs9NDS4pysxLV7BVUFJIzigCCigkFeWXF6cWKVlzFaUWl%2BaUAOUy84ACJRoKSu75%2Bek5qUo6CsVwrToKBgqa1lzlRZklqf6lJQWlQHVQjUBhAKORIUA%3D" target="_blank">Run Example</a>

```java
someString = " chrome browser";
result = insert( "Google", someString, 0 );
writeOutput( result );

```

Result: Google chrome browser

### Simple insert function example with position

To add substring on suffix of the given string

<a href="https://try.boxlang.io/?code=eJwrzs9NDS4pysxLV7BVUPJLLVcoKMosSyxJVcjNr8rMyUlUSMssSlWy5spJzUsvyQAqAjI0FIoR2jStucqLMktS%2FUtLCkpLNBQy84pTi4C0Ulp%2BhZIOkkodBagZmiA9ABjVKSI%3D" target="_blank">Run Example</a>

```java
someString = "New private mozilla fire";
length = len( someString );
writeOutput( insert( "fox", someString, length ) );

```

Result: New private mozilla firefox

### Additional Examples

<a href="https://try.boxlang.io?code=eJxVjbsOgkAQRfv5iputICFSWhA7LSz8CMDRbLIPMjMonw%2BY1cT2npxz1QQnuCtCfjFcR2%2Fxxuc5ThV8Uhar4Ia8hD49XQM1aXBEjbpD26JohdO23DgOLHjMaTSfE6nt%2BcvSxynwf17t8HvAmO%2Fsvmna28X5EFoBANkzHQ%3D%3D" target="_blank">Run Example</a>

```java
str = "I love ";
writeDump( insert( "boxlang", str, 7 ) ); // I love boxlang
// Member function
st = "Example";
writeDump( st.insert( " code", 7 ) );
 // Example code

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
