[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArraySet`

In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

## Method Signature

```
ArraySet(array=[modifiablearray], start=[any], end=[any], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `modifiablearray` | `true` | The array to modify |  |
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
  * [ArrayMax](./ArrayMax.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayDeleteAt](./ArrayDeleteAt.md)
  * [ArraySort](./ArraySort.md)
  * [ArrayEach](./ArrayEach.md)
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
