[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayInsertAt`

Append a value to an array

## Method Signature

```
ArrayInsertAt(array=[modifiableArray], position=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to be inserted into |  |
| `position` | `integer` | `true` | The position to insert at |  |
| `value` | `any` | `true` | The value to insert |  |

## Examples

### Insert an Item in an Array at Position 2

Inserts the number 4 at position 2

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmOuWGuuRJCEZ15xalGJY4mGQjFMrY6CkY6CiYKmNVd5UWZJqn9pSUEpUN4r2N8vOLUoMzEnsyoVSbmCJkgpAHpvIAc%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3
];
arrayInsertAt( someArray, 2, 4 );
writeOutput( JSONSerialize( someArray ) );

```

Result: [1,4,2,3]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyFjTsOwjAMQGdyCisTSBUdGCuGjpwBMbjEQRbkI5Oo4vYkAbVsyMuT%2FfRsJXMaRfAFRziD2miM8UG6K3TnmRtM6Ms0DIL%2B9jm7QmEV1WVQWEMn%2FyRJY9qCXeIdHDrQnmbgdiUDnMhp2A3KZBd%2F3brre3DkJhKw2V8TB69WYc%2FLh1r9imjMv%2Bobm5pKjg%3D%3D" target="_blank">Run Example</a>

```java
fruitArray = [ 
	"apple",
	"kiwi",
	"banana",
	"orange",
	"mango",
	"kiwi"
];
arrayInsertAt( fruitArray, 3, "new inserted item" );
dump( fruitArray );
// member function
fruitArray.insertAt( 3, "member added item" );
dump( fruitArray );

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
