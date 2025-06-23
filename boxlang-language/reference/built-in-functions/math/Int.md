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
