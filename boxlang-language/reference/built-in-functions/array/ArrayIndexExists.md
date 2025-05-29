[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayIndexExists`

Returns whether there exists an item in the array at the selected index.

## Method Signature

```
ArrayIndexExists(array=[array], index=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to be searched. |  |
| `index` | `any` | `true` | The index to check. |  |

## Examples

### Simple example

To check an array element is define or not

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmMgNgFiU65Ya67yosySVP%2FSkoLSEg2FRJBqz2KX1LTMvNQUDYVimAk6CsYKmgqa1lwAtkgXRQ%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3,
	4,
	5
];
writeOutput( arrayIsDefined( someArray, 3 ) );

```

Result: Yes

### Simple example

To check an array element is define or not

<a href="https://try.boxlang.io/?code=eJwrzs9NdSwqSqxUsFWIVuDiNNTh4jQCYmMgNgFiU65Ya67yosySVP%2FSkoLSEg2FRJBqz2KX1LTMvNQUDYVimAk6CmYKmgqa1lwAtl0XSA%3D%3D" target="_blank">Run Example</a>

```java
someArray = [ 
	1,
	2,
	3,
	4,
	5
];
writeOutput( arrayIsDefined( someArray, 6 ) );

```

Result: false

### Simple example with two dimensional array

To check an array element is define or not

<a href="https://try.boxlang.io/?code=eJxzyywqLnEsKkqsVLBViFbg4jTU4eI0AmJjrlhrruLU5Py8FLg0UBYkbQiSNwQrSM7PTcrMS4WpSATRfqnlGgpGCprWXGCuY0FBal6KhgKyUh2FNIS9%2BBUiOwGosrwosyTVv7SkoLREA2KdZ7FLahpQPYZOYwVNkA4AntpGyg%3D%3D" target="_blank">Run Example</a>

```java
FirstArray = [ 
	1,
	2,
	3
];
secondArray = [
	11,
	12,
	13
];
combineArray = arrayNew( 2 );
arrayAppend( combineArray, firstArray );
arrayAppend( combineArray, secondArray );
writeOutput( arrayIsDefined( combineArray, 3 ) );

```

Result: No

### Simple example with two dimensional array

To check an array element is define or not

<a href="https://try.boxlang.io/?code=eJxzyywqLnEsKkqsVLBViFbg4jTU4eI0AmJjrlhrruLU5Py8FLg0UBYkbQiSNwQrSM7PTcrMS4WpSATRfqnlGgpGCprWXGCuY0FBal6KhgKyUh2FNIS9%2BBUiOwGosrwosyTVv7SkoLREA2KdZ7FLahpQPYZOoBNAOgCe00bJ" target="_blank">Run Example</a>

```java
FirstArray = [ 
	1,
	2,
	3
];
secondArray = [
	11,
	12,
	13
];
combineArray = arrayNew( 2 );
arrayAppend( combineArray, firstArray );
arrayAppend( combineArray, secondArray );
writeOutput( arrayIsDefined( combineArray, 2 ) );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxFjcEKwjAMhs%2FmKcJOGwwn7Dg8CF58BvGQuVSCa1eyFvHt7apYcsgHf74%2FRqOEkyq98YhXhF1F3s9ctYme8pIMI7k0GRcl9%2FjGNtFSDuE2wBStr5G2ust6ZiOOpxrN%2F0eLPTbYDNh1GDQypG3ZjqxoorsHWdyvozh7KU39Ieuw%2BYbmleEDVd85ZQ%3D%3D" target="_blank">Run Example</a>

```java
fruitArray = [ 
	"apple",
	"kiwi",
	"banana",
	"orange",
	"mango",
	"kiwi"
];
dump( arrayIsDefined( fruitArray, 3 ) ); // true
// member function
dump( fruitArray.isDefined( 30 ) );
 // false

```



## Related

  * [ArrayPrepend](./ArrayPrepend.md)
  * [ArrayResize](./ArrayResize.md)
  * [ArrayReduce](./ArrayReduce.md)
  * [ArrayMerge](./ArrayMerge.md)
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
