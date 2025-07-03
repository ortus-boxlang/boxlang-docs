# StructEvery

Used to iterate over a struct and test whether **every** item meets the test callback.

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
StructEvery(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                   | Required | Description                                                                                                                                                                                                       | Default |
| ------------ | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`     | `struct`               | `true`   | The target struct to test                                                                                                                                                                                         |         |
| `callback`   | `function:BiPredicate` | `true`   | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args.                       |         |
| `parallel`   | `boolean`              | `false`  | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool.                                                                                       | `false` |
| `maxThreads` | `integer`              | `false`  | <p>The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>If parallel is false, this argument is ignored.</p> |         |

## Examples

### Simple structEvery example

Here we have simple example about structevery function.

```java
var struct = { 
	"Name" : "Dhar",
	"Age" : "20",
	"Country" : "US"
};
structevery( struct, ( Any key, Any value ) => {
	writeOutput( key & ":" & value & " " );
	return true;
} );

```

Result: Country:US Name:Dhar Age:20

### Simple structEvery member function example

Here we have simple example about structevery member function.

```java
var struct = { 
	"Name" : "Dhar",
	"Age" : "20",
	"Country" : "US"
};
struct.every( ( Any key, Any value ) => {
	writeOutput( key & ":" & value & " " );
	return false;
} );

```

Result: Country:US

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJy9kEtLw0AUhdeZX3HMKoHS7A0RQi1SFB%2BoiBQXU7m1QyYzOo9KKP3vTiZUWuxK0OU9d%2Ba75xyuRMulRYUNWDK5ecIp0lbrdMSS29lFP2mhmn6c1A9xSfozZduSFQUeLeHeGf%2FqpmsyXZbDaQhHhjuCDhIa6iyEgo2vxphIbb0hGHLeKIsgU7EMDmjMuJT1YKc2dK2F7YKtfTz4sB4hQ626Ho4c1Rk2LAluZku4FUV1xS041lz63al4CZmK2IGTs0QsM1yR%2BibPwc2bb0k5O76cPuMl8PMen%2BxRSpZs2U6I3ku2RV6yc9%2B%2BZ5B8QbJKf6ZJR8GRqY7EzP%2B6zTsvyP26TWGxkFw1h1V%2BROZBlSf%2F0WXMcqzLIWT4%2BwXfD%2B4F)

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	CAT : "meow"
};
// Use StructEvery() to iterate over keys in struct. Closure returns true/false.
allAnimalsAreNoisy = StructEvery( animals, ( Any key ) => {
	// If the key has a value return true (noisy animal)
	if( Len( animals[ arguments.KEY ] ) ) {
		return true;
	}
	return false;
} );
Dump( label="allAnimalsAreNoisy", var=allAnimalsAreNoisy );
// Use StructEvery() to iterate over keys in struct. Closure returns true/false.
allAnimalsAreQuiet = StructEvery( animals, ( Any key ) => {
	// If the key is blank return true (quiet animal)
	if( !Len( animals[ arguments.KEY ] ) ) {
		return true;
	}
	return false;
} );
Dump( label="allAnimalsAreQuiet", var=allAnimalsAreQuiet );

```

## Related

* [StructAppend](StructAppend.md)
* [StructClear](StructClear.md)
* [StructCopy](StructCopy.md)
* [StructDelete](StructDelete.md)
* [StructEach](StructEach.md)
* [StructEquals](StructEquals.md)
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
* [StructNone](StructNone.md)
* [StructReduce](StructReduce.md)
* [StructSome](StructSome.md)
* [StructSort](StructSort.md)
* [StructToQueryString](StructToQueryString.md)
* [StructToSorted](StructToSorted.md)
* [StructUpdate](StructUpdate.md)
* [StructValueArray](StructValueArray.md)
