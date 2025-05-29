[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayReduce`

Run the provided udf over the array to reduce the values to a single output

## Method Signature

```
ArrayReduce(array=[array], callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the accumulator, the current item, and the<br>                    current index. You can alternatively pass a Java BiFunction which will only receive the first 2 args. The function should return the new accumulator value. |  |
| `initialValue` | `any` | `false` | The initial value of the accumulator |  |

## Examples

### Simple arrayReduce Example

Sum each `a` element in the array

<a href="https://try.boxlang.io/?code=eJxVjcEKwjAQRM%2FZr5hjikEsKIilQsC74FU8hLgHoUlDTNQi%2FXdjQYq3fTuzb23vQsevg0kGLc4g8SYhNHZYkxjVjPX2nzd1Ybo0dM%2BuXJoYzXDia7YsYWepgoT2A0Lkh5om7tixT6jQ7lFskVOOfipg8UuXuqFRYYWqoWe8JT7mFHKS%2BH4ruw8PZTLx" target="_blank">Run Example</a>

```java
complexData = [ 
	{
		A : 4
	},
	{
		A : 18
	},
	{
		A : 51
	}
];
sum = arrayReduce( complexData, ( Any prev, Any element ) => {
	return prev + element.A;
}, 0 );
writeOutput( sum );

```

Result: 73

### Additional Examples

<a href="https://try.boxlang.io?code=eJyVjs0KglAQhdfOUxzuwh8S1GonBr5C22hx0yGDm8akkUTv3uXqwkUtYjhwhrP4PuF6qLhGgVJEj3v3hjiAvCwmb22zsdnSMUaIsh1RaZExdvWhzcCIUOzwIk%2B4H6SddqymMad3jBRRTvVwvYWQGRflSBKMFzb1HVlK8kODPNWwMZ2yDqpvWNi1U%2Fc0uj2rf618KHv%2Bwk2pb3K0sAucABwcMzigD5k6WtY%3D" target="_blank">Run Example</a>

```java
reduced = ArrayReduce( [ 
	1,
	2,
	3,
	4
], ( Any carry, Any value ) => {
	return carry + value;
}, 0 );
dump( reduced ); // yields 10
reduced = ArrayReduce( [
	"hello",
	"there",
	"boxlang"
], ( Any carry, Any value ) => {
	return carry & " " & value;
}, "" );
dump( reduced );
 // yields 'hello there boxlang'

```



## Related

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
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
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayEvery](./ArrayEvery.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
