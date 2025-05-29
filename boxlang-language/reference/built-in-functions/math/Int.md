[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Int`

Returns the closest integer that is smaller than the number

## Method Signature

```
Int(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to calculate the closest integer for |  |

## Examples

### Closest integer less than 1.8



<a href="https://try.boxlang.io/?code=eJzLzCvRUDDUs1DQtOYCABWgArk%3D" target="_blank">Run Example</a>

```java
int( 1.8 );

```

Result: 1

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMjMK9FQMNczUNBU0LRW0NdXMOcqR5M107OEy5phyOoaQaW5QPK6xlwAzC4YAw%3D%3D" target="_blank">Run Example</a>

```java
writeDump( int( 7.0 ) ); // 7
writeDump( int( 6.9 ) ); // 6
writeDump( int( -2.9 ) );
 // -3

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
