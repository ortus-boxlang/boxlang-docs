[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructSome`

Used to iterate over a struct and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the key, the value, and the struct.
 You can alternatively pass a Java BiPredicate which will only receive the first 2 args.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.
 <p>

## Method Signature

```
StructSome(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. |  |

## Examples

### The simple StructSome example

Here we have simple example about structsome function.


```java
<bx:script>
	struct = {
		"Name" : "Raja",
		"age" : 20,
		"mark" : 80
	};
	result = structSome( struct, ( Any key, Any value ) => {
		return key == "Name";
	} );
	writeOutput( (result ? "" : "No") & " Key Exists." );
</bx:script>

```

Result: Key Exists.

### The structSome member function example

Here we have simple example about structsome as member function.


```java
<bx:script>
	struct = {
		"Name" : "Raja",
		"age" : 20,
		"mark" : 80
	};
	result = struct.some( ( Any key, Any value ) => {
		return key == "average";
	} );
	writeOutput( (result ? "" : "No") & " Key Exists." );
</bx:script>

```

Result: No Key Exists.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJx1jb0KAjEQhOvsU2yZgyConSHCIRbWin3UtTF3J%2FkRjiPv7uZylWA3s9%2FOTIhocEIQa9zhBEK0h8vpemQTfSIQWYHY%2FKKndWFh238MsgZPIbkyELjsHs9DR5K1QoltP%2BKLRjWLj3WJsEGzL12P1L0l37yZ7wqdvZEz%2FI2NBuEpJt%2FXzKrOasgF1eAyyv4Lv8A9hg%3D%3D" target="_blank">Run Example</a>

```java
st = { 
	1 : {
		ACTIVE : true
	},
	2 : {
		ACTIVE : false
	},
	3 : {
		ACTIVE : false
	}
};
result = structSome( st, ( Any key, Any value ) => {
	dump( var=value, label=key );
	return value.ACTIVE;
} );
dump( result );

```



## Related

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEach](./StructEach.md)
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
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
