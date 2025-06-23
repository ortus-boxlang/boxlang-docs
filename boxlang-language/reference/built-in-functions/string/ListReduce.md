[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListReduce`

Run the provided udf over a delimited list to reduce the values to a single output

## Method Signature

```
ListReduce(list=[string], callback=[function:BiFunction], initialValue=[any], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | The delimited list to perform operations on |  |
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java BiFunction which will only receive the ffirst 2 args. |  |
| `initialValue` | `any` | `false` | The initial value of the reduction |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxVjc8KgkAYxM%2F5FMN6MfoO2v8whZ4giOieudWCrrK7nxHRu7dml24z85thNNeFNBYZREJTmtGcFrSkFa1pQ0ks0sBy7WmlrDvIki8ygh42hAg7%2FURrZKcatqdzxZK%2BUddLjJHleAUjIx0b%2Fd%2FDZCilwZsQY5wGD6Oc3LNr2UUQx7tE%2F9xc4bws1U05i%2FB3HUJ543m4LUwu%2BvkHSig%2B6w%3D%3D" target="_blank">Run Example</a>

```java
numbers = "1,2,3,4,5,6,7,8,9,10";
sum = listReduce( numbers, ( Any previousValue, Any value ) => {
	return previousValue + value;
}, 0 );
writeOutput( "The sum of the digits #numbers# is #sum#<br>" );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVjsEKwjAQRM%2FmK4b00mIOioiH0oJfIIh4V7tqoE1LslsR8d9NW0G8zT4eO%2BOkOZMPKKCXZmXWZqNz5amSC1XHUx15bQPvR5DCTbZBiq17ovPU21ZCFIXMiPohIkNR4qVmnli8%2B%2Fcwn6RcvQ0WyHL18JZpJ9wJp9CHOyFIg%2FYKjrGyN8sBybc6gY3Hb2Cihw8fC7FAew%3D%3D" target="_blank">Run Example</a>

```java
numbers = "1,3,5,7";
reducedVal = listReduce( numbers, ( Any previousValue, Any value ) => {
	return previousValue + value;
}, 0 );
writeOutput( "The sum of the digits #numbers# is #reducedVal#" );

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
