[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructFilter`

Filters a struct and returns a new struct with the values that pass the filter criteria.

This BIF will invoke the callback function for each entry in the struct, passing the key, value, and the struct itself.
 <ul>
 <li>If the callback returns true, the entry will be included in the new struct.</li>
 <li>If the callback returns false, the entry will be excluded from the new struct.</li>
 <li>If the callback requires strict arguments, it will only receive the key and value.</li>
 <li>If the callback does not require strict arguments, it will receive the key, value, and the original struct.</li>
 </ul>
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
StructFilter(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiPredicate` | `true` | The function used to filter. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### Example using a simple numeric comparison

Take a struct of items with their rating and use structFilter to return ones of a rating 3 and higher.

<a href="https://try.boxlang.io/?code=eJxVjUELgkAQhc%2FOr5ijgpeyLonCBhlSqXjpLLnGklmss4aI%2F73Z6FDM5Xvz4HuNNorKilR37THCCcERRXHc4QZXPjhbkfFxWHDIS5HtbbPmcGLOmZfMh%2FScMgYwh9BUw0MrkokVW2VP2lwoUS1J7WLzs%2Beji6Ib8SZH%2FwND1RqJHkYxTuBoSUZ332ccYRDCjF4IL6uvzf3Jtv8xLt%2FF2j2S" target="_blank">Run Example</a>

```java
fruitRatings = { 
	APPLE : 4,
	BANANA : 1,
	ORANGE : 5,
	MANGO : 2,
	KIWI : 3
};
favoriteFruits = structFilter( fruitRatings, ( Any key, Any value ) => {
	return value >= 3;
} );
writedump( favoriteFruits );

```

Result: {apple=4,orange=5,kiwi=3}

### Example using a member function

This is the same example, but using a member function on the struct instead of a standalone function.

<a href="https://try.boxlang.io/?code=eJxdjcEKgkAURdfOV9ylggRlbRKFCSqkUnHTWnAmhsximjFE%2FPfeRIuItzn3XThXaqtMVRvVXZ5IMIJ5vCyPW6yxDJm34TkdhTmFouL53jUrCifignhBfMjOGWHEppjJur9rZcTOiZ1S%2FizMpGqN0D588G7AVQzhB%2Fq6tQIBkhQj87QwVnffZ5ogitmEIGYv523s7eHjb4XKN%2FmnOu8%3D" target="_blank">Run Example</a>

```java
fruitRatings = { 
	APPLE : 4,
	BANANA : 1,
	ORANGE : 5,
	MANGO : 2,
	KIWI : 3
};
favoriteFruits = fruitRatings.filter( ( Any key, Any value ) => {
	return value >= 3;
} );
writedump( favoriteFruits );

```

Result: {apple=4,orange=5,kiwi=3}

### Additional Examples

<a href="https://try.boxlang.io/?code=eJy1kE9LxDAQxc%2FJp3j21EJx7y4Vin%2BW4rIqPYiIhyhTG5qmmqZKWfrdTeLuag8e9zIwb3i%2FmXlCy1aoHhm24Ozi9gFniNqui1LO7oqV7zqpG9%2BWm7xYeyHi05IvFijr7gtCKYgfCL8c2vcYSryQyqL8dxCl%2BBQm23VIgntFdj%2BHrYVFKxqC7mRP3NcxP5xWWjO82mupLJl4b0oRI9cjGhqRIDvHljOHLSpHo6DWoodwm9VAMGQHo%2BFAhDjgd5yEM1nFWJM%2BkJ8gzNvQkrb96c3VI54dP%2FF49oey5Gzie6FyLqdM%2FrVZCJuwKZ%2FFMHvunyyEIXwMkiwP9XhRBPw8ipMjZXEfVs2zmH3nDN8nsNCR" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	SNAIL : ""
};
// Show all animals
Dump( label="All animals", var=animals );
// Get animals that make noise
noisyAnimals = StructFilter( animals, ( Any key ) => {
	// If the key has a value return true (noisy animal)
	if( Len( animals[ arguments.KEY ] ) ) {
		return true;
	}
	return false;
} );
Dump( label="Noisy Animals", var=noisyAnimals );
// Get animals that are quiet
quietAnimals = StructFilter( animals, ( Any key ) => {
	// If the key has a value return true (quiet animal)
	if( !Len( animals[ arguments.KEY ] ) ) {
		return true;
	}
	return false;
} );
Dump( label="Quiet Animals", var=quietAnimals );

```



## Related

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEach](./StructEach.md)
  * [StructEquals](./StructEquals.md)
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructGet](./StructGet.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructInsert](./StructInsert.md)
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructMap](./StructMap.md)
  * [StructNew](./StructNew.md)
  * [StructNone](./StructNone.md)
  * [StructReduce](./StructReduce.md)
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
