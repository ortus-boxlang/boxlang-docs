# StringEach

Iterates all the elements in a string and runs the passed callback on each character

## Method Signature

```
StringEach(list=[string], callback=[function:Consumer], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean], parallel=[boolean], maxThreads=[integer], ordered=[boolean])
```

### Arguments

| Argument                  | Type                | Required | Description             | Default |
| ------------------------- | ------------------- | -------- | ----------------------- | ------- |
| `list`                    | `string`            | `true`   |                         |         |
| `callback`                | `function:Consumer` | `true`   | The callback to execute |         |
| `delimiter`               | `string`            | `false`  |                         | `,`     |
| `includeEmptyFields`      | `boolean`           | `false`  |                         | `false` |
| `multiCharacterDelimiter` | `boolean`           | `false`  |                         | `true`  |
| `parallel`                | `boolean`           | `false`  |                         | `false` |
| `maxThreads`              | `integer`           | `false`  |                         |         |
| `ordered`                 | `boolean`           | `false`  |                         | `false` |

## Examples

## Related

* [Ascii](ascii.md)
* [CamelCase](camelcase.md)
* [Char](char.md)
* [CharsetDecode](charsetdecode.md)
* [CharsetEncode](charsetencode.md)
* [Compare](compare.md)
* [CompareNoCase](comparenocase.md)
* [Find](find.md)
* [FindNoCase](findnocase.md)
* [FindOneOf](findoneof.md)
* [Insert](insert.md)
* [JSStringFormat](jsstringformat.md)
* [KebabCase](kebabcase.md)
* [LCase](lcase.md)
* [Left](left.md)
* [ListReduce](listreduce.md)
* [LJustify](ljustify.md)
* [LTrim](ltrim.md)
* [Mid](mid.md)
* [ParagraphFormat](paragraphformat.md)
* [PascalCase](pascalcase.md)
* [QueryStringToStruct](querystringtostruct.md)
* [ReEscape](reescape.md)
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
* [Slugify](slugify.md)
* [SnakeCase](snakecase.md)
* [SpanExcluding](spanexcluding.md)
* [SpanIncluding](spanincluding.md)
* [SQLPrettify](sqlprettify.md)
* [StringBind](stringbind.md)
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
