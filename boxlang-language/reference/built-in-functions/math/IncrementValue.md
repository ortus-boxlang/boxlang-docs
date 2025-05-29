
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

There is a difference in the behavior of this function between engines. ACF will return the integer incremented removing the decimal part. Boxlang ( and Lucee ) will increment the integer part but return both.

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
