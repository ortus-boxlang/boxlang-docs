# StructReduce

Run the provided udf against struct to reduce the values to a single output

## Method Signature

```
StructReduce(struct=[structloose], callback=[function], initialValue=[any])
```

### Arguments

| Argument       | Type       | Required | Description                                                                                                                                                                                                                                   | Default |
| -------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`       | `struct`   | `true`   | The struct to reduce                                                                                                                                                                                                                          |         |
| `callback`     | `function` | `true`   | <p>The function to invoke for each entry in the struct. The function will be passed 4 arguments: the accumulator, they entry key,<br>the<br>current index, and the original struct. The function should return the new accumulator value.</p> |         |
| `initialValue` | `any`      | `false`  | The initial value of the accumulator                                                                                                                                                                                                          |         |

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
* [StructSome](structsome.md)
* [StructSort](structsort.md)
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
