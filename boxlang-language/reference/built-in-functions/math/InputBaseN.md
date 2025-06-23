[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `InputBaseN`

Converts a string, using the base specified by radix, to an integer.

## Method Signature

```
InputBaseN(string=[string], radix=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to convert to an integer. |  |
| `radix` | `integer` | `true` | Base of the number represented by string, in the range 2-36. |  |

## Examples

### Binary string to decimal



<a href="https://try.boxlang.io/?code=eJzLzCsoLXFKLE7101BQMjQwNFDSUTBS0LTmAgBlkwZU" target="_blank">Run Example</a>

```java
inputBaseN( "1010", 2 );

```

Result: 10

### Hexadecimal string to decimal



<a href="https://try.boxlang.io/?code=eJzLzCsoLXFKLE7101BQMnZzU9JRMDRT0LTmAgBnZwaG" target="_blank">Run Example</a>

```java
inputBaseN( "3FF", 16 );

```

Result: 1023

### Decimal string to decimal



<a href="https://try.boxlang.io/?code=eJzLzCsoLXFKLE7101BQMjQyVdJRMDRQ0LTmAgBlqwZZ" target="_blank">Run Example</a>

```java
inputBaseN( "125", 10 );

```

Result: 125

### Binary number to decimal



<a href="https://try.boxlang.io/?code=eJzLzCsoLXFKLE7101AwNDA00FEwUtC05gIAWYMGEA%3D%3D" target="_blank">Run Example</a>

```java
inputBaseN( 1010, 2 );

```

Result: 10

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUPDMKygtcUosTvXTUFAyNDAAIiUdBSMFTQVNawV9fQVjMwWnzLzEokqFknyFlNTkzNzEHIW0%2FKLcxBKuchzGmJqYAs2wQJhhaq7gAtUKNMU%2FuYSwGY5AEwzNwEZwgcwwNFDwSK1ITEEYA2VyAQCMXTzo" target="_blank">Run Example</a>

```java
writeDump( InputBaseN( "100100", 2 ) ); // 36 Binary to decimal format
writeDump( InputBaseN( "545", 8 ) ); // 357 Decimal to Octal format
writeDump( InputBaseN( "A", 16 ) );
 // 10 Hexadecimal to decimal

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
