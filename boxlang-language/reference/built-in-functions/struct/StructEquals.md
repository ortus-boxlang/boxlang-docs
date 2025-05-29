[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructEquals`

Tests equality between two structs

## Method Signature

```
StructEquals(struct1=[structloose], struct2=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct1` | `struct` | `true` | The reference struct |  |
| `struct2` | `struct` | `true` | The struct to test for equality |  |

## Examples

### Append options to config struct (without overwrite flag)



<a href="https://try.boxlang.io/?code=eJxLzs9Ly0w3VLBVqFbg4nRUsFIw0OHidALRXLXWXMlgaSOQNKqsIUi2vCizJNW%2FtKSgtERDobikqDS5xLWwNDGnWEMBotFQRwFmgqaCpjUXABwCHhk%3D" target="_blank">Run Example</a>

```java
config1 = { 
	A : 0,
	B : 0
};
config2 = {
	A : 0,
	B : 1
};
writeOutput( structEquals( config1, config2 ) );

```

Result: NO


## Related

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
  * [StructEvery](./StructEvery.md)
  * [StructFind](./StructFind.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructAppend](./StructAppend.md)
