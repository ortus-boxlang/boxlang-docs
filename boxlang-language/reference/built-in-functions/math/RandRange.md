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
| `number1` | `numeric` | `true` |  |  |
| `number2` | `numeric` | `true` |  |  |
| `algorithm` | `string` | `false` |  |  |

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
