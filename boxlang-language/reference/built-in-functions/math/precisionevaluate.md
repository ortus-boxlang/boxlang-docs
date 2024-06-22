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
