[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySwap`

Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements

## Method Signature

```
ArraySwap(array=[array], position1=[any], position2=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array containing the elements to swap. |  |
| `position1` | `any` | `true` | The first position to swap |  |
| `position2` | `any` | `true` | The second position to swap |  |

## Examples

### Swap the position of two values in an array



<a href="https://try.boxlang.io/?code=eJwrLi1ILcrML3IsKkqsVLBViFbg4lQKLshMSS3S9U3MU9IBct2LUlPzFNzzk3IyIQIu%2Bckl%2BUUK%2FkCyoLQYLBSWmpefq8QVa82VCDIpuDyxQEOhGNlwHQVDHQVjBU1rrvKizJJUl9JcdBUgOQDRVi2p" target="_blank">Run Example</a>

```java
superiorArray = [ 
	"Spider-Man",
	"Green Goblin",
	"Doctor Octopus",
	"Venom"
];
arraySwap( superiorArray, 1, 3 );
writeDump( superiorArray );

```

Result: ['Doctor Octopus', 'Green Goblin', 'Spider-Man', 'Venom']

### Swap the position of two values in an array using the member function

<a href="https://try.boxlang.io/?code=eJwrLi1ILcrML3IsKkqsVLBViFbg4lQKLshMSS3S9U3MU9IBct2LUlPzFNzzk3IyIQIu%2Bckl%2BUUK%2FkCyoLQYLBSWmpefq8QVa81VjGyiXnF5YoGGgqGOgrGCpjVXeVFmSapLaS5QCEUZSA4Av3srjA%3D%3D" target="_blank">Run Example</a>

```java
superiorArray = [ 
	"Spider-Man",
	"Green Goblin",
	"Doctor Octopus",
	"Venom"
];
superiorArray.swap( 1, 3 );
writeDump( superiorArray );

```

Result: ['Doctor Octopus', 'Green Goblin', 'Spider-Man', 'Venom']

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLi1ILcrML3IsKkqsVLBViFbg4lQKLshMSS3S9U3MU9IBct2LUlPzFNzzk3IyIQIu%2Bckl%2BUUK%2FkCyoLQYLBSWmpefq8QVa82VCDIpuDyxQEOhGNlwHQVDHQVjBU1rrpTSXHRJkLC%2BvkJuam5SapFCWmlecklmfh4Xihq9YrChBEwBADEkQw8%3D" target="_blank">Run Example</a>

```java
superiorArray = [ 
	"Spider-Man",
	"Green Goblin",
	"Doctor Octopus",
	"Venom"
];
arraySwap( superiorArray, 1, 3 );
dump( superiorArray );
// member function
superiorArray.swap( 1, 3 );
dump( superiorArray );

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
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
