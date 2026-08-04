[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `PrecisionEvaluate`

Evaluates one or more string expressions dynamically from left to right using BigDecimal precision arithmetic.

Note, this is provided for compat. It acutally works the same as evaluate() and will use the same high precision
 math setting that Boxlang is configured with. BoxLang will always use high precision math by default.

## Method Signature

```
PrecisionEvaluate(expression=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `expression` | `string` | `true` | Expression to evaluate. String expressions can be complex. |  |

## Examples

## Description

Evaluates one or more string expressions dynamically from left to right, using BigDecimal precision arithmetic to calculate arbitrary-precision arithmetic expressions.

## Returns

An object containing the result of the evaluations. The result is the value returned by the rightmost expression.

## Category

Mathematical functions, Dynamic evaluation functions

## Function Syntax

```java
precisionEvaluate( string_expression1 [, string_expression2, ... ] )
```

## Parameters

| Parameter | Description |
| --- | --- |
| `string_expression1`, `string_expression2`, ... | Expressions to evaluate. Expressions are evaluated from left to right, and the result of an expression on the left can be used by an expression on the right. |

## Usage

`precisionEvaluate` calculates arbitrarily long decimal values using BigDecimal precision arithmetic. BigDecimal arithmetic accepts and generates decimal numbers of any length without using exponential notation.

Precision arithmetic applies to addition, subtraction, multiplication, and division. Exponentiation (`^`), modulus (`MOD` or `%`), and integer division use normal integer or floating-point arithmetic instead of returning BigDecimal values.

This function differs from `evaluate` in its use of BigDecimal precision arithmetic. If an expression contains a single- or double-quotation mark, the mark must be escaped. If an expression such as `1/3` results in an infinitely repeating decimal value, the decimal portion is limited to 20 digits.

For better processing efficiency, do not put arithmetic expressions in quotation marks. `precisionEvaluate( a * b )` compiles more efficiently than `precisionEvaluate( "a * b" )`, although both forms produce the same result.

## Example

```java
num1 = 5;
num2 = 3 / 8;
writeOutput( "The resultant expression is: " & precisionEvaluate( num1 / num2 ) );
```

Output:

```text
The resultant expression is: 13.33333333333333333333
```

## Additional Examples

### precisionEvaluate of 1/3 plus 5

1/3 is calculated then 5 is added to the total.  Display is limited to 20 threes.

<a href="https://try.boxlang.io/?code=eJwrKEpNzizOzM9zLUvMKU0sSdVQMFTQVzBW0FYwVdC05gIAu0AJTQ%3D%3D" target="_blank">Run Example</a>

```java
precisionEvaluate( 1 / 3 + 5 );

```

Result: 5.333333333333333333333333333333333

### precisionEvaluate of 1/(7*12)

Calculate 1 divided by the product of 7 x 12

<a href="https://try.boxlang.io/?code=eJwrKEpNzizOzM9zLUvMKU0sSdVQMFTQV9AwV9BSMDTSVNC05gIA2IoJzw%3D%3D" target="_blank">Run Example</a>

```java
precisionEvaluate( 1 / (7 * 12) );

```

Result: 0.0119047619047619047619047619047619

```java
dump( (59 + 10.99) * 100 ); // 6998.999999999999
dump( PrecisionEvaluate( "( 59+10.99 ) * 100" ) );
 // 6999

```

## Related

  * [Evaluate](./Evaluate.md)
