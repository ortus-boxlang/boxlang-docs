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

  * [Sqr](./Sqr.md)
  * [Asin](./Asin.md)
  * [Sgn](./Sgn.md)
  * [Pi](./Pi.md)
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
