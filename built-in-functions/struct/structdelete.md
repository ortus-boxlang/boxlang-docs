# StructDelete

Deletes a key from a struct

## Method Signature

```
StructDelete(struct=[modifiableStruct], key=[string], indicateNotExists=[boolean])
```

### Arguments

| Argument            | Type               | Required   | Description       | Default   |
| ------------------- | ------------------ | ---------- | ----------------- | --------- |
| `struct`            | `modifiableStruct` | `true`     | The struct target |           |
| `key`               | `string`           | `true`     | The key to delete |           |
| `indicateNotExists` | `boolean`          | `false`    |                   | false     |
| ----------          | ------             | ---------- | -------------     | --------- |

## Examples

```
StructDelete(struct=[modifiableStruct], key=[string], indicateNotExists=[boolean])
```

## Related

* [StructAppend](structappend.md)
* [StructClear](structclear.md)
* [StructCopy](structcopy.md)
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
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
