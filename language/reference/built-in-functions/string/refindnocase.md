# reFindNoCase

Uses a regular expression (RE) to search a string for a pattern, starting from a specified position.

## Method Signature

```
reFindNoCase(reg_expression=[string], string=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
```

### Arguments

| Argument               | Type      | Required | Description                                                                                                          | Default |
| ---------------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------- | ------- |
| `reg_expression`       | `string`  | `true`   | The regular expression to search for                                                                                 |         |
| `string`               | `string`  | `true`   | The string to serach in                                                                                              |         |
| `start`                | `integer` | `false`  | The position from which to start searching in the string. Default is 1.                                              | 1       |
| `returnSubExpressions` | `boolean` | `false`  | True: if the regular expression is found, the first array element contains the length and position, respectively, of |         |

```
                            the first match. If the regular expression contains parentheses that group subexpressions, each subsequent array
                            element contains the length and position, respectively, of the first occurrence of each group. If the regular
                            expression is not found, the arrays each contain one element with the value 0. False: the function returns the
                            position in the string where the match begins. Default. | false|
```

| `scope` | `string` | `false` | "one": returns the first value that matches the regex. "all": returns all values that match the regex. | one |
| ------- | -------- | ------- | ------------------------------------------------------------------------------------------------------ | --- |

## Examples

```
reFindNoCase(reg_expression=[string], string=[string], start=[integer], returnSubExpressions=[boolean], scope=[string])
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
