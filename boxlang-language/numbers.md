---
description: Integers and floats to rule the world!
---

# Numbers

There are two basic kinds of numbers in BoxLang: **integers** (whole numbers) and **floats** (have a decimal point). Internally, each BoxLang engine treats them uniquely and backs up each numerical value as a Java class: `java.lang.Double` or `java.lang.Integer`.

<table><thead><tr><th width="149">Type</th><th width="119">Size (bits)</th><th width="207">Min Value</th><th>Max Value</th></tr></thead><tbody><tr><td><code>Integer</code></td><td>32</td><td>-2,147,483,648 (-231)</td><td>2,147,483,647 (231 - 1)</td></tr></tbody></table>

<table><thead><tr><th width="120">Type</th><th width="114">Size (bits)</th><th width="147">Significant Bits</th><th width="164">Exponent Bits</th><th>Decimal Digits</th></tr></thead><tbody><tr><td><code>Double</code></td><td>64</td><td>53</td><td>11</td><td>15-16</td></tr></tbody></table>

{% hint style="success" %}
**Tip:** If you are dealing with currency or tracking precision, please read about `precisionEvaluate()` to represent big numbers and precision results: [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math/precisionevaluate](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math/precisionevaluate)
{% endhint %}

```javascript
a = 1;
b = 50.1;
writeOutput( a * b );
```

Also, note that BoxLang will do the auto-casting for you when converting between integers and doubles.

## Numeric Type

Once we start looking at functions/closures and lambdas, you will see that you can also type the incoming arguments and results of functions. You also won't need to type it with integer or float, just as `numeric:`

```javascript
numeric function add( numeric a, numeric b ){
    return a + b;
}
```

## Operators & Functions

BoxLang offers tons of mathematical [operators](operators.md#arithmetic-operators) and functions: [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/math)

| abs               | aCos           | arrayAvg       |
| ----------------- | -------------- | -------------- |
| arraySum          | aSin           | atn            |
| bitAnd            | bitMaskClear   | bitMaskRead    |
| bitMaskSet        | bitNot         | bitOr          |
| bitSHLN           | bitSHRN        | bitXor         |
| ceiling           | cos            | decrementValue |
| expt              | fix            | floor          |
| formatBaseN       | incrementValue | inputBaseN     |
| int               | log            | log10          |
| max               | min            | pi             |
| precisionEvaluate | rand           | randomize      |
| randRange         | round          | sgn            |
| sin               | sqr            | tan            |

## Casting/Parsing

BoxLang also has a `toNumeric()` function that you can use to cast a value to a number using different [radixes](https://en.wikipedia.org/wiki/Radix).

```java
toNumeric( "29.5" )
toNumeric( "FF0011", "hex" )
toNumeric( "1010", "bin" )
```

The `parseNumber()` is also used to convert a string number into a numeral system ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/parsenumber](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/parsenumber))

{% hint style="info" %}
In a [positional numeral system](https://en.wikipedia.org/wiki/Positional\_numeral\_system), the radix or base is the number of unique [digits](https://en.wikipedia.org/wiki/Numerical\_digit), including the digit zero, used to represent numbers. For example, for the [decimal system](https://en.wikipedia.org/wiki/Decimal) (the most common system in use today) the radix is ten, because it uses the ten digits from 0 through 9.
{% endhint %}

## Is it a number?

BoxLang provides the `isNumeric()` function to determine if the passed value can be converted to a numeric value.

```java
isNumeric( 23 ) // yes
isNumeric( "twenty" ) // no
isNumeric( 5e2 ) // yes
```

## Repeating Instructions

Number variables can be used to repeat instructions. Like in many other languages, BoxLang supports the `for`, `while` and `loop` constructs:

```javascript
for( var i = 0; i <= 10; i++ ){
    writeOutput( "Showing day " & i );
}

i =1;
while( i <= 10 ){
    writeOutput( "Showing day " & i++ );
}
```

{% hint style="info" %}
Please note that the syntax varies from tag to script, so refer to the docs for subtle differences. Please also note that you can iterate over structures, arrays, queries, and objects in BoxLang; we will see this in later sections.

See [https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/loop](https://boxlang.ortusbooks.com/boxlang-language/reference/components/system/loop) for more information
{% endhint %}
