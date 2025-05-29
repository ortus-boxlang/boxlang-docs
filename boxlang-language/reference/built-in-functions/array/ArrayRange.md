[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ArrayRange`

Build an array out of a range of numbers or using our range syntax: {start}..{end}
 or using the from and to arguments

<p>
 You can also build negative ranges
 <p>

 <pre>
 arrayRange( "1..5" )
 arrayRange( "-10..5" )
 arrayRange( 1, 500 )
 </pre>

## Method Signature

```
ArrayRange(from=[any], to=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `from` | `any` | `false` | The initial index, defaults to 1 or you can use the {start}..{end} notation | `1` |
| `to` | `numeric` | `false` | The last index item, or defaults to the from value |  |

## Examples

### Create an array of sequential numbers using the string syntax.



<a href="https://try.boxlang.io/?code=eJxLLCpSsFVILCpKrAxKzEtP1VBQMtLTM1VS0LTmKi%2FKLEn1Ly0pKC0BCodkZBZDFCpkJBYrKCmoQXg%2BqXkaIJaCJlBESSE1JzU3Na%2BkWA9sBACINxyk" target="_blank">Run Example</a>

```java
arr = arrayRange( "2..5" );
writeOutput( "This array has " & arrayLen( arr ) & " elements." );

```

Result: This array has 4 elements.

### Create an array of sequential numbers using the string syntax.



<a href="https://try.boxlang.io/?code=eJxLLCpSsFVILCpKrAxKzEtP1VAw1VEwNFDQtOYqL8osSfUvLSkoLdFQUArJyCyGqFPISCxWUFJQg%2FB8UvM0QCwFTaCIkkJqTmpual5JsZ4SyAgAdvQcfw%3D%3D" target="_blank">Run Example</a>

```java
arr = arrayRange( 5, 10 );
writeOutput( "This array has " & arrayLen( arr ) & " elements." );

```

Result: This array has 6 elements.


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
