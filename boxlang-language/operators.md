---
description: Operate all things++--==!^%/\
icon: function
---

# Operators

**Operators** are the foundation of **any** programming language. Operators are symbols that help a programmer to perform specific mathematical, structuring, destructuring, and logical computations on operands (variables or expressions). We can categorize the BoxLang operators into the following categories:

1. Arithmetic/Mathematical
2. Assignment
3. Logical
4. Comparison
5. Ternary
6. Elvis (Null Coalescing)
7. Function
8. Collections

{% hint style="danger" %}
BoxLang does not offer the capability to overload operators like other languages.
{% endhint %}

## 📊 Operator Precedence

The order of precedence exists in BoxLang, just like in mathematics. You can also control the order of precedence by using the grouping operator `()` like in mathematics, the magical ordering parenthesis.

{% code lineNumbers="true" %}
```javascript
^
*, /
\
MOD
+, -
..
&
EQ, NEQ, LT, LTE, GT, GTE, CONTAINS, DOES NOT CONTAIN, ==, !=, >, >=, <, <=
NOT, !
AND, &&
OR, ||
XOR
EQV
IMP
```
{% endcode %}

{% hint style="success" %}
Remember that using parenthesis `(Grouping Operator)` is very important to denote precedence.
{% endhint %}

## ➕ Arithmetic Operators

These operators are used to perform arithmetic/mathematical operations on operands.

| Operator | Name                | Description                                                                                                                                                                                     |
| -------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+`      | Add                 | `a = 1 + 4`                                                                                                                                                                                     |
| `-`      | Subtract            | `a = 4 - 2`                                                                                                                                                                                     |
| `*`      | Multiply            | `a = 4 * b`                                                                                                                                                                                     |
| `/`      | Divide              | `a = 4 / myVariable`                                                                                                                                                                            |
| `^`      | Exponentiate        | `a = 2^2 // 4`                                                                                                                                                                                  |
| `%, MOD` | Modulus / Remainder | `5 % 2 = 1` or `5 mod 2`                                                                                                                                                                        |
| `\`      | Integer Divide      | `a = 7 \ 3` is 2. Please note it does not round off the integer.                                                                                                                                |
| `..`     | Inclusive Range     | <p>Creates an inclusive integer range.<br><code>1..5</code> → <code>[1,2,3,4,5]</code><br><code>5..1</code> → <code>[5,4,3,2,1]</code></p>                                                      |
| `++`     | Increment           | <p><code>a = b++</code> assign b to a and THEN increment b<br><code>a = ++b</code> increment b and THEN assign to a</p>                                                                         |
| `--`     | Decrement           | <p><code>a = b--</code> assign b to a and THEN decrement b<br><code>a = --b</code> decrement b and THEN assign to a</p>                                                                         |
| `-`      | Negate              | `a = -b` Negate the value of b                                                                                                                                                                  |
| `+`      | Positive            | `a = +b` Make the value of b a positive number                                                                                                                                                  |
| `()`     | Grouping            | <p>The grouping operator is used just like in mathematics, to give precedence to operations.<br><code>result = 3 * (2+3)</code> which is not the same as<br><code>result = 3 * 2 + 3</code></p> |

### 🔢 Range Operator

{% hint style="info" %}
Since BoxLang 1.12.x
{% endhint %}

BoxLang supports the inclusive `..` range operator in BoxScript expressions.

```javascript
1..5   // [1, 2, 3, 4, 5]
5..1   // [5, 4, 3, 2, 1]

