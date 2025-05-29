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

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayMerge](./ArrayMerge.md)
  * [ArrayIndexExists](./ArrayIndexExists.md)
  * [ArrayIsDefined](./ArrayIsDefined.md)
  * [ArrayFindAll](./ArrayFindAll.md)
  * [ArrayFindAllNoCase](./ArrayFindAllNoCase.md)
  * [ArraySum](./ArraySum.md)
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
