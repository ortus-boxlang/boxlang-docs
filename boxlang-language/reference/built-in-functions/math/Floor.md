[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Floor`

Round a number down to the nearest integer

## Method Signature

```
Floor(number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to round down to the nearest integer |  |

## Examples

### Floor Value of 4.0



<a href="https://try.boxlang.io/?code=eJxLy8nPL9JQMNEzUNC05gIAIN4Diw%3D%3D" target="_blank">Run Example</a>

```java
floor( 4.0 );

```

Result: 4

### Floor Value of 4.3



<a href="https://try.boxlang.io/?code=eJxLy8nPL9JQMNEzVtC05gIAIO0Djg%3D%3D" target="_blank">Run Example</a>

```java
floor( 4.3 );

```

Result: 4

### Floor Value of 4.7



<a href="https://try.boxlang.io/?code=eJxLy8nPL9JQMNEzV9C05gIAIQEDkg%3D%3D" target="_blank">Run Example</a>

```java
floor( 4.7 );

```

Result: 4

### Floor Value of -4.3



<a href="https://try.boxlang.io/?code=eJxLy8nPL9JQ0DXRM1bQtOYCACTAA7s%3D" target="_blank">Run Example</a>

```java
floor( -4.3 );

```

Result: -5

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBIy8nPL9JQMNIzUNBU0LRW0NdXMOJKQZYy1zOCS5mjSpnoWcKlTFCldE31zMFyXCBJXTMuAEgSGwg%3D" target="_blank">Run Example</a>

```java
dump( floor( 2.0 ) ); // 2
dump( floor( 7.2 ) ); // 7
dump( floor( 4.9 ) ); // 4
dump( floor( -5.7 ) );
 // -6

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
