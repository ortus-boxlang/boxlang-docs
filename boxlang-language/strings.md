---
description: Strings in BoxLang/Java are immutable! Remember that well!
icon: spell-check
---

# Strings

In BoxLang, strings are a type of variable that is used to store collections of letters and numbers. Usually defined within single or double quotes ( `'` or `"` ). Some simple strings would be `"hello"` or `"This sentence is a string!"`. Strings can be anything from `""`, the empty string, to long sets of text.

## 🔤 Java String Interoperability

The underlying type for a string in BoxLang is the native Java [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html), which is **immutable**, meaning it can never change. Thus, a new string object is always created when concatenating strings together.

{% hint style="info" %}
**Important:** Since BoxLang strings are Java strings, you have access to **all Java String methods** directly! This means you can call any method from the [Java String API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) on BoxLang strings using member function syntax.
{% endhint %}

```js
// Access Java String methods directly
text = "Hello BoxLang"
writeOutput( text.toUpperCase() )        // HELLO BOXLANG
writeOutput( text.substring(0, 5) )      // Hello
writeOutput( text.contains("Box") )      // true
writeOutput( text.startsWith("Hello") )  // true
writeOutput( text.endsWith("Lang") )     // true
writeOutput( text.indexOf("Box") )       // 6
writeOutput( text.split(" ") )           // ["Hello", "BoxLang"]
```

{% hint style="success" %}
**BoxLang 1.15.0+** ships with a first-class **`BoxStringBuilder`** type and automatic compile-time optimizations that make string-heavy code faster with no changes required. For loops and accumulators, use `BoxStringBuilder` instead of raw Java StringBuilder for a fully integrated, 1-based API.

👉 See the [StringBuilder](string-builder.md) documentation for the complete guide.
{% endhint %}

```js
// BoxLang 1.15+ — use the native BoxStringBuilder type
sb = sb{ "Items: " }
for ( i = 1; i <= 1000; i++ ) {
    sb.append( "Item #i#, " )
}
result = sb.toString()

// BoxLang also automatically uses StringBuilder under the hood
// for any string concatenation with 4 or more segments — no manual effort needed!
result = "Hello" & " " & firstName & " " & lastName & "!"
// ↑ compiled to use StringBuilder automatically
```

## 🔍 Character Extractions

You can reference characters in a string stream via their position in the string using array syntax: `varname[ position ]`. Please note that string and array positions in BoxLang start at 1 and not 0.

```javascript
name = "luis";
writeoutput( name[ 1 ] ) => will produce l
```

You can use negative indices to get characters from the end backward:

```js
name = "luis";
writeoutput( name[ -1 ] ) => will produce s
```

## 📏 Character Extractions by Range

BoxLang also supports extraction as ranges using the following array syntax:

```javascript
array[ start:stop:step ]
```

Which is extremely useful for doing character extractions in ranges

```js
data = "Hello BoxLang. You Rock!";

writeOutput( data[ 1 ] )        // Returns H
writeOutput( data[ -3 ] )       // Returns c
writeOutput( data[ 4:10:2 ] )   // Returns l FL
writeOutput( data[ 4:12 ] )     // Returns lo BoxLang
writeOutput( data[ -10:-4:2])   // Returns o o
```

