[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Exp`

Calculates the exponent whose base is e that represents a number.

## Method Signature

```
Exp(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to calculate the exponent for. |  |

## Examples

### exponent of 1.13140211149

The result could vary depending on if the server is running windows or linux.  On a windows box the result will be round to 3.1

<a href="https://try.boxlang.io/?code=eJxLrSjQUDDUMzQ2NDEwMjQ0NLFU0LTmAgA9twSu" target="_blank">Run Example</a>

```java
exp( 1.13140211149 );

```

Result: 3.099999999991346707809724952544356

### Additional Examples


```java
<bx:output>#exp( 10 )#</bx:output>
```



## Related

  * [Abs](./Abs.md)
  * [Acos](./Acos.md)
  * [Asin](./Asin.md)
  * [Atn](./Atn.md)
  * [Ceiling](./Ceiling.md)
  * [Cos](./Cos.md)
  * [DecrementValue](./DecrementValue.md)
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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
