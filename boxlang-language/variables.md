---
description: name = "Amazing Programmer"
icon: gear-code
---

# Variables

In BoxLang, variables are just pointers to a piece of data. They can hold **any** value you like and even change their value or **type** at runtime since BoxLang is a dynamic language. In some languages, you need to specify the type of data you want your variable to hold at compile-time and it can never change. You do not need to assign one in BoxLang, as everything is dynamic and/or inferred. It infers types according to the initial value you assign to your variable.

```javascript
a = "string" // string
b = now() // datetime
c = 123 // integer
d = 1.34 // float
d2 = 12312377324234234234 // BigDecimal
f = false // boolean
g = [] // array
h = { name : "luis", isActive : true } // struct
```

{% hint style="danger" %}
Please note that assignments are evaluated from right to left instead of traditional reading from left to right.
{% endhint %}

Why don't you open the BoxLang REPL: `boxlang` or go to [try.boxlang.io](https://try.boxlang.io) and try some stuff out.

```bash
> hello = "world"
world

> a = 5
5

> b = 10 + a
15

> c = 15 + a + b
35

> b = c * a
175

> d = [ 1, 2, 3, 4, 5 ]
[ 1, 2, 3, 4, 5 ]

> myStruct = { key = "hola", today = now(), id = createUUID() }
{
  id : "B634D0D9-A32F-4781-A9F519258ED4B73D",
  today : {ts '2024-08-10 19:43:01'},
  key : "hola"
}

> println( a + b + c )
215
```

As you can see, we can create [strings](strings.md), [numerics](numbers.md), [arrays](arrays.md), [structs](structures.md), uses headless functions (BIFS) and more. There is no need for types or special assignments. The BoxLang engine will determine or infer it and use it accordingly, thus a dynamic language.

### BIFs

BoxLang leverages several headless built-in functions that are available anywhere you code.  These will be referred to you as BIFs.  You can see our [reference guide](reference/built-in-functions/) to check them out.  Here are some we used:

```java
print() // print to the out stream
println() // print with a line break
now() // get today's date time
createUUID() // generate a unique id
```

## Case Insensitive

**BoxLang is a case-insensitive language** as well. Meaning if you create a variable `a` and reference it as `A` they are the same. This can be a big gotcha for developers from languages like Java or JavaScript. However, as best practice, we would recommend **ALWAYS** using the same case as when you define the variable:

**Don't do this**

```javascript
a = "Hola Luis";
println( A );
```

**Do this**

```javascript
a = "Hola Luis";
println( a );
```

## Naming Requirements

Most BoxLang variables have a few requirements imposed by the Virtual Machine (VM)

* It must begin with a letter, underscore, or Unicode currency symbol.
* It can contain letters, numbers, underscore characters, and Unicode currency symbols.
* NO SPACES!
* Not case-sensitive

### Reserved Words

As with any programming language, there are specific names you can't use, and some you can use.  Here are the rules:

* The name of any of the internal BoxLang persistent scopes: `form, session, cgi, client, url, application, function`
  * Technically you can create the variable by long scoping (`local.form`), but it is confusing and error-prone. So please be careful.
* Reserved Operators
  * `AND`
  * `EQ`
  * `EQUAL`
  * `EQV`
  * `GE`
  * `GREATER`
  * `GT`
  * `GTE`
  * `IMP`
  * `IS`
  * `LE`
  * `LESS`
  * `LT`
  * `LTE`
  * `MOD`
  * `NEQ`
  * `NOT`
  * `OR`
  * `THAN`
  * `XOR`
