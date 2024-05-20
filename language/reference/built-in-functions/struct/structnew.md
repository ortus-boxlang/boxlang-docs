# StructNew

Creates a new struct of the specified type

## Method Signature

```
StructNew(type=[string], sortType=[string], sortOrder=[string], callback=[function])
```

### Arguments

| Argument    | Type       | Required   | Description                                         | Default   |
| ----------- | ---------- | ---------- | --------------------------------------------------- | --------- |
| `type`      | `string`   | `false`    | The struct type                                     | default   |
| `sortType`  | `string`   | `false`    | An optional sort type to apply to that type         |           |
| `sortOrder` | `string`   | `false`    | The sort order applicable to the sortType argument  | asc       |
| `callback`  | `function` | `false`    | An optional callback to use as the sorting function |           |
| ----------  | ------     | ---------- | -------------                                       | --------- |

## Examples

```
StructNew(type=[string], sortType=[string], sortOrder=[string], callback=[function])
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
* [StructReduce](structreduce.md)
* [StructSome](structsome.md)
* [StructSort](structsort.md)
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
