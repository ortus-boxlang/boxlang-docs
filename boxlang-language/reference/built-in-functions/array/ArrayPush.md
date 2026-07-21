[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

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

### Member function version.

Using the member function.

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

### Push an object onto an array.

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

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
  * [ArrayClear](./ArrayClear.md)
  * [ArrayContains](./ArrayContains.md)
  * [ArrayContainsNoCase](./ArrayContainsNoCase.md)
  * [ArrayDelete](./ArrayDelete.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArrayDeleteNoCase](./ArrayDeleteNoCase.md)
  * [ArrayEach](./ArrayEach.md)
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
