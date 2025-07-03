# ArrayRange

Build an array out of a range of numbers or using our range syntax: {start}..{end}\
or using the from and to arguments

You can also build negative ranges

```
 arrayRange( "1..5" )
 arrayRange( "-10..5" )
 arrayRange( 1, 500 )
 
```

## Method Signature

```
ArrayRange(from=[any], to=[numeric])
```

### Arguments

| Argument | Type      | Required | Description                                                                 | Default |
| -------- | --------- | -------- | --------------------------------------------------------------------------- | ------- |
| `from`   | `any`     | `false`  | The initial index, defaults to 1 or you can use the {start}..{end} notation | `1`     |
| `to`     | `numeric` | `false`  | The last index item, or defaults to the from value                          |         |

## Examples

### Create an array of sequential numbers using the string syntax.

[Run Example](https://try.boxlang.io/?code=eJxLLCpSsFVILCpKrAxKzEtP1VBQMtLTM1VS0LTmKi%2FKLEn1Ly0pKC0BCodkZBZDFCpkJBYrKCmoQXg%2BqXkaIJaCJlBESSE1JzU3Na%2BkWA9sBACINxyk)

```java
arr = arrayRange( "2..5" );
writeOutput( "This array has " & arrayLen( arr ) & " elements." );

```

Result: This array has 4 elements.

### Create an array of sequential numbers using the string syntax.

[Run Example](https://try.boxlang.io/?code=eJxLLCpSsFVILCpKrAxKzEtP1VAw1VEwNFDQtOYqL8osSfUvLSkoLdFQUArJyCyGqFPISCxWUFJQg%2FB8UvM0QCwFTaCIkkJqTmpual5JsZ4SyAgAdvQcfw%3D%3D)

```java
arr = arrayRange( 5, 10 );
writeOutput( "This array has " & arrayLen( arr ) & " elements." );

```

Result: This array has 6 elements.

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
* [ArrayFilter](ArrayFilter.md)
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
