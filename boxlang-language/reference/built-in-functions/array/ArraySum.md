[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySum`

Returns the sum of all values in an array

## Method Signature

```
ArraySum(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to sum the values of. |  |

## Examples

### Sum of values in an array

Uses the arraySum function to get sum of values in an array

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI0NNDh4rS0BBJG5kDC3Igr1pqrvCizJNW%2FtKSgtERDIRGkOrg0V0MhD0m3poKmNRcAaewWoQ%3D%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	10,
	99,
	27,
	72
];
writeOutput( arraySum( numberArray ) );

```

Result: 208

### Sum of values in an array

To get sum of values in an empty array

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYiOteYqL8osSfUvLSkoLdFQSARJBJfmaijkISnUVNC05gIAa%2F4UAg%3D%3D" target="_blank">Run Example</a>

```java
numberArray = [];
writeOutput( arraySum( numberArray ) );

```

Result: 0

### Sum of values in an array

 Uses the sum member function is the same as running arraySum.

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI0NNDh4rS0BBJG5kDC3Igr1pqrvCizJNW%2FtKSgtERDIQ%2BhR6%2B4NFdDU0HTmgsA42QUkA%3D%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	10,
	99,
	27,
	72
];
writeOutput( numberArray.sum() );

```

Result: 208

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI0NNDh4rS0BBJG5kDC3Igr1porpTS3QEMhEaQsuDRXQyEPSZumgqY1l76%2BQm4qSEwhrTQvuSQzPw%2BqB0mlXjFQK1g1ALxLIwk%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	10,
	99,
	27,
	72
];
dump( arraySum( numberArray ) );
// member function
dump( numberArray.sum() );

```



## Related

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
  * [ArrayChunk](./ArrayChunk.md)
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
  * [ArrayFindFirst](./ArrayFindFirst.md)
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayFlatMap](./ArrayFlatMap.md)
  * [ArrayFlatten](./ArrayFlatten.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
  * [ArrayGroupBy](./ArrayGroupBy.md)
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
  * [ArrayReject](./ArrayReject.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReverse](./ArrayReverse.md)
  * [ArraySet](./ArraySet.md)
  * [ArrayShift](./ArrayShift.md)
  * [ArraySlice](./ArraySlice.md)
  * [ArraySome](./ArraySome.md)
  * [ArraySort](./ArraySort.md)
  * [ArraySplice](./ArraySplice.md)
  * [ArraySwap](./ArraySwap.md)
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