a = 2
b = 4
result = a..b  // [2, 3, 4]
```

Use this when you want a compact way to create integer ranges without calling a helper function.

#### Notes on mathematical casting:

For basic arithmetic operations (addition, subtraction, multiplication, and division), dates and time spans may be cast as numeric values. In BoxLang, the numeric value of a [DateTime](../boxlang-framework/modularity/compat-cfml/reference/types/datetime.md) object represents the number of decimal days since the Unix epoch. A [timespan](reference/built-in-functions/temporal/CreateTimeSpan.md) or Java [Duration](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/time/Duration.html) object is represented as decimal days for the purpose of mathematical operations.

## 🔢 Bitwise Operators

{% hint style="info" %}
BoxLang has native [bitwise](https://en.wikipedia.org/wiki/Bitwise_operation) operators, and it also implements bitwise operations via functions (since functions can also be operators in BoxLang): `bitAnd, bitMaskClear, bitMaskRead, bitMaskSet, bitNot, bitOr, bitSHLN, bitSHRN, bitXOR` . You can find much more information here: [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math)
{% endhint %}

These operators are used to perform bitwise operations on operands.

The bitwise operators look a bit different in BoxLang vs other languages like Java since the normal bitwise operators are already used for other purposes in BoxLang.

<table><thead><tr><th width="125">Operator</th><th width="147">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>b|</code></td><td>Bitwise OR</td><td><code>a = 12 b| 25</code></td></tr><tr><td><code>b&#x26;</code></td><td>Bitwise AND</td><td><code>a = 5 b&#x26; 9</code></td></tr><tr><td><code>b^</code></td><td>Bitwise XOR</td><td><code>a = 10 b^ 12</code></td></tr><tr><td><code>b~</code></td><td>Bitwise Complement</td><td><code>a = b~ 35</code></td></tr><tr><td><code>b&#x3C;&#x3C;</code></td><td>Bitwise Signed Left Shift</td><td><code>a = 14 b&#x3C;&#x3C; 4</code></td></tr><tr><td><code>b>></code></td><td>Bitwise Signed Right Shift</td><td><code>a = 4 b>> 2</code></td></tr><tr><td><code>b>>></code></td><td>Bitwise Unsigned Right Shift</td><td><code>a = 25 b>>> 3</code></td></tr></tbody></table>

{% hint style="success" %}
For more information about bitwise operations, you can read more here: [https://en.wikipedia.org/wiki/Bitwise\_operation](https://en.wikipedia.org/wiki/Bitwise_operation)
{% endhint %}

## ✏️ Assignment Operators

These operators are usually used for compound evaluations and assignments.

| Operator | Name                   | Description                                                                                                                                                                                                          |
| -------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `=`      | Assignment             | <p><code>a = 5</code> The way to assign a value to a variable. You can also assign them to multiple variables by chaining them:<br><code>a=b=c=5</code> which is the same as saying:<br><code>a=5;b=5;c=5</code></p> |
| `+=`     | Compound Add           | `a += b` is equivalent to `a = a + b`                                                                                                                                                                                |
| `-=`     | Compound Substract     | `a -= b` is equivalent to `a = a - b`                                                                                                                                                                                |
| `*=`     | Compound Multiply      | `a *= b` is equivalent to `a = a * b`                                                                                                                                                                                |
| `/+`     | Compound Divide        | `a /= b` is equivalent to `a = a / b`                                                                                                                                                                                |
| `%=`     | Compound Modulus       | `a %= b` is equivalent to `a = a % b`                                                                                                                                                                                |
| `&=`     | Compound Concatenation | <p>A way to concatenate strings together<br><code>a = "hello "</code><br><code>a &#x26;= "luis"</code> The result will be <code>hello luis</code></p>                                                                |
| `&`      | Concatenation          | Concatenates two strings: `"Hola" & space & "Luis"`                                                                                                                                                                  |

## 🔀 Logical Operators

Logical operators perform logic between values or values, usually denoting a `boolean` result.

| Operator   | Name         | Description                                                                                                                                                                                                                                                       |
| ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!,NOT`    | Negation     | `!true = false` or `a = not true`                                                                                                                                                                                                                                 |
| `&&,AND`   | And          | <p>Returns true if both operands are true.<br><code>a = b &#x26;&#x26; c</code></p>                                                                                                                                                                               |
| `\|\|, OR` | Or           | <p>Returns true if either operand is true.<br><code>a = b</code></p>                                                                                                                                                                                              |
| `XOR`      | Exclusive Or | <p>Returns true when either of the operands is true (one is true, and the other is false), but both are not true, and both are not false.<br><code>true XOR true = false</code><br><code>true XOR false = true</code><br><code>false XOR false = false</code></p> |
| `EQV`      | Equivalence  | <p>The exact opposite of an exclusive or. Meaning that it will return true when both operands are either true or false.<br><code>true EQV true = true</code><br><code>true EQV false = false</code><br><code>false EQV false = true</code></p>                    |
| `IMP`      | Implication  | A implies B is equivalent to `if a then b`. A imp b is false ONLY if a is true and b is false; else, it returns true always.                                                                                                                                      |

## Comparison Operators

Comparison operators are used when comparing two values, expressions, or variables. The return of a comparison is either `true` or `false`.

