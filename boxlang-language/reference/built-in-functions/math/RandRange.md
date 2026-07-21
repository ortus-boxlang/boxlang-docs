[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `RandRange`

Return a random int between number1 and number 2

## Method Signature

```
RandRange(number1=[numeric], number2=[numeric], algorithm=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `numeric` | `true` | The lower bound of the range. |  |
| `number2` | `numeric` | `true` | The upper bound of the range. |  |
| `algorithm` | `string` | `false` | The algorithm to use to generate the random number. |  |

## Examples

### Tag Example

The following example calls the Randomize function to seed the random number generator and generates 10 random numbers.  


```java
<bx:set r = randomize( 7, "SHA1PRNG" ) > 
 <bx:set local.MYINT = 1 > 
 <bx:set local.MYINT2 = 999 > 
<!--- Generate and display the random number. ---> 
 <bx:output><p><b> 
 RandRange returned: #randRange( local.MYINT, local.MYINT2, "SHA1PRNG" )# 
 </bx:output></b></p>  
```


### Script Example

 


```java
<bx:script>
	bytes = [];
	bytecount = 32;
	arrayResize( bytes, byteCount );
	for( i = 1; i <= byteCount; i++ ) {
		bytes[ i ] = randRange( -128, 127, "SHA1PRNG" );
	}
</bx:script>
 
 <bx:dump var="#bytes#"/>  
```


### Additional Examples


```java
writeDump( randRange( 25, 125, "bxmX_COMPAT" ) );
writeDump( randRange( 100, 500, "SHA1PRNG" ) );

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
  * [Rand](./Rand.md)
  * [Randomize](./Randomize.md)
  * [Round](./Round.md)
  * [Sgn](./Sgn.md)
  * [Sin](./Sin.md)
  * [Sqr](./Sqr.md)
  * [Tan](./Tan.md)
