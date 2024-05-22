[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringMap`

Iterates over all elements in a string and returns a new mapped string

## Method Signature
```
StringMap(list=[string], callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function` | `true` | The callback which returns a boolean and filters the string |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

## Examples

```
StringMap(list=[string], callback=[function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```

## Related
  * [Ascii](./Ascii.md)
  * [Char](./Char.md)
  * [CharsetDecode](./CharsetDecode.md)
  * [CharsetEncode](./CharsetEncode.md)
  * [Compare](./Compare.md)
  * [CompareNoCase](./CompareNoCase.md)
  * [Find](./Find.md)
  * [FindNoCase](./FindNoCase.md)
  * [FindOneOf](./FindOneOf.md)
  * [Insert](./Insert.md)
  * [LCase](./LCase.md)
  * [Left](./Left.md)
  * [ListReduce](./ListReduce.md)
  * [LJustify](./LJustify.md)
  * [LTrim](./LTrim.md)
  * [Mid](./Mid.md)
  * [ParagraphFormat](./ParagraphFormat.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
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
  * [SpanExcluding](./SpanExcluding.md)
  * [SpanIncluding](./SpanIncluding.md)
  * [StringEach](./StringEach.md)
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringReduce](./StringReduce.md)
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
