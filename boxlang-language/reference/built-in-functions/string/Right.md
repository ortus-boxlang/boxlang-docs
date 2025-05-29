[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Right`

Extract the rightmost count characters from a string

## Method Signature

```
Right(string=[string], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to extract from |  |
| `count` | `integer` | `true` | The number of characters to retrieve. |  |

## Examples

### Using right() on a string

In this example we'll use right() to return part of a string.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQKMpMzwBSSiEZqQqFpZnJ2QpJRfnleQpp%2BRUKWaW5BakpCvllqUUKJUD5nMSqSoWU%2FHQlHQULBU0FTWsuAAmGGTk%3D" target="_blank">Run Example</a>

```java
writeOutput( right( "The quick brown fox jumped over the lazy dog", 8 ) );

```

Result: lazy dog

### Using right() with a negative count on a string

In this example we'll use a negative count right() to return part of a string. CF2018+

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQKMpMzwBSSiEZqQqFpZnJ2QpJRfnleQpp%2BRUKWaW5BakpCvllqUUKJUD5nMSqSoWU%2FHQlHQVdYyMFTQVNay4APN0Zkw%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( right( "The quick brown fox jumped over the lazy dog", -32 ) );

```

Result: the lazy dog

### Using right() in a function

In this example we'll use right() in a function to help us to capitalize the last letter in a string.

<a href="https://try.boxlang.io/?code=eJxtjLEKAkEMBWv3K1KJBypYW4qd5RXXxjW3BtZ4ZhMQxX83FjZi84ph5qXJj5UzNFOWAqNLNr4KZJzYsPKDDthsAUo3Z6XTVzS6G3TwTDMlcxWoNIaGWvxCYm3d74d%2BGVR%2BYVQr2MTOwXfYKL65nP%2B0H6fbpld6A7RHNk4%3D" target="_blank">Run Example</a>

```java

public string function capitalizeLast( required string text ) {
	return left( arguments.TEXT, len( arguments.TEXT ) - 1 ) & uCase( right( arguments.TEXT, 1 ) );
}

```


### Using right() to test values

In this example we'll use right() to test the last five characters of a request context variable.


```java
if( listFindNoCase( "super,great,coder,rulez", right( rc.ANSWER, 5 ) ) ) {
	writeOutput( "You are an awesome developer!" );
}

```


### Using right() as a member function

 In this example we'll use right() as a member function inside a function to help us to capitalize the last letter in a string.

<a href="https://try.boxlang.io/?code=eJxly6EOQjEMhWHNnqKKbIIlaDQOeQW2jN7RZJRL1yYEwrszgwF7%2FvOFxU%2BNC3RTlgqzSzG%2BCRRc2LDxkw7YLYLS3Vnp%2FD0aPQwSvMJKyVwFUKtfSaznaX%2BccqN5qL9RYoINbIdc%2F0blehlktOwFO8W0C%2B%2FwAf%2FtNg4%3D" target="_blank">Run Example</a>

```java

public string function capitalizeLast( required string text ) {
	return arguments.TEXT.left( arguments.TEXT.len() - 1 ) & arguments.TEXT.right( 1 ).ucase();
}

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJx1jcsKwjAQRff5iktWLZQGFFfFnQguXPkFtUxNII8ymejvm%2FoAN%2B4OF849xiC7sHjCscRJXIrqwU7oUMLSgN3NSgN9gk93gi8Tke6wQ4t2gDHvRVU4U7gSY%2F6eZGHsoS9j1YSJcoe8snczIUWIJdDIYns9%2FBar13%2Bqm%2B0ro9bOH1c9AQSvPJg%3D" target="_blank">Run Example</a>

```java
// simple Function
writeDump( right( "I love boxlang", 5 ) ); // boxlang
// Member function
str = "Save trees, save life on the earth.";
writeDump( str.right( 23 ) );
 // save life on the earth.

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
