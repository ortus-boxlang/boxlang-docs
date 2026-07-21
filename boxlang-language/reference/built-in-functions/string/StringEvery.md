[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringEvery`

Tests a string that all elements meet the specified criteria

## Method Signature

```
StringEvery(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Predicate` | `true` | The callback to use for the test |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `any` | `false` |  |  |
| `virtual` | `boolean` | `false` |  | `false` |

## Examples

### Full function

Do all letters in the string meet the callback condition?

<a href="https://try.boxlang.io/?code=eJzLSS0pSS0qVrBVUIqKSqyqUrLmSk7MyUlKTM4GimkoOOZVKmTmFShoKtjaKVRzcRallpQW5YGFbIF6QOprrbmAOqJAZgSXFGXmpbuWpRZVaijkQIzWUYAbqGnNVV6UWZLqX1pSUFqioQDRBhQFABXtKps%3D" target="_blank">Run Example</a>

```java
letters = "ZZazz";
callback = ( Any inp ) => {
	return inp == "z";
};
allZs = StringEvery( letters, callback );
writeOutput( allZs );

```

Result: NO

### Member function

Do all letters in the string meet the callback condition?


```java
letters = "zzZZz";
callback = ( Any inp ) => {
	return inp == "z";
};
allZs = letters.every( callback );
writeOutput( allZs );

```

Result: YES

### Additional Examples

<a href="https://try.boxlang.io?code=eJyNzcEKgkAQxvFz%2BxQfe1Lo4lkMggx8DJVBlqZRxllLondvIbvUpeuf%2BX7DZEY6o4JvwONC6MY7tzL40vUtc9f2l3OU3sIo6SjDUVYEmaIhR3XAw%2B2ULKpssUoQpe2zdEpz5FQwmwYZ6oV0zcDvh3v86HnpbhqMTvE6ZdjW%2BccpviFfE%2Fk%2FmSLVF%2BFSTpA%3D" target="_blank">Run Example</a>

```java
letters = "I love boxlang";
callbackFunction = ( Any input ) => {
	return input == "e";
};
result = stringEvery( letters, callbackFunction );
writeDump( result );
result1 = stringEvery( "Eee", callbackFunction );
writeDump( result1 );

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
  * [StringEndsWith](./StringEndsWith.md)
  * [StringEndsWithNoCase](./StringEndsWithNoCase.md)
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
