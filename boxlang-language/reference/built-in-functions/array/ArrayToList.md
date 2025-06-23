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

  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayAvg](./ArrayAvg.md)
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
  * [ArrayFindNoCase](./ArrayFindNoCase.md)
  * [ArrayFirst](./ArrayFirst.md)
  * [ArrayGetMetadata](./ArrayGetMetadata.md)
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
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayUnshift](./ArrayUnshift.md)
