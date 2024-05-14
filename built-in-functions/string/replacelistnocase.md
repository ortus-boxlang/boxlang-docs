# ReplaceListNoCase

Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

## Method Signature

```
ReplaceListNoCase(string=[string], list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])
```

### Arguments

| Argument             | Type      | Required   | Description                                         | Default   |
| -------------------- | --------- | ---------- | --------------------------------------------------- | --------- |
| `string`             | `string`  | `true`     | The string to operate on                            |           |
| `list1`              | `string`  | `true`     | The first delimited list of search values           |           |
| `list2`              | `string`  | `true`     | The second delimited list of replacement values     |           |
| `delimiter_list1`    | `string`  | `false`    | The delimiters for list 1                           | ,         |
| `delimiter_list2`    | `string`  | `false`    | The delimiters for list 2                           | ,         |
| `includeEmptyFields` | `boolean` | `false`    | Whether to include empty fields in the final result | false     |
| ----------           | ------    | ---------- | -------------                                       | --------- |

## Examples

```
ReplaceListNoCase(string=[string], list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])
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
* [ListReduce](listreduce.md)
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
