[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringSome`

Tests whether any item in a string meets the specified callback

## Method Signature

```
StringSome(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |
| `virtual` | `boolean` | `false` |  | `false` |

## Examples

### Full function

Are any of the characters in the string greater than our condition?

<a href="https://try.boxlang.io/?code=eJw9jUEKgCAUBdd5iocrhW4gBZ2hE5hZSPUL%2BxIR3T0paDsMM4F2joFGVJC2c70fRmmEs%2FPcWTdlqtDQiUAbNKoalyii5xTpRTXkkPXbiCMG9mviLbFC%2BybbdfEqa9%2BgxB%2FV0EY8N6wmrw%3D%3D" target="_blank">Run Example</a>

```java
instring = "abcdefg";
callback = ( Any inp ) => {
	return inp > "f";
};
writeoutput( StringSome( instring, callback ) );

```

Result: YES

### Member function

Are any of the characters in the string greater than our condition?


```java
instring = "abcdefg";
callback = ( Any inp ) => {
	return inp > "f";
};
writeoutput( instring.some( callback ) );

```

Result: YES

### Additional Examples

<a href="https://try.boxlang.io?code=eJzLrQwuKcrMS1ewVVBKyq%2FIScxLV7LmSk7MyUlKTM4GimooOOZVKlQoaCrY2gEpO6C6RCVra67yosySVJfS3AINBYgJwfm5qRoKuVDzdBTgZmgqaCJMjDfEbmYVSWYCTQGZCgDNVDqs" target="_blank">Run Example</a>

```java
myString = "boxlang";
callback = ( Any x ) => x >= "a";;
writeDump( StringSome( myString, callback ) );
callback_1 = ( Any x ) => x >= "z";;
writeDump( StringSome( myString, callback_1 ) );

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
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
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
