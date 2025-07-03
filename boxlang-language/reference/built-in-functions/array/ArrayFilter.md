# ArrayFilter

Filters an array and returns a new array containing the result\
This BIF will invoke the callback function for each item in the array, passing the item, its index, and the array itself.

* If the callback returns true, the item will be included in the new array.
* If the callback returns false, the item will be excluded from the new array.
* If the callback requires strict arguments, it will only receive the item and its index.
* If the callback does not require strict arguments, it will receive the item, its index, and the array itself.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
ArrayFilter(array=[array], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `array`      | `array`              | `true`   | The array to filter entries from                                                                                                                                                                                  |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg.                  |         |
| `parallel`   | `boolean`            | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`            | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### Simple numeric comparison

Take an array of struct items and use arrayFilter to return ones of a rating 3 and higher.

[Run Example](https://try.boxlang.io/?code=eJxt0MEKgkAQBuCz%2BxTDnhQkKOuSKHgx6mCQ3aLDRruypKtMa2Lhu7fbIchkbj8f%2FzAjsJU6QWQ9RHAC4ryI41BhUwproKxpSk59GyLTUhU2XRJn8P%2FohSkzYzuftDUyVfz1riZtZWg9potJepOdHMvASHIOiWCPGqXmqdV3cy2zV6ey1BxdEN8%2F%2BOBConowtAIPohjMEuS6RfXJZofkuM02EEcQhGQALySd7b22VePCLt9nOUfJSvnkpvZ3qWf1G9r8Zvs%3D)

```java
fruitArray = [ 
	{
		"fruit" : "apple",
		"rating" : 4
	},
	{
		"fruit" : "banana",
		"rating" : 1
	},
	{
		"fruit" : "orange",
		"rating" : 5
	},
	{
		"fruit" : "mango",
		"rating" : 2
	},
	{
		"fruit" : "kiwi",
		"rating" : 3
	}
];
favoriteFruits = arrayFilter( fruitArray, ( Any item ) => {
	return item.RATING >= 3;
} );
writedump( JSONSerialize( favoriteFruits ) );

```

Result: \[{"fruit":"apple","rating":4},{"fruit":"orange","rating":5},{"fruit":"kiwi","rating":3}]

### Using a member function

This is the same example as above, but using a member function on the array instead of a standalone function.

[Run Example](https://try.boxlang.io/?code=eJxtz0ELgkAQBeCz%2ByuGPSmIUNYlUfBS1MEgu0WHjXZlSVeZ1sTC%2F95uhw4qc3t8vOEJbKVOEVkPMVyAOB%2FiOFTYlMIGKGuaklPfhsi0VIVNV8QZ%2FAm9MWVubBeztkamiknvetZWhtZjupylD9nJsQyNJNeICPaqUWq%2Btfpp1or%2F9EDIUnN0wYVU9WBQBR7ECZh65LpF9cuCU3reZztIYggjMoAXkc423tuqceGQH7Oco2SlfHMXRu88q79fCGTe)

```java
fruitArray = [ 
	{
		"fruit" : "apple",
		"rating" : 4
	},
	{
		"fruit" : "banana",
		"rating" : 1
	},
	{
		"fruit" : "orange",
		"rating" : 5
	},
	{
		"fruit" : "mango",
		"rating" : 2
	},
	{
		"fruit" : "kiwi",
		"rating" : 3
	}
];
favoriteFruits = fruitArray.filter( ( Any item ) => {
	return item.RATING >= 3;
} );
writedump( JSONSerialize( favoriteFruits ) );

```

Result: \[{"fruit":"apple","rating":4},{"fruit":"orange","rating":5},{"fruit":"kiwi","rating":3}]

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxtz0ELgkAQBeDz7q8YPClIUNYlUfBieOkgdooOG62ypKtMayHhf2%2BMCFZkbo%2BPN7wSe2USRDFABGfg7M0ZS%2FNTVsAeHNF1tXR8ivKkyI4Hyracjf6MXYWms916wbUodDXr2y24hlhrs80Cu6uXslVAil9CXopni8rIdFr3oGViWpiq2kh0ofxv9sGFRA9AtAEPohjoAUrTo%2F5mq19zHEEQ8hG8kN%2F6pqMK%2BwHlH8T%2BVdU%3D)

```java
fruitArray = [ 
	{
		FRUIT : "apple",
		RATING : 4
	},
	{
		FRUIT : "banana",
		RATING : 1
	},
	{
		FRUIT : "orange",
		RATING : 5
	},
	{
		FRUIT : "mango",
		RATING : 2
	},
	{
		FRUIT : "kiwi",
		RATING : 3
	}
];
favoriteFruits = arrayFilter( fruitArray, ( Any item ) => {
	return item.RATING >= 3;
} );
dump( favoriteFruits );

```

[Run Example](https://try.boxlang.io/?code=eJxtz0ELgkAUBODz7q94eFIQoaxLouDF8NJB7BQdNtqVJV3ltRYS%2FvdeEYEicxs%2BBkZhr22KKAaI4QScvThjWXHMS9iBI7qulo5PVZGW%2BWFP3Yaz0Z%2BxizCUqVstuBaFqWZ72wXXEGunbL3Abvqppyokxc8RV%2BLRorYy%2B7y70zP1vxkoXVuJLriQmgEINeBBnABNo7Q9mm8X%2FDaTGMKIj%2BBF%2FNo3nQuzaerfsLhTuA%3D%3D)

```java
fruitArray = [ 
	{
		FRUIT : "apple",
		RATING : 4
	},
	{
		FRUIT : "banana",
		RATING : 1
	},
	{
		FRUIT : "orange",
		RATING : 5
	},
	{
		FRUIT : "mango",
		RATING : 2
	},
	{
		FRUIT : "kiwi",
		RATING : 3
	}
];
favoriteFruits = fruitArray.filter( ( Any item ) => {
	return item.RATING >= 3;
} );
dump( favoriteFruits );

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
* [ArrayResize](ArrayResize.md)
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
