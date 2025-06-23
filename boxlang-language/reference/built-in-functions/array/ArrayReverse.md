[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayReverse`

Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.

## Method Signature

```
ArrayReverse(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reverse |  |

## Examples

### Reverse an Array

Creates a new array with reversed positions

<a href="https://try.boxlang.io/?code=eJzLrXQsKkqsVLBViFbg4jTU4eI0AmJjrlhrrlyIVFBqWWpRcWoKUEkiEl9DASqvoGnNVV6UWZLqX1pSUFqioeAV7O8XnFqUmZiTWYVQBjdGE6QBAJDEJjM%3D" target="_blank">Run Example</a>

```java
myArray = [ 
	1,
	2,
	3
];
myArrayReversed = arrayReverse( myArray );
writeOutput( JSONSerialize( myArrayReversed ) );

```

Result: [3,2,1]

### Reverse an Array via Member Function



<a href="https://try.boxlang.io/?code=eJzLrXQsKkqsVLBViFbg4jTU4eI0AmJjrlhrrvKizJJU%2F9KSgtISDQWvYH%2B%2F4NSizMSczKpUDYVciDa9otSy1KLiVA1NBSC05gIAcYEXFg%3D%3D" target="_blank">Run Example</a>

```java
myArray = [ 
	1,
	2,
	3
];
writeOutput( JSONSerialize( myArray.reverse() ) );

```

Result: [3,2,1]

### Reverse an Array using array slice syntax

Reverse an Array using array slice syntax adding in Boxlang 2018


```java
myArray = [1,2,3]; 
writeOutput( serializeJSON( myArray[::-1] ) );
```

Result: [3,2,1]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLK81NSi0qVrBViFbg4jTU4eI0AmJjIDbhirXmSiwqSqwMSi0DKknVUMiDKta05nIpzS1AFlDQ11eINtEx1jHSMYzlAnJyU0FSCmmlecklmfl5XEUQQ1KANkF16UGFNODGwdUARQAU9S3%2F" target="_blank">Run Example</a>

```java
numbers = [ 
	1,
	2,
	3,
	4
];
arrayReverse( numbers );
Dump( numbers ); // [4,3,2,1]
// member function
reversed = numbers.reverse();
Dump( reversed );

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
  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayPush](./ArrayPush.md)
  * [ArrayRange](./ArrayRange.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayReduceRight](./ArrayReduceRight.md)
  * [ArrayResize](./ArrayResize.md)
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
