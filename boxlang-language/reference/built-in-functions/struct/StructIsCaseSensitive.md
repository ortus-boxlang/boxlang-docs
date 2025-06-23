[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructIsCaseSensitive`

Returns whether the give struct is case sensitive

## Method Signature

```
StructIsCaseSensitive(struct=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to test for type |  |

## Examples

### Full Function with Explicit CaseSensitive

Show when the struct is explicitly set to casesensitive.

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLjFUsFWAsPxSyzUUlJITi1OLU%2FOKM0syy1KVFDStuXJhKvVcfVx9QeqVUnNcc%2F3zUpXQJY3Akj6puSXl%2FhiSxhCdQMmMolSQ3vKizJJU%2F9KSgNISDagbPIudgfYHw%2BzXUIAboaAJcgsAgzY7%2Bw%3D%3D" target="_blank">Run Example</a>

```java
myStruct1 = StructNew( "casesensitive" );
myStruct1.ELEM1 = "elEmOne";
myStruct1.ELEM2 = "eLemtwO";
myStruct1.ELEM3 = "elemthree";
writeOutPut( StructIsCaseSensitive( myStruct1 ) );

```

Result: YES

### Member Function with Explicit CaseSensitive

Show when the struct is explicitly set to casesensitive.

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLjFUsFWAsPxSyzUUlJITi1OLU%2FOKM0syy1KVFDStuXJhKvVcfVx9QeqVUnNcc%2F3zUpXQJY3Akj6puSXl%2FhiSxhCdQMmMolSQ3vKizJJU%2F9KSgNISDQWE2sxiZ6AbgmFu0NAEOQIA3Ng5hA%3D%3D" target="_blank">Run Example</a>

```java
myStruct1 = StructNew( "casesensitive" );
myStruct1.ELEM1 = "elEmOne";
myStruct1.ELEM2 = "eLemtwO";
myStruct1.ELEM3 = "elemthree";
writeOutPut( myStruct1.isCaseSensitive() );

```

Result: YES

### Full Function with Implicit Struct Creation and Default Case Sensitivity

Show when the struct is implicitly created.

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLjFRsFWoVuDiVErNSc01VFKwUgCyXHP981KVdMCirrlGEFGf1NyScn%2BoaGquMVQtUDSjKDVViavWmqu8KLMk1b%2B0JKC0REMBYr5nsXNicWpwal5xZklmWaqGQi7cYk0FTWsuALPjKbA%3D" target="_blank">Run Example</a>

```java
myStruct4 = { 
	"elem1" : "elEmOne",
	"elEm2" : "eLemtwO",
	"elem3" : "elemthree"
};
writeOutPut( StructIsCaseSensitive( myStruct4 ) );

```

Result: NO


## Related

  * [StructAppend](./StructAppend.md)
  * [StructClear](./StructClear.md)
  * [StructCopy](./StructCopy.md)
  * [StructDelete](./StructDelete.md)
  * [StructEach](./StructEach.md)
  * [StructEquals](./StructEquals.md)
  * [StructEvery](./StructEvery.md)
  * [StructFilter](./StructFilter.md)
  * [StructFind](./StructFind.md)
  * [StructFindKey](./StructFindKey.md)
  * [StructFindValue](./StructFindValue.md)
  * [StructGet](./StructGet.md)
  * [StructGetMetadata](./StructGetMetadata.md)
  * [StructInsert](./StructInsert.md)
  * [StructIsOrdered](./StructIsOrdered.md)
  * [StructKeyArray](./StructKeyArray.md)
  * [StructKeyExists](./StructKeyExists.md)
  * [StructKeyList](./StructKeyList.md)
  * [StructKeyTranslate](./StructKeyTranslate.md)
  * [StructMap](./StructMap.md)
  * [StructNew](./StructNew.md)
  * [StructNone](./StructNone.md)
  * [StructReduce](./StructReduce.md)
  * [StructSome](./StructSome.md)
  * [StructSort](./StructSort.md)
  * [StructToQueryString](./StructToQueryString.md)
  * [StructToSorted](./StructToSorted.md)
  * [StructUpdate](./StructUpdate.md)
  * [StructValueArray](./StructValueArray.md)
