[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Min`

Return larger of two numbers

## Method Signature

```
Min(number1=[numeric], number2=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `numeric` | `true` | The first number |  |
| `number2` | `numeric` | `true` | The second number |  |

## Examples

### Minimum of 4 and 9




```java
<bx:set myNum1 = 4 > 
<bx:set myNum2 = 9 > 
<bx:output>The minimum of #myNum1# and #myNum2# numbers is #min( myNum1, myNum2 )#.</bx:output>
```

Result: The minimum of 4 and 9 is 4.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLTc7I11DIzczTUDDUUTBV0FTQtOYCAEIwBP0%3D" target="_blank">Run Example</a>

```java
echo( min( 1, 5 ) );

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
  * [Abs](./Abs.md)
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
