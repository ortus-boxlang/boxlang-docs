[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayEach`

Used to iterate over an array and run the function closure for each item in the array.

## Method Signature
```
ArrayEach(array=[array], callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |
| `ordered` | `boolean` | `false` | (BoxLang only) whether parallel operations should execute and maintain order | `false` |
| `initialValue` | `any` | `false` |  |  |

## Examples

```
ArrayEach(array=[array], callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])
```

## Related
  * [ArrayAppend](boxlang-language/reference/built-in-functions/ArrayAppend.md)
  * [ArrayAvg](boxlang-language/reference/built-in-functions/ArrayAvg.md)
  * [ArrayClear](boxlang-language/reference/built-in-functions/ArrayClear.md)
  * [ArrayContains](boxlang-language/reference/built-in-functions/ArrayContains.md)
  * [ArrayContainsNoCase](boxlang-language/reference/built-in-functions/ArrayContainsNoCase.md)
  * [ArrayDelete](boxlang-language/reference/built-in-functions/ArrayDelete.md)
  * [ArrayDeleteAt](boxlang-language/reference/built-in-functions/ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](boxlang-language/reference/built-in-functions/ArrayDeleteNoCase.md)
  * [ArrayEvery](boxlang-language/reference/built-in-functions/ArrayEvery.md)
  * [ArrayFilter](boxlang-language/reference/built-in-functions/ArrayFilter.md)
  * [ArrayFind](boxlang-language/reference/built-in-functions/ArrayFind.md)
  * [ArrayFindAll](boxlang-language/reference/built-in-functions/ArrayFindAll.md)
  * [ArrayFindAllNoCase](boxlang-language/reference/built-in-functions/ArrayFindAllNoCase.md)
  * [ArrayFindNoCase](boxlang-language/reference/built-in-functions/ArrayFindNoCase.md)
  * [ArrayFirst](boxlang-language/reference/built-in-functions/ArrayFirst.md)
  * [ArrayGetMetadata](boxlang-language/reference/built-in-functions/ArrayGetMetadata.md)
  * [ArrayIndexExists](boxlang-language/reference/built-in-functions/ArrayIndexExists.md)
  * [ArrayInsertAt](boxlang-language/reference/built-in-functions/ArrayInsertAt.md)
  * [ArrayIsDefined](boxlang-language/reference/built-in-functions/ArrayIsDefined.md)
  * [ArrayLast](boxlang-language/reference/built-in-functions/ArrayLast.md)
  * [ArrayMap](boxlang-language/reference/built-in-functions/ArrayMap.md)
  * [ArrayMax](boxlang-language/reference/built-in-functions/ArrayMax.md)
  * [ArrayMedian](boxlang-language/reference/built-in-functions/ArrayMedian.md)
  * [ArrayMerge](boxlang-language/reference/built-in-functions/ArrayMerge.md)
  * [ArrayMid](boxlang-language/reference/built-in-functions/ArrayMid.md)
  * [ArrayMin](boxlang-language/reference/built-in-functions/ArrayMin.md)
  * [ArrayNew](boxlang-language/reference/built-in-functions/ArrayNew.md)
  * [ArrayPop](boxlang-language/reference/built-in-functions/ArrayPop.md)
  * [ArrayPrepend](boxlang-language/reference/built-in-functions/ArrayPrepend.md)
  * [ArrayPush](boxlang-language/reference/built-in-functions/ArrayPush.md)
  * [ArrayReduce](boxlang-language/reference/built-in-functions/ArrayReduce.md)
  * [ArrayReduceRight](boxlang-language/reference/built-in-functions/ArrayReduceRight.md)
  * [ArrayResize](boxlang-language/reference/built-in-functions/ArrayResize.md)
  * [ArrayReverse](boxlang-language/reference/built-in-functions/ArrayReverse.md)
  * [ArraySet](boxlang-language/reference/built-in-functions/ArraySet.md)
  * [ArrayShift](boxlang-language/reference/built-in-functions/ArrayShift.md)
  * [ArraySlice](boxlang-language/reference/built-in-functions/ArraySlice.md)
  * [ArraySome](boxlang-language/reference/built-in-functions/ArraySome.md)
  * [ArraySort](boxlang-language/reference/built-in-functions/ArraySort.md)
  * [ArraySplice](boxlang-language/reference/built-in-functions/ArraySplice.md)
  * [ArraySum](boxlang-language/reference/built-in-functions/ArraySum.md)
  * [ArraySwap](boxlang-language/reference/built-in-functions/ArraySwap.md)
  * [ArrayToList](boxlang-language/reference/built-in-functions/ArrayToList.md)
  * [ArrayToStruct](boxlang-language/reference/built-in-functions/ArrayToStruct.md)
  * [ArrayUnshift](boxlang-language/reference/built-in-functions/ArrayUnshift.md)
