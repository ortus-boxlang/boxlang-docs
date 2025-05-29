[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructKeyArray`

Get keys of a struct as an array

## Method Signature

```
StructKeyArray(structure=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `structure` | `struct` | `true` |  |  |

## Examples

### Traditional function



<a href="https://try.boxlang.io/?code=eJwrLkksKS12zk9JLVawVahW4OL091awUjAyMNDh4nQOcnUMcXUB8w2BfD%2F%2FkHhffxdPN0%2BwoLGBCVDQydElPsg1MNQ1OAQoZgLWCFLo5h%2Fq5wIWMeGqteYqL8osSXUpzS3QUCguKSpNLvFOrXQsKkqsBPERbtBU0LTmAgBCNyiV" target="_blank">Run Example</a>

```java
statusCodes = { 
	OK : 200,
	CREATED : 201,
	NOT_MODIFIED : 304,
	BAD_REQUEST : 400,
	NOT_FOUND : 404
};
writeDump( structKeyArray( statusCodes ) );

```

Result: [NOT_FOUND, BAD_REQUEST, CREATED, OK, NOT_MODIFIED]

### Using Member Function

 Retrieve a comma separated list of keys using the member function

<a href="https://try.boxlang.io/?code=eJwrLkksKS12zk9JLVawVahW4OL091awUjAyMNDh4nQOcnUMcXUB8w2BfD%2F%2FkHhffxdPN0%2BwoLGBCVDQydElPsg1MNQ1OAQoZgLWCFLo5h%2Fq5wIWMeGqteYqL8osSXUpzS3QUChG2KmXnVrpWFSUWKmhqaBpzQUAJU0l%2Fg%3D%3D" target="_blank">Run Example</a>

```java
statusCodes = { 
	OK : 200,
	CREATED : 201,
	NOT_MODIFIED : 304,
	BAD_REQUEST : 400,
	NOT_FOUND : 404
};
writeDump( statusCodes.keyArray() );

```

Result: [NOT_FOUND, BAD_REQUEST, CREATED, OK, NOT_MODIFIED]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLzMvMTcwpVrBVqFbg4nT2D1ewUlDKzc9X0uHiDPB0B%2FHyM%2FOyQVxnxxCwZGp%2BOYjr5BnkAuInZ2QWFShx1VpzpZTmFmgoBJcUlSaXeKdWOhYVJVZqKCRCbdBU0LTmAgB3qB7N" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	CAT : "meow",
	BIRD : "chirp"
};
dump( StructKeyArray( animals ) );

```


<a href="https://try.boxlang.io/?code=eJxLzMvMTcwpVrBViFbg4nT2D1ewUlDKzc9X0uHiDPB0B%2FHyM%2FOyQVxnxxCwZGp%2BOYjr5BnkAuInZ2QWFShxxVpzpZTmFmgoBJcUlSaXeKdWOhYVJVZqKCRCbdBU0LTmAgBmSB6N" target="_blank">Run Example</a>

```java
animals = [ 
	COW : "moo",
	PIG : "oink",
	CAT : "meow",
	BIRD : "chirp"
];
dump( StructKeyArray( animals ) );

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
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
