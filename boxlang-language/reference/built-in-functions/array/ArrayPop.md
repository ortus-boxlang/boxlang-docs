
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
| `defaultValue` | `any` | `false` |  |  |

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

### Member function version

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

* [ArrayPrepend](./ArrayPrepend.md)
* [ArrayResize](./ArrayResize.md)
* [ArrayReduce](./ArrayReduce.md)
* [ArrayMerge](./ArrayMerge.md)
* [ArrayIndexExists](./ArrayIndexExists.md)
* [ArrayIsDefined](./ArrayIsDefined.md)
* [ArrayFindAll](./ArrayFindAll.md)
* [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
* [ArraySum](./ArraySum.md)
* [ArraySplice](./ArraySplice.md)
* [ArrayReduceRight](./ArrayReduceRight.md)
* [ArrayReverse](./ArrayReverse.md)
* [ArrayFind](./ArrayFind.md)
* [ArrayFindNoCase](./ArrayFindNoCase.md)
* [ArrayContains](./ArrayContains.md)
* [ArrayContainsNoCase](./ArrayContainsNoCase.md)
* [ArrayPush](./ArrayPush.md)
* [ArrayGetMetadata](./ArrayGetMetadata.md)
* [ArrayMap](./ArrayMap.md)
* [ArraySome](./ArraySome.md)
* [ArrayDelete](./ArrayDelete.md)
* [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
* [ArrayMedian](./ArrayMedian.md)
* [ArrayAvg](./ArrayAvg.md)
* [ArrayToList](./ArrayToList.md)
* [ArrayFilter](./ArrayFilter.md)
* [ArrayClear](./ArrayClear.md)
* [ArrayRange](./ArrayRange.md)
* [ArraySwap](./ArraySwap.md)
* [ArrayShift](./ArrayShift.md)
* [ArrayToStruct](./ArrayToStruct.md)
* [ArrayUnshift](./ArrayUnshift.md)
* [ArraySlice](./ArraySlice.md)
* [ArrayMid](./ArrayMid.md)
* [ArrayInsertAt](./ArrayInsertAt.md)
* [ArrayNew](./ArrayNew.md)
* [ArraySet](./ArraySet.md)
* [ArrayMax](./ArrayMax.md)
* [ArrayFirst](./ArrayFirst.md)
* [ArrayDeleteAt](./ArrayDeleteAt.md)
* [ArraySort](./ArraySort.md)
* [ArrayEach](./ArrayEach.md)
* [ArrayAppend](./ArrayAppend.md)
* [ArrayEvery](./ArrayEvery.md)
* [ArrayLast](./ArrayLast.md)
* [ArrayMin](./ArrayMin.md)
