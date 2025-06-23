[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Round`

Rounds a number to the closest integer.

## Method Signature

```
Round(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to be rounded. |  |

## Examples

### Round 1.56



<a href="https://try.boxlang.io/?code=eJwryi%2FNS9FQMNQzNVPQtOYCACV1A8k%3D" target="_blank">Run Example</a>

```java
round( 1.56 );

```

Result: 2

### Round 1.49



<a href="https://try.boxlang.io/?code=eJwryi%2FNS9FQMNQzsVTQtOYCACV%2BA8s%3D" target="_blank">Run Example</a>

```java
round( 1.49 );

```

Result: 1

### Round -0.9



<a href="https://try.boxlang.io/?code=eJwryi%2FNS9FQ0NWzVNC05gIAIVoDkw%3D%3D" target="_blank">Run Example</a>

```java
round( -.9 );

```

Result: -1

### Additional Examples


```java
var pi = 3.1415926535;
var pi_rounded = Round( pi, 2 );
echo( pi ); // 3.1415926535
echo( "<br>" );
echo( pi_rounded );
 // 3.14

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
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
