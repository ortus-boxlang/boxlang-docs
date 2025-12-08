---
description: Integers and floats to rule the world!
icon: arrow-down-1-9
---

# Numbers

There are two basic kinds of numbers in BoxLang: **integers** (whole numbers) and **floats** (have a decimal point). BoxLang provides sophisticated number handling with automatic type promotion and high-precision arithmetic.

## 🔢 Number Types

BoxLang uses Java's numeric types internally:

| Type | Size (bits) | Range | Usage |
|------|-------------|-------|-------|
| `Integer` | 32 | -2,147,483,648 to 2,147,483,647 | Whole numbers |
| `Long` | 64 | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | Large whole numbers |
| `Double` | 64 | ±4.9E-324 to ±1.7976931348623157E308 | Decimal numbers (15-16 digits precision) |
| `BigDecimal` | Arbitrary | Unlimited precision | High-precision calculations, currency |
| `BigInteger` | Arbitrary | Unlimited size | Very large whole numbers |

## 🎯 Type Promotion & Type Contagion

BoxLang is smart enough to automatically promote numeric types at runtime with **no need for explicit casting**. This is called **type contagion** - when you mix different numeric types in an operation, BoxLang automatically promotes to the most appropriate type:

```js
// Integer operations stay as integers
result = 10 + 5  // Integer: 15

// Mixing integer and decimal promotes to decimal
result = 10 + 5.5  // Double: 15.5

// Large numbers automatically become BigDecimal/BigInteger
result = 111111111111111111111111111 + 222222222222222222222222222
// BigInteger: 333333333333333333333333333

// Decimal operations use BigDecimal for precision
result = 0.1 + 0.2  // BigDecimal: 0.3 (not 0.30000000000000004!)

// Mixed operations promote to the highest precision type
intVal = 10
doubleVal = 5.5
bigDecVal = 100.123456789
result = intVal + doubleVal + bigDecVal  // BigDecimal
```

{% hint style="success" %}
**No Precision Loss!** BoxLang automatically uses `BigDecimal` for decimal operations to avoid floating-point precision issues. For example, `(0.1 + 0.2)` correctly returns `0.3`, not `0.30000000000000004` like in other languages.
{% endhint %}

## ⚡ High Precision Math

**High precision math is enabled by default** in BoxLang! This means BoxLang automatically uses `BigDecimal` for decimal arithmetic to maintain precision:

```js
// Automatic high precision
result = 1.0 / 3.0  // BigDecimal with full precision

// No precision loss in calculations
total = 0.1 + 0.2 + 0.3  // Exactly 0.6

// Currency calculations are safe
price = 19.99
quantity = 3
total = price * quantity  // Exactly 59.97
```

You can configure high precision math in your `boxlang.json` configuration:

```json
{
    // By default BoxLang uses high-precision mathematics via BigDecimal operations
    // You can turn this off here for all applications
    "useHighPrecisionMath": true,
}
```

{% hint style="info" %}
**Configuration Options:**
- `highPrecisionMath` - Enable/disable automatic BigDecimal usage (default: `true`)
- `mathPrecision` - Number of significant digits (default: `128`)
- `mathRoundingMode` - Rounding strategy: `HALF_UP`, `HALF_DOWN`, `CEILING`, `FLOOR`, etc.
- Use the `ortus.boxlang.runtime.types.util.MathUtil` to change other parameters for high precision math.
{% endhint %}

### 💰 PrecisionEvaluate for Complex Expressions

For string-based math expressions requiring guaranteed precision, use `precisionEvaluate()`, or if you disable high precision math:

```js
// Evaluate complex expressions with full precision
result = precisionEvaluate("1/3 + 2/3")  // Exactly 1.0
result = precisionEvaluate("(10.5 * 3) + (7.2 / 4)")  // Precise calculation
```

