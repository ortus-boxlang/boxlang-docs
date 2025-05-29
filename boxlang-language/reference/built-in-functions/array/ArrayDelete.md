[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayDelete`

Delete first occurance of item in array case sensitive

## Method Signature

```
ArrayDelete(array=[modifiableArray], value=[any], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to be deleted from. |  |
| `value` | `any` | `true` | The value to deleted. |  |
| `scope` | `string` | `false` |  | `one` |

## Examples

### Delete an element from an array

Deletes the first `apple` element from the array `arr`.

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiVEosKMhJVdIBsvKLEvPSIcyC1MQiMMMRLMsVa82VWFSUWOmSmpNakuqX75xYnKqhABTSUYAqUdC05iovyixJdSnNLQBLgUQA9s0eFg%3D%3D" target="_blank">Run Example</a>

```java
arr = [ 
	"apple",
	"orange",
	"pear",
	"Apple"
];
arrayDeleteNoCase( arr, "Apple" );
writeDump( arr );

```

Result: ['orange','pear','Apple']

### Additional Examples

<a href="https://try.boxlang.io?code=eJyNjr8KwjAQxmfzFEemCoU%2BQMlQ7eLSJTiJw0WuUoi2XFOrb29yirhUXL77w3ff%2FZAZDBxArbTr7x6vZ53H3u7tTqtjqWbuAtXTZcjghmyQOQePjrzRG2p7Jg3rUsU1PmryFKjptzhSBuLU42Q7cfzIqdpAnExQFPCGSIkNzQkt0qAwVU7K6TWI4gJjPP0fU8zpRxTvF2i%2FEz%2FAT7cRXw8%3D" target="_blank">Run Example</a>

```java
arr = [ 
	"boxlang",
	"SUSI"
];
writeDump( var=arr, label="Before" );
arrayDeleteNoCase( arr, "suSi" );
writeDump( var=arr, label="After" ); // boxlang
arrNew = [
	"a",
	"Ab",
	"c",
	"A",
	"a"
];
writeDump( var=arrNew, label="Before" );
arrayDeleteNoCase( arrNew, "a", "all" );
writeDump( var=arrNew, label="After" );

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
