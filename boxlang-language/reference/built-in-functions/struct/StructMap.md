[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructMap`

This BIF will iterate over each key-value pair in the struct and invoke the callback function for each item so you can do
 any operation on the key-value pair and return a new value that will be set in a new struct.

The callback function will be passed the key, the value, and the original struct.
 <ul>
 <li>If the callback requires strict arguments, it will only receive the key and value.</li>
 <li>If the callback does not require strict arguments, it will receive the key, value, and the original struct.</li>
 </ul>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
StructMap(struct=[structloose], callback=[function:BiFunction], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiFunction` | `true` | The function used to produce the right-hand value assignment in the new struct. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiFunction which will only receive the<br>                    first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. |  |

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

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEach](./StructEach.md)
  * [StructEquals](./StructEquals.md)
  * [StructEvery](./StructEvery.md)
  * [StructFilter](./StructFilter.md)
  * [StructFind](./StructFind.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructGet](./StructGet.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructInsert](./StructInsert.md)
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructNew](./StructNew.md)
  * [StructNone](./StructNone.md)
  * [StructReduce](./StructReduce.md)
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