{% hint style="warning" %}
`precisionEvaluate()` works with `+`, `-`, `*`, `/`, `()`, and `MOD` operators. Other operators (`^`, `%`, `\`) will use standard precision.
{% endhint %}

[Learn more about precisionEvaluate()](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math/precisionevaluate)

## 🧮 Basic Arithmetic

```js
a = 1
b = 50.1
writeOutput( a * b )  // 50.1 (automatic type promotion)

// All basic operations
sum = 10 + 5        // 15
diff = 10 - 5       // 5
product = 10 * 5    // 50
quotient = 10 / 5   // 2
power = 10 ^ 2      // 100
modulo = 10 % 3     // 1
```

[Try it online!](https://try.boxlang.io)

## 🏷️ The `numeric` Type

When typing function arguments and return values, use the `numeric` type instead of specific types like `integer` or `double`. This allows BoxLang's type promotion to work naturally:

```js
numeric function add( numeric a, numeric b ) {
    return a + b
}

// Works with any numeric type
result = add(10, 5)           // Integer inputs
result = add(10.5, 5.2)       // Double inputs
result = add(10, 5.5)         // Mixed inputs - automatic promotion
```

[Try it online!](https://try.boxlang.io)

## 📚 Mathematical Built-In Functions (BIFs)

BoxLang provides comprehensive mathematical functions organized by category:

### 🔢 Basic Math Operations

| Function | Purpose | Example |
|----------|---------|----------|
| `abs()` | Absolute value | `abs(-5)` → `5` |
| `ceiling()` | Round up to integer | `ceiling(4.3)` → `5` |
| `floor()` | Round down to integer | `floor(4.7)` → `4` |
| `round()` | Round to nearest integer/decimal | `round(4.567, 2)` → `4.57` |
| `fix()` | Convert to integer (truncate) | `fix(4.7)` → `4` |
| `int()` | Closest smaller integer | `int(4.7)` → `4` |
| `sgn()` | Sign of number (-1, 0, 1) | `sgn(-5)` → `-1` |
| `max()` | Maximum of two numbers | `max(10, 20)` → `20` |
| `min()` | Minimum of two numbers | `min(10, 20)` → `10` |

### 📐 Trigonometric Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `sin()` | Sine (radians) | `sin(pi()/2)` → `1` |
| `cos()` | Cosine (radians) | `cos(0)` → `1` |
| `tan()` | Tangent (radians) | `tan(pi()/4)` → `1` |
| `asin()` | Arc sine (inverse) | `asin(1)` → `1.5708` |
| `acos()` | Arc cosine (inverse) | `acos(1)` → `0` |
| `atn()` | Arc tangent (inverse) | `atn(1)` → `0.7854` |
| `pi()` | Value of π | `pi()` → `3.14159...` |

### 📊 Exponential & Logarithmic

| Function | Purpose | Example |
|----------|---------|----------|
| `exp()` | Exponential (e^x) | `exp(1)` → `2.71828` |
| `log()` | Natural logarithm | `log(10)` → `2.302585` |
| `log10()` | Base-10 logarithm | `log10(100)` → `2` |
| `sqr()` | Square root | `sqr(16)` → `4` |

### 🎲 Random Number Generation

| Function | Purpose | Example |
|----------|---------|----------|
| `rand()` | Random float (0 to 1) | `rand()` → `0.742351` |
| `randRange()` | Random integer in range | `randRange(1, 100)` → `42` |
| `randomize()` | Seed random generator | `randomize(12345)` |

### 🔧 Number Manipulation

| Function | Purpose | Example |
|----------|---------|----------|
| `incrementValue()` | Increment integer part | `incrementValue(4.7)` → `5.7` |
| `decrementValue()` | Decrement integer part | `decrementValue(4.7)` → `3.7` |
| `formatBaseN()` | Convert to base-N string | `formatBaseN(255, 16)` → `\"FF\"` |
| `inputBaseN()` | Parse base-N string | `inputBaseN(\"FF\", 16)` → `255` |

### 🔨 Bitwise Operations

| Function | Purpose | Example |
|----------|---------|----------|
| `bitAnd()` | Bitwise AND | `bitAnd(12, 10)` → `8` |
| `bitOr()` | Bitwise OR | `bitOr(12, 10)` → `14` |
| `bitXor()` | Bitwise XOR | `bitXor(12, 10)` → `6` |
| `bitNot()` | Bitwise NOT | `bitNot(12)` → `-13` |
| `bitSHLN()` | Shift left | `bitSHLN(5, 2)` → `20` |
| `bitSHRN()` | Shift right | `bitSHRN(20, 2)` → `5` |
| `bitMaskSet()` | Set bits in mask | `bitMaskSet(0, 0, 3)` → `7` |
| `bitMaskClear()` | Clear bits in mask | `bitMaskClear(7, 0, 2)` → `4` |
| `bitMaskRead()` | Read bits from mask | `bitMaskRead(7, 0, 2)` → `3` |

### 🎯 High Precision

| Function | Purpose | Example |
|----------|---------|----------|
| `precisionEvaluate()` | Evaluate with BigDecimal | `precisionEvaluate(\"1/3 + 2/3\")` → `1.0` |

{% hint style="success" %}
**Complete Reference**: For detailed documentation of each function, visit the [Math BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math).
{% endhint %}

## ⚙️ Member Functions

All numeric BIFs can be called as member functions on number variables:

```js
num = 42.7

// Basic math
num.abs()           // 42.7
num.ceiling()       // 43
num.floor()         // 42
num.round()         // 43
num.round(1)        // 42.7
num.sgn()           // 1

// Trigonometric
angle = 1.5708
angle.sin()         // 1.0
angle.cos()         // 0.0
angle.tan()         // Infinity

// Logarithmic
num.log()           // Natural log
num.log10()         // Base-10 log
num.exp()           // e^num
num.sqr()           // Square root

// Comparison
num.max(50)         // 50
num.min(50)         // 42.7

// Manipulation
num.incrementValue() // 43.7
num.decrementValue() // 41.7
num.fix()           // 42
num.int()           // 42
```

### Java Number Methods

Since BoxLang numbers are Java objects, you also have access to Java methods:

```js
import java.lang.Math
import java.math.BigDecimal

// Integer/Long methods
num = 42
num.toString()              // "42"
num.longValue()             // 42L
num.doubleValue()           // 42.0
Math.abs(num)              // 42

// BigDecimal methods (when using high precision)
bigNum = 123.456789
bigNum.scale()              // Number of decimal places
bigNum.precision()          // Total significant digits
bigNum.add(10)             // 133.456789
bigNum.subtract(3)         // 120.456789
bigNum.multiply(2)         // 246.913578
bigNum.divide(3, 10)       // Divide with scale
bigNum.setScale(2)         // Round to 2 decimals

// Math class methods
Math.sqrt(16)              // 4.0
Math.pow(2, 8)             // 256.0
Math.random()              // Random 0.0-1.0
Math.ceil(4.3)             // 5.0
Math.floor(4.7)            // 4.0
Math.round(4.5)            // 5
```


## 🔄 Casting/Parsing

While BoxLang automatically handles type promotion, you can explicitly convert values to numbers:

```js
// Basic conversion
toNumeric("29.5")                // 29.5
toNumeric("42")                  // 42

// Different radix/base conversions
toNumeric("FF", "hex")          // 255 (hexadecimal)
toNumeric("1010", "bin")        // 10 (binary)
toNumeric("77", "oct")          // 63 (octal)

// Parse with radix
val("123abc")                    // 123 (extracts leading number)
inputBaseN("FF", 16)            // 255 (hex to decimal)
formatBaseN(255, 16)            // "FF" (decimal to hex)
```

The `parseNumber()` function converts strings to numbers in different numeral systems:

```js
parseNumber("1,234.56", "en")   // 1234.56
parseNumber("1.234,56", "de")   // 1234.56 (German format)
```

[Learn more about parseNumber()](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/parsenumber)

{% hint style="info" %}
**Radix/Base Systems**: A [radix](https://en.wikipedia.org/wiki/Radix) (or base) is the number of unique digits used to represent numbers. Common systems: decimal (base 10: 0-9), binary (base 2: 0-1), octal (base 8: 0-7), hexadecimal (base 16: 0-9, A-F).
{% endhint %}

[Try it online!](https://try.boxlang.io)

## ✅ Is it a number?

Use `isNumeric()` to check if a value can be converted to a number:

```js
isNumeric(23)           // true
isNumeric("42")         // true
isNumeric("42.5")       // true
isNumeric("twenty")     // false
isNumeric(5e2)          // true (scientific notation)
isNumeric("0xFF")       // true (hex literal)
isNumeric("1,234.56")   // false (contains comma)
isNumeric(true)         // true (true = 1, false = 0)
```

[Try it online!](https://try.boxlang.io)

## 🔁 Looping with Numbers

Numbers are commonly used in loops for repetition and iteration:

```js
// For loop
for (var i = 1; i <= 10; i++) {
    writeOutput("Day #i#")
}

// While loop
i = 1
while (i <= 10) {
    writeOutput("Day #i#")
    i++
}

// Loop construct
loop from="1" to="10" index="i" {
    writeOutput("Day #i#")
}

// Times helper
10.times((i) => {
    writeOutput("Iteration #i#")
})
```

{% hint style="info" %}
BoxLang provides multiple looping constructs. You can also iterate over arrays, structures, queries, and objects. See the [Loop component reference](https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/loop) for details.
{% endhint %}

[Try it online!](https://try.boxlang.io)

## 🔗 Related Documentation

- [Math BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math) - Complete list of mathematical functions
- [Numeric Type Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/types/numeric) - Member function documentation
- [Operators](operators.md) - Arithmetic and bitwise operators
- [Java Number API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html) - Native Java methods
- [Java BigDecimal API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigDecimal.html) - High precision arithmetic
- [Java Math API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Math.html) - Java Math class methods
