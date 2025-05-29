[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructCopy`

Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.

## Method Signature

```
StructCopy(struct=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to copy |  |

## Examples

### Copy a structure and change it. Original structure stays unchanged



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJUSlRSsFIw1AGykkAsIxArGcQy5qq15sqt9Esth2soBjOc8wsqNRRyYeZooqjScwKqM0URilZQSlFSiAWKm1hzQYxwSc1JLUkFGQJXpaMAshZoWHlRZkmqf2lJQWmJBtRG79RKn8ziEmRLFdQUlBQetU0CkmqYqhCO1gQZCQAMZEy5" target="_blank">Run Example</a>

```java
myStruct = { 
	"a" : 1,
	"b" : 2,
	"c" : 3
};
myNewStruct = structCopy( myStruct );
myNewStruct.B = 5;
myNewStruct[ "d" ] = 4;
structDelete( myNewStruct, "c" );
writeOutput( structKeyList( myStruct ) & " → " & structKeyList( myNewStruct ) );

```

Result: b,a,c → b,a,d

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtkEFrgzAYhs%2FNr3jx1IK09w0P0tGx0wYd9JyaiMGYT2KsjLL%2FviRaUdaL8CXv9%2BTx5UY1XHfIcAfbHD8veEHSECUp23x9vIeJlKkT9vvKDgecKxpQ9NZK48DHXfbWN%2B0Wml%2BlzpLj%2BjJJceM2mybsIuVI7c8jgM7ZvnBwhJLbhoWPtznH0xDcYr0cFUIqhSaqO2hVy%2Bcup8DipZN2ydtNTvGlkZkL4QnkKp8cSXtclNbwZx5QSi8Y4ns2cvK2lUbMZinuvrv8O3YnafBtLWXnlPGDMoXuhexQcLe2zaffHJSrwi24EFI8LXDRgSDPCpoVv8n%2F0FhBQa2SAqWlZi7zKkuycQED71ZvPYr5A2vYsJc%3D" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink"
};
// Show current animals
Dump( label="Current animals", var=animals );
// Copy animals struct to farm
farm = StructCopy( animals );
// Show farm, looks like animals
Dump( label="Farm after StructCopy()", var=farm );
// Add another animal. Will not affect farm.
StructAppend( animals, {
	CAT : "meow"
} );
// Show animals, now includes cat
Dump( label="Animals with cat added", var=animals );
// Show farm, does not have cat
Dump( label="Farm copied from animals before cat was added", var=farm );

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
  * [StructFindKey](./StructFindKey.md)
  * [StructInsert](./StructInsert.md)
  * [StructMap](./StructMap.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructValueArray](./StructValueArray.md)
  * [StructSome](./StructSome.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
