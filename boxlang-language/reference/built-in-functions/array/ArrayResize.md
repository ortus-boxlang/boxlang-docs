# ArrayResize

Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its\
expected maximum. For more than 500 elements, use arrayResize\
immediately after using the ArrayNew BIF.

## Method Signature

```
ArrayResize(array=[modifiablearray], size=[any])
```

### Arguments

| Argument | Type              | Required | Description                       | Default |
| -------- | ----------------- | -------- | --------------------------------- | ------- |
| `array`  | `modifiablearray` | `true`   | The array to resize               |         |
| `size`   | `any`             | `true`   | The new minimum size of the array |         |

## Examples

### Tag Syntax

```java
<bx:set MyArray = arrayNew( 1 ) > 
 <!--- Resize that array to the number of records in the query. ---> 
 <bx:set temp = <!--- Transpiler workaround for BIF return type --->(( <bx:argument>, <bx:argument> ) => <bx:set arrayResize( arg1, arg2 ) ><bx:return true>)( MyArray, 8 ) > 
  <bx:dump var="#MyArray#"/>  
```

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJzLK81NSi0qVrBViFbg4jTU4eI0AmJjIDbhirXmSiwqSqwMSi3OrErVUMiDqNVRMDRQ0LTmcinNLYALggT09RVyU0E8hbTSvOSSzPw8LqisXhHUCENTrDoB9AgnmQ%3D%3D)

```java
numbers = [ 
	1,
	2,
	3,
	4
];
arrayResize( numbers, 10 );
Dump( numbers );
// member function
numbers.resize( 15 );
Dump( numbers );

```

## Related

* [ArrayAppend](ArrayAppend.md)
* [ArrayAvg](ArrayAvg.md)
* [ArrayClear](ArrayClear.md)
* [ArrayContains](ArrayContains.md)
* [ArrayContainsNoCase](ArrayContainsNoCase.md)
* [ArrayDelete](ArrayDelete.md)
* [ArrayDeleteAt](ArrayDeleteAt.md)
* [ArrayDeleteNoCase](ArrayDeleteNoCase.md)
* [ArrayEach](ArrayEach.md)
* [ArrayEvery](ArrayEvery.md)
* [ArrayFilter](ArrayFilter.md)
* [ArrayFind](ArrayFind.md)
* [ArrayFindAll](ArrayFindAll.md)
* [ArrayFindAllNoCase](ArrayFindAllNoCase.md)
* [ArrayFindNoCase](ArrayFindNoCase.md)
* [ArrayFirst](ArrayFirst.md)
* [ArrayGetMetadata](ArrayGetMetadata.md)
* [ArrayIndexExists](ArrayIndexExists.md)
* [ArrayInsertAt](ArrayInsertAt.md)
* [ArrayIsDefined](ArrayIsDefined.md)
* [ArrayLast](ArrayLast.md)
* [ArrayMap](ArrayMap.md)
* [ArrayMax](ArrayMax.md)
* [ArrayMedian](ArrayMedian.md)
* [ArrayMerge](ArrayMerge.md)
* [ArrayMid](ArrayMid.md)
* [ArrayMin](ArrayMin.md)
* [ArrayNew](ArrayNew.md)
* [ArrayNone](ArrayNone.md)
* [ArrayPop](ArrayPop.md)
* [ArrayPrepend](ArrayPrepend.md)
* [ArrayPush](ArrayPush.md)
* [ArrayRange](ArrayRange.md)
* [ArrayReduce](ArrayReduce.md)
* [ArrayReduceRight](ArrayReduceRight.md)
* [ArrayReverse](ArrayReverse.md)
* [ArraySet](ArraySet.md)
* [ArrayShift](ArrayShift.md)
* [ArraySlice](ArraySlice.md)
* [ArraySome](ArraySome.md)
* [ArraySort](ArraySort.md)
* [ArraySplice](ArraySplice.md)
* [ArraySum](ArraySum.md)
* [ArraySwap](ArraySwap.md)
* [ArrayToList](ArrayToList.md)
* [ArrayToStruct](ArrayToStruct.md)
* [ArrayUnshift](ArrayUnshift.md)
