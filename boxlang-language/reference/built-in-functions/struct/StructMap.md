[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructMap`

Used to map a struct to a new struct of the same type containing the result

## Method Signature

```
StructMap(struct=[structloose], callback=[function:BiFunction], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiFunction` | `true` | The function used to produce the right-hand value assignment in the new struct. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiFunction which will only receive the<br>                    first 2 args. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxNj80KwjAQhM%2FZp1h6aqEI%2FpwsHgTxpPgA0kOoqQ21iWw3rSJ9d5Nii6dh%2BWZmdy3puzbygTv8IIjIGhXhFj8gxNJrxLLSEYgh9Yx7O7FVYOTkjCpSc3A9Bi25iZbW0QQ3AfbVmIQhAyidKVhbg418Xn7XxLg3b6zTUTpMQpIUOzLYXfGkWz5qajnGblGrd5jjxLvyDAYo9Uvd%2FDstkyv4LJ8x2l9t%2Br8Dkwx60qwOrvGeK4jZBmIsgTx4voO7Uho%3D" target="_blank">Run Example</a>

```java
original = { 
	"one" : {
		1 : "tahi"
	},
	"two" : {
		2 : "rua"
	},
	"three" : {
		3 : "toru"
	},
	"four" : {
		4 : "wha"
	}
};

function mapOriginal( Any k, Any v ) {
	return v[ ListFirst( v.keyList() ) ];
}
fixed = structMap( original, mapOriginal );
writeDump( [
	original,
	fixed
] );

```


### Using Member Function

 

<a href="https://try.boxlang.io/?code=eJw9jssKgzAQRdeZrxiyilCEPlYVC4XSVf9AXAiNNVhNGROtiP%2FeJDSuLsO5j9GkXqqv3pjjgsC47iXHMy7A2N4pN1WjOLB155iZdGQHz8hWG2pIbsFjCGqykdbaUoQnD6cmJGHNoFZf%2BXTr%2Bv9I2lUfgQKv%2FYztLsiICeYXnyZpLPU4FvhQg7krGozAMW3l7G%2BROGOZwYpJBhMpI2%2B2c2UFsNjuvgmDUHrPD8gKQ5I%3D" target="_blank">Run Example</a>

```java
original = { 
	"one" : {
		1 : "tahi"
	},
	"two" : {
		2 : "rua"
	},
	"three" : {
		3 : "toru"
	},
	"four" : {
		4 : "wha"
	}
};
fixed = original.map( ( Any k, Any v ) => {
	return v[ ListFirst( v.keyList() ) ];
} );
writeDump( [
	original,
	fixed
] );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxdjssKwjAQRdfmK4YspIViUXeWCNW1bvyCtB0kNI0lj5Yi%2FrvTVETcDAfuzJnrag8CnLeh9lccE%2BBamRYbDmnBXO03JcXbBU%2BEuwXPhPuCjVZ5bELXJzBIKyjJQMsKteAPq%2B7KSP1xR1%2BeQyUdgkfnmUVHkltML5IM8TqB0kzQ4pRFGKQOCCmIIzzZyqIP1swprIEfOM24ULBXBiTC%2BclfJ3rz7dTJvsfmt9EbWntPYw%3D%3D" target="_blank">Run Example</a>

```java
sct = structNew( "linked" );
sct.A = 1;
sct.B = 2;
sct.C = 3;
writedump( var=sct, label="original struct" );
// base test
res = StructMap( sct, ( Any key, Any value ) => {
	return key & ":" & value;
}, true );
writedump( var=res, label="mapped struct" );

```



## Related

  * [StructEquals](./StructEquals.md)
  * [StructReduce](./StructReduce.md)
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
  * [StructNew](./StructNew.md)
  * [StructGet](./StructGet.md)
  * [StructDelete](./StructDelete.md)
  * [StructFilter](./StructFilter.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructSort](./StructSort.md)
  * [StructEach](./StructEach.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructClear](./StructClear.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructCopy](./StructCopy.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructInsert](./StructInsert.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructValueArray](./StructValueArray.md)
  * [StructSome](./StructSome.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
