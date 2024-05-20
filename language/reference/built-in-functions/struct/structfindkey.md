# StructFindKey

Searches a struct for a given key and returns an array of values

## Method Signature

```
StructFindKey(struct=[structloose], key=[string], scope=[string])
```

### Arguments

| Argument   | Type          | Required   | Description                                                                      | Default   |
| ---------- | ------------- | ---------- | -------------------------------------------------------------------------------- | --------- |
| `struct`   | `structloose` | `true`     | The struct to search                                                             |           |
| `key`      | `string`      | `true`     | The key to search for                                                            |           |
| `scope`    | `string`      | `false`    | Either one (default), which finds the first instance or all to return all values | one       |
| ---------- | ------        | ---------- | -------------                                                                    | --------- |

## Examples

```
StructFindKey(struct=[structloose], key=[string], scope=[string])
```

## Related

* [StructAppend](structappend.md)
* [StructClear](structclear.md)
* [StructCopy](structcopy.md)
* [StructDelete](structdelete.md)
* [StructEach](structeach.md)
* [StructEquals](structequals.md)
* [StructEvery](structevery.md)
* [StructFilter](structfilter.md)
* [StructFind](structfind.md)
* [StructFindValue](structfindvalue.md)
* [StructGet](structget.md)
* [StructGetMetadata](structgetmetadata.md)
* [StructInsert](structinsert.md)
* [StructIsCaseSensitive](structiscasesensitive.md)
* [StructIsOrdered](structisordered.md)
* [StructKeyArray](structkeyarray.md)
* [StructKeyExists](structkeyexists.md)
* [StructKeyList](structkeylist.md)
* [StructKeyTranslate](structkeytranslate.md)
* [StructMap](structmap.md)
* [StructNew](structnew.md)
* [StructReduce](structreduce.md)
* [StructSome](structsome.md)
* [StructSort](structsort.md)
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
