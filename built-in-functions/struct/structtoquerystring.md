# StructToQueryString

Converts a struct to a query string using the specified delimiter.

## Method Signature

```
StructToQueryString(struct=[structloose], delimiter=[string])
```

### Arguments

| Argument    | Type          | Required   | Description                                              | Default   |
| ----------- | ------------- | ---------- | -------------------------------------------------------- | --------- |
| `struct`    | `structloose` | `true`     | The struct to convert                                    |           |
| `delimiter` | `string`      | `false`    | The delimiter to use in the query string. Default is "&" | &         |
| ----------  | ------        | ---------- | -------------                                            | --------- |

## Examples

```
StructToQueryString(struct=[structloose], delimiter=[string])
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
* [StructFindKey](structfindkey.md)
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
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
