[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Atn`

Returns the arc tangent (inverse tangent) of a number

## Method Signature

```
Atn(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to calculate the arc tangent of |  |

## Examples

### Arctangent of 0.3



<a href="https://try.boxlang.io/?code=eJxLLMnTUNAzVtC05gIAEkoCew%3D%3D" target="_blank">Run Example</a>

```java
atn( .3 );

```

Result: 0.2911599378021857457108346581625601

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLzEvPSY0vScxLT80rUbBVMLTmSinNLdBQcCzJ01BIRJHVVNC05lLQ11cw0DO3MDW2tDA0Mza2NFfIzFMoSkzJTMwr5gIA5RQXZg%3D%3D" target="_blank">Run Example</a>

```java
angle_tangent = 1;
dump( Atn( angle_tangent ) );
 // 0.785398163397 in radians

```



## Related

  * [Abs](./Abs.md)
  * [Acos](./Acos.md)
  * [Asin](./Asin.md)
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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