* Reserved Keywords
  * `ABSTRACT`
  * `ANY`
  * `ARRAY`
  * `AS`
  * `ASSERT`
  * `BOOLEAN`
  * `BREAK`
  * `CASE`
  * `CASTAS`
  * `CATCH`
  * `CLASS`
  * `CONTAIN`
  * `CONTAINS`
  * `CONTINUE`
  * `DEFAULT`
  * `DO`
  * `DOES`
  * `ELIF`
  * `ELSE`
  * `FALSE`
  * `FINAL`
  * `FINALLY`
  * `FOR`
  * `FUNCTION`
  * `IF`
  * `IMPORT`
  * `IN`
  * `INCLUDE`
  * `INSTANCEOF`
  * `INTERFACE`
  * `JAVA`
  * `MESSAGE`
  * `NEW`
  * `NULL`
  * `NUMERIC`
  * `PACKAGE`
  * `PARAM`
  * `PRIVATE`
  * `PROPERTY`
  * `PUBLIC`
  * `QUERY`
  * `REMOTE`
  * `REQUEST`
  * `REQUIRED`
  * `RETHROW`
  * `RETURN`
  * `SERVER`
  * `SETTING`
  * `STATIC`
  * `STRING`
  * `STRUCT`
  * `SWITCH --> Could possibly be a var name, but not a function/method name`
  * `THROW`
  * `TO`
  * `TRUE`
  * `TRY`
  * `TYPE`
  * `VARIABLES`
  * `VAR`
  * `WHEN`
  * `WHILE`

## Flexible Typing

You can also create a variable with one type and then switch it to another dynamically:

```bash
a = "hello"
hello
a = 123
123
a = now()
{ts '2024-08-10 19:51:24'}
a = [1,2,3]
[1,2,3]
```

As you can see, the last equality wins! In this case, `a` is now an array.

## 🔤 The `var` Keyword

The `var` keyword is an **assignment modifier** that explicitly scopes variables to a function's `local` scope. While not mandatory in BoxLang (the runtime will auto-assign unscoped variables to the function's local scope if they don't exist in the `variables` or `this` scope), using `var` is considered a **best practice** for clarity and intentionality.

```js
function processData() {
    // Without var - BoxLang auto-assigns to local scope
    result = "processed"

    // With var - explicitly scoped to local
    var status = "complete"

    // Both are equivalent and end up in local scope
    return { result: result, status: status }
}
```

{% hint style="success" %}
**Best Practice**: Use `var` to make your intent explicit, especially in complex functions. It clearly communicates that you're creating a function-local variable and not accessing an outer scope variable.
{% endhint %}

### Auto-Scoping Behavior

When you assign a variable without a scope prefix inside a function, BoxLang follows this logic:

1. **Check if variable exists** in `variables` or `this` scope (for class methods)
2. **If exists**, update that existing variable
3. **If NOT exists**, create it in the function's `local` scope

```js
class {
    variables.counter = 0

    function increment() {
        // This updates variables.counter because it exists
        counter = counter + 1

        // This creates a NEW local variable because 'temp' doesn't exist in variables
        temp = counter * 2

        return { counter: counter, temp: temp }
    }
}
```

### Using `var` with Other Modifiers

The `var` keyword can be combined with other assignment modifiers:

```js
function example() {
    var final result = "constant"  // Local and immutable
    final var status = "done"      // Order doesn't matter

    // result = "changed"  // ❌ Error: Cannot reassign final variable
}
```

## 🔒 The `final` Modifier

The `final` modifier creates **immutable variables** that cannot be reassigned after their initial assignment. This is useful for constants and preventing accidental modifications. Final variables can be used in multiple contexts:

### In Scripts (`bxs`, `bxm`)

```js
// Script-level final variables
final name = "Luis Majano"
final VERSION = "1.0.0"
final config = { debug: false, timeout: 30 }

// name = "Changed"  // ❌ Error: Cannot reassign final variable

// Note: For complex types, the reference is final, not the contents
config.debug = true  // ✅ Allowed - modifying contents
// config = {}       // ❌ Error - cannot reassign the reference
```

### In Functions

```js
function calculateTotal( items ) {
    var final TAX_RATE = 0.08      // Local final variable
    final var subtotal = items.sum() // Order doesn't matter

    final total = subtotal * ( 1 + TAX_RATE )

    // TAX_RATE = 0.09  // ❌ Error: Cannot reassign final variable

    return total
}
```

### In Classes (Pseudo-Constructor)

```js
class UserService {
    // Final class-level constants
    final variables.API_VERSION = "2.0"
    final this.MAX_RETRIES = 3
    final static.COMPANY_NAME = "Ortus Solutions"

    function init() {
        final this.instanceId = createUUID()

        // API_VERSION = "3.0"  // ❌ Error: Cannot reassign final variable

        return this
    }
}
```

{% hint style="warning" %}
**Important**: The `final` modifier makes the **variable reference** immutable, not the object it references. For arrays and structs, you can still modify their contents, but you cannot reassign the variable to a different array or struct.

