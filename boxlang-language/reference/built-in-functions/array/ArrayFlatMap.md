[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayFlatMap`

Maps each element and flattens the result one level.

<pre>
 values = [ 1, 2, 3 ];
 values.flatMap( ( value ) => [ value, value * 10 ] );
 // [ 1, 10, 2, 20, 3, 30 ]
 </pre>

## Method Signature

```
ArrayFlatMap(array=[array], callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to transform |  |
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the current item, and the<br>                    current index, and the original array. You can alternatively pass a Java Function which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | If true, the function will be invoked in parallel using multiple threads. Defaults to false. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when parallel is true. If not provided the common thread pool will be used. If a boolean value is passed, it will be assigned as the virtual argument. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual thread. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### Transform each element and flatten the result one level

Each callback result is expected to be an array, and all results are flattened into a single array.

```java
values = [ 1, 2, 3 ];
result = values.flatMap( ( v ) => [ v, v * 10 ] );
writeOutput( result.toString() );

```

Result: [1, 10, 2, 20, 3, 30]

### Expand a list of orders into individual items

```java
orders = [
    { id: 1, items: [ "apple", "banana" ] },
    { id: 2, items: [ "cherry" ] }
];
allItems = orders.flatMap( ( order ) => order.items );
writeOutput( allItems.len() );

```

Result: 3

### Using the global function form

```java
result = arrayFlatMap( [ 1, 2 ], ( v ) => [ v, v + 1 ] );
writeOutput( result.toString() );

```

Result: [1, 2, 2, 3]

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
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
