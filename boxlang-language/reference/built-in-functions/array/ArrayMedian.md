[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMedian`

Return the median value of an array.

Will only work on arrays that contain only numeric values.

## Method Signature

```
ArrayMedian(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to get median value from |  |

## Examples

### Calculates the Median value

Uses the arrayMedian function to calculate the Median value

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYa5Ya65coGAiSNI3NSUzMU9DoRiuWtOaq7wosyTVv7SkoLREQyEXJAIARXgWXQ%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	2
];
m = arrayMedian( someArray );
writeOutput( m );

```

Result: 2

### Additional Examples


```java
aNames = array( 10412, 42, 33, 2, 999, 12769, 888 );
dump( arrayMedian( aNames ) );
// member function
dump( aNames.median() );

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
