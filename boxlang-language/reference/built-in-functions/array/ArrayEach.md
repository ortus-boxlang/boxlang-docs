[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayEach`

Used to iterate over an array and run the function closure for each item in the array.

## Method Signature

```
ArrayEach(array=[array], callback=[function:Consumer], parallel=[boolean], maxThreads=[integer], ordered=[boolean], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Comparator which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |
| `ordered` | `boolean` | `false` | (BoxLang only) whether parallel operations should execute and maintain order | `false` |
| `initialValue` | `any` | `false` |  |  |

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
  * [ArraySome](./ArraySome.md)
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
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
