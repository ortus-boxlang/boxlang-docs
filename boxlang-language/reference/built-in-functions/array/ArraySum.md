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
| `array` | `array` | `true` |  |  |

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

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayMerge](./ArrayMerge.md)
  * [ArrayIndexExists](./ArrayIndexExists.md)
  * [ArrayIsDefined](./ArrayIsDefined.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
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
