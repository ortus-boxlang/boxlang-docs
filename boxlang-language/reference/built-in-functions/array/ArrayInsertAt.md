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

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
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
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayIndexExists](./ArrayIndexExists.md)
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
  * [ArrayUnshift](./ArrayUnshift.md)
