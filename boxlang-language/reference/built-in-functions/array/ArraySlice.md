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