| Operator                                                             | Name                 | Description                                                                                                                                                              |
| -------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `eq, ==`                                                             | Equality             | True if `a eq b` or `a == b`                                                                                                                                             |
| <p><code>neq,</code><br><code>!=,</code><br><code>&#x3C;></code></p> | Not Equal            | The opposite of equality: `a neq b, a != b, a <> b`                                                                                                                      |
| `===`                                                                | Identity             | <p>Returns true if the operands are equal in value and in type.<br><code>2 === "2" // false</code><br><code>2 === 2 // true</code></p>                                   |
| `!===`                                                               | Negated Identity     | Same as the identity operator but negating the result.                                                                                                                   |
| `gt, >`                                                              | Greater than         | If the left operand is greater in value than the right operand                                                                                                           |
| `gte, >=`                                                            | Greater than o equal | If the left operand is greater than or equal in value than the right operand                                                                                             |
| `lt, <`                                                              | Less than            | If the left operand is less than in value than the right operand                                                                                                         |
| `lte, <=`                                                            | Less than or equal   | If the left operand is less than or equal in value than the right operand                                                                                                |
| `contains, ct`                                                       | Contains             | <p>Returns true if the left operand contains the right one.<br><code>'hello' contains 'lo'</code></p>                                                                    |
| `does not contain, nct`                                              | Negated contains     | <p>Returns true if the left operand does NOT contain the right one.<br><code>'hello' does not contain 'pio'</code></p>                                                   |
| `instanceOf`                                                         | Type checking        | <p>Returns true if the left operand is an instance of the right type.<br><code>true instanceOf 'Boolean'</code><br><code>'brad' instanceOf 'java.lang.String'</code></p> |
| `castAs`                                                             | Type casting         | <p>Casts the left operand to the type specified on the right.<br><code>value castAs int</code><br><code>5 castAs String</code></p>                                       |
| `assert`                                                             | Assert an expression | Evaluate an expression and if the expression is falsey it will throw an assert exceptions.                                                                               |

## ✅ Assert Statement <a href="#assert" id="assert"></a>

BoxLang offers an `assert` statement that will evaluate an expression, and if the expression is falsey, it will throw an `AssertionError` exception. The `assert` operator returns `true` if the assertion passes, otherwise throws an exception.

```java
// Asserts that the name is truthy
assert name;

// Assert an expression
assert myService.hasData();
assert name.length() > 3;
assert 5 == 5;  // Passes

// Assert a lambda/closure result - functions are called automatically
assert () -> true
assert () => getUser() != null
```

{% hint style="info" %}
If the assertion expression is a function (closure or lambda), BoxLang automatically invokes it and evaluates the result.
{% endhint %}

### Custom Assertion Messages

You can include a custom message to display if the assertion fails, separated by a colon:

```js
assert user != null : "User must be provided before processing"
assert user.isActive() : "Cannot process an inactive user: #user.name#"
assert price > 0 : "Price must be greater than zero"
```

If the assertion fails, the message is included in the thrown `AssertionError` exception, making it easier to debug failures.

