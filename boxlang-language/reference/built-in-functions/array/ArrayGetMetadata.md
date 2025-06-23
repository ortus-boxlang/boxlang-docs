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
  * [ArrayToList](./ArrayToList.md)
  * [ArrayToStruct](./ArrayToStruct.md)
  * [ArrayUnshift](./ArrayUnshift.md)
