[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructKeyExists`

Tests whether a key exists in a struct and returns a boolean value

## Method Signature

```
StructKeyExists(struct=[structloose], key=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to test |  |
| `key` | `any` | `true` | The key within the struct to test for existence |  |

## Examples

### Check if server struct has OS key



<a href="https://try.boxlang.io/?code=eJwrLikqTS7xTq10rcgsLinWUChOLSpLLdJRUMovVlLQtOYCANfYCy4%3D" target="_blank">Run Example</a>

```java
structKeyExists( server, "os" );

```

Result: true

### Check if server struct has OS key using member function

CF11+ calling the keyExists member function on a struct.

<a href="https://try.boxlang.io/?code=eJwrTi0qSy3Sy06tdK3ILC4p1lBQyi9WUtC05gIAhJEIiw%3D%3D" target="_blank">Run Example</a>

```java
server.keyExists( "os" );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxdjs0KgkAUhdfOUxxmo4HgPmlRFiFBRQmth%2BGKgzoTjlEivnuOCUXczf04PxyhVS0qixV6MC853bAEr43hIfPO6d6RUbp0mKyzSSTzdLhJL1vHslDNnbMhZlGEpCBZojWwRFA5SupAL2VbC6Vh2%2BYhW6byANfpPVC3m9QA4jMkBLdaqIpjMV7PPJKFCcCzgpqx0UJg0l2dP2f80RyzgYEqSz%2BZo5m93wX%2FkTfpU0v8" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	CAT : "meow",
	BIRD : "chirp"
};
// Check to see if key exists in struct
if( StructKeyExists( animals, "snail" ) ) {
	echo( "There is a snail in 'animals'" );
}
 else {
	echo( "No snail exists in 'animals'" );
}

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
