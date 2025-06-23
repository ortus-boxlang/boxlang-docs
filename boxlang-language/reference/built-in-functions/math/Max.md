[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Max`

Return larger of two numbers

## Method Signature

```
Max(number1=[numeric], number2=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `numeric` | `true` | The first number |  |
| `number2` | `numeric` | `true` | The second number |  |

## Examples

### Tag Example

 


```java
<bx:set myNum1 = 4 > 
<bx:set myNum2 = 9 > 
<bx:output>The maximum of #myNum1# and #myNum2# numbers is #max( myNum1, myNum2 )#.</bx:output>
```

Result: The maximum of 4 and 9 is 9.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLTc7I11DITazQUDAx1bM00VEwNtEzMFXQVNC05lLQ11fILy0pKC0phshyAQAdHguH" target="_blank">Run Example</a>

```java
echo( max( 45.94, 34.05 ) );
 // outputs 45.94

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
