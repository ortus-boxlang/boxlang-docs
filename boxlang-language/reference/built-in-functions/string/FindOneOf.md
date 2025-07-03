# FindOneOf

Finds the first occurrence of any character in a set of characters, from a specified start position.

## Method Signature

```
FindOneOf(set=[string], string=[string], start=[integer])
```

### Arguments

| Argument | Type      | Required | Description                                                             | Default |
| -------- | --------- | -------- | ----------------------------------------------------------------------- | ------- |
| `set`    | `string`  | `true`   | The set of characters to search for the first occurrence of.            |         |
| `string` | `string`  | `true`   | The string to search in.                                                |         |
| `start`  | `integer` | `false`  | The position from which to start searching in the string. Default is 1. | `1`     |

## Examples

### Find first instance starting from beginning of string.

We're not passing a start index in this example.

[Run Example](https://try.boxlang.io/?code=eJxdjTEKgDAQBHtfsaRSED8gviGF9hI00YN4htyJ%2BHtjK2wxOyysaCbeZj1n8S4vOwaYaffIjhglY%2FoguBgFR8H4fFbLIsVSpTN9dWdSby9Nl9YIxKtlb0MNQ2xayP%2BhQdNXLxoZKWs%3D)

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "in", string_to_search ) );

```

Result: 7

### Find first instance starting from the twelfth character.

Let's pass in a starting index of 12. The search will start at the twelfth character, just before the word 'Spain'.

[Run Example](https://try.boxlang.io/?code=eJwrLinKzEuPL8mPL05NLErOULBVUArJSFUoSszMUwCi4AIQIy0xJ6dYIRfIzKkEiZYAVRTkALnFekrWXOVFmSWp%2FqUlBaUlGgppmXkp%2Fnmp%2FmkaCkqZeUo6CsVoNugoGBopaCpoWnMBAMInKho%3D)

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "in", string_to_search, 12 ) );

```

Result: 16

### Example showing this function will search all characters from the 'set' argument in the 'string' argument.

This function is case-sensitive so 't' does NOT match the first 'T'. It's the same for 'H' NOT matching the first 'h'. But 'e' matches the 'e' at the third position.\
Since this is the first match, this is the index that is returned.

[Run Example](https://try.boxlang.io/?code=eJxdjbEKgDAQQ3e%2FInRSEMFZ3N066C5Fr1qotfROxL%2B3rkKGl0cgLMmFbZZzZjJp2dFDTTshGReQM8YPrPGecWT0z2clL6LPlRvVFXdyQvqSeEkJ68KqA2lbQslAqgb%2FLmq0qFB1xQvBgioy)

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "tHe", string_to_search, 1 ) );

```

Result: 3

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxLKc0t0FBwy8xL8c9L9U%2FTUFBKVNIBEgoQmASBSgqaCprWXCkYipNIUZyMWzEApfYixg%3D%3D)

```java
dump( FindOneOf( "a", "a a a a b b b b" ) );
dump( FindOneOf( "b", "a a a a b b b b" ) );
dump( FindOneOf( "c", "a a a a b b b b" ) );

```

## Related

* [Ascii](Ascii.md)
* [CamelCase](CamelCase.md)
* [Char](Char.md)
* [CharsetDecode](CharsetDecode.md)
* [CharsetEncode](CharsetEncode.md)
* [Compare](Compare.md)
* [CompareNoCase](CompareNoCase.md)
* [Find](Find.md)
* [FindNoCase](FindNoCase.md)
* [Insert](Insert.md)
* [JSStringFormat](JSStringFormat.md)
* [KebabCase](KebabCase.md)
* [LCase](LCase.md)
* [Left](Left.md)
* [ListReduce](ListReduce.md)
* [LJustify](LJustify.md)
* [LTrim](LTrim.md)
* [Mid](Mid.md)
* [ParagraphFormat](ParagraphFormat.md)
* [PascalCase](PascalCase.md)
* [QueryStringToStruct](QueryStringToStruct.md)
* [ReEscape](ReEscape.md)
* [ReFind](ReFind.md)
* [reFindNoCase](reFindNoCase.md)
* [ReMatch](ReMatch.md)
* [reMatchNoCase](reMatchNoCase.md)
* [RemoveChars](RemoveChars.md)
* [RepeatString](RepeatString.md)
* [Replace](Replace.md)
* [ReplaceList](ReplaceList.md)
* [ReplaceListNoCase](ReplaceListNoCase.md)
* [ReplaceNoCase](ReplaceNoCase.md)
* [ReReplace](ReReplace.md)
* [reReplaceNoCase](reReplaceNoCase.md)
* [Reverse](Reverse.md)
* [Right](Right.md)
* [RJustify](RJustify.md)
* [RTrim](RTrim.md)
* [Slugify](Slugify.md)
* [SnakeCase](SnakeCase.md)
* [SpanExcluding](SpanExcluding.md)
* [SpanIncluding](SpanIncluding.md)
* [SQLPrettify](SQLPrettify.md)
* [StringBind](StringBind.md)
* [StringEach](StringEach.md)
* [StringEvery](StringEvery.md)
* [StringFilter](StringFilter.md)
* [StringMap](StringMap.md)
* [StringReduce](StringReduce.md)
* [StringReduceRight](StringReduceRight.md)
* [StringSome](StringSome.md)
* [StringSort](StringSort.md)
* [StripCR](StripCR.md)
* [Trim](Trim.md)
* [TrueFalseFormat](TrueFalseFormat.md)
* [UCase](UCase.md)
* [UCFirst](UCFirst.md)
* [Val](Val.md)
* [Wrap](Wrap.md)
* [YesNoFormat](YesNoFormat.md)
