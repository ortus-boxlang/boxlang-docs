# ArrayNone

Used to iterate over an array and test whether **NONE** item meets the test callback.

This is the opposite of {@link ArraySome}.

The function will be passed 3 arguments: the value, the index, and the array.\
You can alternatively pass a Java Predicate which will only receive the 1st arg.\
The function should return true if the item meets the test, and false otherwise.

**Note:** This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does meet the test condition.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
This allows for efficient processing of large arrays, especially when the test function is computationally expensive or the array is large.

## Method Signature

```
ArrayNone(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`      | `array`              | `true`   | The array to test against the callback.                                                                                                                                                                           |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg.                  |         |
| `parallel`   | `boolean`            | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`            | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

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
* [ArrayMerge](ArrayMerge.md)
* [ArrayMid](ArrayMid.md)
* [ArrayMin](ArrayMin.md)
* [ArrayNew](ArrayNew.md)
* [ArrayPop](ArrayPop.md)
* [ArrayPrepend](ArrayPrepend.md)
* [ArrayPush](ArrayPush.md)
* [ArrayRange](ArrayRange.md)
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
