[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Pi`

Returns the mathmatical constant Pi accurate to 15 digits

## Method Signature

```
Pi()
```

### Arguments

This function does not accept any arguments

## Examples

### pi to 11 digits



<a href="https://try.boxlang.io/?code=eJwryNTQtOYCAAZOAXA%3D" target="_blank">Run Example</a>

```java
pi();

```

Result: 3.141592653589793238462643383279503

### Display all 15 digits with numberFormat



<a href="https://try.boxlang.io/?code=eJzLK81NSi1yyy%2FKTSzRUCjI1NDUUVAy0DNABUoKmtZcABvgCrE%3D" target="_blank">Run Example</a>

```java
numberFormat( pi(), "0.000000000000000" );

```

Result: 3.141592653589793

### Boxlang only shows up to 15 digits of pi

After 15th digit CF outputs 0's

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yyy%2FKTSzRUCjI1NDUUVAy0DPABEoKmtZcAEmEC3E%3D" target="_blank">Run Example</a>

```java
numberFormat( pi(), "0.0000000000000000000" );

```

Result: 3.1415926535897932385

### Additional Examples


```java
<bx:output>#pi()#</bx:output>
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
  * [PrecisionEvaluate](./PrecisionEvaluate.md)
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [RandRange](./RandRange.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
