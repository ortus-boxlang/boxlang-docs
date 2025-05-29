[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructToQueryString`

Converts a struct to a query string using the specified delimiter.

<p>
 The default delimiter is {@code "&"}

## Method Signature

```
StructToQueryString(struct=[structloose], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to convert |  |
| `delimiter` | `string` | `false` | The delimiter to use in the query string. Default is "&" | `&` |

## Examples

### structToQueryString with the default delimiter

Converting a struct to a query string using the default delimiter (&amp;)

<a href="https://try.boxlang.io/?code=eJwrzs9NDS4pKk0uUbBVqFbg4lRKyywqLvFLzE1VUrBSUPLKz8hT0gEK5yQiibrkpypx1VpzlRdllqS6lOYWaCgUgw0JyQ8sTS2qBJqYmZcOFESYrqmgac0FAIiYI08%3D" target="_blank">Run Example</a>

```java
someStruct = { 
	"firstName" : "John",
	"lastName" : "Doe"
};
writeDump( structToQueryString( someStruct ) );

```

Result: firstName=John&lastName=Doe


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
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
