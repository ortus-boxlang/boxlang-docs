[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayAppend`

Append a value to an array

## Method Signature

```
ArrayAppend(array=[modifiableArray], value=[any], merge=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiableArray` | `true` | The array to which the element should be appended. |  |
| `value` | `any` | `true` | The element to append. Can be any type. |  |
| `merge` | `boolean` | `false` | If true, the value is assumed to be an array and the elements of the array are appended to the array. If false, the value is<br>                 appended as a single element. | `false` |

## Examples

### Append a value to an array

Uses the arrayAppend function to append a value to the end of the array

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmOuWGuuRJCEY0FBal6KhkIxTKWOgomCpjVXeVFmSap%2FaUlBaYmGglewv19walFmYk5mVSqSWgVNkFIA6BUetw%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3
];
arrayAppend( someArray, 4 );
writeOutput( JSONSerialize( someArray ) );

```

Result: [1,2,3,4]

### Append a value to an array using the Array member function

Invoking the append function on an array is the same as running arrayAppend.

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmOuWGuuYpikXmJBQWpeioaCiYKmNVd5UWZJqn9pSUFpiYaCV7C%2FX3BqUWZiTmZVqoYCXIuCJkgpACxLHJo%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3
];
someArray.append( 4 );
writeOutput( JSONSerialize( someArray ) );

```

Result: [1,2,3,4]

### Append more than one item

You can merge two arrays when third parameter is set to true.

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmOuWGsusIRjQUFqXoqGQjFMpY5CNBenCVCNKRCbccXqKJQUlaYqaFpzlRdllqS6lOYWaCh4Bfv7BacWZSbmZFalImlW0AQpBACAdyFm" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3
];
ArrayAppend( someArray, [
	4,
	5,
	6
], true );
writeDump( JSONSerialize( someArray ) );

```

Result: [1,2,3,4,5,6]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJy9kL0KwkAQhOvsU0ypsBDyc0kgWASs9QHCFYpX3nlc7grf3hVBr4iCjcU0s7M7H%2BuSPZuwYIcZVFRMRS1qRC3pkaYQTrfJe%2BMuG7hnlqGwHWmfrH95YqAscUzRp7jIrYpRMxpG%2B4hrcu%2BelRp7DeaQJ5RMOlEvGj6D5Hs%2FIc1QjI7RMwbof%2FAxYkhmjZK%2BfC6DpDtjNG%2Bu" target="_blank">Run Example</a>

```java
numbers = [ 
	1,
	2,
	3,
	4
];
ArrayAppend( numbers, 5 );
Dump( numbers ); // Outputs [ 1, 2, 3, 4, 5 ]
numbers = [
	1,
	2,
	3,
	4
];
moreNumbers = [
	5,
	6,
	7,
	8
];
ArrayAppend( numbers, moreNumbers );
Dump( numbers ); // Outputs [ 1, 2, 3, 4, [ 5, 6, 7, 8 ] ]
numbers = [
	1,
	2,
	3,
	4
];
moreNumbers = [
	5,
	6,
	7,
	8
];
ArrayAppend( numbers, moreNumbers, true );
Dump( numbers );
 // Outputs [ 1, 2, 3, 4, 5, 6, 7, 8 ]

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
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
