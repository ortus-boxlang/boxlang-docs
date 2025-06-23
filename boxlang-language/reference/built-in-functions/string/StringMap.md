[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StringMap`

Iterates over all elements in a string and returns a new mapped string

## Method Signature

```
StringMap(list=[string], callback=[function:Function], delimiter=[string], includeEmptyFields=[boolean], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` |  |  |
| `callback` | `function:Function` | `true` | The callback which returns a boolean and filters the string |  |
| `delimiter` | `string` | `false` |  | `,` |
| `includeEmptyFields` | `boolean` | `false` |  | `false` |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

## Examples

### Full function

Map each element of the string to a new value.

<a href="https://try.boxlang.io/?code=eJw1jTEKAjEQRWtzis9WE7S3CCt4ALHwBNk4rgMhhskEEfHuq6jtezxeZjPWhhFDnNKZL%2FMQXMq31pXfkLAvD0ip8Bh3eLqVsnUtSNeohNiSCP38Glv44F7B3VWMj91qN8LJVMp8iJWQv7MN%2FgP%2FCRae5Skm" target="_blank">Run Example</a>

```java
letters = "abcdefg";
closure = ( Any inp ) => {
	return char( ascii( inp ) + 7 );
};
writeOutput( StringMap( letters, closure ) );

```

Result: hijklmn

### Member function

Map each element of the string to a new value.


```java
letters = "abcdefg";
closure = ( Any inp ) => {
	return char( ascii( inp ) + 7 );
};
writeOutput( letters.map( closure ) );

```

Result: hijklmn

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLrQwuKcrMS1ewVVDySM3JyVcIzy%2FKSVGy5krOyS8uLUoFSmgoOOZVKpQl5ihoKtjaKVRzcRallpQW5SlogMTUFJQSlTStuWqtucqLMktSXUpzCzQUIKb6JgKZuVArdBRgRmoqANUDADxKJig%3D" target="_blank">Run Example</a>

```java
myString = "Hello World";
closure = ( Any val ) => {
	return (val & "a");
};
writeDump( StringMap( myString, closure ) );

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
