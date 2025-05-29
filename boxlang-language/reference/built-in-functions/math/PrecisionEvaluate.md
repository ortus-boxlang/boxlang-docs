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

  * [Sqr](./Sqr.md)
  * [Asin](./Asin.md)
  * [Sgn](./Sgn.md)
  * [Pi](./Pi.md)
  * [DecrementValue](./DecrementValue.md)
  * [InputBaseN](./InputBaseN.md)
  * [Round](./Round.md)
  * [Cos](./Cos.md)
  * [Int](./Int.md)
  * [Exp](./Exp.md)
  * [Ceiling](./Ceiling.md)
  * [RandRange](./RandRange.md)
  * [Atn](./Atn.md)
  * [Fix](./Fix.md)
  * [Max](./Max.md)
  * [Min](./Min.md)
  * [Abs](./Abs.md)
  * [Log](./Log.md)
  * [Log10](./Log10.md)
  * [Acos](./Acos.md)
  * [Rand](./Rand.md)
  * [Floor](./Floor.md)
  * [Randomize](./Randomize.md)
  * [FormatBaseN](./FormatBaseN.md)
  * [Tan](./Tan.md)
  * [Sin](./Sin.md)
  * [IncrementValue](./IncrementValue.md)
