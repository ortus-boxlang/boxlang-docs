[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayTranspose`

Returns a transposed array based on all passed in arrays.

<pre>
 arrayTranspose(
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
 );
 // [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
 </pre>

## Method Signature

```
ArrayTranspose()
```

### Arguments

This function does not accept any arguments

## Examples

### Swap rows and columns in a 2D array

```java
matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ]
];
result = matrix.transpose();
writeOutput( result.len() & "," & result[ 1 ].len() );

```

Result: 3,2

### Transposed result

```java
matrix = [
    [ 1, 2 ],
    [ 3, 4 ]
];
result = matrix.transpose();
writeOutput( result[ 1 ].toString() );

```

Result: [1, 3]

### Using the global function form

```java
result = arrayTranspose( [ [ "a", "b" ], [ "c", "d" ] ] );
writeOutput( result[ 2 ].toString() );

```

Result: [b, d]

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
  * [ArraySum](./ArraySum.md)
  * [ArraySwap](./ArraySwap.md)
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
