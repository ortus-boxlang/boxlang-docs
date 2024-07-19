[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayEvery`

Returns true if every closure returns true, otherwise false

## Method Signature

```
ArrayEvery(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |
| `initialValue` | `any` | `false` |  |  |

## Examples



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEach](./ArrayEach.md)
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
