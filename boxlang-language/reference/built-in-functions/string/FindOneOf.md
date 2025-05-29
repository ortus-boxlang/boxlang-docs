[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FindOneOf`

Finds the first occurrence of any character in a set of characters, from a specified start position.

## Method Signature

```
FindOneOf(set=[string], string=[string], start=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `string` | `true` | The set of characters to search for the first occurrence of. |  |
| `string` | `string` | `true` | The string to search in. |  |
| `start` | `integer` | `false` | The position from which to start searching in the string. Default is 1. | `1` |

## Examples

### Find first instance starting from beginning of string.

We're not passing a start index in this example.

<a href="https://try.boxlang.io/?code=eJxdjTEKgDAQBHtfsaRSED8gviGF9hI00YN4htyJ%2BHtjK2wxOyysaCbeZj1n8S4vOwaYaffIjhglY%2FoguBgFR8H4fFbLIsVSpTN9dWdSby9Nl9YIxKtlb0MNQ2xayP%2BhQdNXLxoZKWs%3D" target="_blank">Run Example</a>

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "in", string_to_search ) );

```

Result: 7

### Find first instance starting from the twelfth character.

Let's pass in a starting index of 12. The search will start at the twelfth character, just before the word 'Spain'.

<a href="https://try.boxlang.io/?code=eJwrLinKzEuPL8mPL05NLErOULBVUArJSFUoSszMUwCi4AIQIy0xJ6dYIRfIzKkEiZYAVRTkALnFekrWXOVFmSWp%2FqUlBaUlGgppmXkp%2Fnmp%2FmkaCkqZeUo6CsVoNugoGBopaCpoWnMBAMInKho%3D" target="_blank">Run Example</a>

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "in", string_to_search, 12 ) );

```

Result: 16

### Example showing this function will search all characters from the 'set' argument in the 'string' argument.

This function is case-sensitive so 't' does NOT match the first 'T'. It's the same for 'H' NOT matching the first 'h'. But 'e' matches the 'e' at the third position.
Since this is the first match, this is the index that is returned.

<a href="https://try.boxlang.io/?code=eJxdjbEKgDAQQ3e%2FInRSEMFZ3N066C5Fr1qotfROxL%2B3rkKGl0cgLMmFbZZzZjJp2dFDTTshGReQM8YPrPGecWT0z2clL6LPlRvVFXdyQvqSeEkJ68KqA2lbQslAqgb%2FLmq0qFB1xQvBgioy" target="_blank">Run Example</a>

```java
string_to_search = "The rain in Spain falls mainly in the plains.";
writeOutput( findOneOf( "tHe", string_to_search, 1 ) );

```

Result: 3

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBwy8xL8c9L9U%2FTUFBKVNIBEgoQmASBSgqaCprWXCkYipNIUZyMWzEApfYixg%3D%3D" target="_blank">Run Example</a>

```java
dump( FindOneOf( "a", "a a a a b b b b" ) );
dump( FindOneOf( "b", "a a a a b b b b" ) );
dump( FindOneOf( "c", "a a a a b b b b" ) );

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
