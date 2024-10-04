# StructInsert

Inserts a key/value pair in to a struct - with an optional overwrite argument

## Method Signature

```
StructInsert(struct=[modifiableStruct], key=[string], value=[any], overwrite=[boolean])
```

### Arguments

| Argument    | Type               | Required | Description                                                                  | Default |
| ----------- | ------------------ | -------- | ---------------------------------------------------------------------------- | ------- |
| `struct`    | `modifiableStruct` | `true`   | The target struct                                                            |         |
| `key`       | `string`           | `true`   | The struct key                                                               |         |
| `value`     | `any`              | `true`   | The value to assign for the specified key                                    |         |
| `overwrite` | `boolean`          | `false`  | Whether to overwrite the existing value if the key exists ( default: false ) | `false` |

## Examples

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
