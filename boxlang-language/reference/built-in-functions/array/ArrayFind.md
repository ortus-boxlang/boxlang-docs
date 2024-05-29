[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayFind`

Array finders and contains functions with and without case sensitivity.

Please note that "contain" methods return a boolean, while "find" methods return an index.

## Method Signature

```
ArrayFind(array=[array], value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to be searched. |  |
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |

## Examples

```
ArrayFind(array=[array], value=[any], substringMatch=[boolean])
```

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
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayFilter](./ArrayFilter.md)
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
