[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySlice`

Extracts a sub array from an existing array.

## Method Signature

```
ArraySlice(array=[array], start=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` |  |  |
| `start` | `integer` | `true` |  | `1` |
| `length` | `integer` | `false` |  | `0` |

## Examples

### Simple arraySlice Example



<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI01OHiNAJiYyA2AWJTIDYDYnMgtuCKtebKSy13hKpPBNHBOZnJqRoQto6CkY6CsYKmNVd5UWZJakppboGGAlwDUBgA%2Baoa%2Bw%3D%3D" target="_blank">Run Example</a>

```java
array = [ 
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
];
newArray = arraySlice( array, 2, 3 );
writedump( newArray );

```

Result: [2,3,4]

### arraySlice with no length specified



<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI01OHiNAJiYyA2AWJTIDYDYnMgtuCKtebKSy13hKpPBNHBOZnJqRoQto6CiYKmNVd5UWZJakppboGGAlw1UBgAtbwafg%3D%3D" target="_blank">Run Example</a>

```java
array = [ 
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
];
newArray = arraySlice( array, 4 );
writedump( newArray );

```

Result: [4,5,6,7,8]

### arraySlice using a negative offset



<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI01OHiNAJiYyA2AWJTIDYDYnMgtuCKtebKSy13hKpPBNHBOZnJqRoQto6CrqmOgrGCpjVXeVFmSWpKaW6BhgJcB1AYABFyGys%3D" target="_blank">Run Example</a>

```java
array = [ 
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
];
newArray = arraySlice( array, -5, 3 );
writedump( newArray );

```

Result: [4,5,6]

### Slice an array using member function

CF11+ calling the slice member function on an array.

<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI01OHiNAJiYyA2AWJTIDYDYnMgtuCKtebKSy13hKpPBNF6xTmZyakaCkY6CsYKmtZc5UWZJakppbkFGgpwpUBhAFFlGN4%3D" target="_blank">Run Example</a>

```java
array = [ 
	1,
	2,
	3,
	4,
	5,
	6,
	7,
	8
];
newArray = array.slice( 2, 3 );
writedump( newArray );

```

Result: [2,3,4]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLSy13LCpKrFSwVYhW4OJUSlTSAZJJYDIZiZ2CxE4Fk2lKXLHWXCmluQUaCnkwUzStuTISi4Pzc1MNgSYmgsSCczKTUxFKdBQMdRRMQAohWuHKgSL6%2Bgq5qblJqUUKaaV5ySWZ%2BXkw04yApsFM0CuGmGiso2CGYY4RSAQAuEg6ow%3D%3D" target="_blank">Run Example</a>

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
hasSome1 = arraySlice( newArray, 1, 4 );
dump( hasSome1 );
// member function
hasSome2 = newArray.slice( 3, 6 );
dump( hasSome2 );

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
  * [ArrayPush](./ArrayPush.md)
  * [ArrayRange](./ArrayRange.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayReduceRight](./ArrayReduceRight.md)
  * [ArrayReject](./ArrayReject.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReverse](./ArrayReverse.md)
  * [ArraySet](./ArraySet.md)
  * [ArrayShift](./ArrayShift.md)
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
