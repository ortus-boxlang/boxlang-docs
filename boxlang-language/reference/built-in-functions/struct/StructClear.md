[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructClear`

Clear all items from struct

## Method Signature

```
StructClear(structure=[modifiableStruct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `structure` | `modifiableStruct` | `true` | The struct to clear. |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJwrKMpPy8xJVbBVqFbg4vRz9HVVsFJQ8srPyFPS4eL09AsOCQr1dfULAYmml2aWJBaBxP2dnUMDHEM8%2Ff1A4sWZeempRUpctdZcxSVFpcklzjmpiUUaCgVQszWtucqLMktS%2FUtLCkpLNBS8gv39glOLMhNzMqtSkZSBFAIA3vYrvA%3D%3D" target="_blank">Run Example</a>

```java
profile = { 
	NAME : "John",
	INSTRUMENT : "guitar",
	OCCUPATION : "singer"
};
structClear( profile );
writeOutput( JSONSerialize( profile ) );

```

Result: An empty struct

### Tag Syntax




```java
<bx:set profile = { 
	NAME : "John",
	INSTRUMENT : "guitar",
	OCCUPATION : "singer"
	} >
<bx:set structClear( profile ) >
<bx:dump var="#profile#"/>
```

Result: An empty struct

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljs0KwjAQhM%2FNUww5tRDoXelBIognhR48ryVqMD8lTRUR311NezB4Wr7ZnZklpy2ZAQ2eYIXcHbAAt95zwYr9dvMlr92Vs9eS1TXai7%2BjG0NQLoImL1uPti9h6KhMw2W%2B5AI3Cs1MqFKKNIoChhjGLrJpJKlEfpfaZknAfUDZPj7ywtVsoVNUAR0Zo90Z7U9q9f%2FEG64LUEQ%3D" target="_blank">Run Example</a>

```java
animals = { 
	COW : "moo",
	PIG : "oink"
};
// Show current animals
Dump( label="Current animals", var=animals );
// Clear struct
structClear( animals );
// Show animals, now empty
Dump( label="Animals after calling StructClear()", var=animals );

```



## Related

  * [StructAppend](./StructAppend.md)
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
  * [StructIsCaseSensitive](./StructIsCaseSensitive.md)
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
