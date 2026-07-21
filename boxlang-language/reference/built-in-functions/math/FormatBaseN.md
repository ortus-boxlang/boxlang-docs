[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FormatBaseN`

Converts a number to a string representation in the specified base.

## Method Signature

```
FormatBaseN(number=[numeric], radix=[integerTruncate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `numeric` | `true` | The number to convert to the specified base. |  |
| `radix` | `integerTruncate` | `true` | The base to convert the number to, in the range 2-36. |  |

## Examples

### Format 10 as dual number



<a href="https://try.boxlang.io/?code=eJxLyy%2FKTSxxSixO9dNQMDTQUTBS0LTmAgBU9gYI" target="_blank">Run Example</a>

```java
formatBaseN( 10, 2 );

```

Result: 1010

### Format 1024 as hexadecimal number



<a href="https://try.boxlang.io/?code=eJxLyy%2FKTSxxSixO9dNQMDQwMtFRMDRT0LTmAgBpOAaj" target="_blank">Run Example</a>

```java
formatBaseN( 1024, 16 );

```

Result: 400

### Format 125 as decimal number



<a href="https://try.boxlang.io/?code=eJxLyy%2FKTSxxSixO9dNQMDQy1VEwNFDQtOYCAGJHBm4%3D" target="_blank">Run Example</a>

```java
formatBaseN( 125, 10 );

```

Result: 125

### Format a float

Floors float to integer then formats with radix given

<a href="https://try.boxlang.io/?code=eJxLyy%2FKTSxxSixO9dNQMDTQMzfVUTBS0LTmAgBpTQai" target="_blank">Run Example</a>

```java
formatBaseN( 10.75, 2 );

```

Result: 1010

### Additional Examples


```java
<bx:output>
  #formatBaseN( 15, 2 )# <!--- 1111 (binary) ---> 
  #formatBaseN( 15, 16 )# <!--- f (hexadecimal) ---> 
  #formatBaseN( 15, 8 )# <!--- 17 (octal) ---> 
</bx:output>
```



```java
<bx:set max = CreateObject( "java", "java.lang.Integer" ).MAX_VALUE >
<bx:output>
  #formatBaseN( max, 16 )# <!--- 7fffffff (correct) ---> 
  #formatBaseN( max + 1, 16 )# <!--- 7fffffff (incorrect) ---> 
</bx:output>
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
