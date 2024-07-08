---
description: name = "Amazing Programmer"
---

# Variables

In BoxLang, variables are just pointers to a piece of data. They can hold **any** value you like and even change their value or **type** at runtime. In some languages, you need to specify the type of data you want your variable to hold at compile-time. You do not need to assign one in BoxLang, as everything is dynamic or inferred. It infers types according to the initial value you assign to your variable.

```javascript
a = "string"; // string
b = now(); // datetime
c = 123; // integer
d = 1.34; // float
f = false; // boolean, or a string
```

{% hint style="danger" %}
Please note that assignments are evaluated from right to left instead of traditional reading from left to right.
{% endhint %}

Open up the CommandBox Shell and go into CommandBox **REPL** mode by typing `repl`. Whenever you assign a value to a variable, the CommandBox REPL will output or echo the variable for you. Please note that in REPL mode, the termination for a line of code is omitted. A line terminator in BoxLang is the `;`.

![](<../.gitbook/assets/variables (1).png>)

As you can see, we can create [strings](strings.md), [numerics](numbers.md), [arrays](arrays.md), [structs](structures.md), and so much more. There is no need for types or special assignments. The BoxLang engine will determine or infer it and use it accordingly, thus a dynamic language.

{% hint style="success" %}
In the CommandBox REPL semi-colons are optional, and the default syntax is script and not tags.
{% endhint %}

## Case Insensitive

**BoxLang is a case-insensitive language** as well. Meaning if you create a variable `a` and reference it as `A` they are the same. This can be a big gotcha for developers from languages like Java or JavaScript. However, as best practice, we would recommend **ALWAYS** using the same case as when you define the variable:

**Don't do this**

```javascript
a = "Hola Luis";
writeOutput( A );
```

**Do this**

```javascript
a = "Hola Luis";
writeOutput( a );
```

## Naming Requirements

Most BoxLang variables have a few requirements imposed by the Virtual Machine (VM)

* It must begin with a letter, underscore, or Unicode currency symbol.
* It can contain letters, numbers, underscore characters, and Unicode currency symbols.
* NO SPACES!
* Not case-sensitive

#### Reserved Words

As with any programming language, there are specific names you can't use, and some you can use, but they can be very confusing for developers or the engine. Here is a list of some of those:

* The name of any of the internal BoxLang engine scopes: `form, session, cgi, client, url, application, function`
  * Technically you can create the variable by long scoping (`local.form`), but it is confusing and error-prone. So please be careful.

| Reserved Word                  |
| ------------------------------ |
| `abstract`                     |
| `and`                          |
| `break`                        |
| `case`                         |
| `catch`                        |
| `continue`                     |
| `contains`                     |
| `default`                      |
| `do`                           |
| `else`                         |
| `eq`                           |
| `eqv`                          |
| `false`                        |
| `finally`                      |
| `final`                        |
| `for`                          |
| `function`                     |
| `gt`                           |
| `gte`                          |
| `import`                       |
| `imp`                          |
| `in`                           |
| `is`                           |
| `if`                           |
| `interface`                    |
| `lt`                           |
| `lte`                          |
| `local` (within a function)    |
| `neq`                          |
| `not`                          |
| `null` (If null support is on) |
| `pageenconding`                |
| `or`                           |
| `return`                       |
| `switch`                       |
| `true`                         |
| `try`                          |
| `while`                        |
| `xor`                          |

## Flexible Typing

You can also create a variable with one type and then switch it to another dynamically:

![](<../.gitbook/assets/flexible-typing (1) (1).png>)

As you can see, the last equality wins! In this case, `a` is now an array.

## Types

BoxLang is a typeless language, but internal types always exist. BoxLang will automatically cast so you can do flexible typing assignments when evaluating expressions. It does all the tedious and hard job for you. If we were to categorize BoxLang variables into categories, these would be:

| Category    | Description                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| **Binary**  | Raw data from files such as images, pdfs, etc                                                                       |
| **Complex** | A data container that represents more than one value: structures, arrays, queries, XML document objects, etc.       |
| **Objects** | Complex constructs representing data and functional operations. BoxLang Classes or Java Objects.                    |
| **Simple**  | One value and used directly in expressions. These include numbers, strings, floats, booleans, and date-time values. |

BoxLang also includes many validation functions that are available to you to test for the type of variable you are working with. You can also use the `getmetdata()` function to get the metadata about the variable as well.

```javascript
qData = getMetadata( query )
a = now()
writedump( a.getMetadata() )
```

* `isArray()`
* `isBinary()`
* `isBoolean()`
* `isCustomFunction()`
* `isClosure()`
* `isDate()`
* `isDateObject()`
* `isDDX()`
* `isJSON()`
* `isNumeric()`
* `isNumericDate()`
* `isObject()`
* `isNull()`
* `isPDFFile()`
* `isPDFObject()`
* `isQuery()`
* `isSimpleValue()`
* `isSpreadsheetFile()`
* `isSpreadsheetObject()`
* `isStruct()`
* `isWDDX()`
* `isXML()`
* `isXmlDoc()`

### Conversions

You can also convert variables from one type to another in BoxLang. Here are some functions that will assist you in conversions:

