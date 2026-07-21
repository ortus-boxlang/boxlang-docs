[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructEach`

Used to iterate over a struct and run the function closure for each key/value pair.

<p>
 The function will be passed 3 arguments: the key, the value, and the struct.
 You can alternatively pass a Java BiConsumer which will only receive the first 2 args (key and value).
 <p>
 This BIF is useful for performing side effects on each item in the struct, such as logging or modifying external state.
 <p>

 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

## Method Signature

```
StructEach(struct=[structloose], callback=[function:BiConsumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to iterate |  |
| `callback` | `function:BiConsumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiConsumer which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | Whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### structEach() with an inline function (closure)

Use a function to write out the keys in a structure to the screen

<a href="https://try.boxlang.io/?code=eJwrzs9NDS4pKk0uUbBVqFbg4nRUsFIw1OHidALSRkDaGUgbc9VacxWDVbkmJmdoKBTDdekoaCg45lUqZKdW6oAZZYk5pakKmgq2dgrVXJzlRZklqf6lJQWlJRoKSt6plQpKCmogxUBSSSGzGMyFaAEKWAO5mtZctSACAOHWKZ8%3D" target="_blank">Run Example</a>

```java
someStruct = { 
	A : 1,
	B : 2,
	C : 3
};
structEach( someStruct, ( Any key, Any value ) => {
	writeOutput( "Key " & key & " is " & value & "; " );
} );

```

Result: Key a is 1; Key b is 2; Key c is 3; 

### Using a function reference



<a href="https://try.boxlang.io/?code=eJylUE1rwkAQPWd%2FxSMHq5DivWKhtPXUkmL7B8a4MUviJuzOJkTxvze7DVYK9uJlmJn3sW82p9ZiiSNE9Jy%2BpWs8IN5UTsaJiFZp%2BuLnRh0O5BefH%2Bn6KzDIlpI3VFWxOC2EmM%2BhaS%2B3yJ3OWNU6bGpWmQQXxEORZwxMpbTgrgaZndtLzTYJjFL2IL1FS0MCNKQM6jwgmTNm4EGxNBRMRsCycRk7I%2B%2Bsl9%2F%2FSq04P7iTvKK2NoPaTvGke09NQvPDn%2BEoos7jqePG8RTxe4981CDGJGSbDJ2yYRx1C3HypxqnxySvlBXTGTrFBejvp1xQvPlw9WUy73bdS0PpSmn5n9uV25aPN5znyzfgvrLD" target="_blank">Run Example</a>

```java
favs = { 
	COLOR : "blue",
	FOOD : "pizza",
	SPORT : "basketball"
};

// named function
// notice that the function takes two arguments, the key and value pair of the current iteration of the structure's key-value pairs
function getFavorites( Any key, Any value ) {
	writeOutput( "My favorite " & key & " is " & value );
}
// run structEach() with a named function
structEach( favs, getFavorites );
// run structEach() with an inline function
structEach( favs, ( Any key, Any value ) => {
	writeOutput( "My favorite " & key & " is " & value );
} );

```


### Using the member function



<a href="https://try.boxlang.io/?code=eJxFjcEKgkAQhs%2FuUwzuRUHKylOmYO4KErlkeharhaKocHcLEd%2B9dS9dhvm%2F%2BYZfyFYqkb4uXEAEAyCL7WANS9%2F3kJWWNKkoMXmhc8GqZs9InuUGrvxAw21CmpIeanqsNAvM4yRmrC6IIQEaQyT%2BRTPenq8OOJA8e7jz3jPLp30oDi5EMQzI%2BnY3yZmSbyUdsLG28HTBxsKbUwfz2AY3ROM0fh9xNO4%3D" target="_blank">Run Example</a>

```java
statusCodes = { 
	OK : 200,
	CREATED : 201,
	NOT_MODIFIED : 304,
	BAD_REQUEST : 400,
	NOT_FOUND : 404
};
statusCodes.each( ( Any key, Any value ) => {
	writeOutput( "#key# => #value#<br />" );
} );

```

Result: NOT_FOUND => 404
BAD_REQUEST => 400
CREATED => 201
OK => 200
NOT_MODIFIED => 304

### Accessing a reference to the looping struct in the callback

<a href="https://try.boxlang.io/?code=eJwrLkksKS12zk9JLVawVahW4OL091awUjAyMNDh4nQOcnUMcXUB8w2BfD%2F%2FkHhffxdPN0%2BwoLGBCVDQydElPsg1MNQ1OAQoZgLWCFLo5h%2Fq5wIWMeGqteYqRlikl5qYnKGhoKHgmFepkJ1aqQNmlCXmlKZCmMUlRaXJJQqaCrZ2CtVcnOVFmSWpLqW5BRpwGWuuWhABAJnsNEM%3D" target="_blank">Run Example</a>

```java
statusCodes = { 
	OK : 200,
	CREATED : 201,
	NOT_MODIFIED : 304,
	BAD_REQUEST : 400,
	NOT_FOUND : 404
};
statusCodes.each( ( Any key, Any value, Any struct ) => {
	writeDump( struct );
} );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxdjUsLgkAUhdfOrzjMIhUk94mBmES4KDCIiBaTDCk%2BJtRJRPzv%2BUjCNhe%2Be8%2F9DsvjjKUlbLQginu8YAOaCUENopwO%2B4FEnCcDus55PHJRU9JZJKgKGVYeCyMNbNIY0ODkDRLeQIe9RUsU00QQiXrcqax4yoznVbnuUSXKTmYvDSl78NSmPm%2BogTcr7F%2FM967QrYVFLftMKnlvm1pvC%2Bv9T7t0rUDn%2F7nrK8EyeB9qu2F8AE2dWYA%3D" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	CAT : "meow"
};
StructEach( animals, ( Any key ) => {
	// Show key 'arguments.key'
	Dump( label="Key", var=arguments.KEY );
	// Show key's value 'animals[arguments.key]'
	Dump( label=arguments.KEY & "'s value", var=animals[ arguments.KEY ] );
} );

```



## Related

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEquals](./StructEquals.md)
  * [StructEvery](./StructEvery.md)
  * [StructFilter](./StructFilter.md)
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
