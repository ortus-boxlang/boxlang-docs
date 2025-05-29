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
  * [ArrayPop](./ArrayPop.md)
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
  * [ArraySort](./ArraySort.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
