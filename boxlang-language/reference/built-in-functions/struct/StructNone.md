# StructNone

Used to iterate over a struct and test whether **NONE** item meets the test callback.

This is the opposite of {@link StructSome}.

The function will be passed 3 arguments: the value, the index, and the struct.\
You can alternatively pass a Java Predicate which will only receive the 1st arg.\
The function should return true if the item meets the test, and false otherwise.

**Note:** This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.

## Parallel Execution

If the `parallel` argument is set to true, and no `max_threads` are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.\
If `max_threads` is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.\
This allows for efficient processing of large structs, especially when the test function is computationally expensive or the struct is large.

## Method Signature

```
StructNone(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                   | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`     | `struct`               | `true`   | The target struct to test                                                                                                                                                                                         |         |
| `callback`   | `function:BiPredicate` | `true`   | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args.                       |         |
| `parallel`   | `boolean`              | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`              | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

## Related

* [StructAppend](StructAppend.md)
* [StructClear](StructClear.md)
* [StructCopy](StructCopy.md)
* [StructDelete](StructDelete.md)
* [StructEach](StructEach.md)
* [StructEquals](StructEquals.md)
* [StructEvery](StructEvery.md)
* [StructFilter](StructFilter.md)
* [StructFind](StructFind.md)
* [StructFindKey](StructFindKey.md)
* [StructFindValue](StructFindValue.md)
* [StructGet](StructGet.md)
* [StructGetMetadata](StructGetMetadata.md)
* [StructInsert](StructInsert.md)
* [StructIsCaseSensitive](StructIsCaseSensitive.md)
* [StructIsOrdered](StructIsOrdered.md)
* [StructKeyArray](StructKeyArray.md)
* [StructKeyExists](StructKeyExists.md)
* [StructKeyList](StructKeyList.md)
* [StructKeyTranslate](StructKeyTranslate.md)
* [StructMap](StructMap.md)
* [StructNew](StructNew.md)
* [StructReduce](StructReduce.md)
* [StructSome](StructSome.md)
* [StructSort](StructSort.md)
* [StructToQueryString](StructToQueryString.md)
* [StructToSorted](StructToSorted.md)
* [StructUpdate](StructUpdate.md)
* [StructValueArray](StructValueArray.md)
