# ArraySplice

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by elementCountForRemoval, and puts the replacements starting from index position.

## Method Signature

```
ArraySplice(array=[modifiablearray], index=[Integer], elementCountForRemoval=[Integer], replacements=[array])
```

### Arguments

| Argument                 | Type              | Required | Description                                   | Default |
| ------------------------ | ----------------- | -------- | --------------------------------------------- | ------- |
| `array`                  | `modifiablearray` | `true`   | The array to splice                           |         |
| `index`                  | `Integer`         | `true`   | The initial position to remove or insert from |         |
| `elementCountForRemoval` | `Integer`         | `false`  | The number of elemetns to remove              | `0`     |
| `replacements`           | `array`           | `false`  | An array of elements to insert                |         |

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
* [ArraySome](arraysome.md)
* [ArraySort](arraysort.md)
* [ArraySum](arraysum.md)
* [ArraySwap](arrayswap.md)
* [ArrayToList](arraytolist.md)
* [ArrayToStruct](arraytostruct.md)
* [ArrayUnshift](arrayunshift.md)
