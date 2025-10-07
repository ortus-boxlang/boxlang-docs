[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `PrecisionEvaluate`

Evaluates one or more string expressions using BigDecimal precision arithmetic.

If the results ends in an infinitely repeating decimal value only the first 20 digits of the decimal
 portion will be used. BigDecimal precision results only work with addition, subtraction,
 multiplication and division. The use of ^, MOD, % or \ arithmetic operators will result in
 normal integer precision.

## Method Signature

```
PrecisionEvaluate(expressions=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `expressions` | `string` | `true` | Expressions to evaluate |  |

## Examples

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

### Additional Examples


```java
dump( (59 + 10.99) * 100 ); // 6998.999999999999
dump( PrecisionEvaluate( "( 59+10.99 ) * 100" ) );
 // 6999

```



## Related

  * [Abs](./Abs.md)
  * [Acos](./Acos.md)
  * [Asin](./Asin.md)
  * [Atn](./Atn.md)
  * [Ceiling](./Ceiling.md)
  * [Cos](./Cos.md)
  * [DecrementValue](./DecrementValue.md)
  * [Exp](./Exp.md)
  * [Fix](./Fix.md)
  * [Floor](./Floor.md)
  * [FormatBaseN](./FormatBaseN.md)
  * [IncrementValue](./IncrementValue.md)
  * [InputBaseN](./InputBaseN.md)
  * [Int](./Int.md)
  * [Log](./Log.md)
  * [Log10](./Log10.md)
  * [Max](./Max.md)
  * [Min](./Min.md)
  * [Pi](./Pi.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
