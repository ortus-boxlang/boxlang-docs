[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructUpdate`

Updates or sets a key/value pair in to a struct

## Method Signature

```
StructUpdate(struct=[modifiableStruct], key=[any], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `modifiableStruct` | `true` | The target struct |  |
| `key` | `any` | `true` | The struct key |  |
| `value` | `any` | `true` | The value to assign for the specified key |  |

## Examples

### Updates a structure value at specific key

Change value of structure item

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJ0VLBSMNTh4nQC0kZA2hlIGwNpFyBtwlVrzVUMVh1akJJYkqqhkAvVraOglKyko2BoqqBpzVVelFmS6lKaW6Ch4BXs7xecWpSZmJNZhaRcQROkDgDFciI%2F" target="_blank">Run Example</a>

```java
myStruct = { 
	A : 1,
	B : 2,
	C : 3,
	D : 4
};
structUpdate( myStruct, "c", 15 );
writeDump( JSONSerialize( myStruct ) );

```

Result: {"A":1,"B":2,"C":15,"D":4}

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljk0LgjAcxs%2FuUzz8TwaC98KDGESnAovOSweOdJO15SH67unUyDo%2Bbz8ermTD6zsSPMGC7HDBGtRoTRELjvvdoLRUt0Fm6cmHQnfEXhsWx8gr3aFwxghlwUcU27qmDVHzq6gTypYhRXhwk0wKK085tyW3AgW3kOqDya1xhR2zcHYjUF%2FrKdT2YJoA%2FsbM7KSt4Pys%2FGUurqXfg6E4jf4%2FvgHMuF3T" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink",
	CAT : "meow"
};
// Show current animals
Dump( label="Current animals", var=animals );
// Update cat in animals
StructUpdate( animals, "cat", "purr" );
// Show animals with updated cat in animals
Dump( label="Animals with cat updated", var=animals );

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
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
