[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringFilter`

Filters all the elements in a string according to a specified callback

## Method Signature

```
StringFilter(list=[string], filter=[function:Predicate], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `filter` | `function:Predicate` | `true` |  |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `true` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

## Examples

### Full function

Return only the letters in the string that meet the callback condition.

<a href="https://try.boxlang.io/?code=eJzLSS0pSS0qVrBVUKqqCgyMUrLmSk7MyUlKTM4GimkoOOZVKmTmFShoKtjaKVRzcRallpQW5YGFbEF6gOprrbny83Iqo0CGBJcUZealu2XmAA3VUMiBGK6jADdS05qrvCizJNW%2FtKSgtERDAaoRKAwAnFYr7w%3D%3D" target="_blank">Run Example</a>

```java
letters = "zzQQZ";
callback = ( Any inp ) => {
	return inp == "z";
};
onlyZs = StringFilter( letters, callback );
writeOutput( onlyZs );

```

Result: zzZ

### Member function

Return only the letters in the string that meet the callback condition.


```java
letters = "zzQQZ";
callback = ( Any inp ) => {
	return inp == "z";
};
onlyZs = letters.filter( callback );
writeOutput( onlyZs );

```

Result: zzZ

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyNjTEKAjEQRWtziiFVAjZbhwiK7D0yMUhwzC6TCYuIdzfiWm1j%2Bz7%2FPUoiiSt40AExXk7aqRiIMMTb2EqUPJU%2BGjiWB%2BQyNwEL%2FgBPteMkjcsKfRdg%2F76c4lQbdQJVOJfrmKkXDNC3tIeN3jq1cJZ0bvfZwHq3P9GwMWmcUP%2FpGT70DSRqTHU%3D" target="_blank">Run Example</a>

```java
letters = "abbcdB";
callbackFunction = ( Any input ) => {
	return input == "b";
};
result = stringFilter( letters, callbackFunction );
writeDump( result );
result1 = stringFilter( "bob", callbackFunction );
writeDump( result1 );

```



## Related

  * [SpanIncluding](./SpanIncluding.md)
  * [ReFind](./ReFind.md)
  * [reFindNoCase](./reFindNoCase.md)
  * [KebabCase](./KebabCase.md)
  * [Ascii](./Ascii.md)
  * [Val](./Val.md)
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
  * [StringSome](./StringSome.md)
  * [SQLPrettify](./SQLPrettify.md)
  * [StringMap](./StringMap.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
