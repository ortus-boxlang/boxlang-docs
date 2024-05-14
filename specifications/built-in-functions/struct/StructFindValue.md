[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructFindValue`

Searches a struct for a given value and returns an array of results

## Method Signature
```
StructFindValue(struct=[structloose], value=[string], scope=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `structloose` | `true` | The struct to search | |
| `value` | `string` | `true` | The value to search for | |
| `scope` | `string` | `false` | Either one (default), which finds the first instance or all to return all values | one|
|----------|------|----------|-------------|---------|



## Examples

```
StructFindValue(struct=[structloose], value=[string], scope=[string])
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
  * [StructFindKey](StructFindKey.md)
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
