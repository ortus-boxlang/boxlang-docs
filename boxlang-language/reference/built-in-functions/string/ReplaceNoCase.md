[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ReplaceNoCase`

Replaces occurrences of substring1 in a string with obj, in a specified scope.

The search is case-sensitive. Function returns original string with
 replacements made

## Method Signature

```
ReplaceNoCase(string=[string], substring1=[string], obj=[any], scope=[string], start=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to search |  |
| `substring1` | `string` | `true` | The substring to search for |  |
| `obj` | `any` | `true` | The string to replace substring1 with |  |
| `scope` | `string` | `true` | The scope to search in | `one` |
| `start` | `string` | `false` |  | `1` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxLTy0JS8xRsFUoSi3ISUxO9ct3TixO1VBQcs7PSXELLc7Mz1PSUVAqBRGJSgqa1lzlRZklqS6luQUaCukQzUBBADcDFdY%3D" target="_blank">Run Example</a>

```java
getVal = replaceNoCase( "Boxlang", "u", "a" );
writeDump( getVal );

```

Result: Expected Result: Boxlang

### Tag Syntax

<a href="https://try.boxlang.io?code=eJxLSEiwSaqwKk4tUUhPLQlLzFGwVShKLchJTE71y3dOLE7VUFByyq%2FIScxLV9JRUPIHEYkgwtHHR0lBU8GOC6Q9pTS3QKEsschWSRliirKSHVdCQgIAdZUcFA%3D%3D" target="_blank">Run Example</a>


```java
<bx:set getVal = replaceNoCase( "Boxlang", "O", "a", "ALL" ) >
<bx:dump var="#getVal#">
```

Result: Expected Result: Boxlang

### Additional Examples


```java
writeDump( replaceNoCase( "xxabcxxabcxx", "ABC", "def" ) );
writeDump( replaceNoCase( "xxabcxxabcxx", "abc", "def", "All" ) );
writeDump( replaceNoCase( "xxabcxxabcxx", "AbC", "def", "hans" ) );
writeDump( replaceNoCase( "a.b.c.d", ".", "-", "all" ) );
test = "camelcase CaMeLcAsE CAMELCASE";
test2 = replaceNoCase( test, "camelcase", "CamelCase", "all" );
writeDump( test2 );
writeDump( var=replaceNoCase( "One string, two strings, Three strings", {
	"one" : 1,
	"Two" : 2,
	"three" : 3,
	"string" : "txt",
	"text" : "string"
} ), label="replaceNoCase via a struct" );
 // struct keys need to be quoted

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
  * [Justify](./Justify.md)
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
  * [StringEndsWith](./StringEndsWith.md)
  * [StringEndsWithNoCase](./StringEndsWithNoCase.md)
  * [StringEvery](./StringEvery.md)
  * [StringFilter](./StringFilter.md)
  * [StringMap](./StringMap.md)
  * [StringReduce](./StringReduce.md)
  * [StringReduceRight](./StringReduceRight.md)
  * [StringSome](./StringSome.md)
  * [StringSort](./StringSort.md)
  * [StringStartsWith](./StringStartsWith.md)
  * [StringStartsWithNoCase](./StringStartsWithNoCase.md)
  * [StripCR](./StripCR.md)
  * [Trim](./Trim.md)
  * [UCase](./UCase.md)
  * [UCFirst](./UCFirst.md)
  * [Val](./Val.md)
  * [Wrap](./Wrap.md)
  * [YesNoFormat](./YesNoFormat.md)
