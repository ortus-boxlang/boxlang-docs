[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayMerge`

This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).

## Method Signature

```
ArrayMerge(array1=[array], array2=[array], leaveIndex=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array1` | `array` | `true` | The first array to merge |  |
| `array2` | `array` | `true` | The second array to merge |  |
| `leaveIndex` | `boolean` | `true` | Set to true maintain value indexes - if two values have the same index it will keep values from array1 | `false` |

## Examples

### Standard function syntax

 Merge two arrays resulting in a single re-indexed array. All elements of both arrays are preserved.

<a href="https://try.boxlang.io/?code=eJxVjjEOwjAMRWdyiihTK%2FUGFSsTiIUNdTDgppFKbTkOqLcnSWFAXp7l52%2BPkoLavb1as3PAPKPrMt1gyVWRBBaPzgy9eaH3AWPR80DpCUrVuYMI6YYkSwVGiF9gRok1YUKYdVoPRI8Sk9dgPaF4bOxYPuns70bbm7cExXNSTtps6oWOIebmL6Yt7gf8AT2c" target="_blank">Run Example</a>

```java
fruit = [ 
	"apple",
	"banana",
	"orange"
];
veggies = [
	"tomato",
	"carrot",
	"corn",
	"peas",
	"peppers"
];
healthyFoods = arrayMerge( fruit, veggies );
writeOutput( arrayToList( healthyFoods ) );

```

Result: apple,banana,orange,tomato,carrot,corn,peas,peppers

### Member function syntax

Merge two arrays resulting in a single re-indexed array. All elements of both arrays are preserved.

<a href="https://try.boxlang.io/?code=eJxVjbEKAjEMQGf7FaXTHYg%2FcLg6CS5u4hA11yvcNSFNlft726qDZHkhj5dRclC7txdrNg6YZ3TbQjeIZRqSQPTozHUwT%2FQ%2BYKp6OSgtoNScO4iQfpAkNmCE9AVmlNQKE8Ks03ogetTMWL%2FvFhSPnf3V%2B8G8JCiesnLWzpY2rGc6hlSWv0Bf3TeMSzt%2F" target="_blank">Run Example</a>

```java
fruit = [ 
	"apple",
	"banana",
	"orange"
];
veggies = [
	"tomato",
	"carrot",
	"corn",
	"peas",
	"peppers"
];
healthyFoods = fruit.merge( veggies );
writeOutput( arrayToList( healthyFoods ) );

```

Result: apple,banana,orange,tomato,carrot,corn,peas,peppers

### Example where leaveIndex parameter is true

Merge two arrays resulting in a single re-indexed array. Where the both arrays have elements in the same position, only values from the first array are included in the result. Valid using standard or member function syntax.

Note how the first three elements of the veggies array are not merged because the fruit array already has values for elements 1-3.

<a href="https://try.boxlang.io/?code=eJxVjjsOwjAMhmdyCitTK%2FUGFSsTiIUNdTDgppFKHTkOqLcnSbsgL5%2Fl%2F%2BFRklc4wh3MwWIIM9ku0wOXPBVZcHFkzdCbDznnKRZ5Pii%2FUblqnijCuiHLUiEQxh1CIIk1YSKcdVpPzK8Sk224XkgcNTCWTzrYOzpQSQRtb77ila5JQ9JmM9z47GNe%2FsLaov0BdY4%2FqA%3D%3D" target="_blank">Run Example</a>

```java
fruit = [ 
	"apple",
	"banana",
	"orange"
];
veggies = [
	"tomato",
	"carrot",
	"corn",
	"peas",
	"peppers"
];
healthyFoods = arrayMerge( fruit, veggies, true );
writeOutput( arrayToList( healthyFoods ) );

```

Result: apple,banana,orange,peas,peppers

### Additional Examples


```java
aNames = array( 10412, 42, 33, 2, 999, 12769, 888 );
aNames2 = array( 33, "b", "c", "d", "e", "f", "g" );
dump( arrayMerge( aNames, aNames2 ) );
// member function
dump( aNames.merge( aNames2 ) );
dump( aNames.merge( aNames2, true ) );

```



## Related

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReduce](./ArrayReduce.md)
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
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
