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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
