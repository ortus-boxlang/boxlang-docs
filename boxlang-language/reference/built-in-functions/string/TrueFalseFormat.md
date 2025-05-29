[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TrueFalseFormat`

Return Yes/No based on whether the input is true/false

## Method Signature

```
TrueFalseFormat(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to check for true/false and return Yes/No |  |

## Examples

### Numeric 1 is interpreted as true



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUDBU0LTmAgBfpgcc" target="_blank">Run Example</a>

```java
trueFalseFormat( 1 );

```

Result: true

### Numeric 0 is interpreted as false



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUDBQ0LTmAgBfoQcb" target="_blank">Run Example</a>

```java
trueFalseFormat( 0 );

```

Result: false

### String representation of 1 is interpreted as true



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUFAyVFLQtOYCAG4pB2A%3D" target="_blank">Run Example</a>

```java
trueFalseFormat( "1" );

```

Result: true

### String representation of 0 is interpreted as false



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUFAyUFLQtOYCAG4jB18%3D" target="_blank">Run Example</a>

```java
trueFalseFormat( "0" );

```

Result: false

### YES is recognized as synonym for true as well



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUFCKdA1WUtC05gIAgJ4IIA%3D%3D" target="_blank">Run Example</a>

```java
trueFalseFormat( "YES" );

```

Result: true

### And NO as synonym for false



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUFDy81dS0LTmAgB3fgfM" target="_blank">Run Example</a>

```java
trueFalseFormat( "NO" );

```

Result: false

### An empty string results in false again



<a href="https://try.boxlang.io/?code=eJwrKSpNdUvMKU51yy%2FKTSzRUFBSUtC05gIAZoQHLw%3D%3D" target="_blank">Run Example</a>

```java
trueFalseFormat( "" );

```

Result: false

### Additional Examples


```java
<bx:output>
	False: #trueFalseFormat( false )#<br>
	True: #trueFalseFormat( true )#<br>
	0: #trueFalseFormat( 0 )#<br>
	1: #trueFalseFormat( 1 )#<br>
	No: #trueFalseFormat( "No" )#<br>
	Yes: #trueFalseFormat( "Yes" )#
</bx:output>
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
  * [StringMap](./StringMap.md)
  * [QueryStringToStruct](./QueryStringToStruct.md)
  * [Mid](./Mid.md)
  * [LCase](./LCase.md)
  * [ParagraphFormat](./ParagraphFormat.md)