* `arrayToList()`
* `binaryDecode()`
* `binaryEncode()`
* `charsetDecode()`
* `charsetEncode()`
* `deserializeJSON()`
* `entityToQuery()`
* `hash()`
* `hmac()`
* `HTMLParse()`
* `lcase()`
* `listToArray()`
* `parseNumber()`
* `serializeJSON()`
* `toBase64()`
* `toBinary()`
* `toScript()`
* `toString()`
* `URLDecode()`
* `URLEncode()`
* `URLEncodedFormat()`
* `val()`
* `XMLFormat()`
* `XMLParse()`
* `XMLTransform()`

{% hint style="info" %}
Please note that some of them can be used as member functions directly on a specific object type. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion)
{% endhint %}

## Outputting Variables (Interpolation)

You can also output or evaluate variables by using the `#` operators and using the variable name. This is referred to as interpolation in some languages:

```javascript
a = "Hola Luis"
writeoutput( "Welcome to BoxLang: #a#" )
// Echo is the same as writeOutput
echo( "Welcome" )
```

Also, note that using the `#` hashes for output on assignments can be redundant if you do NOT use string interpolation but just variable assignments.

**Don't do this**

```javascript
a = "hello luis";
b = #a#;
or
b = "#a#";
```

**Do this**

```javascript
a = "hello luis";
b = a;
```

## Debugging Variables

BoxLang offers one of the most used functions/tags ever: `<bx:dump>, writeDump()` and `<bx:abort>, abort;`. These are used to dump all the contents of a variable into the browser, console, or even a file. You can then leverage the `abort` construct to abort the request and see the output of your dumped variables. This will work with both simple and complex variables. However, be very careful when using it with Nested ORM objects, as you can potentially dump your entire database and crash the server. Leverage the `top` argument to limit dumping.

```javascript
writeDump( complex );abort;

<bx:dump var="#server#" abort=true>

writeDump( var=arrayOfORM, top=5 );abort;
```

### Server Debugging Templates

BoxLang also allows you to turn on/off a debugging template that shows up at the bottom of requests when running in server mode. You can activate this debugging by logging in to the appropriate engine administrator and looking for the **debugging** section. Turn it on and debug like a champ.

## Paraming Variables

BoxLang allows you to set default values for variables if you use a variable that doesn't exist. You can use the `<bx:param>` tag or the `param` construct:

```markup
<bx:param name="myVariable" default="luis">
```

or

```javascript
param myVariable = "luis";
```

{% hint style="success" %}
You can even assign types to parameterize variables and much more. Check out the docs for it: [https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/param](https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/param)
{% endhint %}

## Checking For Existence

You can verify if variables exist in many different ways. The following section showcases how variables are stored in visibility and persistence scopes, all of which are structures or hash maps in Java terms. This means you can leverage structure operations to check for existence and much more. Below are several ways to verify variable existence:

*   `isDefined()` - Evaluates a string value to determine whether the variable

    named in it exists.
* `isNull()` - Returns `true` if the specified object is null, else `false`.
* `structKeyExists( key, value )` - Verifies if the specified key variable exists in a structure.

```javascript
// Notice the variable name is in quotes
if( isDefined( "myVariable" ) ){
    writeOutput( myVariable );
} else {
    writeOutput( "Not Defined!" );
}

// Notice that the variable is NOT in quotes
if( isNull( myVariable ) ){
    writeOutput( "Not Defined!" );
} else {
    writeOutput( myVariable );
}

// What is this variables scopes???
if( structKeyExists( variables, "myVariable" ) ){
    writeOutput( myVariable );
} else {
    writeOutput( "Not Defined!" );
}
```

## Java Integration

As we have discussed, BoxLang is a dynamic language built on Java. Thus each variable internally is represented by a native Java data type: `String, Int, Float, Array, Vector, HashMap, etc`. This is important because each variable you create has member functions available to you that delegate or reflect its native Java class.

```javascript
a = "hello";
writeOutput( a.getClass().getName() );
```

If you run the script above in the REPL tool, you will see the output as `java.lang.String`. Therefore, the variable is typed as a `String` and can call on any method that `java.lang.String` implements. You can try this for the many types in BoxLang, like structs, arrays, objects, etc.

## Member Functions

Besides the native Java member functions available to you, BoxLang also allows you to call on each variable's data type functions and chain them to create friendly language DSLs. This way, you do not have to pass variables into functions but treat the variables as objects. You can see all the member functions available according to data type here: [https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions)

Here are some examples:

```javascript
// Function passing
var myArray = [];
ArrayAppend( myArray, "objec_new" );
ArraySort( myArray, "ASC" );

// Member Functions
myArray.append( "objec_new" );
myArray.sort( "ASC" );

// Java Functions + BoxLang Functions
var myProductObject = createObject( "java", "myJavaclass" );
myjavaList = myProductObject.getProductList();
myjavaList.add( "newProduct" ); // Java API

myjavaList.append( "newProduct" ); // CF API
myjavaList.sort( "ASC" );

// DSL Chaining
s="the";
s = s.listAppend("quick brown fox", " ")
     .listAppend("jumps over the lazy dog", " ")
     .ucase()
     .reverse();
```

#### Member functions for the following data types are supported:

* Array
* String
* List
* Struct
* Date
* Spreadsheet
* XML
* Query
* Image

Please see [https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) for further information on member functions.

## Naming Coding Standards

At [Ortus Solutions](https://www.ortussolutions.com), we have developed a set of development standards for many languages. You can find our BoxLang standards here: [https://github.com/Ortus-Solutions/coding-standards](https://github.com/Ortus-Solutions/coding-standards)
