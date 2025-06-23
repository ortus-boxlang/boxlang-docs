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
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
