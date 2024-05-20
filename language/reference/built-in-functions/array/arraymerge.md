[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMerge`

This function creates a new array with data from the two passed arrays.

## Method Signature
```
ArrayMerge(array1=[array], array2=[array], leaveIndex=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array1` | `array` | `true` | The first array to merge |  |
| `array2` | `array` | `true` | The second array to merge |  |
| `leaveIndex` | `boolean` | `true` | Set to true maintain value indexes - if two values have the same index it will keep values from array1 | `false` |

## Examples

```
ArrayMerge(array1=[array], array2=[array], leaveIndex=[boolean])
```

## Related
  * [ArrayAppend](ArrayAppend.md)
  * [ArrayAvg](ArrayAvg.md)
  * [ArrayClear](ArrayClear.md)
  * [ArrayContains](ArrayContains.md)
  * [ArrayContainsNoCase](ArrayContainsNoCase.md)
  * [ArrayDelete](ArrayDelete.md)
  * [ArrayDeleteAt](ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](ArrayDeleteNoCase.md)
  * [ArrayEach](ArrayEach.md)
  * [ArrayEvery](ArrayEvery.md)
  * [ArrayFilter](ArrayFilter.md)
  * [ArrayFind](ArrayFind.md)
  * [ArrayFindAll](ArrayFindAll.md)
  * [ArrayFindAllNoCase](ArrayFindAllNoCase.md)
  * [ArrayFindNoCase](ArrayFindNoCase.md)
  * [ArrayFirst](ArrayFirst.md)
  * [ArrayGetMetadata](ArrayGetMetadata.md)
  * [ArrayIndexExists](ArrayIndexExists.md)
  * [ArrayInsertAt](ArrayInsertAt.md)
  * [ArrayIsDefined](ArrayIsDefined.md)
  * [ArrayLast](ArrayLast.md)
  * [ArrayMap](ArrayMap.md)
  * [ArrayMax](ArrayMax.md)
  * [ArrayMedian](ArrayMedian.md)
  * [ArrayMid](ArrayMid.md)
  * [ArrayMin](ArrayMin.md)
  * [ArrayNew](ArrayNew.md)
  * [ArrayPop](ArrayPop.md)
  * [ArrayPrepend](ArrayPrepend.md)
  * [ArrayPush](ArrayPush.md)
  * [ArrayReduce](ArrayReduce.md)
  * [ArrayReduceRight](ArrayReduceRight.md)
  * [ArrayResize](ArrayResize.md)
  * [ArrayReverse](ArrayReverse.md)
  * [ArraySet](ArraySet.md)
  * [ArrayShift](ArrayShift.md)
  * [ArraySlice](ArraySlice.md)
  * [ArraySome](ArraySome.md)
  * [ArraySort](ArraySort.md)
  * [ArraySplice](ArraySplice.md)
  * [ArraySum](ArraySum.md)
  * [ArraySwap](ArraySwap.md)
  * [ArrayToList](ArrayToList.md)
  * [ArrayToStruct](ArrayToStruct.md)
  * [ArrayUnshift](ArrayUnshift.md)
