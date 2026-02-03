[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayDeleteAt`

Delete item at specified index in array

## Method Signature

```
ArrayDeleteAt(array=[modifiableArray], index=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to be deleted from. |  |
| `index` | `integer` | `true` | The index to deleted. |  |

## Examples

### Simple example for arrayDeleteAt function

Uses the arrayDeleteAt function to delete the value in specific position

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiVApKTVHSAdLhGZklqWCWe1Fqah6Y5ZRTChEKyMzLVuKKteZKBGl1Sc1JLUl1LNFQKIaZpqNgrKBpzVVeBDTEv7SkoBQo6RXs7xecWpSZmJNZlYqkVkETpBQAhJIoyQ%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	"Red",
	"White",
	"Green",
	"Blue",
	"Pink"
];
arrayDeleteAt( someArray, 3 );
writeOutput( JSONSerialize( someArray ) );

```

Result: ["Red", "White", "Blue", "Pink"]

### Simple example with member function

Uses the member function is the same as running arrayDeleteAt.

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiVApKTVHSAdLhGZklqWCWe1Fqah6Y5ZRTChEKyMzLVuKKteYqhmnXc0nNSS1JdSzRUDBS0LTmKi8CavcvLSkoBYp4Bfv7BacWZSbmZFalaijANSlogpQCAIUrJos%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	"Red",
	"White",
	"Green",
	"Blue",
	"Pink"
];
someArray.DeleteAt( 2 );
writeOutput( JSONSerialize( someArray ) );

```

Result: ["Red", "Green", "Blue", "Pink"]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNDTS4eI0AGJDIAaxjYHYBIhNgdiMK9aaK6U0t0BDIRGoQ9OaC0glVrqk5qSWpDqWgEV1FExAEiiqAJteFeI%3D" target="_blank">Run Example</a>

```java
arr = [ 
	12,
	0,
	1,
	2,
	3,
	4,
	5,
	6
];
dump( arr );
arrayDeleteAt( arr, 4 );
dump( arr );

```


<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNDTS4eI0AGJDIAaxjYHYBIhNgdiMK9aaK6U0t0BDIRGoQ9OaC0jppaTmpJakOpZoKJiAhFDkAQ8KE8U%3D" target="_blank">Run Example</a>

```java
arr = [ 
	12,
	0,
	1,
	2,
	3,
	4,
	5,
	6
];
dump( arr );
arr.deleteAt( 4 );
dump( arr );

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
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
