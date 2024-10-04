# ArraySome

Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

## Method Signature

```
ArraySome(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments

| Argument       | Type                 | Required | Description                                                                                                                                                                                      | Default |
| -------------- | -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `array`        | `array`              | `true`   | The array to reduce                                                                                                                                                                              |         |
| `callback`     | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |         |
| `parallel`     | `boolean`            | `false`  | Specifies whether the items can be executed in parallel                                                                                                                                          | `false` |
| `maxThreads`   | `integer`            | `false`  | The maximum number of threads to use when parallel = true                                                                                                                                        |         |
| `initialValue` | `any`                | `false`  |                                                                                                                                                                                                  |         |

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
* [ArrayReduceRight](arrayreduceright.md)
* [ArrayResize](arrayresize.md)
* [ArrayReverse](arrayreverse.md)
* [ArraySet](arrayset.md)
* [ArrayShift](arrayshift.md)
* [ArraySlice](arrayslice.md)
* [ArraySort](arraysort.md)
* [ArraySplice](arraysplice.md)
* [ArraySum](arraysum.md)
* [ArraySwap](arrayswap.md)
* [ArrayToList](arraytolist.md)
* [ArrayToStruct](arraytostruct.md)
* [ArrayUnshift](arrayunshift.md)
