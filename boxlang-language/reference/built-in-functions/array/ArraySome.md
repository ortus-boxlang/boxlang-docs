[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySome`

Calls a given closure/function with every element in a given array and returns true if one of the closure calls returns true

## Method Signature

```
ArraySome(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |
| `initialValue` | `any` | `false` |  |  |

## Examples

### Simple Example



<a href="https://try.boxlang.io/?code=eJxFjjFrAkEQhWv3V7xMIXsguT5iRNImMZAihaQYzKgL3u4yO4uI5L%2Fn7pTYPN684vumbfGiwibgCFblsxvzNRTDAhs3Ic75KDTrWw5R7lfHcZ%2FGxlnDNhm577lrW7yxbQ8oqROnUupxAI3Qz37y%2BOfP4LGKZ%2By0BkODxTMubqJiVeN1fCzGauUr2MGDmNDM3e8QveVDQzRcBe6kwWRdLVfz8DfrEjQYCU%2Bg90QNpiB0w3NSgJOoYJdq%2FHkYuX8nvVIz" target="_blank">Run Example</a>

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



<a href="https://try.boxlang.io/?code=eJxFjr2KAkEQhGPnKeo6kF043PxE5bj0foQLLjgMGm11wJ0ZenoQEd%2Fd3VU0Kaoq%2BKqaBh8qbAIOYFU%2BuUE%2FfTbM8O9GxCkdhF47l3yQZ2o57OLgOKlfRyO3mrqmwRfbeo8cW3EquRx60AM66fsKFd7DCVst3lBjNsfZjVSsaLiVEwmb%2FOdtX4GYUE%2FdpZeOvlQfDDewO6o3%2BSmWinXM%2B9oC9NuNEN5A35FqjEFo%2B1OSgaOoYBtL2LwM3CtS9U8f" target="_blank">Run Example</a>

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

<a href="https://try.boxlang.io/?code=eJydjrEKgzAYhGfzFEcmBanUVVLwGTqWDlF%2FqZTEEg2tlL57k0hah05djvuP475f0702Ri4QOIElXPLcaRO03fhu4yloz9m5Yp1VtxQ6rmQVu8jpOCrau0XpM398GzlS1HrBMJPKV9c9VuPayCAOeLLE0GyNDi0IAQeu2Muvr7wPwyVFAUWqIYPe6nYeRh1fKN0Lkbubwht%2Fwa8%2F4aVP3u3AWrY%3D" target="_blank">Run Example</a>

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

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayMerge](./ArrayMerge.md)
  * [ArrayIndexExists](./ArrayIndexExists.md)
  * [ArrayIsDefined](./ArrayIsDefined.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
  * [ArraySum](./ArraySum.md)
  * [ArraySplice](./ArraySplice.md)
  * [ArrayReduceRight](./ArrayReduceRight.md)
  * [ArrayReverse](./ArrayReverse.md)
  * [ArrayFind](./ArrayFind.md)
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayPush](./ArrayPush.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayMap](./ArrayMap.md)
  * [ArrayPop](./ArrayPop.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayMedian](./ArrayMedian.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayToList](./ArrayToList.md)
  * [ArrayFilter](./ArrayFilter.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayRange](./ArrayRange.md)
  * [ArraySwap](./ArraySwap.md)
  * [ArrayShift](./ArrayShift.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArraySlice](./ArraySlice.md)
  * [ArrayMid](./ArrayMid.md)
  * [ArrayInsertAt](./ArrayInsertAt.md)
  * [ArrayNew](./ArrayNew.md)
  * [ArraySet](./ArraySet.md)
  * [ArrayMax](./ArrayMax.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArraySort](./ArraySort.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
