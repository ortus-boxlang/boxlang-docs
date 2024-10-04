# ArrayReduceRight

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value, from the right to the left, and return it.

## Method Signature

```
ArrayReduceRight(array=[array], callback=[function:BiFunction], initialValue=[any])
```

### Arguments

| Argument       | Type                  | Required | Description                                                                                                                                                                                                                                                                                     | Default |
| -------------- | --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`        | `array`               | `true`   | The array to reduce                                                                                                                                                                                                                                                                             |         |
| `callback`     | `function:BiFunction` | `true`   | <p>The function to invoke for each item. The function will be passed 3 arguments: the accumulator, the current item, and the<br>current index. You can alternatively pass a Java BiFunction which will only receive the first 2 args. The function should return the new accumulator value.</p> |         |
| `initialValue` | `any`                 | `false`  | The initial value of the accumulator                                                                                                                                                                                                                                                            |         |

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
* [ArrayMap](arraymap.md)
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
