[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructKeyTranslate`

Converts a struct with dot-notated keys in to an unflattened version

## Method Signature

```
StructKeyTranslate(struct=[structloose], deep=[boolean], retainKeys=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to unflatten |  |
| `deep` | `boolean` | `false` | Whether to recurse in to nested keys - default false | `false` |
| `retainKeys` | `boolean` | `false` | Whether to retain the original dot-notated keys - default false | `false` |

## Examples

### Translate struct keys using a mapping

```java
data = { first_name: "Luis", last_name: "Majano" };
mapping = { first_name: "firstName", last_name: "lastName" };
result = structKeyTranslate( data, mapping );
writeOutput( result.containsKey( "firstName" ) );

```

Result: true

### Using the member function

```java
data = { usr_name: "admin" };
result = data.keyTranslate( { usr_name: "username" } );
writeOutput( result.username );

```

Result: admin

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
