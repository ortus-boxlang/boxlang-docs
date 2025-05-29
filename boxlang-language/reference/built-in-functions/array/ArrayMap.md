[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMap`

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

## Method Signature

```
ArrayMap(array=[array], callback=[function:Function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the current item, and the<br>                    current index, and the original array. You can alternatively pass a Java Function which will only receive the 1st arg. The function should return the value that will be set at the same index in the new array. |  |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |
| `initialValue` | `any` | `false` |  |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxLzs8tyEmtcEksSVSwVYhW4OKs5uLkdFSwUjDh4qzVQXANLVD5poZAPlesNVdearljUVFiJVB7Ioj2TSzQUEhGGKujoKHgmFepkFmSmqugqWBrpwA0oii1pLQoDyym52jNVaugac1VXgTkupTmArXDzQQKAwAMuCw5" target="_blank">Run Example</a>

```java
complexData = [ 
	{
		A : 4
	},
	{
		A : 18
	},
	{
		A : 51
	}
];
newArray = arrayMap( complexData, ( Any item ) => {
	return item.A;
} );
writeDump( newArray );

```

Result: [4, 18, 51]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJy1jk0LgkAQhs%2B7v2LYk4IkeUwMvAZ26RgdJh3Jw46xupSE%2F739APsF3R5m5p33wTNqmqCCK0ihGjStnVTm8IIGH4FO40T9wKTkrZSd1c8EMKbSUjK9Au%2FdCzQGlwa3fQYJ1LzAMJPOInFH74juGFKojvCRwtBsDXsSil1SwSGEpFhLufqaWPsrc6M8B036TgZ6y%2B08jLzJFF4m0E57nT9pFH70BQgcX4A%3D" target="_blank">Run Example</a>

```java
aNames = [ 
	"Marcus",
	"Sarah",
	"Josefine"
];
dump( aNames );
newNames1 = arrayMap( aNames, ( Any item, Any index, Any arr ) => {
	return {
		"name" : item
	};
} );
dump( newNames1 );
// member function
newNames2 = aNames.map( ( Any item, Any index, Any arr ) => {
	return {
		"name" : item
	};
} );
dump( newNames2 );

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