```js
final users = [ "Luis", "Brad" ]
users.append( "Jose" )  // ✅ Allowed
// users = []            // ❌ Error: Cannot reassign
```
{% endhint %}

## ⚡ The `static` Modifier

The `static` modifier is **ONLY available for classes** and creates class-level variables that are shared across all instances. Static variables belong to the class blueprint, not individual instances.

```js
class Counter {
    static totalCount = 0

    function init() {
        static.totalCount++  // Increment shared counter
        this.instanceId = createUUID()
        return this
    }

    static function getTotal() {
        return static.totalCount
    }
}

// Usage
counter1 = new Counter()
counter2 = new Counter()
println( Counter::getTotal() )  // 2
```

For complete documentation on static members, see: [Static Class Members](classes/static.md)

## 🔍 Scope Hunting & Lookup Order

When you reference a variable **without a scope prefix**, BoxLang must search for it across multiple scopes. This is called **scope hunting**, and the order varies by execution context.

### 🎯 In Functions (UDFs, Closures, Lambdas)

1. **`local`** - Function-scoped variables
2. **`arguments`** - Function parameters
3. **`this`** - Public class scope (if in a class method)
4. **`variables`** - Private class scope (if in a class method)
5. **`static`** - Static class scope (if in a class method, internal calls only)
6. Then delegates to parent context scopes (request, server, etc.)

```js
class Example {
    variables.name = "Class Variable"

    function test( name ) {
        var name = "Local Variable"

        // Unscoped 'name' finds local first
        println( name )                // "Local Variable"
        println( local.name )          // "Local Variable"
        println( arguments.name )      // (function parameter)
        println( variables.name )      // "Class Variable"
    }
}
```

### 📄 In Scripts/Templates (`bxs`, `bxm`)

1. **`variables`** - The implicit default scope
2. Then delegates to runtime scopes (request, server, cgi, url, form, cookie)

```js
// In a bxs script
name = "Luis"  // Goes to variables scope
println( variables.name )  // "Luis"
```

### 🗳️ In Class Pseudo-Constructors

1. **`this`** - Public scope
2. **`variables`** - Private scope
3. **`static`** - Static scope
4. Then delegates to parent scopes

{% hint style="danger" %}
**Performance Impact**: Scope hunting has a performance cost! BoxLang must check multiple scopes in order until it finds the variable. **Always explicitly scope your variables** for:
- Better performance
- Code clarity
- Avoiding unexpected variable collisions
{% endhint %}

### Best Practice: Explicit Scoping

```js
// ❌ BAD - Requires scope hunting
function calculate( a, b ) {
    result = a + b
    return result
}

// ✅ GOOD - Explicit scoping
function calculate( a, b ) {
    var result = arguments.a + arguments.b
    return local.result
}
```

## 👥 Variable Shadowing

**Variable shadowing** occurs when variables with the same name exist in different scopes. The scope lookup order determines which variable is accessed when using an unscoped reference.

### Shadowing in Functions

```js
class {
    variables.count = 10

    function process( count ) {
        var count = 5

        // Unscoped 'count' finds local scope first (value: 5)
        println( count )              // 5

        // Explicit scoping accesses the intended variable
        println( local.count )        // 5
        println( arguments.count )    // (parameter value)
        println( variables.count )    // 10
    }
}
```

### Shadowing Examples by Precedence

```js
function demo( userId ) {
    var userId = 123              // Local shadows arguments
    variables.userId = 456        // Class variable

    // Scope hunting order: local -> arguments -> variables
    println( userId )             // 123 (local wins)
    println( local.userId )       // 123
    println( arguments.userId )   // (parameter value)
    println( variables.userId )   // 456
}
```

{% hint style="info" %}
**Pro Tip**: Use different variable names across scopes to avoid confusion. If you must shadow, always use explicit scoping (`local.name`, `arguments.name`, `variables.name`) to make your intent clear.
{% endhint %}

## ⚠️ Variable-Method Name Collisions

{% hint style="danger" %}
**CRITICAL WARNING**: Creating variables with the same name as methods will cause **collisions** because functions in classes are stored in scopes as variables!

### How Functions Are Stored:
- **Public/Remote functions** → Stored in **both** `this` AND `variables` scopes
- **Package/Private functions** → Stored in **`variables`** scope only
{% endhint %}

