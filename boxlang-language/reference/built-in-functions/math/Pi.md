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

  * [Sqr](./Sqr.md)
  * [Asin](./Asin.md)
  * [Sgn](./Sgn.md)
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
  * [IncrementValue](./IncrementValue.md)
