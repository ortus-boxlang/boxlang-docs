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

  * [Abs](./Abs.md)
  * [Acos](./Acos.md)
  * [Asin](./Asin.md)
  * [Atn](./Atn.md)
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
