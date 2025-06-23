[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringReduce`

Run the provided udf over all characters in a string to reduce the values to a single output

## Method Signature

```
StringReduce(list=[string], callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:BiFunction` | `true` | The callback to use for the test |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` |  | `true` |

## Examples

### Full function

Reduce the string to a single value.

<a href="https://try.boxlang.io/?code=eJzLSS0pSS0qVrBVUEpMSk5JTVOy5krOyS8uLUoFimkoOOZVKmTmFRjqwFhGCpoKtnYK1VycRaklpUV5YFkFNbCUNVetNVd5UWZJqn9pSUFpiYZCcElRZl56UGpKaXKqhkIOxDIdBagNOgpKVUpA8zStuQCLXirm" target="_blank">Run Example</a>

```java
letters = "abcdef";
closure = ( Any inp1, Any inp2 ) => {
	return inp1 & inp2;
};
writeOutput( StringReduce( letters, closure, "z" ) );

```

Result: zabcdef

### Member function

Reduce the string to a single value.


```java
letters = "abcdef";
closure = ( Any inp1, Any inp2 ) => {
	return inp1 & inp2;
};
writeOutput( letters.reduce( closure, "z" ) );

```

Result: zabcdef

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxFjcEKwjAQRM%2FuVww5SAq56DVU8AsE%2F6CmqxRClM2uYov%2FbsGAt2HmMS%2BzKktFDzdc0shXFynlezXhtfM4ljeeQzbehX%2Feo0N%2FwEIbYTUpjcC2zZE%2BkV4yKZ9MH6YeVWUqtzOPltgj%2F6QBzRTgZrd%2BdpG%2BNo4uXg%3D%3D" target="_blank">Run Example</a>

```java
letters = "abcdef";
closure = ( Any value1, Any value2 ) => {
	return value1 & value2;
};
writeOutput( stringReduce( letters, closure, "z" ) );

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
