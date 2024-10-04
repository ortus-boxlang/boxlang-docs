# StructMap

Used to map a struct to a new struct of the same type containing the result

## Method Signature

```
StructMap(struct=[structloose], callback=[function:BiFunction], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                  | Required | Description                                                                                                                                                                                                                                               | Default |
| ------------ | --------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `struct`     | `struct`              | `true`   | The target struct to test                                                                                                                                                                                                                                 |         |
| `callback`   | `function:BiFunction` | `true`   | <p>The function used to produce the right-hand value assignment in the new struct. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiFunction which will only receive the<br>first 2 args.</p> |         |
| `parallel`   | `boolean`             | `false`  | Specifies whether the items can be executed in parallel                                                                                                                                                                                                   | `false` |
| `maxThreads` | `integer`             | `false`  | The maximum number of threads to use when parallel = true                                                                                                                                                                                                 |         |

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
* [StructNew](structnew.md)
* [StructReduce](structreduce.md)
* [StructSome](structsome.md)
* [StructSort](structsort.md)
* [StructToQueryString](structtoquerystring.md)
* [StructToSorted](structtosorted.md)
* [StructUpdate](structupdate.md)
* [StructValueArray](structvaluearray.md)
