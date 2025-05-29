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
  * [ArrayEach](./ArrayEach.md)
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
