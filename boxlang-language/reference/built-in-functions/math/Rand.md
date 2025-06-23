[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Rand`

Return a random double between 0 and 1

## Method Signature

```
Rand(algorithm=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `algorithm` | `string` | `false` | The algorithm to use to generate the random number. |  |

## Examples

### simple example Using rand()

To generate a random number between 0 to 1

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQKErMS9HQVNC05gIAaa4HiQ%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( rand() );

```


### simple example Using rand() with algorithm

To generate a random number between 0 to 1 by using bxmX_COMPAT algorithm


```java
writeOutput( rand( "bxmX_COMPAT" ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUChKzEvR0FSws1UwUFBTg3FtbBUMFTStucrRFCooBXs4GgYE%2BbkrKeDUBADz0hiR" target="_blank">Run Example</a>

```java
writeDump( rand() >= 0 && rand() <= 1 );
writeDump( rand( "SHA1PRNG" ) >= 0 && rand() <= 1 );

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
  * [Int](./Int.md)
  * [Log](./Log.md)
  * [Log10](./Log10.md)
  * [Max](./Max.md)
  * [Min](./Min.md)
  * [Pi](./Pi.md)
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
