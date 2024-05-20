# StructEvery

Used to iterate over a struct and test whether every item in the struct meets the test.

## Method Signature

```
StructEvery(struct=[structloose], callback=[function], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type          | Required   | Description                                                                                         | Default   |
| ------------ | ------------- | ---------- | --------------------------------------------------------------------------------------------------- | --------- |
| `struct`     | `structloose` | `true`     | The target struct to test                                                                           |           |
| `callback`   | `function`    | `true`     | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. |           |
| `parallel`   | `boolean`     | `false`    | Specifies whether the items can be executed in parallel                                             | false     |
| `maxThreads` | `integer`     | `false`    | The maximum number of threads to use when parallel = true                                           |           |
| ----------   | ------        | ---------- | -------------                                                                                       | --------- |

## Examples

```
StructEvery(struct=[structloose], callback=[function], parallel=[boolean], maxThreads=[integer])
```

## Related

* [StructAppend](structappend.md)
* [StructClear](structclear.md)
* [StructCopy](structcopy.md)
* [StructDelete](structdelete.md)
* [StructEach](structeach.md)
* [StructEquals](structequals.md)
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
