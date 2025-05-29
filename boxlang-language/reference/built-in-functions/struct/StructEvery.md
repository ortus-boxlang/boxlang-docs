[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructEvery`

Used to iterate over a struct and test whether every item in the struct meets the test.

## Method Signature

```
StructEvery(struct=[structloose], callback=[function:BiPredicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The target struct to test |  |
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

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

<a href="https://try.boxlang.io/?code=eJy9kEtLw0AUhdeZX3HMKoHS7A0RQi1SFB%2BoiBQXU7m1QyYzOo9KKP3vTiZUWuxK0OU9d%2Ba75xyuRMulRYUNWDK5ecIp0lbrdMSS29lFP2mhmn6c1A9xSfozZduSFQUeLeHeGf%2FqpmsyXZbDaQhHhjuCDhIa6iyEgo2vxphIbb0hGHLeKIsgU7EMDmjMuJT1YKc2dK2F7YKtfTz4sB4hQ626Ho4c1Rk2LAluZku4FUV1xS041lz63al4CZmK2IGTs0QsM1yR%2BibPwc2bb0k5O76cPuMl8PMen%2BxRSpZs2U6I3ku2RV6yc9%2B%2BZ5B8QbJKf6ZJR8GRqY7EzP%2B6zTsvyP26TWGxkFw1h1V%2BROZBlSf%2F0WXMcqzLIWT4%2BwXfD%2B4F" target="_blank">Run Example</a>

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
  * [StructSome](./StructSome.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