### The Problem

```js
class UserService {
    // This creates a function reference in variables and this
    function getUser() {
        return { name: "Luis" }
    }

    function init() {
        // ❌ BAD - Overwrites the getUser function!
        variables.getUser = "some string"

        // Now getUser() will fail because it's no longer a function
        // this.getUser()  // Error: getUser is not a function

        return this
    }
}
```

### The Solution

```js
class UserService {
    function getUser() {
        return { name: "Luis" }
    }

    function init() {
        // ✅ GOOD - Use different variable names
        variables.userData = "some string"
        variables.userName = "Luis"

        // Function remains accessible
        user = this.getUser()  // ✅ Works!

        return this
    }
}
```

### Variable Names to Avoid

Avoid creating variables with names that match:
- Any function/method names in your class
- Common BIF names if you plan to call them unscoped
- Reserved scope names (`local`, `arguments`, `variables`, `this`, `session`, `cgi`, `session`, `server`, etc.)

> See: [Variable Scopes](variable-scopes.md) for more on scopes and best practices.

```js
class {
    function getData() { return [] }

    function process() {
        // ❌ BAD - Don't do this
        variables.getData = []  // Overwrites the method!

        // ✅ GOOD - Use different names
        variables.data = []
        variables.dataList = []
        variables.retrievedData = []
    }
}
```

## 🔒 Immutability

BoxLang supports **immutable collections** for arrays, queries, and structs. Once a collection is made immutable, its contents cannot be modified, providing thread-safe and error-resistant data structures.

### Making Collections Immutable

```js
// Immutable Array
data = [ 1, 2, 3 ].toUnmodifiable()
// data.append( 4 )  // ❌ Error: Cannot modify immutable collection

// Immutable Struct
config = { debug: false }.toUnmodifiable()
// config.debug = true  // ❌ Error: Cannot modify immutable struct

// Immutable Query
users = queryNew( "id,name", "integer,varchar", [
    [ 1, "Luis" ],
    [ 2, "Brad" ]
]).toUnmodifiable()
// users.addRow( [ 3, "Eric" ] )  // ❌ Error: Cannot modify immutable query
```

### Combining `final` and Immutable

For maximum safety, combine `final` (immutable reference) with `.toUnmodifiable()` (immutable contents):

```js
final config = { api: "v2", timeout: 30 }.toUnmodifiable()

// config = {}              // ❌ Error: Cannot reassign final variable
// config.api = "v3"        // ❌ Error: Cannot modify immutable struct
```

### Learn More

- [Arrays - Immutability](arrays.md#immutability)
- [Structures - Immutability](structures.md#immutability)
- [Queries - Immutability](queries.md#immutability)

## Types

BoxLang is a typeless language, but internal types always exist which can be inferred or declared. BoxLang will automatically cast so you can do flexible typing assignments when evaluating expressions. It does all the tedious and hard job for you. If we were to categorize BoxLang variables into categories, these would be:

<table><thead><tr><th width="259">Category</th><th>Description</th></tr></thead><tbody><tr><td><strong>Binary</strong></td><td>Raw data from files such as images, pdfs, etc</td></tr><tr><td><strong>Complex</strong></td><td>A data container that represents more than one value: structures, arrays, queries, XML document objects, etc.</td></tr><tr><td><strong>Objects</strong></td><td>Complex constructs representing data and functional operations. BoxLang Classes or Java Objects.</td></tr><tr><td><strong>Simple</strong></td><td>One value and used directly in expressions. These include numbers, strings, floats, booleans, and date-time values.</td></tr></tbody></table>

BoxLang also includes many validation functions that are available to you to test for the type of variable you are working with. You can also use the `getmetdata()` function to get the metadata about the variable as well.

```javascript
qData = query.getMetadata()
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
* `isFileObject()`
* `isJSON()`
* `isIPv6()`
* `isLeapYear()`
* `isNumeric()`
* `isNumericDate()`
* `isObject()`
* `isLocalHost()`
* `isNull()`
* `isPDFFile()`
* `isPDFObject()`
* `isQuery()`
* `isSimpleValue()`
* `isStruct()`
* `isValid( type, value )`
* `isXML()`
* `isXmlDoc()`
* `isXMLElem()`
* `isXMLNode()`
* `ixXMLRoot()`

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
