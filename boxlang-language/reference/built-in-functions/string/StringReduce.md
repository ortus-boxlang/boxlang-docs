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
