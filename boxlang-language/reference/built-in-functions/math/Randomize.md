[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Randomize`

Seeds the pseudo-random number generator with an
 integer number, ensuring repeatable number patterns.

## Method Signature

```
Randomize(seed=[numeric], algorithm=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `seed` | `numeric` | `true` | The number to seed the Random with |  |
| `algorithm` | `string` | `false` | The algorithm to use to generate the random number. |  |

## Examples

### Tag Example

The following example calls the Randomize function to seed the random number generator and generates 10 random numbers.  


```java
<bx:set randomize( 12345 ) > <!--- if one was to remove this line, the random numbers are different every time --->  
 <bx:loop index="i" from="1" to="10"> 
 <bx:output>#rand()#</bx:output> 
 </bx:loop> 
```


### Additional Examples


```java
writeDump( Randomize( 8, "SHA1PRNG" ) );
writeDump( Randomize( 10 ) >= 0 && Randomize( 10 ) <= 1 );
randomize( 55 );
bx:loop index="i" from="1" to="3" {
	writeDump( rand() );
}

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
  * [FormatBaseN](./FormatBaseN.md)
  * [Tan](./Tan.md)
  * [Sin](./Sin.md)
  * [IncrementValue](./IncrementValue.md)
