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
