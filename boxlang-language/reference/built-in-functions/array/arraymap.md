# ArrayMap

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the same index in a new array and the new array will be returned

## Method Signature

```
ArrayMap(array=[array], callback=[function:Function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments

| Argument       | Type                | Required | Description                                                                                                                                                                                                                                                                                                                         | Default |
| -------------- | ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`        | `array`             | `true`   | The array to reduce                                                                                                                                                                                                                                                                                                                 |         |
| `callback`     | `function:Function` | `true`   | <p>The function to invoke for each item. The function will be passed 3 arguments: the current item, and the<br>current index, and the original array. You can alternatively pass a Java Function which will only receive the 1st arg. The function should return the value that will be set at the same index in the new array.</p> |         |
| `parallel`     | `boolean`           | `false`  |                                                                                                                                                                                                                                                                                                                                     | `false` |
| `maxThreads`   | `integer`           | `false`  |                                                                                                                                                                                                                                                                                                                                     |         |
| `initialValue` | `any`               | `false`  |                                                                                                                                                                                                                                                                                                                                     |         |

## Examples

## Related

* [ArrayAppend](arrayappend.md)
* [ArrayAvg](arrayavg.md)
* [ArrayClear](arrayclear.md)
* [ArrayContains](arraycontains.md)
* [ArrayContainsNoCase](arraycontainsnocase.md)
* [ArrayDelete](arraydelete.md)
* [ArrayDeleteAt](arraydeleteat.md)
* [ArrayDeleteNoCase](arraydeletenocase.md)
* [ArrayEach](arrayeach.md)
* [ArrayEvery](arrayevery.md)
* [ArrayFilter](arrayfilter.md)
* [ArrayFind](arrayfind.md)
* [ArrayFindAll](arrayfindall.md)
* [ArrayFindAllNoCase](arrayfindallnocase.md)
* [ArrayFindNoCase](arrayfindnocase.md)
* [ArrayFirst](arrayfirst.md)
* [ArrayGetMetadata](arraygetmetadata.md)
* [ArrayIndexExists](arrayindexexists.md)
* [ArrayInsertAt](arrayinsertat.md)
* [ArrayIsDefined](arrayisdefined.md)
* [ArrayLast](arraylast.md)
* [ArrayMax](arraymax.md)
* [ArrayMedian](arraymedian.md)
* [ArrayMerge](arraymerge.md)
* [ArrayMid](arraymid.md)
* [ArrayMin](arraymin.md)
* [ArrayNew](arraynew.md)
* [ArrayPop](arraypop.md)
* [ArrayPrepend](arrayprepend.md)
* [ArrayPush](arraypush.md)
* [ArrayRange](arrayrange.md)
* [ArrayReduce](arrayreduce.md)
* [ArrayReduceRight](arrayreduceright.md)
* [ArrayResize](arrayresize.md)
* [ArrayReverse](arrayreverse.md)
* [ArraySet](arrayset.md)
* [ArrayShift](arrayshift.md)
* [ArraySlice](arrayslice.md)
* [ArraySome](arraysome.md)
* [ArraySort](arraysort.md)
* [ArraySplice](arraysplice.md)
* [ArraySum](arraysum.md)
* [ArraySwap](arrayswap.md)
* [ArrayToList](arraytolist.md)
* [ArrayToStruct](arraytostruct.md)
* [ArrayUnshift](arrayunshift.md)
