[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayPrepend`

Append a value to the start an array

## Method Signature

```
ArrayPrepend(array=[modifiableArray], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to prepend to |  |
| `value` | `any` | `true` | The value to prepend |  |

## Examples

### Prepend a value to an array

Uses the arrayPrepend function to prepend a value to the beginning of an array and shifts the positions of the existing elements.

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNbh4jQCYkOuWGuuRJBEQFFqQWpeioZCMUypjoKJgqY1V3lRZkmqS2luAZIUSBwA6XgYvw%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	3,
	2,
	1
];
arrayPrepend( someArray, 4 );
writeDump( someArray );

```

Result: [4,3,2,1]

### Prepend a value to an array using the Array member function

 Invoking the prepend function on an array is the same as running arrayPrepend.

<a href="https://try.boxlang.io/?code=eJxLyU8uyS9yLCpKrFSwVYhW4OJUck1OzkktLsnPU9IB8kJS8%2FIS80rA7ODczJIMMMs5sSAxJyVTiSvWmisFYYReQVFqQWpeioaCkkdpUYmSgqY1V3lRZkmqS2lugYYCkkqQDABQTSa%2B" target="_blank">Run Example</a>

```java
doctorArray = [ 
	"Eccleston",
	"Tennant",
	"Smith",
	"Capaldi"
];
doctorArray.prepend( "Hurt" );
writeDump( doctorArray );

```

Result: ['Hurt','Eccleston','Tennant','Smith','Capaldi']

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNbh4jQCYkOuWGuuRJBEQFFqQWpeioZCMUypjoKJgqY1V0ppbgGSKEhIX18hNzU3KbVIIa00L7kkMz%2BPKyU%2FuSS%2FKDwjH24LF6dSeEZmSUlidmqREtAqpZDUvLzEvBIw2wksCrIcVaNeAcwZSh6lRSVKCAegWQAUBwDY4UIY" target="_blank">Run Example</a>

```java
someArray = [ 
	3,
	2,
	1
];
arrayPrepend( someArray, 4 );
dump( someArray );
// member function
doctorWhoArray = [
	"Whittaker",
	"Tennant",
	"Baker"
];
doctorWhoArray.prepend( "Hurt" );
dump( doctorWhoArray );

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
