[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMin`

Return length of array

## Method Signature

```
ArrayMin(array=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `any` | `true` | The array to get min value from |  |

## Examples

### Simple example with empty array

To get the smallest numeric value of an array

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFVIBNF%2BqeUaCoYKmtZc5UWZJan%2BpSUFpSUaEDnfzDwNhWK4Dk2QKgDk7BWa" target="_blank">Run Example</a>

```java
someArray = arrayNew( 1 );
writeOutput( arrayMin( someArray ) );

```

Result: 0

### Get smallest numeric value of an array

Uses the arrayMin function to get the smallest numeric value of an array

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNDLW4eI0MQUSFuZAwgjE44q15iovyixJ9S8tKSgt0VBIBGnwzczTUCiGa9dU0LTmAgAYShUj" target="_blank">Run Example</a>

```java
someArray = [ 
	23,
	45,
	87,
	2,
	4
];
writeOutput( arrayMin( someArray ) );

```

Result: 2

### Get smallest numeric value of an array using member function



<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNDLW4eI0MQUSlpZAwhDE44q15iovyixJ9S8tKSgt0VAohmnS883M09BU0LTmAgCZMBL0" target="_blank">Run Example</a>

```java
someArray = [ 
	23,
	45,
	99,
	1,
	4
];
writeOutput( someArray.Min() );

```

Result: 1

### Additional Examples


```java
aNames = array( 10412, 42, 33, 2, 999, 12769, 888 );
dump( arrayMin( aNames ) );
// member function
dump( aNames.min() );

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
