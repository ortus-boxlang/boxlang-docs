[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructFindKey`

Searches a struct for a given key and returns an array of values

## Method Signature
```
StructFindKey(struct=[structloose], key=[string], scope=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to search | |
| `key` | `string` | `true` | The key to search for | |
| `scope` | `string` | `false` | Either one (default), which finds the first instance or all to return all values | one|
|----------|------|----------|-------------|---------|



## Examples

```
StructFindKey(struct=[structloose], key=[string], scope=[string])
```

## Related
  * [StructAppend](StructAppend.md)
  * [StructClear](StructClear.md)
  * [StructCopy](StructCopy.md)
  * [StructDelete](StructDelete.md)
  * [StructEach](StructEach.md)
  * [StructEquals](StructEquals.md)
  * [StructEvery](StructEvery.md)
  * [StructFilter](StructFilter.md)
  * [StructFind](StructFind.md)
  * [StructFindValue](StructFindValue.md)
  * [StructGet](StructGet.md)
  * [StructGetMetadata](StructGetMetadata.md)
  * [StructInsert](StructInsert.md)
  * [StructIsCaseSensitive](StructIsCaseSensitive.md)
  * [StructIsOrdered](StructIsOrdered.md)
  * [StructKeyArray](StructKeyArray.md)
  * [StructKeyExists](StructKeyExists.md)
  * [StructKeyList](StructKeyList.md)
  * [StructKeyTranslate](StructKeyTranslate.md)
  * [StructMap](StructMap.md)
  * [StructNew](StructNew.md)
  * [StructReduce](StructReduce.md)
  * [StructSome](StructSome.md)
  * [StructSort](StructSort.md)
  * [StructToQueryString](StructToQueryString.md)
  * [StructToSorted](StructToSorted.md)
  * [StructUpdate](StructUpdate.md)
  * [StructValueArray](StructValueArray.md)