[Try it on try.boxlang.io](https://try.boxlang.io)

## 🏷️ InstanceOf Operator

The `instanceOf` operator checks if an object is an instance of a specified type. It works with both BoxLang types and Java classes.

```java
// BoxLang types
result = true instanceOf 'Boolean'  // true
result = "hello" instanceOf 'String'  // true

// Java classes
result = "brad" instanceOf 'java.lang.String'  // true

// BoxLang classes
class User {}
user = new User()
result = user instanceOf 'User'  // true
```

{% hint style="info" %}
The `instanceOf` operator performs case-insensitive class name matching and supports short names (e.g., `String` instead of `java.lang.String`).
{% endhint %}

[Try it on try.boxlang.io](https://try.boxlang.io)

## 🔄 CastAs Operator

BoxLang provides a native `castAs` operator for type casting. This operator is more fluent and readable than using the `javaCast()` function.

```java
// Casting to primitives
age = value castAs int
price = value castAs double
active = value castAs boolean

// Casting to objects
name = value castAs String
tags = value castAs String[]

// Dynamic type casting
result = {
    age: value castAs int,
    tags: value castAs String[],
    isActive: "#value#" castAs Boolean
}

// Unquoted identifiers are treated as string literals
result = value castAs Long  // Same as castAs "Long"
```

{% hint style="success" %}
The `castAs` operator is integrated into the BoxLang language and is preferred over the `javaCast()` BIF for most type casting scenarios.
{% endhint %}

[Try it on try.boxlang.io](https://try.boxlang.io)

## ❓ Ternary Operator

The ternary operator is a conditional operator that works just like an `if-then-else` statement but in shorthand syntax. It has three operands:

```
condition ? value1 if true : value2 if false
```

The `condition` must evaluate to a `Boolean` value. If `true` then the `value1` will be used, or else `value2` will be used. You can combine this operator with parenthesis, Elvis operators, etc., to build rich expressions.

```javascript
result = ( 10 > 0 ) ? true : false
result = animal eq 'dog' ? 'bark' : 'not a dog'

// More complex approach
result = creditScore > 800 ? "Excellent" :
    ( creditScore > 700 ) ? "Good" :
    ( creditScore > 600 ) ? "Average" : "Bad"
```

## 🎸 Elvis Operator (Null Coalescing)

The Elvis operator is usually referred to as the [null coalescing operator](https://en.wikipedia.org/wiki/Null_coalescing_operator). Its name comes from the symbol it represents, which looks like Elivs hair turned sideways: `?:`. If the expression to the operator's left is `null` , then the expression on the right will be evaluated as the result of the expression.

```
expression ?: defaultValueOrExpression
```

Here is a simple example:

```javascript
function process( result ){
    writeOutput( result ?: "nothing passed" )
}
process() // produces 'nothing passed'
process( "hello" ) // produces 'hello'

displayName = rc.name ?: 'Anonymous'

event
    .getResponse()
    .setError( true )
    .setData( rc.id ?: "" )
```

## 🔧 Function Expressions

In BoxLang, a function invocation can be used as an expression, where the results of the function call is the effective value used.

```javascript
results = ucase( "this is text " ) & toString( 12 + 50 )
```

`Function` is also a proper type, allowing a reference to a function to be passed as an argument to another function or returned from another function as the return value. Functions which accept or return other functions are called higher order functions\*\*.

```javascript
// I can also pass lambdas or anonymous functions as arguments
results = listener( 2 * 3, (result) => result + 1 )
```

## 📦 Collections Operators

Many operators can work on collection objects like arrays, structs, and queries. So let's start investigating them.

### 🛡️ Safe Navigation Operator

The [Safe Navigation operator](https://en.wikipedia.org/wiki/Safe_navigation_operator) avoids accessing a key in a structure or a value in an object that does `null` or doesn't exist. Typically when you have a reference to an object, you might need to verify that it exists before accessing the methods or properties of the object. To avoid this, the safe navigation operator will return `null` instead of throwing an exception, like so:

```javascript
var user = userService.findById( id )
// If user is not found, then this will still work but no exception is thrown.
echo( user?.getSalary() )

s = { name : "luis" }
echo( s.name )
echo( s?.name )
```

### 🌟 Spread Operator

{% hint style="info" %}
Since BoxLang 1.12.x
{% endhint %}

The spread operator expands arrays and structs into function calls and literals.

See [Spread Syntax](syntax/spread-syntax.md) for full coverage.

#### Function Calls

Spread an array as positional arguments.

```javascript
numbers = [ 1, 2, 3 ]
result = sum( ...numbers )
```

Spread a struct as named arguments.

```javascript
person = { first: "Jane", last: "Smith" }
result = greet( ...person )
```

#### Literals

Spread also works inside array and struct literals.

```javascript
myArray = [ 3, 4, ...numbers ]
mergedStruct = { ...defaults, ...overrides }
orderedStruct = [ ...defaults, retries: 5 ]
```

Declaration order wins. Later keys overwrite earlier keys.

```javascript
result = { ...left, ...right, shared: "literal" }
```

### 💤 Rest Operator

{% hint style="info" %}
Since BoxLang 1.12.x
{% endhint %}

The rest operator collects the remaining values into one binding.

It is available in function parameters and destructuring patterns.

```javascript
function findById( entityName, ...ids ){
    return ids
}

findById( "User", 1, 2, 3 ) // [ 1, 2, 3 ]
```

It also works in destructuring:

```javascript
[ first, ...rest ] = values
({ id, ...rest } = payload)
```

See [Destructuring](syntax/destructuring.md) for nested patterns, defaults, and middle-rest behavior.
