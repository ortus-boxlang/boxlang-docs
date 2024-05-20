# StructUpdate

Updates or sets a key/value pair in to a struct

## Method Signature

```
StructUpdate(struct=[modifiableStruct], key=[string], value=[any])
```

### Arguments

| Argument   | Type               | Required   | Description                               | Default   |
| ---------- | ------------------ | ---------- | ----------------------------------------- | --------- |
| `struct`   | `modifiableStruct` | `true`     | The target struct                         |           |
| `key`      | `string`           | `true`     | The struct key                            |           |
| `value`    | `any`              | `true`     | The value to assign for the specified key |           |
| ---------- | ------             | ---------- | -------------                             | --------- |

## Examples

```
StructUpdate(struct=[modifiableStruct], key=[string], value=[any])
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
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructValueArray](structvaluearray.md)
