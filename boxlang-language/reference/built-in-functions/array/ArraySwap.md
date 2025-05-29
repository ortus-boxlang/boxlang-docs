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
| `array` | `array` | `true` |  |  |
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
