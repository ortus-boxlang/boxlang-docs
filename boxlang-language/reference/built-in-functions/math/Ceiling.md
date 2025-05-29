[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Ceiling`

Determines the closest integer that is greater than a specified floating point number.

## Method Signature

```
Ceiling(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number for which to find the ceiling value. |  |

## Examples

### Ceiling of 1.1



<a href="https://try.boxlang.io/?code=eJxLTs3MycxL11Aw1DNU0LTmAgAsVARC" target="_blank">Run Example</a>

```java
ceiling( 1.1 );

```

Result: 2

### Ceiling of 1

When ceiling an integer the result is equal to the value passed

<a href="https://try.boxlang.io/?code=eJxLTs3MycxL11AwVNC05gIAI6ED4w%3D%3D" target="_blank">Run Example</a>

```java
ceiling( 1 );

```

Result: 1

### Additional Examples


```java
<bx:output>
    1.2: #ceiling( 1.2 )# <!--- 1.2: 2 ---><br> 
    1.5: #ceiling( 1.5 )# <!--- 1.5: 2 ---><br> 
    1.7: #ceiling( 1.7 )# <!--- 1.7: 2 ---><br> 
</bx:output>
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
