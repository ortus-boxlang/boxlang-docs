# Randomize

Seeds the pseudo-random number generator with an\
integer number, ensuring repeatable number patterns.

## Method Signature

```
Randomize(seed=[numeric], algorithm=[string])
```

### Arguments

| Argument    | Type      | Required | Description                                         | Default |
| ----------- | --------- | -------- | --------------------------------------------------- | ------- |
| `seed`      | `numeric` | `true`   | The number to seed the Random with                  |         |
| `algorithm` | `string`  | `false`  | The algorithm to use to generate the random number. |         |

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

* [Abs](Abs.md)
* [Acos](Acos.md)
* [Asin](Asin.md)
* [Atn](Atn.md)
* [Ceiling](Ceiling.md)
* [Cos](Cos.md)
* [DecrementValue](DecrementValue.md)
* [Exp](Exp.md)
* [Fix](Fix.md)
* [Floor](Floor.md)
* [FormatBaseN](FormatBaseN.md)
* [IncrementValue](IncrementValue.md)
* [InputBaseN](InputBaseN.md)
* [Int](Int.md)
* [Log](Log.md)
* [Log10](Log10.md)
* [Max](Max.md)
* [Min](Min.md)
* [Pi](Pi.md)
* [PrecisionEvaluate](PrecisionEvaluate.md)
* [Rand](Rand.md)
* [RandRange](RandRange.md)
* [Round](Round.md)
* [Sgn](Sgn.md)
* [Sin](Sin.md)
* [Sqr](Sqr.md)
* [Tan](Tan.md)
