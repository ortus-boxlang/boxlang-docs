[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayGetMetadata`

Gets metadata for items of an array and indicates the array type.

## Method Signature

```
ArrayGetMetadata(array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `true` | The array to be inserted into |  |

## Examples

### Simple Example



<a href="https://try.boxlang.io/?code=eJxFjLEKAjEQRGv3K5ZUJ4j5ALEStTnxChsRi0UXDXgxrHPI%2Fb1JLK4ZdmZnnve8MRUoS2Qxk5GqtuEDXvOFZk5Seqlb5CuFqJPrJT7ejq4r8p53ituTe4XwXSBUJO8ra6845EeJGp7o8zrsLET8U8aYlL4WoMcBaUBTWcvTuduW9g83kzbW" target="_blank">Run Example</a>

```java
// Create an array
arrayList = [
	"apple",
	"pineapple",
	"mango"
];
// Fetch meta data
data = arrayGetMetadata( arrayList );
// Print array type
writeOutput( data.TYPE );

```

Result: synchronized

### Member Function Example



<a href="https://try.boxlang.io/?code=eJxFTDsKwkAQrZ1TDFtFkOwBxEq0UkyRRsRi0CEumHUZXwi5vZsVtHm8v%2Fe8NRUoS2Qxk4kKHsIbvOELLZyk9FS3yiyFqH%2FVS%2Bxejq5r8p73ituDe4XwXSA0Q97%2FvupOcczp7FfLMmksRHwbjCkpjRagpwFpQFVe6vbc7Di3P%2B5SNMU%3D" target="_blank">Run Example</a>

```java
// Create an array
arrayList = [
	"apple",
	"pineapple",
	"mango"
];
// Fetch meta data
data = arrayList.getMetadata();
// Print array type
writeOutput( data.TYPE );

```

Result: synchronized

### Dump Metadata of Typed Array (Member syntax)

Return struct has a new key called `dimensions` and can also have a defined datatype. Supported datatypes are String, Numeric, Boolean, Date, Array, Struct, Query, Component, [Component name], Binary, and Function.


```java
arr = arrayNew[ "String" ]( 1 );
writeOutput( JSONSerialize( arr.getMetadata() ) );

```

Result: {"dimensions":1,"datatype":"String","type":"synchronized"}


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
