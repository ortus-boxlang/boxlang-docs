[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayFind`

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.
 If you use a function as the value, it will be used as a search closure or lambda. The signature of the function should be:

 <pre>
    ( value, index ) => {
 	  	return true; // if the value is found, else false
   }
 </pre>

 Example:

 <pre>
   array = [ 1, 2, 3, 4, 5 ];
  index = array.find( ( value, index ) -> {
 		return value == 3;
 } );
 </pre>

 We recommend you use BoxLang lambdas ({@code ->}) for this purpose, so they only act upon the value and index without any side effects.
 They will be faster and more efficient.

## Method Signature

```
ArrayFind(array=[array], value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to be searched. |  |
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |

## Examples

### Find an "Apple" in an array of fruit

Returns the index of the element "Apple" in the array

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSCwqSqx0y8xL8ct3TixO1VCIVuDiVMovSsxLT1XSATILMvNSEwsKciA8CIsrVkdByRHMVNBU0LTmAgCKPhkK" target="_blank">Run Example</a>

```java
writeOutput( arrayFindNoCase( [ 
	"orange",
	"pineapple",
	"apple"
], "Apple" ) );

```

Result: 3

### arrayFind is not Case Sensitive

Not case sensitive so "Apple" will be found in the array, returns 1. Use arrayFind for case sensitive matching.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSCwqSqx0y8xL8ct3TixO1VCIVuDiVMovSsxLT1XSATILMvNSEwsKciA8CIsrVkdByRHMVNBU0LTmAgCKPhkK" target="_blank">Run Example</a>

```java
writeOutput( arrayFindNoCase( [ 
	"orange",
	"pineapple",
	"apple"
], "Apple" ) );

```

Result: 1

### Member Functions: Find an "Apple" in an array of fruit

Calls the findNoCase member function of the array object.

<a href="https://try.boxlang.io/?code=eJxLKyrNLFGwVYhW4OJUyi9KzEtPVdIBMgsy81ITCwpyIDwIiyvWmqu8KLMk1b%2B0pKC0REMhDaRZLy0zL8Uv3zmxOFVDQckRrFJBU0HTmgsAGFQcAw%3D%3D" target="_blank">Run Example</a>

```java
fruit = [ 
	"orange",
	"pineapple",
	"apple"
];
writeOutput( fruit.findNoCase( "Apple" ) );

```

Result: 3

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLLCoKSyzKTEzKSVWwVYhW4OJUCk8sSS1S0gGygrMrQbQRiO2YWaTEFWvNFV6UWZLqUppboKHgWFSUWOmWmZfil%2B%2BcWJyqoZCIMExHwVRBU0HTWkFfX8G%2FtKSgtKRYwYB4zUqJQOswDDAh3gAjsGYuZN3GXAAzo0hq" target="_blank">Run Example</a>

```java
arrVariable = [ 
	"Water",
	"Sky",
	2,
	"Air"
];
WriteDump( ArrayFindNoCase( arrVariable, 5 ) ); // Outputs 0
WriteDump( ArrayFindNoCase( arrVariable, "air" ) ); // Outputs 4
WriteDump( ArrayFindNoCase( arrVariable, 2 ) );
 // Outputs 3

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayFilter](./ArrayFilter.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayIndexExists](./ArrayIndexExists.md)
  * [ArrayInsertAt](./ArrayInsertAt.md)
  * [ArrayIsDefined](./ArrayIsDefined.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMap](./ArrayMap.md)
  * [ArrayMax](./ArrayMax.md)
  * [ArrayMedian](./ArrayMedian.md)
  * [ArrayMerge](./ArrayMerge.md)
  * [ArrayMid](./ArrayMid.md)
  * [ArrayMin](./ArrayMin.md)
  * [ArrayNew](./ArrayNew.md)
  * [ArrayNone](./ArrayNone.md)
  * [ArrayPop](./ArrayPop.md)
  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayPush](./ArrayPush.md)
  * [ArrayRange](./ArrayRange.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayReduceRight](./ArrayReduceRight.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReverse](./ArrayReverse.md)
  * [ArraySet](./ArraySet.md)
  * [ArrayShift](./ArrayShift.md)
  * [ArraySlice](./ArraySlice.md)
  * [ArraySome](./ArraySome.md)
  * [ArraySort](./ArraySort.md)
  * [ArraySplice](./ArraySplice.md)
  * [ArraySum](./ArraySum.md)
  * [ArraySwap](./ArraySwap.md)
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayUnshift](./ArrayUnshift.md)
