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
