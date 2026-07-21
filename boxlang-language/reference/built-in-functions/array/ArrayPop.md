[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayPop`

Remove last item in array and return it

## Method Signature

```
ArrayPop(array=[modifiablearray], defaultValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiablearray` | `true` | The array to get the last |  |
| `defaultValue` | `any` | `false` | The value to return when the array is empty. If omitted, an exception is thrown for an empty array. |  |

## Examples

### Remove the last value from an array

This is the full function version of arrayPop to remove the last value of an array.

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNNTh4jQCYhMjrlhrrgKgaGJRUWJlQH6BBoRlCyQVNK25yosyS1L9S0sKSks0FApAIgBcoRL4" target="_blank">Run Example</a>

```java
arr = [ 
	1,
	2,
	42
];
p = arrayPop( array=arr );
writeOutput( p );

```

Result: 42

### Member function version.

Using the member function.

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNNTh4jQCYhMjrlhrrgKgaGJRkV5BfoGGpjVXeVFmSap%2FaUlBaYmGQoECUAQAf3kOiw%3D%3D" target="_blank">Run Example</a>

```java
arr = [ 
	1,
	2,
	42
];
p = arr.pop();
writeOutput( p );

```

Result: 42

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtjb0Kg0AQhOvbp5gyBwuinj9wWOQFEnuxSIjlqZxe4du7xZEopvhgYWb2G4N7D35Bgw6kUiaVCblgqLf0CW6%2B4e79a2snucZY19AWSYJnWOewLjCx%2Bc1PaYeUkTFy9OQmPzx%2BUlKFuEqhEup%2FzsOCYS7qOg6Oj7Wls79glIxK%2FDtWokMS" target="_blank">Run Example</a>

```java
numbers = [ 
	1,
	2,
	3,
	4
];
dump( ArrayPop( numbers ) ); // Outputs 4
dump( numbers ); // Outputs [ 1, 2, 3 ]
moreNumbers = [
	5,
	6,
	7,
	8
];
dump( ArrayPop( moreNumbers, 4 ) ); // Outputs 8
dump( moreNumbers );
 // Outputs [ 5, 6, 7 ]

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
  * [ArrayClear](./ArrayClear.md)
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
