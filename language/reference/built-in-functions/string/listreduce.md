# ListReduce

Run the provided udf over a delimited list to reduce the values to a single output

## Method Signature

```
ListReduce(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments

| Argument                  | Type       | Required   | Description                                                                                                     | Default   |
| ------------------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| `list`                    | `string`   | `true`     | The delimited list to perform operations on                                                                     |           |
| `callback`                | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |           |
| `initialValue`            | `any`      | `false`    | The initial value of the reduction                                                                              |           |
| `delimiter`               | `string`   | `false`    | string the list delimiter                                                                                       | ,         |
| `includeEmptyFields`      | `boolean`  | `false`    | boolean whether to include empty fields in the returned result                                                  | false     |
| `multiCharacterDelimiter` | `boolean`  | `false`    | boolean whether the delimiter is multi-character                                                                | true      |
| ----------                | ------     | ---------- | -------------                                                                                                   | --------- |

## Examples

```
ListReduce(list=[string], callback=[function], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

## Related

* [Ascii](ascii.md)
* [Char](char.md)
* [CharsetDecode](charsetdecode.md)
* [CharsetEncode](charsetencode.md)
* [Compare](compare.md)
* [CompareNoCase](comparenocase.md)
* [Find](find.md)
* [FindNoCase](findnocase.md)
* [FindOneOf](findoneof.md)
* [Insert](insert.md)
* [LCase](lcase.md)
* [Left](left.md)
* [LJustify](ljustify.md)
* [LTrim](ltrim.md)
* [Mid](mid.md)
* [ParagraphFormat](paragraphformat.md)
* [QueryStringToStruct](querystringtostruct.md)
* [ReFind](refind.md)
* [reFindNoCase](refindnocase.md)
* [ReMatch](rematch.md)
* [reMatchNoCase](rematchnocase.md)
* [RemoveChars](removechars.md)
* [RepeatString](repeatstring.md)
* [Replace](replace.md)
* [ReplaceList](replacelist.md)
* [ReplaceListNoCase](replacelistnocase.md)
* [ReplaceNoCase](replacenocase.md)
* [ReReplace](rereplace.md)
* [reReplaceNoCase](rereplacenocase.md)
* [Reverse](reverse.md)
* [Right](right.md)
* [RJustify](rjustify.md)
* [RTrim](rtrim.md)
* [SpanExcluding](spanexcluding.md)
* [SpanIncluding](spanincluding.md)
* [StringEach](stringeach.md)
* [StringEvery](stringevery.md)
* [StringFilter](stringfilter.md)
* [StringMap](stringmap.md)
* [StringReduce](stringreduce.md)
* [StringReduceRight](stringreduceright.md)
* [StringSome](stringsome.md)
* [StringSort](stringsort.md)
* [StripCR](stripcr.md)
* [Trim](trim.md)
* [TrueFalseFormat](truefalseformat.md)
* [UCase](ucase.md)
* [UCFirst](ucfirst.md)
* [Val](val.md)
* [Wrap](wrap.md)
* [YesNoFormat](yesnoformat.md)
