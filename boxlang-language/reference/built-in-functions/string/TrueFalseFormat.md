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
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
