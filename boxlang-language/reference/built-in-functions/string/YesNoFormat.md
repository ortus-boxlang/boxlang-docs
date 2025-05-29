[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `YesNoFormat`

Return Yes/No based on whether the input is true/false

## Method Signature

```
YesNoFormat(value=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `boolean` | `true` | The value to check for true/false and return Yes/No |  |

## Examples

### Example of Yes

Pass in a true value outputs Yes

<a href="https://try.boxlang.io/?code=eJyrTC32y3fLL8pNLNFQKCkqTVXQtOYCAFcYBw4%3D" target="_blank">Run Example</a>

```java
yesNoFormat( true );

```

Result: Yes

### Example of No

Pass in a false value outputs No

<a href="https://try.boxlang.io/?code=eJyrTC32y3fLL8pNLNFQSEvMKU5V0LTmAgBeoAdZ" target="_blank">Run Example</a>

```java
yesNoFormat( false );

```

Result: No

### Example of empty string

Pass in an empty string outputs No


```java
yesNoFormat( "" );

```

Result: No

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FCoTC3Oy3fLL8pNLNFQSEvMKU5V0FTQtFbQ11fwy%2BdKwVRTUlSKUBKZWoxNjQEBMwwJGaDkl69EwAwloFaIGi6YQQC0bj5j" target="_blank">Run Example</a>

```java
dump( yesnoFormat( false ) ); // No
dump( yesnoFormat( true ) ); // Yes
dump( yesnoFormat( 0 ) ); // No
dump( yesnoFormat( 1 ) ); // Yes
dump( yesnoFormat( "No" ) ); // No
dump( yesnoFormat( "Yes" ) );
 // Yes

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
