[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructInsert`

Inserts a key/value pair in to a struct - with an optional overwrite argument

## Method Signature

```
StructInsert(struct=[modifiableStruct], key=[any], value=[any], overwrite=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `modifiableStruct` | `true` | The target struct |  |
| `key` | `any` | `true` | The struct key |  |
| `value` | `any` | `true` | The value to assign for the specified key |  |
| `overwrite` | `boolean` | `false` | Whether to overwrite the existing value if the key exists ( default: false ) | `false` |

## Examples

### Simple Example

Inserts a new key/value into the structure

<a href="https://try.boxlang.io/?code=eJwli1EKgzAQBb%2BbUzz2q4InqHgAaaFnSNtFA5qG3Q0i4t2N%2BjUwzEw%2BocUKd6PBByE8QB%2F5z5HqonhhPVUvzJHc1jg1yV%2FrorLYHZNPNWgMSalQ%2BEeoGjdLMH5nS7kk1%2FDk5RX0OlAd0Q6fbSUY" target="_blank">Run Example</a>

```java
map = { 
	"hair" : "brown",
	"eyes" : "green"
};
structInsert( map, "lips", "red" );
writeOutput( structKeyList( map ) );

```

Result: eyes,lips,hair

### Overwrite Example

Throws exception when you try to add a duplicate key, when allowoverwrite parameter is false.

<a href="https://try.boxlang.io/?code=eJwljEEOgjAQRdfMKb6zgoQTSDyAK89Q6ygkUprpNNgQ7m7F1Ute%2Fvuzi7hgAzU8ukkZZ%2FBdlzVwX5UUSYd6qUhg2gcyLdioSabZ2zUkUWsxu9jjf1Cp8qh4uncSdAPt8M78iNaFAvl0v3zVyeSWLeZas6gueuJjTF80fCtJ" target="_blank">Run Example</a>

```java
map = { 
	"hair" : "brown",
	"eyes" : "green"
};
try {
	structInsert( map, "hair", "red", false );
} catch (any ex) {
	writeOutput( "error!" );
}

```

Result: error!

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljs0KwjAQhM%2FNUyx7qlDoXelBKkhPCj14jkmgwWQjaWIO4rvbPwvF4%2BzMfjOctOWmhwrewLL6coM9oHUOC5Zdm%2FOonKYHss%2BBlSW0nUsgoveKAvD5l52ifeZg%2BF2ZCuutiQW8uK8WBbuJ0lCvfADBA2gKbgW1wUcRZjf%2FXQvAIThw0CqXcEFMQ9YEDUKTMFGqfsRuJx2X8qRDN5VyKZX8X%2FYFW0NWfw%3D%3D" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink"
};
// Show current animals
Dump( label="Current animals", var=animals );
// Insert cat into animals
StructInsert( animals, "cat", "meow" );
// Show animals, now includes cat
Dump( label="Animals with cat added", var=animals );

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
