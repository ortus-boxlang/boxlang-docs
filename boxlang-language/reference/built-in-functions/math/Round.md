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

  * [Sqr](./Sqr.md)
  * [Asin](./Asin.md)
  * [Sgn](./Sgn.md)
  * [Pi](./Pi.md)
  * [DecrementValue](./DecrementValue.md)
  * [InputBaseN](./InputBaseN.md)
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