[Try it online!](https://try.boxlang.io)

## 📚 String Built-In Functions (BIFs)

BoxLang provides a rich set of Built-In Functions for string manipulation. Below is an overview organized by category:

### 🔤 Case Conversion

| Function | Purpose | Example |
|----------|---------|---------|
| `uCase()` / `lCase()` | Convert to upper/lowercase | `uCase("hello")` → `"HELLO"` |
| `camelCase()` | Convert to camelCase | `camelCase("hello_world")` → `"helloWorld"` |
| `pascalCase()` | Convert to PascalCase | `pascalCase("hello_world")` → `"HelloWorld"` |
| `kebabCase()` | Convert to kebab-case | `kebabCase("helloWorld")` → `"hello-world"` |
| `snakeCase()` | Convert to snake_case | `snakeCase("helloWorld")` → `"hello_world"` |
| `ucFirst()` | Uppercase first character | `ucFirst("hello")` → `"Hello"` |

### 🔍 Search & Find

| Function | Purpose | Example |
|----------|---------|---------|
| `find()` / `findNoCase()` | Find substring position | `find("Box", "Hello BoxLang")` → `7` |
| `reFind()` / `reFindNoCase()` | Find regex pattern position | `reFind("[0-9]+", "Age: 25")` → `6` |
| `reMatch()` / `reMatchNoCase()` | Get all regex matches | `reMatch("[0-9]+", "123 and 456")` → `["123", "456"]` |
| `findOneOf()` | Find first char from set | `findOneOf("aeiou", "hello")` → `2` |
| `spanIncluding()` | Get chars in set | `spanIncluding("0123456789", "123abc")` → `"123"` |
| `spanExcluding()` | Get chars not in set | `spanExcluding("0123456789", "abc123")` → `"abc"` |

### ✂️ Extraction & Substring

| Function | Purpose | Example |
|----------|---------|---------|
| `left()` / `right()` | Get leftmost/rightmost chars | `left("Hello", 3)` → `"Hel"` |
| `mid()` | Extract substring | `mid("Hello", 2, 3)` → `"ell"` |
| `removeChars()` | Remove characters | `removeChars("Hello", 2, 2)` → `"Hlo"` |

### 🔄 Replace & Transform

| Function | Purpose | Example |
|----------|---------|---------|
| `replace()` / `replaceNoCase()` | Replace substring | `replace("Hello", "l", "L")` → `"HeLlo"` |
| `reReplace()` / `reReplaceNoCase()` | Replace with regex | `reReplace("test123", "[0-9]", "X", "ALL")` → `"testXXX"` |
| `replaceList()` / `replaceListNoCase()` | Multiple replacements | `replaceList("a,b,c", "a,c", "1,3")` → `"1,b,3"` |
| `reverse()` | Reverse string | `reverse("Hello")` → `"olleH"` |
| `insert()` | Insert substring | `insert("XXX", "Hello", 3)` → `"HelXXXlo"` |

### 🎨 Formatting & Padding

| Function | Purpose | Example |
|----------|---------|---------|
| `trim()` / `lTrim()` / `rTrim()` | Remove whitespace (or custom chars) | `trim("  hello  ")` → `"hello"`, `trim("**hi**", "*")` → `"hi"` |
| `justify()` | Center justify | `justify("Hi", 10)` → `"    Hi    "` |
| `lJustify()` / `rJustify()` | Left/right justify | `rJustify("Hi", 10)` → `"        Hi"` |
| `repeatString()` | Repeat string | `repeatString("*", 5)` → `"*****"` |
| `wrap()` | Wrap text to width | `wrap("Long text", 10)` → wrapped text |
| `paragraphFormat()` | Convert newlines to `<p>` | `paragraphFormat("Line1\nLine2")` |
| `stripCR()` | Remove carriage returns | `stripCR("hello\r\nworld")` → `"hello\nworld"` |

### 🔢 Comparison & Analysis

| Function | Purpose | Example |
|----------|---------|---------|
| `compare()` / `compareNoCase()` | Lexicographic comparison | `compare("a", "b")` → `-1` |
| `len()` | Get string length | `len("Hello")` → `5` |
| `stringStartsWith()` | Check if string starts with prefix | `stringStartsWith("Hello", "Hel")` → `true` |
| `stringStartsWithNoCase()` | Case-insensitive prefix check | `stringStartsWithNoCase("HELLO", "hel")` → `true` |
| `stringEndsWith()` | Check if string ends with suffix | `stringEndsWith("BoxLang", "Lang")` → `true` |
| `stringEndsWithNoCase()` | Case-insensitive suffix check | `stringEndsWithNoCase("BOXLANG", "lang")` → `true` |
| `ascii()` | Get ASCII value | `ascii("A")` → `65` |
| `char()` | Get character from ASCII | `char(65)` → `"A"` |
| `val()` | Extract numeric value | `val("123abc")` → `123` |

### 🔐 Encoding & Escaping

| Function | Purpose | Example |
|----------|---------|---------|
| `charsetEncode()` / `charsetDecode()` | Character set conversion | `charsetEncode("Hello", "UTF-8")` |
| `jsStringFormat()` | Escape for JavaScript | `jsStringFormat("He said \"Hi\"")` |
| `reEscape()` | Escape regex special chars | `reEscape("a.b*c")` → `"a\.b\*c"` |

### 🧮 Advanced String Operations

| Function | Purpose | Example |
|----------|---------|---------|
| `stringEach()` | Iterate over characters | `stringEach("abc", (char) => println(char))` |
| `stringEvery()` | Test if all chars match | `stringEvery("123", (c) => isNumeric(c))` → `true` |
| `stringSome()` | Test if any char matches | `stringSome("abc1", (c) => isNumeric(c))` → `true` |
| `stringFilter()` | Filter characters | `stringFilter("a1b2c3", (c) => !isNumeric(c))` → `"abc"` |
| `stringMap()` | Transform characters | `stringMap("abc", (c) => uCase(c))` → `"ABC"` |
| `stringReduce()` / `stringReduceRight()` | Reduce to single value | `stringReduce("123", (acc, c) => acc + val(c), 0)` → `6` |
| `stringSort()` | Sort characters | `stringSort("dcba")` → `"abcd"` |
| `stringBind()` | Bind values to placeholders | `stringBind("Hello {1}", ["World"])` → `"Hello World"` |
| `slugify()` | Create URL-friendly slug | `slugify("Hello World!")` → `"hello-world"` |

### 🔢 Boolean Formatting

| Function | Purpose | Example |
|----------|---------|---------|
| `yesNoFormat()` | Format as Yes/No | `yesNoFormat(true)` → `"Yes"` |
| `trueFalseFormat()` | Format as True/False | `trueFalseFormat(1)` → `"True"` |

{% hint style="success" %}
**Complete Reference**: For detailed documentation of each function, visit the [String BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/types/string).
{% endhint %}

## 🎯 Common String Functions

Below are detailed examples of commonly used string functions:

### � Prefix and Suffix Checking

{% hint style="info" %}
**Since BoxLang 1.14.0**. These BIFs provide explicit prefix/suffix checking with case-sensitive and case-insensitive variants.
{% endhint %}

```js
// Case-sensitive prefix check
stringStartsWith( "Hello World", "Hello" )     // true
stringStartsWith( "Hello World", "hello" )     // false
"Hello World".startsWith( "Hello" )            // true (member method)

// Case-insensitive prefix check
stringStartsWithNoCase( "HELLO", "hello" )     // true
stringStartsWithNoCase( "Hello", "hel" )       // true
"HELLO".startsWithNoCase( "hello" )            // true (member method)

// Case-sensitive suffix check
stringEndsWith( "Hello World", "World" )       // true
stringEndsWith( "Hello World", "world" )       // false
"Hello World".endsWith( "World" )              // true (member method)

// Case-insensitive suffix check
stringEndsWithNoCase( "WORLD", "world" )       // true
stringEndsWithNoCase( "Hello", "Lo" )          // true
"WORLD".endsWithNoCase( "world" )              // true (member method)

// Practical usage
function startsWithHttp( url ) {
    return url.startsWithNoCase( "http://" ) || url.startsWithNoCase( "https://" )
}

function isImageFile( filename ) {
    return filename.endsWithNoCase( ".jpg" )
        || filename.endsWithNoCase( ".png" )
        || filename.endsWithNoCase( ".gif" )
}

startsWithHttp( "HTTP://boxlang.io" )    // true
isImageFile( "photo.JPG" )                // true
```

{% hint style="success" %}
**Java Compatibility**: BoxLang's `stringStartsWith()` and `stringEndsWith()` wrap Java's `String.startsWith()` and `String.endsWith()`. The member method names `.startsWith()` and `.endsWith()` are shared with Java — the BIF and Java method are interchangeable. The `NoCase` variants are BoxLang-only additions.
{% endhint %}

### �📏 len()

Returns the number of characters in a string. Trailing spaces are counted.

```js
message = "Hola Luis"
writeOutput( message.len() )  // 9

// Useful in conditionals
if( len(message) > 0 ) {
    // String is not empty
}
```

[Try it online!](https://try.boxlang.io)

### ✂️ trim(), lTrim(), rTrim()

Remove whitespace and control characters from strings. As of BoxLang 1.13.0, an optional `chars` argument lets you trim any custom character set instead of just whitespace.

```js
text = "  Hello World  "
writeOutput( trim(text) )      // "Hello World"
writeOutput( lTrim(text) )     // "Hello World  "
writeOutput( rTrim(text) )     // "  Hello World"

// Method chaining
result = "  BoxLang  ".trim().len()  // 8

// Trim custom characters (1.13.0+)
"**Urgent**".trim( "*" )       // "Urgent"
"000123".lTrim( "0" )          // "123"
"report....".rTrim( "." )      // "report"
```

[Try it online!](https://try.boxlang.io)

### 🔄 replace(), replaceNoCase(), reReplace(), reReplaceNoCase()

Replace substrings or patterns within strings.

```js
// Simple replacement (first occurrence)
result = replace("Hello", "l", "L")  // "HeLlo"

// Replace all occurrences
result = replace("Hello", "l", "L", "ALL")  // "HeLLo"

// Case-insensitive replacement
result = replaceNoCase("Hello WORLD", "world", "Universe")  // "Hello Universe"

// Regex replacement
result = reReplace("test 123!", "[^a-z0-9]", "", "ALL")  // "test123"
result = reReplace("123abc456", "[0-9]+([a-z]+)[0-9]+", "\1")  // "abc"
```

[Try it online!](https://try.boxlang.io)

### 🗑️ removeChars()

Remove characters from a string at a specific position.

```js
result = removeChars("hello bob", 2, 5)  // "hbob"
// Removes 5 characters starting at position 2
```

[Try it online!](https://try.boxlang.io)

### 📋 mid()

Concatenate strings using the `&` operator or string interpolation with `#` symbols.

```js
name = "Luis"
greeting = "Hello " & name & " how are you today?"

// Concatenate and assign
message = "Welcome"
message &= " to BoxLang!"  // "Welcome to BoxLang!"
```

String interpolation allows you to embed variables and expressions directly within strings using `#` hash symbols.

```js
name = "Luis"
age = 25
welcome = "Good morning #name#, you are #age# years old!"
// "Good morning Luis, you are 25 years old!"

// Expressions work too
message = "The time is #now()# and 2+2 = #2+2#"
// "The time is {date/time} and 2+2 = 4"

// Complex expressions
items = ["apple", "banana", "orange"]
output = "First item: #items[1]#"
// "First item: apple"
```

{% hint style="success" %}
**Note:** Anything between hashes (`#...#`) is interpreted as a **BoxLang expression**, not just simple variables.
{% endhint %}

BoxLang automatically casts many types to strings, but you can explicitly convert values using `toString()`.

```js
// Automatic casting
number = 42
text = "The answer is " & number  // "The answer is 42"

// Explicit conversion with toString()
struct = { a: "1", b: "2" }
writeOutput( toString(struct) )
writeOutput( struct.toString() )

number = 42222.222
writeOutput( number.toString() )  // "42222.222"

// Arrays
arr = [1, 2, 3]
writeOutput( arr.toString() )  // "[1, 2, 3]"
```

[Try it online!](https://try.boxlang.io)

## 🔗 Related Documentation

- [String BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/types/string) - Complete list of all string functions
- [Operators](operators.md) - String concatenation and assignment operators
- [Java String API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) - Native Java methods available on strings
- [Regular Expressions](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html) - Pattern syntax for regex functionssage = "Data: #toJSON(data)#"
```

[Try it online!](https://try.boxlang.io)

## 🔄 Castingfunction syntax
writeOutput( text.left(3) )    // "Box"
```

[Try it online!](https://try.boxlang.io)

### 📋 listToArray()

Convert a delimited string into an array.

```js
// Default delimiter (comma)
list = "luis,majano,lucas,alexia,veronica"
myArray = list.listToArray()  // ["luis", "majano", "lucas", "alexia", "veronica"]

// Custom delimiter
names = "John|Jane|Bob"
myArray = listToArray(names, "|")

// Multi-character delimiter
list = "boxlang,php,|test,java,|sql"
getArray = listToArray(list, ",|", false, true)
```

[Try it online!](https://try.boxlang.io)

## ⚙️ Member Functions

All string BIFs can be called as member functions on string variables. Additionally, since BoxLang strings are Java strings, you have access to all Java String methods:

### BoxLang String Member Functions

```js
text = "Hello BoxLang"

// Case conversion
text.uCase()            // "HELLO BOXLANG"
text.lCase()            // "hello boxlang"
text.camelCase()        // "helloBoxlang"

// Search & find
text.find("Box")        // 7
text.reFind("[A-Z]+")   // 1

// Extraction
text.left(5)            // "Hello"
text.right(7)           // "BoxLang"
text.mid(7, 3)          // "Box"

// Replace & transform
text.replace(" ", "_")  // "Hello_BoxLang"
text.reverse()          // "gnaLxoB olleH"

// Formatting
"  test  ".trim()       // "test"
"hi".repeatString(3)    // "hihihi"

// Iteration
"abc".stringEach((char) => println(char))
"123".stringEvery((c) => isNumeric(c))  // true
```

### Java String Member Functions

```js
text = "Hello BoxLang"

// Java String methods
text.length()                    // 13
text.toUpperCase()               // "HELLO BOXLANG"
text.toLowerCase()               // "hello boxlang"
text.substring(0, 5)             // "Hello"
text.contains("Box")             // true
text.startsWith("Hello")         // true
text.endsWith("Lang")            // true
text.indexOf("Box")              // 6
text.lastIndexOf("o")            // 7
text.charAt(0)                   // "H"
text.split(" ")                  // ["Hello", "BoxLang"]
text.replace("Box", "Test")      // "Hello TestLang"
text.trim()                      // "Hello BoxLang"
text.isEmpty()                   // false
text.matches(".*Box.*")          // true
text.replaceAll("[aeiou]", "X")  // "HXllX BXxLXng"
text.replaceFirst("l", "L")      // "HeLlo BoxLang"
text.concat(" Rocks!")           // "Hello BoxLang Rocks!"
```

{% hint style="success" %}
**Pro Tip**: Use member function syntax for cleaner, more readable code with method chaining: `text.trim().uCase().left(10)`
{% endhint %}

[Try it online!](https://try.boxlang.io)

## 🔗 Combining Strings

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
