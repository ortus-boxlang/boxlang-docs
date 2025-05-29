[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Sgn`

Determine the sign of a number

## Method Signature

```
Sgn(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to determine the sign of. |  |

## Examples

### Sign of any number greater than 0



<a href="https://try.boxlang.io/?code=eJwrTs%2FTUNAzVtC05gIAEo4CgA%3D%3D" target="_blank">Run Example</a>

```java
sgn( .3 );

```

Result: 1

### Sign of 0



<a href="https://try.boxlang.io/?code=eJwrTs%2FTUDBQ0LTmAgAP2gJP" target="_blank">Run Example</a>

```java
sgn( 0 );

```

Result: 0

### Sign of any number less than 0



<a href="https://try.boxlang.io/?code=eJwrTs%2FTUNDVM1bQtOYCABVaAq0%3D" target="_blank">Run Example</a>

```java
sgn( -.3 );

```

Result: -1

### Additional Examples


```java
15 = <bx:output>#sgn( 15 )#</bx:output><br>
-15 = <bx:output>#sgn( -15 )#</bx:output>
```



## Related

  * [Sqr](./Sqr.md)
  * [Asin](./Asin.md)
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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Acos](./Acos.md)
  * [Rand](./Rand.md)
  * [Floor](./Floor.md)
  * [Randomize](./Randomize.md)
  * [FormatBaseN](./FormatBaseN.md)
  * [Tan](./Tan.md)
  * [Sin](./Sin.md)
  * [IncrementValue](./IncrementValue.md)
