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
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
