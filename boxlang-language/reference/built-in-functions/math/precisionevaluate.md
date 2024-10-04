# PrecisionEvaluate

Evaluates one or more string expressions using BigDecimal precision arithmetic.

If the results ends in an infinitely repeating decimal value only the first 20 digits of the decimal portion will be used. BigDecimal precision results only work with addition, subtraction, multiplication and division. The use of ^, MOD, % or \ arithmetic operators will result in normal integer precision.

## Method Signature

```
PrecisionEvaluate(expressions=[string])
```

### Arguments

| Argument      | Type     | Required | Description             | Default |
| ------------- | -------- | -------- | ----------------------- | ------- |
| `expressions` | `string` | `true`   | Expressions to evaluate |         |

## Examples

## Related

* [Abs](abs.md)
* [Acos](acos.md)
* [Asin](asin.md)
* [Atn](atn.md)
* [Ceiling](ceiling.md)
* [Cos](cos.md)
* [DecrementValue](decrementvalue.md)
* [Exp](exp.md)
* [Fix](fix.md)
* [Floor](floor.md)
* [FormatBaseN](formatbasen.md)
* [IncrementValue](incrementvalue.md)
* [InputBaseN](inputbasen.md)
* [Int](int.md)
* [Log](log.md)
* [Log10](log10.md)
* [Max](max.md)
* [Min](min.md)
* [Pi](pi.md)
* [Rand](rand.md)
* [Randomize](randomize.md)
* [RandRange](randrange.md)
* [Round](round.md)
* [Sgn](sgn.md)
* [Sin](sin.md)
* [Sqr](sqr.md)
* [Tan](tan.md)
