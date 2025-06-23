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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
