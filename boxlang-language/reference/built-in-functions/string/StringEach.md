[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringEach`

Iterates all the elements in a string and runs the passed callback on each character

## Method Signature

```
StringEach(list=[string], callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Consumer` | `true` | The callback to execute |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `any` | `false` |  |  |
| `ordered` | `boolean` | `false` |  | `false` |
| `virtual` | `boolean` | `false` |  | `false` |

## Examples

### Full function



<a href="https://try.boxlang.io/?code=eJzLSS0pSS0qVrBVUErMKCyvUrLmSk7MyUlKTM4GimkoOOZVKmTmFShoKtjaKVRzcZYXZZak5peWFJSWaIAlbIE6C5UUNK25aq25gkuKMvPSXROTMzQUciAm6yjAzQOqAQCnTSKs" target="_blank">Run Example</a>

```java
letters = "ahqwz";
callback = ( Any inp ) => {
	writeoutput( inp == "q" );
};
StringEach( letters, callback );

```

Result: NONOYESNONO

### Member function




```java
letters = "ahqwz";
letters.each( ( Any inp ) => {
	writeoutput( inp == "q" );
} );

```

Result: NONOYESNONO

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLzCsoLQkuKcrMS1ewVVBKTEpOUbLmKgYLuCYmZ2goZCJU6ChoKDjmVSqUJeYoaCrY2ilUc3GWF2WWpOaXlgAVaYAlbIHGJCspaFpz1YIIADyIHkE%3D" target="_blank">Run Example</a>

```java
inputString = "abcd";
stringEach( inputString, ( Any val ) => {
	writeoutput( val == "c" );
} );

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
  * [StringEndsWith](./StringEndsWith.md)
  * [StringEndsWithNoCase](./StringEndsWithNoCase.md)
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [StringStartsWith](./StringStartsWith.md)
  * [StringStartsWithNoCase](./StringStartsWithNoCase.md)
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
