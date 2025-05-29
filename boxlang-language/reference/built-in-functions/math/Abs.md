[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Abs`

Returns the absolute value of a number

## Method Signature

```
Abs(value=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `numeric` | `true` | The number to return the absolute value of |  |

## Examples

### Absolute Value of -4.3



<a href="https://try.boxlang.io/?code=eJxLTCrWUNA10TNW0LTmAgAXlQLP" target="_blank">Run Example</a>

```java
abs( -4.3 );

```

Result: 4.3

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLTCoOS8xRsFVITCrWUDBU0LTmSinNLdAA8UESQH4iqhI9IhTpEqUGu0kA9Lso%2BQ%3D%3D" target="_blank">Run Example</a>

```java
absVal = abs( 1 );
dump( absVal );
absVal = abs( 1.1 );
dump( absVal );
absVal = abs( -1 );
dump( absVal );
absVal = abs( -1.1 );
dump( absVal );

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
  * [Log](./Log.md)
  * [Log10](./Log10.md)
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Acos](./Acos.md)
  * [Rand](./Rand.md)
  * [Floor](./Floor.md)
  * [Randomize](./Randomize.md)
  * [FormatBaseN](./FormatBaseN.md)
  * [Tan](./Tan.md)
  * [Sin](./Sin.md)
  * [IncrementValue](./IncrementValue.md)
