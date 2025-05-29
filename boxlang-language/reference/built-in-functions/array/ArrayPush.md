
# Function: `ArrayPush`

Adds an element or an object to the end of an array, then returns the size of the modified array.

## Method Signature

```
ArrayPush(array=[modifiableArray], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to which the element should be appended. |  |
| `value` | `any` | `true` | The element to append. Can be any type. |  |

## Examples

### Push a value onto an array

This is the full function version of arrayPush to push a value onto the end of the array.

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNNTh4jQCYmOuWGuuxKKixMqA0uIMDQUw0xZI6iiUJeaUptqaGCloWnOVF2WWpPqXlhSUlmgoKIVkZBZDVCpkJBYrKCmoQXg%2BqXlgExQ0gSJKCqk5qbmpeSXFekogIwCmqCRL" target="_blank">Run Example</a>

```java
arr = [ 
	1,
	2,
	3
];
arrayPush( array=arr, value=42 );
writeOutput( "This array has " & arrayLen( arr ) & " elements." );

```

Result: This array has 4 elements.

### Member function version

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDiNNTh4jQCYmOuWGuuxBygaGJRkV5BaXGGhoKJkYKmNVd5UWZJqn9pSUFpiYaCUkhGZjFISWKlQkZisYKSgpoCUJcakJGak5qbmldSrKcE0gUA358aew%3D%3D" target="_blank">Run Example</a>

```java
arr = [ 
	1,
	2,
	3
];
al = arr.push( 42 );
writeOutput( "This array has " & al & " elements." );

```

Result: This array has 4 elements.

### Push an object onto an array

This demonstrates pushing an object onto an array.

<a href="https://try.boxlang.io/?code=eJxLLCpSsFWIVuDijObi5DTk4ozVgTCVSsrzlRDcaiDmdFSwUjAGMmqB4lyx1lyJOUC9iUVFegWlxRkaCkB1JkZcsQqa1lzlRZklqf6lJQWlJRoKSiEZmcUgdYmVChmJxQpKCmoKQK1qQEZqTmpual5JsZ4SSBcAPPchZQ%3D%3D" target="_blank">Run Example</a>

```java
arr = [ 
	[
		1
	],
	[
		"two"
	],
	[
		{
			A : 3
		}
	]
];
al = arr.push( [
	42
] );
writeOutput( "This array has " & al & " elements." );

```

Result: This array has 4 elements.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLK81NSi0qVrBViFbg4jTU4eI0AmJjIDbhirXmcinNLdBQcCwqSqwMKC3O0FDIg6jXUTBQ0FTQtFbQ11fwLy0pKC0pVjDlys0vSvVDGMjFaQo0xwyIzYHYAqt5SFp0FEzAZnKhGgoAoF8rrw%3D%3D" target="_blank">Run Example</a>

```java
numbers = [ 
	1,
	2,
	3,
	4
];
Dump( ArrayPush( numbers, 0 ) ); // Outputs 5
moreNumbers = [
	5,
	6,
	7,
	8
];
Dump( ArrayPush( moreNumbers, 4 ) );
 // Outputs 5

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
* [ArrayEach](./ArrayEach.md)
* [ArrayAppend](./ArrayAppend.md)
* [ArrayEvery](./ArrayEvery.md)
* [ArrayLast](./ArrayLast.md)
* [ArrayMin](./ArrayMin.md)
