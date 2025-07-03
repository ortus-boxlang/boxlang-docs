# ArrayReduceRight

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,\
from the right to the left, and return it.

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

### Simple arrayReduceRight Example

Demonstrate how the function works from right to left.

[Run Example](https://try.boxlang.io/?code=eJw9jsEKwjAQRM%2FNVww5SAr5g1Chv9CreKjNojkklCW1DeK%2FuyboZWZY3u5sLCPzXDDgAtXpWVvRW9Wlqtfq6lSi%2FcfNX5%2FIbwtN4f7IBrHdsDAYU8HK9LQ1JTpyS8EfLcg2egxnvFTHlDdOlcepwmJCOvW20Bq9UzuHLFVxNfi%2FIOMPjtg1uQ%3D%3D)

```java
myArray = [ 
	"a",
	"b",
	"c",
	"d"
];
newArray = arrayReduceRight( myArray, ( Any prev, Any next, Any idx, Any arr ) => {
	return prev & next & idx;
}, "" );
writedump( newArray );

```

Result: d4c3b2a1

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
* [ArrayNone](ArrayNone.md)
* [ArrayPop](ArrayPop.md)
* [ArrayPrepend](ArrayPrepend.md)
* [ArrayPush](ArrayPush.md)
* [ArrayRange](ArrayRange.md)
* [ArrayReduce](ArrayReduce.md)
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
