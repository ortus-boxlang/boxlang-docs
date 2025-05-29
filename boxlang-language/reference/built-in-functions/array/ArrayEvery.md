[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayEvery`

Returns true if every closure returns true, otherwise false

## Method Signature

```
ArrayEvery(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to reduce |  |
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |
| `initialValue` | `any` | `false` |  |  |

## Examples

### Example for positive result

Checks whether all items in an array are greater than 2 and outputs true because all of them fulfill the requirement.

<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI00eHiNAViMyA254q15iovyixJ9S8tKSgt0VBIBKl0LUstqoSydRQ0FBzzKhXKEnNKUxU0FWztFKq5OItSS0qL8qCCdgpG1ly1QDlNay4AGTodsA%3D%3D" target="_blank">Run Example</a>

```java
array = [ 
	4,
	5,
	6,
	7
];
writeOutput( arrayEvery( array, ( Any value ) => {
	return value > 2;
} ) );

```

Result: true

### Example for negative result

Checks whether all items in an array are greater than 2 and outputs false because some of them do not fulfill the requirement.

<a href="https://try.boxlang.io/?code=eJxLLCpKrFSwVYhW4OI01OHiNAJiYyA24Yq15iovyixJ9S8tKSgt0VBIBKl0LUstqoSydRQ0FBzzKhXKEnNKUxU0FWztFKq5OItSS0qL8qCCdgpG1ly1QDlNay4AFRodpA%3D%3D" target="_blank">Run Example</a>

```java
array = [ 
	1,
	2,
	3,
	4
];
writeOutput( arrayEvery( array, ( Any value ) => {
	return value > 2;
} ) );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljkELgjAYhs%2F7fsWLJ4WhFXpJFDxUENSlY4QMWpfmlOmCEf73JhgYXR8envdtXC2MEQ4FriD2JsbO1WmHLYK9EfoZcE%2BqwwTSFbGR%2FzoXKxfGZv1vHNt%2BqWSpV%2BiWk1CqbtXd7zbzhVi%2BpHEhQlTaoZOmbzUiFCV8z8jBGj3TeGqVhX%2BU08gxGCs5MkQ53W3Thfi2PUCS4CFUL%2BkDrGE7rw%3D%3D" target="_blank">Run Example</a>

```java
my_array = [ 
	{
		NAME : "Frank",
		AGE : 40
	},
	{
		NAME : "Sue",
		AGE : 21
	},
	{
		NAME : "Jose",
		AGE : 54
	}
];
all_old = my_array.every( ( Any person ) => {
	return person.AGE >= 40;
}, true, 5 );
dump( all_old );
 // false

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
  * [ArrayAppend](./ArrayAppend.md)
  * [ArrayLast](./ArrayLast.md)
  * [ArrayMin](./ArrayMin.md)
