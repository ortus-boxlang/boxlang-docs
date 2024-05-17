# StructAppend

Appends the contents of a second struct to the first struct either with or without overwrite

## Method Signature

```
StructAppend(struct1=[structloose], struct2=[structloose], overwrite=[boolean])
```

### Arguments

| Argument    | Type          | Required   | Description                                                                                    | Default   |
| ----------- | ------------- | ---------- | ---------------------------------------------------------------------------------------------- | --------- |
| `struct1`   | `structloose` | `true`     | The target struct which will be the recipient of the appending                                 |           |
| `struct2`   | `structloose` | `true`     | The struct containing the values to be appended                                                |           |
| `overwrite` | `boolean`     | `false`    | Default true. Whether to overwrite existing values found in struct1 from the values in struct2 | true      |
| ----------  | ------        | ---------- | -------------                                                                                  | --------- |

## Examples

```
StructAppend(struct1=[structloose], struct2=[structloose], overwrite=[boolean])
```

## Related

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
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
