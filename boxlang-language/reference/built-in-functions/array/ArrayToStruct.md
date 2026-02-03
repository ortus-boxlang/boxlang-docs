[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayToStruct`

Transform the array to a struct, the index of the array is the key of the struct

## Method Signature

```
ArrayToStruct(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to convert |  |

## Examples

### Convert an array to a struct using arrayToStruct()



<a href="https://try.boxlang.io/?code=eJzzCvb3C04tykzMyaxK1VBILCpKrAzJDy4pKk0u0VCIVuDiVEpU0gGSSUpcsQqaCprWXACxsA4w" target="_blank">Run Example</a>

```java
JSONSerialize( arrayToStruct( [ 
	"a",
	"b"
] ) );

```

Result: {"1":"a","2":"b"}

### Additional Examples


```java
arr = [ 
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g"
];
dump( arrayToStruct( arr ) );
if( listFirst( server.BOXLANG.VERSION, "." ) >= 6 ) dump( arrayToStruct( arr, true ) );
// member function
dump( arr.toStruct() );

```


<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDirObi5PRz9HVVsFJQSlTi4qzVQRVLwiKWjEUsBYtYKkiMK9aaK6U0t0BDIbGoKLEyJD%2B4pKg0uQTMVdBU0LTm0tdXyE3NTUotUkgrzUsuyczPQ2jQK4GpBysFAEnqLQ0%3D" target="_blank">Run Example</a>

```java
arr = [ 
	{
		NAME : "a"
	},
	{
		NAME : "b"
	},
	{
		NAME : "c"
	},
	{
		NAME : "d"
	},
	{
		NAME : "e"
	}
];
dump( arrayToStruct( arr ) );
// member function
dump( arr.toStruct() );

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
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
