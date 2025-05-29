[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringSome`

Tests whether any item in a string meets the specified callback

## Method Signature

```
StringSome(list=[string], callback=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `true` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

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
  * [SQLPrettify](./SQLPrettify.md)
  * [StringMap](./StringMap.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
