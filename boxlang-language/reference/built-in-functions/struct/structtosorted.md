# StructToSorted

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

## Method Signature

```
StructToSorted(struct=[structloose], sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function:Comparator])
```

### Arguments

| Argument          | Type                  | Required | Description                                                                                                            | Default |
| ----------------- | --------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`          | `struct`              | `true`   | The struct to sort                                                                                                     |         |
| `sortType`        | `any`                 | `false`  | An optional sort type to apply to that type - if a callback is given in this position it will be used as that argument | `text`  |
| `sortOrder`       | `string`              | `false`  | The sort order applicable to the sortType argument                                                                     | `asc`   |
| `localeSensitive` | `any`                 | `false`  |                                                                                                                        | `false` |
| `callback`        | `function:Comparator` | `false`  | An optional callback to use as the sorting function. You can alternatively pass a Java Comparator.                     |         |

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
* [StructNew](structnew.md)
* [StructReduce](structreduce.md)
* [StructSome](structsome.md)
* [StructSort](structsort.md)
* [StructToQueryString](structtoquerystring.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
