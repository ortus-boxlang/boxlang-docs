[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayEach`

Used to iterate over an array and run the function closure for each item in the array.

This BIF is used to perform an operation on each item in the array, similar to Java's forEach method.
 It can also be used to perform operations in parallel if the `parallel` argument is set to true.

 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the iterator will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the iterator in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
ArrayEach(array=[array], callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Comparator which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### Simple Example



<a href="https://try.boxlang.io/?code=eJzLSS0pSS0qVrBViFbg4lRKVNIBkklgMhlMpihxxVpzJRYVJVa6JiZnaCjkQHToKGgoOOZVKqTmpOam5pXogDmZeSmpFQqaCrZ2CtVcnOVFmSWp%2FqUlBaUlGgpKymBJZStlqA5layUFTWuuWhABAKk3JdU%3D" target="_blank">Run Example</a>

```java
letters = [ 
	"a",
	"b",
	"c",
	"d"
];
arrayEach( letters, ( Any element, Any index ) => {
	writeOutput( "#index#:#element#;" );
} );

```

Result: 1:a;2:b;3:c;4:d;

### Member Function Example



<a href="https://try.boxlang.io/?code=eJxLVLBViFbg4lRKVNIBkklgMlmJK9aaK1EvNTE5Q0NBQ8Exr1IhNSc1NzWvRAfMycxLSa2AMBOLihIrFTQVbO0Uqrk4y4syS1L9S0sKSks0FJSUweqUrZShmpWtlRQ0rblqQQQAdHghQA%3D%3D" target="_blank">Run Example</a>

```java
a = [ 
	"a",
	"b",
	"c"
];
a.each( ( Any element, Any index, Any array ) => {
	writeOutput( "#index#:#element#;" );
} );

```

Result: 1:a;2:b;3:c;

### Additional Examples


```java
aNames = array( "Marcus", "Sarah", "Josefine" );
arrayEach( aNames, ( Any element ) => {
	dump( element );
} );

```


<a href="https://try.boxlang.io/?code=eJxVkEFrwzAMhc%2FJr3jYFwc81rFblwbG2HmX3EoPrqO1pk5SbIWtjP33JdoY5PKhJ570hDK7xNjhRNwGf3kZp4FN9VS6ubcvC%2BWUnXkUemEnJOG78CQ8C4MqD%2FN0Su726vzZwFkYPA83UKSeBrYiwtDR528pXlTYNfgqi48UmN4mvk5soGo%2FdtRoceut%2Fluhsdfre%2FWhvhdrfUyNwnx%2FkSPR1eBhs1nktwWniSweF7UOaUd2EW3oaQtt1otxh7x8qNLoQ4whkx%2BHLv%2FH%2FAC9Els8" target="_blank">Run Example</a>

```java
start = getTickCount();
a = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i"
];
arrayEach( a, ( Any element, Any index, Any array ) => {
	writeOutput( "<code>#index#:#element# [#getTickCount()#]</code><br>" );
	sleep( 100 );
}, true, 3 );
writeOutput( "Total Time: #(getTickCount() - start)# milliseconds<br>" );

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayFilter](./ArrayFilter.md)
  * [ArrayFind](./ArrayFind.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
  * [ArrayFindFirst](./ArrayFindFirst.md)
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayFlatMap](./ArrayFlatMap.md)
  * [ArrayFlatten](./ArrayFlatten.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayGroupBy](./ArrayGroupBy.md)
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
  * [ArrayNone](./ArrayNone.md)
  * [ArrayPop](./ArrayPop.md)
  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayPush](./ArrayPush.md)
  * [ArrayRange](./ArrayRange.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayReduceRight](./ArrayReduceRight.md)
  * [ArrayReject](./ArrayReject.md)
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
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
