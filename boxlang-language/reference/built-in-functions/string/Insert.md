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
