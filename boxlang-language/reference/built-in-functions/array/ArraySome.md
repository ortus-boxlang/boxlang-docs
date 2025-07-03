# ArraySome

Used to iterate over an array and test whether **ANY** items meet the test callback.

The function will be passed 3 arguments: the value, the index, and the array.\
You can alternatively pass a Java Predicate which will only receive the 1st arg.\
The function should return true if the item meets the test, and false otherwise.

**Note:** This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
ArraySome(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`      | `array`              | `true`   | The array to reduce                                                                                                                                                                                               |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg.                  |         |
| `parallel`   | `boolean`            | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`            | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### Simple Example

[Run Example](https://try.boxlang.io/?code=eJxFjjFrAkEQhWv3V7xMIXsguT5iRNImMZAihaQYzKgL3u4yO4uI5L%2Fn7pTYPN684vumbfGiwibgCFblsxvzNRTDAhs3Ic75KDTrWw5R7lfHcZ%2FGxlnDNhm577lrW7yxbQ8oqROnUupxAI3Qz37y%2BOfP4LGKZ%2By0BkODxTMubqJiVeN1fCzGauUr2MGDmNDM3e8QveVDQzRcBe6kwWRdLVfz8DfrEjQYCU%2Bg90QNpiB0w3NSgJOoYJdq%2FHkYuX8nvVIz)

```java
// Create an array
arrayList = [
	"apple",
	"pineapple",
	"mango",
	"apricot"
];
// Match some
result = arraySome( arrayList, ( Any fruit ) => {
	return fruit.startsWith( "a" );
} );
// Print result
writeOutput( (result ? "Some" : "No") & " matches  were found!" );

```

Result: Some matches were found!

### Member Function Example

[Run Example](https://try.boxlang.io/?code=eJxFjr2KAkEQhGPnKeo6kF043PxE5bj0foQLLjgMGm11wJ0ZenoQEd%2Fd3VU0Kaoq%2BKqaBh8qbAIOYFU%2BuUE%2FfTbM8O9GxCkdhF47l3yQZ2o57OLgOKlfRyO3mrqmwRfbeo8cW3EquRx60AM66fsKFd7DCVst3lBjNsfZjVSsaLiVEwmb%2FOdtX4GYUE%2FdpZeOvlQfDDewO6o3%2BSmWinXM%2B9oC9NuNEN5A35FqjEFo%2B1OSgaOoYBtL2LwM3CtS9U8f)

```java
// Create an array
arrayList = [
	"apple",
	"pineapple",
	"mango",
	"apricot"
];
// Match some
result = arrayList.some( ( Any fruit ) => {
	return fruit.endsWith( "a" );
} );
// Print result
writeOutput( (result ? "Some" : "No") & " matches  were found!" );

```

Result: No matches were found!

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJydjrEKgzAYhGfzFEcmBanUVVLwGTqWDlF%2FqZTEEg2tlL57k0hah05djvuP475f0702Ri4QOIElXPLcaRO03fhu4yloz9m5Yp1VtxQ6rmQVu8jpOCrau0XpM398GzlS1HrBMJPKV9c9VuPayCAOeLLE0GyNDi0IAQeu2Muvr7wPwyVFAUWqIYPe6nYeRh1fKN0Lkbubwht%2Fwa8%2F4aVP3u3AWrY%3D)

```java
newArray = [ 
	"a",
	"b",
	"c",
	"b",
	"d",
	"b",
	"e",
	"f"
];
dump( newArray );
hasSome1 = arraySome( newArray, ( Any item, Any idx, Any arr ) => {
	return item == "b";
} );
dump( hasSome1 );
// member function
hasSome2 = newArray.some( ( Any item, Any idx, Any arr ) => {
	return item == "k";
} );
dump( hasSome2 );

```

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
* [ArrayReduceRight](ArrayReduceRight.md)
* [ArrayResize](ArrayResize.md)
* [ArrayReverse](ArrayReverse.md)
* [ArraySet](ArraySet.md)
* [ArrayShift](ArrayShift.md)
* [ArraySlice](ArraySlice.md)
* [ArraySort](ArraySort.md)
* [ArraySplice](ArraySplice.md)
* [ArraySum](ArraySum.md)
* [ArraySwap](ArraySwap.md)
* [ArrayToList](ArrayToList.md)
* [ArrayToStruct](ArrayToStruct.md)
* [ArrayUnshift](ArrayUnshift.md)
