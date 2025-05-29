[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructSome`

Used to iterate over a struct and test whether any items meet the test callback.

## Method Signature

```
StructSome(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

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

  * [StructEquals](./StructEquals.md)
  * [StructReduce](./StructReduce.md)
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
  * [StructNew](./StructNew.md)
  * [StructGet](./StructGet.md)
  * [StructDelete](./StructDelete.md)
  * [StructFilter](./StructFilter.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructSort](./StructSort.md)
  * [StructEach](./StructEach.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructClear](./StructClear.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructCopy](./StructCopy.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructInsert](./StructInsert.md)
  * [StructMap](./StructMap.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructValueArray](./StructValueArray.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
