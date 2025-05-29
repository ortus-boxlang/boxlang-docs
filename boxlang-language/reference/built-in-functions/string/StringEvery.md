[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringEvery`

Tests a string that all elements meet the specified criteria

## Method Signature

```
StringEvery(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Predicate` | `true` | The callback to use for the test |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `true` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

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
  * [CharsetEncode](./CharsetEncode.md)
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
