[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySet`

In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

## Method Signature

```
ArraySet(array=[assignablearray], start=[any], end=[any], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `assignablearray` | `true` | The array to modify |  |
| `start` | `any` | `true` | The starting index |  |
| `end` | `any` | `true` | The ending index |  |
| `value` | `any` | `true` |  |  |

## Examples

### Tag Syntax




```java
<bx:set MyNewArray = arrayNew( 1 ) > 
<!--- ArrayToList does not function properly if the Array has not been initialized with arraySet. ---> 
<bx:set temp = <!--- Transpiler workaround for BIF return type --->(( <bx:argument>, <bx:argument>, <bx:argument>, <bx:argument> ) => <bx:set arraySet( arg1, arg2, arg3, arg4 ) ><bx:return true>)( MyNewArray, 1, 6, "Initial Value" ) > 
<bx:output>#ArrayToList( myNewArray, ", " )#</bx:output>
```

Result: Initial Value, Initial Value, Initial Value, Initial Value, Initial Value, Initial Value

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLSy13LCpKrFSwVUgE0X6p5RoKhgqa1lxgbnBqiYZCHlSNjoKhjoKJjoKSY06OQmaxQnlqTo4SSGlKaW4BQhlIRF9fITc1Nym1SCGtNC%2B5JDM%2FjwsmrVcMMhNokhHQpJzUkmKF5IzEvPRUhcwSHIYBAK6VMzo%3D" target="_blank">Run Example</a>

```java
newArray = arrayNew( 1 );
arraySet( newArray, 1, 4, "All is well" );
dump( newArray );
// member function
newArray.set( 1, 2, "lets change it" );
dump( newArray );

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
