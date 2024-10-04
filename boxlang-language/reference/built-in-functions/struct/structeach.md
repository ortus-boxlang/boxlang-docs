# StructEach

Used to iterate over a struct and run the function closure for each key/value pair.

## Method Signature

```
StructEach(struct=[structloose], callback=[function:BiConsumer], parallel=[boolean], maxThreads=[integer], ordered=[boolean])
```

### Arguments

| Argument     | Type                  | Required | Description                                                                                                                                                                                           | Default |
| ------------ | --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`     | `struct`              | `true`   | The target struct to iterate                                                                                                                                                                          |         |
| `callback`   | `function:BiConsumer` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiConsumer which will only receive the first 2 args. |         |
| `parallel`   | `boolean`             | `false`  | Specifies whether the items can be executed in parallel                                                                                                                                               | `false` |
| `maxThreads` | `integer`             | `false`  | The maximum number of threads to use when parallel = true                                                                                                                                             |         |
| `ordered`    | `boolean`             | `false`  | (BoxLang only) whether parallel operations should execute and maintain order                                                                                                                          | `false` |

## Examples

## Related

* [StructAppend](structappend.md)
* [StructClear](structclear.md)
* [StructCopy](structcopy.md)
* [StructDelete](structdelete.md)
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
