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

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayFilter](./ArrayFilter.md)
  * [ArrayFind](./ArrayFind.md)
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
