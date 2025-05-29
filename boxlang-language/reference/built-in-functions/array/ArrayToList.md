[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayToList`

Used to iterate over an array and run the function closure for each item in the array.

## Method Signature

```
ArrayToList(array=[array], delimiter=[String], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to join together |  |
| `delimiter` | `String` | `false` | The character to use as a separator | `,` |
| `initialValue` | `any` | `false` |  |  |

## Examples

### Retrieve an array as a list

Uses the arrayToList function with a pipe delimiter to retrieve an array as a list

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmMgNuGKteYqBirwySwuAcongtSF5IN4GgrFMI06Cko1Sgqa1lzlRZklqf6lJQWlUGmwNqAEAIeLHbQ%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3,
	4
];
someList = arrayToList( someArray, "|" );
writeOutput( someList );

```

Result: "1|2|3|4"

### Retrieve an array as a list using the Array member function

 Uses the Array member function to retrieve an array as a list

<a href="https://try.boxlang.io/?code=eJwrTs3MS0vNSXEsKkqsVLBViFbg4lTySi0qqlTSAbJccxIz81LBTO%2BixNzUIjDTPTW%2FKD1ViSvWmqsYqt8ns7gEqL0Y2Ti9knyQsIamNVd5UWZJqn9pSUFpiYYCih6gJACWdipK" target="_blank">Run Example</a>

```java
seinfeldArray = [ 
	"Jerry",
	"Elaine",
	"Kramer",
	"George"
];
seinfeldList = seinfeldArray.toList();
writeOutput( seinfeldList );

```

Result: "Jerry,Elaine,Kramer,George"

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLSy13LCpKrFSwVYhW4OJUSlTSAZJJYDIZiZ2CxE4Fk2lKXLHWXCmluQUaCokgI0LyfTKLSzQU8mBGaipoWnPp6yvkpuYmpRYppJXmJZdk5ufpKJRnlmQoJJcWl%2BTnKhSnFiQWJZbkF0GNgunWK4Eap6SrqwQxCgC31S%2FC" target="_blank">Run Example</a>

```java
newArray = [ 
	"a",
	"b",
	"c",
	"b",
	"d",
	"b",
	"e",
	"f"
];
dump( arrayToList( newArray ) );
// member function, with custom separator
dump( newArray.toList( "--" ) );

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
