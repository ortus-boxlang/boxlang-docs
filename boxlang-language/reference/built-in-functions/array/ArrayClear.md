[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayClear`

Clear all items from array

## Method Signature

```
ArrayClear(array=[modifiableArray])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to clear. |  |

## Examples

### Clear the value of an array

Uses the arrayClear function to clear the value of an array

<a href="https://try.boxlang.io/?code=eJw9js0KgkAUhdfepzi4GiGQ1mKQQdGqiKBFtBjwVoM2I9cZRKJ3Tw1bnY%2FzA6d1L16L6B45rqAoPnEZLwa9PI3niXbCbCcq6vCzjsZWMd0y6mRoHYJvgleUpjiLtm1jahZ0TiotLtgSdyco9lsI%2ByAWvm%2BYlIKWxxIJ8hXeFOnxxKZmLXOQUTQPJHBGn0Sh%2Fd9NxsIXzbM43A%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	"Red",
	"White",
	"Green",
	"Blue",
	"Pink"
];
writeOutput(
// Transpiler workaround for BIF return type
(( arg1 ) => {
	arrayClear( arg1 );
	return true;
})( someArray ) );

```

Result: Yes

### Clear the value of an array
To clear the value of an array

<a href="https://try.boxlang.io/?code=eJw9js0KgkAUhdfepzi4GiGQ1mKQQdGqiKBFtBjwVoM2I9cZRKJ3Tw1bnY%2FzA6d1L16L6B45rqAoPnEZLwa9PI3niXbCbCcq6vCzjsZWMd0y6mRoHYJvgleUpjiLtm1jahZ0TiotLtgSdyco9lsI%2ByAWvm%2BYlIKWxxIJ8hXeFOnxxKZmLXOQUTQPJHBGn0Sh%2Fd9NxsIXzbM43A%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	"Red",
	"White",
	"Green",
	"Blue",
	"Pink"
];
writeOutput(
// Transpiler workaround for BIF return type
(( arg1 ) => {
	arrayClear( arg1 );
	return true;
})( someArray ) );

```

Result: true

### Clear value of an array using member function

Uses the member function is the same as running arrayClear.

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI01OHiNAJiY65Ya67yosySVP%2FSkoLSEg2FPIRaPeec1MQiDU0FTWsuAJ1WE9Q%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	1,
	2,
	3
];
writeOutput( numberArray.Clear() );

```

Result: Yes

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljk0OgjAQhdfMKd5SE6Wi7AgLwzGMi6oTIaGlKVMNt7dgJEQWs3iT9%2FMphcqzFu6hLbT3esC9s6Ib29gncnDLhq30eDdSQ2qGDebGvkeGPfKUfrLEhZJsR8kx3ileTteCHsG4zRzZFlAKXRAXYuNYtlqcWim6qpa1X5qifo2OmXMiOsyEKZ3H95RbTq4Y6B%2BCjZPhW0ofQhRX2g%3D%3D" target="_blank">Run Example</a>

```java
// Creates an array containing 4 elements with the numbers 1 - 4.
numbers = [
	1,
	2,
	3,
	4
];
dump( numbers ); // outputs the array containing 1 - 4
// Clears the array leaving an array with 0 elements.
ArrayClear( numbers );
dump( numbers );
 // outputs the empty array

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayFilter](./ArrayFilter.md)
  * [ArrayFind](./ArrayFind.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
  * [ArrayFindFirst](./ArrayFindFirst.md)
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayFlatMap](./ArrayFlatMap.md)
  * [ArrayFlatten](./ArrayFlatten.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayGroupBy](./ArrayGroupBy.md)
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
  * [ArrayReject](./ArrayReject.md)
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
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
