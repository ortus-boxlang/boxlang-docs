[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySplice`

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

## Method Signature

```
ArraySplice(array=[modifiablearray], index=[Integer], elementCountForRemoval=[Integer], replacements=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiablearray` | `true` | The array to splice |  |
| `index` | `Integer` | `true` | The initial position to remove or insert from |  |
| `elementCountForRemoval` | `Integer` | `false` | The number of elemetns to remove | `0` |
| `replacements` | `array` | `false` | An array of elements to insert |  |

## Examples

### arraySplice inserting replacements at position 2 while removing 0 elements



<a href="https://try.boxlang.io/?code=eJzLzc8ryShWsFWIVuDiVPJKzFPSAdK%2BiUXJGWCWY0FRZg6Y5VWal6rEFWvNlVmSmgvSABRzS00CCyUWFSVWBhfkZCanaijkgo3UUTDSUTDQUQCr1rTmKi8CslJKcwtgCkCCAGPBI3Y%3D" target="_blank">Run Example</a>

```java
months = [ 
	"Jan",
	"March",
	"April",
	"June"
];
item = [
	"Feb"
];
arraySplice( months, 2, 0, item );
writedump( months );

```

Result: ["Jan","Feb","March","April","June"]

### arraySplice inserting replacements at position 3 while removing 2 elements



<a href="https://try.boxlang.io/?code=eJzLzc8ryShWsFWIVuDiVPJKzFPSAdK%2BiUXJGWCWY0FRZg6Y5VWal6rEFWvNlVmSmgvSABRzS00CCyUWFSVWBhfkZCanaijkgo3UUTDWUTDSUQCr1rTmKi8CslJKcwtgCkCCAGQkI3k%3D" target="_blank">Run Example</a>

```java
months = [ 
	"Jan",
	"March",
	"April",
	"June"
];
item = [
	"Feb"
];
arraySplice( months, 3, 2, item );
writedump( months );

```

Result: ["Jan","March","Feb"]

### arraySplice inserting replacements at position -3 while removing 0 elements



<a href="https://try.boxlang.io/?code=eJzLzc8ryShWsFWIVuDiVPJKzFPSAdK%2BiUXJGWCWY0FRZg6Y5VWal6rEFWvNlVmSmgvSABRzS00CCyUWFSVWBhfkZCanaijkgo3UUdA11lEw0FEAK9e05iovArJSSnMLYCpAggCDJyOk" target="_blank">Run Example</a>

```java
months = [ 
	"Jan",
	"March",
	"April",
	"June"
];
item = [
	"Feb"
];
arraySplice( months, -3, 0, item );
writedump( months );

```

Result: ["Jan","Feb","March","April","June"]

### arraySplice inserting replacements at position 5 which is greater than the length of the array



<a href="https://try.boxlang.io/?code=eJzLzc8ryShWsFWIVuDiVPJKzFPSAdK%2BiUXJGWCWY0FRZg6Y5VWal6rEFWvNlVmSmgvSABRzS00CCyUWFSVWBhfkZCanaijkgo3UUTDVUTDQUQCr1rTmKi8CslJKcwtgCkCCAGQqI3k%3D" target="_blank">Run Example</a>

```java
months = [ 
	"Jan",
	"March",
	"April",
	"June"
];
item = [
	"Feb"
];
arraySplice( months, 5, 0, item );
writedump( months );

```

Result: ["Jan","March","April","June","Feb"]

### Splice an array using member function



<a href="https://try.boxlang.io/?code=eJzLzc8ryShWsFWIVuDiVPJKzFPSAdK%2BiUXJGWCWY0FRZg6Y5VWal6rEFWvNlVmSmgvSABRzS00CC%2BWCTdErLsjJTE7VUDDSUTDQUQCr07TmKi8CslJKcws0FCDqQIIAiRAhWQ%3D%3D" target="_blank">Run Example</a>

```java
months = [ 
	"Jan",
	"March",
	"April",
	"June"
];
item = [
	"Feb"
];
months.splice( 2, 0, item );
writedump( months );

```

Result: ["Jan","Feb","March","April","June"]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxzSawsVrBViFbg4lQKLs1T0gHSvvkQOjw1BUyHZJQWFYNZbkWZYDo4sUSJK9aaK7MkNRekG6SoNLUYLOZYVJRYGVyQk5mcqqHgAjReR8FYR8FARwGsWNOaq7wIyEopzS2ASIOEALc4Iyo%3D" target="_blank">Run Example</a>

```java
Days = [ 
	"Sun",
	"Mon",
	"Wed",
	"Thurs",
	"Fri",
	"Sat"
];
item = [
	"Tues"
];
ArraySplice( Days, 3, 0, item );
writedump( Days );

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
  * [ArraySum](./ArraySum.md)
  * [ArraySwap](./ArraySwap.md)
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayTranspose](./ArrayTranspose.md)
  * [ArrayUnique](./ArrayUnique.md)
  * [ArrayUnshift](./ArrayUnshift.md)
  * [ArrayZip](./ArrayZip.md)
