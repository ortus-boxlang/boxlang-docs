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
