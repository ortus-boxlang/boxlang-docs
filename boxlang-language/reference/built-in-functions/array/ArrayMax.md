[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMax`

Get the max value from an array

## Method Signature

```
ArrayMax(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to get max value from |  |

## Examples

### Simple example with empty array

To get the largest numeric value of an array

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFVIBNF%2BqeUaCoYKmtZc5UWZJan%2BpSUFpSUaEDnfxAoNhWK4Dk2QKgDlCBWc" target="_blank">Run Example</a>

```java
someArray = arrayNew( 1 );
writeOutput( arrayMax( someArray ) );

```

Result: 0

### Get largest numeric value of an array

Uses the arrayMax function to get the largest numeric value of an array

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNDLW4eI0MQUSFuZAwhDE44q15iovyixJ9S8tKSgt0VBIBGnwTazQUCiGa9dU0LTmAgAYNxUk" target="_blank">Run Example</a>

```java
someArray = [ 
	23,
	45,
	87,
	1,
	4
];
writeOutput( arrayMax( someArray ) );

```

Result: 87

### Get largest numeric value of an array using member function



<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNDLW4eI0MQUSBkBsCOJwxVpzlRdllqT6l5YUlJZoKBTD9OjlJlZoaCpoWnMBAIh4EtQ%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	23,
	45,
	0,
	1,
	4
];
writeOutput( someArray.max() );

```

Result: 45

### Additional Examples


```java
aNames = array( 10412, 42, 33, 2, 999, 12769, 888 );
dump( arrayMax( aNames ) );
// member function
dump( aNames.max() );

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
