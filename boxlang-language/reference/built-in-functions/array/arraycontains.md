# ArrayContains

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

## Method Signature

```
ArrayContains(array=[array], value=[any], substringMatch=[boolean])
```

### Arguments

| Argument         | Type      | Required | Description                                                                                                                                                         | Default |
| ---------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`          | `array`   | `true`   | The array to be searched.                                                                                                                                           |         |
| `value`          | `any`     | `true`   | The value to find or a closure to be used as a search function.                                                                                                     |         |
| `substringMatch` | `boolean` | `false`  | <p>If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>that just use a function filter.</p> | `false` |

## Examples

## Related

* [ArrayAppend](arrayappend.md)
* [ArrayAvg](arrayavg.md)
* [ArrayClear](arrayclear.md)
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
* [ArraySome](arraysome.md)
* [ArraySort](arraysort.md)
* [ArraySplice](arraysplice.md)
* [ArraySum](arraysum.md)
* [ArraySwap](arrayswap.md)
* [ArrayToList](arraytolist.md)
* [ArrayToStruct](arraytostruct.md)
* [ArrayUnshift](arrayunshift.md)
