[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IncrementValue`

Increment the integer part of a number

## Method Signature

```
IncrementValue(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to increment the integer part of. |  |

## Examples

### Increment 7



<a href="https://try.boxlang.io/?code=eJzLzEsuSs1NzSsJS8wpTdVQMFfQtOYCAFgVBtA%3D" target="_blank">Run Example</a>

```java
incrementValue( 7 );

```

Result: 8

### Increment 7.5

There is a difference between BL engines. ACF will return the integer incremented removing the decimal part. Boxlang will increment the integer part but return both.

<a href="https://try.boxlang.io/?code=eJzLzEsuSs1NzSsJS8wpTdVQMNczVdC05gIAZrYHMw%3D%3D" target="_blank">Run Example</a>

```java
incrementValue( 7.5 );

```

Result: 8.5

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLK81VsFUwNLO05iovyixJdSnNLdBQyMxLLkrNTc0rKUvMKU3VUMgDqtJU0LTmygMr1zMlUjkApk4eFQ%3D%3D" target="_blank">Run Example</a>

```java
num = 169;
writeDump( incrementvalue( num ) );
num = .59;
writeDump( incrementvalue( num ) );

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
