# StructNew

Creates a new struct of the specified type.

The available types are:

* casesensitive
* default
* ordered-casesensitive
* ordered
* soft
* sorted
* weak

## Method Signature

```
StructNew(type=[string], sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function:Comparator])
```

### Arguments

| Argument          | Type                  | Required | Description                                                                                        | Default   |
| ----------------- | --------------------- | -------- | -------------------------------------------------------------------------------------------------- | --------- |
| `type`            | `string`              | `false`  | The struct type                                                                                    | `default` |
| `sortType`        | `any`                 | `false`  | An optional sort type to apply to that type                                                        |           |
| `sortOrder`       | `string`              | `false`  | The sort order applicable to the sortType argument                                                 | `asc`     |
| `localeSensitive` | `any`                 | `false`  |                                                                                                    | `false`   |
| `callback`        | `function:Comparator` | `false`  | An optional callback to use as the sorting function. You can alternatively pass a Java Comparator. |           |

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
