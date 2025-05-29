[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ReplaceList`

Replaces occurrences of the elements from a delimited list, in a string with corresponding elements from another delimited list.

## Method Signature

```
ReplaceList(string=[string], list1=[string], list2=[string], delimiter_list1=[string], delimiter_list2=[string], includeEmptyFields=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to operate on |  |
| `list1` | `string` | `true` | The first delimited list of search values |  |
| `list2` | `string` | `true` | The second delimited list of replacement values |  |
| `delimiter_list1` | `string` | `false` | The delimiters for list 1 | `,` |
| `delimiter_list2` | `string` | `false` | The delimiters for list 2 | `,` |
| `includeEmptyFields` | `boolean` | `false` | Whether to include empty fields in the final result | `false` |

## Examples

### Tag Example




```java
<bx:set myString = "My test string" >
<bx:set mySubstring1 = "Test, String" >
<bx:set mySubString2 = "Replaced, Sentence" >
<bx:output>#replaceListNoCase( myString, mySubstring1, mySubString2 )#</bx:output>
```

Result: My Replaced Sentence

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtjrsKwkAURPt8xXUrhSG%2BX4iFqGChFopou48bs2IS2SS6%2Fr1PsLGbGQ7DuTlb8KxMLlVyfDlLzUubF%2BtsKnOuklhY2m3nmwpoIa9MklKrmYy8hwIkYosyZ%2FeKez7rLGGo0pi7oBrVRlSv03em9%2FznJXgyK04UO4rKVBc2S4O8cDQm4b2fqKnh6Bjbk%2FcHqfTsU8QouP20n3j4T11CQcOAEeGIGBanl2gDTbTQRgdd9NDHAMOPbvAAJBRSiQ%3D%3D" target="_blank">Run Example</a>

```java
writeDump( replaceListNoCase( "Hi USER!, Have a nice day.", "hi,user", "Welcome,buddy" ) ); // Welcome buddy!, Have a nice day.
// Member function
str = "xxxAbCdefghijxxXabcDefghij";
writeDump( str.replaceListNoCase( "a,b,c,d,e,f,g,h,i,j", "0,1,2,3,4,5,6,7,8,9" ) );

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
