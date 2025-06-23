[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DecrementValue`

Decrement the integer part of a number

## Method Signature

```
DecrementValue(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to decrement the integer part of. |  |

## Examples

### Decrement 7



<a href="https://try.boxlang.io/?code=eJxLSU0uSs1NzSsJS8wpTdVQMFfQtOYCAFb4BsI%3D" target="_blank">Run Example</a>

```java
decrementValue( 7 );

```

Result: 6

### Decrement 7.5

<a href="https://try.boxlang.io/?code=eJxLSU0uSs1NzSsJS8wpTdVQMNczVdC05gIAZX0HJQ%3D%3D" target="_blank">Run Example</a>

```java
decrementValue( 7.5 );

```

Result: 6.5

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUEhJTS5KzU3NKwlLzClN1VAwU9BU0LRW0NdXMOUqx6NMzxSskAusUs%2BUCwB4Shib" target="_blank">Run Example</a>

```java
writeDump( decrementValue( 6 ) ); // 5
writeDump( decrementValue( 6.5 ) );
 // 5.5

```



## Related

  * [Abs](./Abs.md)
  * [Acos](./Acos.md)
  * [Asin](./Asin.md)
  * [Atn](./Atn.md)
  * [Ceiling](./Ceiling.md)
  * [Cos](./Cos.md)
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
