[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMap`

Iterates over every entry of the array and calls the closure function to work on the element of the array.

## Method Signature
```
ArrayMap(array=[array], callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce | |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the current item, and the
                    current index, and the original array. The function should return the value that will be set at the same index in the new array. | |
| `parallel` | `boolean` | `false` |  | false|
| `maxThreads` | `integer` | `false` |  | |
| `initialValue` | `any` | `false` |  | |
|----------|------|----------|-------------|---------|



## Examples

```
ArrayMap(array=[array], callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
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
  * [ArrayMax](ArrayMax.md)
  * [ArrayMedian](ArrayMedian.md)
  * [ArrayMerge](ArrayMerge.md)
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
