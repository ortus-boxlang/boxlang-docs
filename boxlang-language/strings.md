---
description: Strings in BoxLang/Java are immutable! Remember that well!
---

# Strings

In BoxLang, strings are a type of variable that is used to store collections of letters and numbers. Usually defined within single or double quotes ( `'` or `"` ). Some simple strings would be `"hello"` or `"This sentence is a string!"`. Strings can be anything from `""`, the empty string, to long sets of text.

The underlying type for a string in BoxLang is the Java [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html), which is immutable, meaning it can never change. Thus, a new string object is always created when concatenating strings together. This is a warning that if you do many string concatenations, you will have to use a Java data type to accelerate the concatenations ([String Builders](https://www.baeldung.com/java-string-builder-string-buffer)).

{% hint style="info" %}
More on String Builders: [https://www.baeldung.com/java-string-builder-string-buffer](https://www.baeldung.com/java-string-builder-string-buffer)
{% endhint %}

## Character Extractions

You can reference characters in a string stream via their position in the string using array syntax: `varname[ position ]`. Please note that string and array positions in BoxLang start at 1 and not 0.

```javascript
name = "luis";
writeoutput( name[ 1 ] ) => will produce l
```

You can use negative indices to get characters from the end backward:

```javascript
name = "luis";
writeoutput( name[ -1 ] ) => will produce s
```

## Character Extractions by Range

BoxLang also supports extraction as ranges using the following array syntax:

```javascript
array[ start:stop:step ]
```

Which is extremely useful for doing character extractions in ranges

```javascript
 data = "Hello BoxLang. You Rock!";

 writeOutput( data[ 1 ] ) // Returns H
 writeOutput( data[ -3 ] ) // Returns c
 writeOutput( data[ 4:10:2 ] ) // Returns l FL
 writeOutput( data[ 4:12 ] ) // Returns lo BoxLang
 writeOutput( data[ -10:-4:2]) // Returns o o
```

## Common String Functions

You can find all the available string functions here: [https://boxlang.ortusbooks.com/boxlang-language/reference/types/string](https://boxlang.ortusbooks.com/boxlang-language/reference/types/string). Below are some common ones that are handy to memorize:

### Len

Call `len()` on a string to get back the number of characters in the string. For instance `Len( "Hello ")` would give you back **6** (notice the trailing space is counted). You can also use member functions: `a.len()`. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/type/len](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/type/len)

```javascript
message = "Hola Luis"
writeOutput( message.len() )

if( len( message ) ){

}
```

### Trim, LTrim, RTrim

The`Trim` function removes leading and trailing spaces and controls characters from a string. You can also use the `ltrim()` to do left trimming and `rtrim()` to do right trimming. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/trim](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/trim)

For instance, `Trim("Hello ")` would give you back `Hello` (notice the trailing space is removed). Combine this with `Len` for example `Len( Trim( "Hello ") )` and you would get back `5`. You can also use member functions:

```javascript
a.trim().len()
```

### Replace, ReplaceNoCase, REReplace, REReplaceNoCase

The `Replace` instruction replaces occurrences of **substring1** in a string with **substring2**, in a specified scope. The search is case-sensitive and the scoped default is one. If you would like the searches to be case-insensitive just use the `noCase()` suffix. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/replace](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/replace)

For instance, `Replace("Hello", "l", "")` would give you back **Helo** after replacing the _first occurrence of l_, or `Replace("Good Morning!", "o", "e", "All")` would give you **Geed Merning!**

`REReplace(), REReplaceNoCase()` are the same functions but using regular expressions:

```javascript
reReplace( "test 123!", "[^a-z0-9]", "", "ALL" )
reReplace( "123abc456", "[0-9]+([a-z]+)[0-9]+", "\1" )
```

### RemoveChars

`RemoveChars` will remove characters from a string. For instance, `RemoveChars("hello bob", 2, 5)` would give you back **hbob**. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/removechars](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/removechars)

### Mid

The `mid` function extracts a substring from a string. For instance, I could call `Mid("Welcome to BoxLang Jumpstart", 4, 12)` and it would give you back: **come to BoxLang**. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/mid](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/string/mid)

```javascript
s = "20001122"
writedump( mid( s, 5, 2 ) )
// You can also use character extraction
writedump( s[ 5:6 ] )
```

### ListToArray

Another great function is `listToArray()` which can take any string and convert it to an array according to a delimiter, empty fields, and even multi-character delimiters. The default delimiter is a comma `,`, but you can use any one or a combination of characters. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/list/listtoarray](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/list/listtoarray)

```javascript
a = "luis,majano,lucas,alexia,veronica";
myArray = a.listToArray();

// Multi-character delimiter
list = "boxlang,php,|test,java,|sql";
getArray = listToArray(list,",|",false,true);
someJSON = serializeJSON(getArray);
writeOutput(someJSON);
```

## Combining Strings

Combining and interpolating strings is part of any programming language and an integral part. We can do both by building upon some language [operators](operators.md). If you have two or more strings, you can concatenate them by using the `&` operator:

```javascript
name = "Luis";
a = "Hello " & name & " how are you today?";
```

You can also concatenate and assign using the `&=` operator. Please [check out the operators](operators.md#assignment-operators) section for more on string assignment operators.

## Interpolating Strings

Interpolating is where we stick a string within another string. In BoxLang, we use the `#` hashes to output a variable to the stream in context. This means we can interpolate into any string:

```javascript
name = "luis";
welcome = "Good morning #name#, how are you today?";
writeoutput( welcome );
```

That's it! If you surround any **simple** variable with hashes, BoxLang will interpret the variable. Now try this with a complex variable and see what happens:

```javascript
complex = [1,2,3];
welcome = "Good morning #complex#, how are you today (#now()#)?";
writeoutput( welcome );
```

{% hint style="success" %}
Please note that anything between hashes is interpreted as an expression in BoxLang.
{% endhint %}

## Casting

BoxLang also will try to automatically infer and auto-cast strings for you. However, there is a built-in function called `toString()` which can be used to try to convert any value to a string.

```javascript
s = {
    "a": "1",
    "b":"2"
};
writeOutput( toString(s) )
writeOutput( s.toString() )

number = 42222.222
writedump( number.toString() )
```
