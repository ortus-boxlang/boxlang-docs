[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructFindValue`

Searches a struct for a given value and returns an array of results

## Method Signature

```
StructFindValue(struct=[structloose], value=[string], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct to search |  |
| `value` | `string` | `true` | The value to search for |  |
| `scope` | `string` | `false` | Either one (default), which finds the first instance or all to return all values | `one` |

## Examples

### Find first match for a nested struct value



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJ0VLBSMNLh4nQC0iZA2hlIWwBpFyBtaABkuIIYIBVuYAZXrTVXLtQIPd%2FIYFdnfz%2BX4JCgUOcQkIlAAw2B6kxBOh2NCOkAckM8PINQ9DsZwix0Auk3M4XoD0vMKU0FqoCY45aZlwIW0VCAGa2joGRopAQk8%2FNSlRQ0rbnCizJLUv1LSwpKSzQUvIL9%2FYJTizITczKrwJog5mmCFAIA3MxIbw%3D%3D" target="_blank">Run Example</a>

```java
myStruct = { 
	A : 2,
	B : 4,
	C : 8,
	D : 10,
	E : 12,
	F : 12
};
myStruct.MYSECONDSTRUCT = {
	A1 : 50,
	A2 : 12
};
myStruct.MYSECONDSTRUCT.MYTHIRDSTRUCT = {
	B1 : 12,
	B2 : 65
};
myValue = StructFindValue( myStruct, "12", "one" );
WriteOutput( JSONSerialize( myValue ) );

```

Result: [{"path":".E","owner":{"A":2,"B":4,"C":8,"D":10,"E":12,"F":12,"MYSECONDSTRUCT":{"A1":50,"A2":12,"MYTHIRDSTRUCT":{"B2":65,"B1":12}}},"key":"E"}]

### Find all matches for a nested struct value



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJ0VLBSMNLh4nQC0iZA2hlIWwBpFyBtaABkuIIYIBVuYAZXrTVXLtQIPd%2FIYFdnfz%2BX4JCgUOcQkIlAAw2B6kxBOh2NCOkAckM8PINQ9DsZwix0Auk3M4XoD0vMKU0FqoCY45aZlwIW0VCAGa2joGRopAQkE3NylBQ0rbnCizJLUv1LSwpKSzQUvIL9%2FYJTizITczKrwJog5mmCFAIA2wdIZg%3D%3D" target="_blank">Run Example</a>

```java
myStruct = { 
	A : 2,
	B : 4,
	C : 8,
	D : 10,
	E : 12,
	F : 12
};
myStruct.MYSECONDSTRUCT = {
	A1 : 50,
	A2 : 12
};
myStruct.MYSECONDSTRUCT.MYTHIRDSTRUCT = {
	B1 : 12,
	B2 : 65
};
myValue = StructFindValue( myStruct, "12", "all" );
WriteOutput( JSONSerialize( myValue ) );

```

Result: [{"path":".E","owner":{"A":2,"B":4,"C":8,"D":10,"E":12,"F":12,"MYSECONDSTRUCT":{"A1":50,"A2":12,"MYTHIRDSTRUCT":{"B2":65,"B1":12}}},"key":"E"},{"path":".F","owner":{"A":2,"B":4,"C":8,"D":10,"E":12,"F":12,"MYSECONDSTRUCT":{"A1":50,"A2":12,"MYTHIRDSTRUCT":{"B2":65,"B1":12}}},"key":"F"},{"path":".MYSECONDSTRUCT.A2","owner":{"A1":50,"A2":12,"MYTHIRDSTRUCT":{"B2":65,"B1":12}},"key":"A2"},{"path":".MYSECONDSTRUCT.MYTHIRDSTRUCT.B1","owner":{"B2":65,"B1":12},"key":"B1"}]

### Find first match for a nested struct value using member function

Calling the findValue member function on a struct.

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJ0VLBSMNLh4nQC0iZA2hlIWwBpFyBtaABkuIIYIBVuYAZXrTVXLtQIPd%2FIYFdnfz%2BX4JCgUOcQkIlAAw2B6kxBOh2NCOkAckM8PINQ9DsZwix0Auk3M4XoD0vMKU0FqoCblJaZlwIW1FBQMjRS0lFQys9LVVLQtOYKL8osSfUvLSkoLdFQ8Ar29wtOLcpMzMmsAiqFGaQJUggA0rZF7A%3D%3D" target="_blank">Run Example</a>

```java
myStruct = { 
	A : 2,
	B : 4,
	C : 8,
	D : 10,
	E : 12,
	F : 12
};
myStruct.MYSECONDSTRUCT = {
	A1 : 50,
	A2 : 12
};
myStruct.MYSECONDSTRUCT.MYTHIRDSTRUCT = {
	B1 : 12,
	B2 : 65
};
myValue = myStruct.findValue( "12", "one" );
WriteOutput( JSONSerialize( myValue ) );

```

Result: [{"path":".E","owner":{"A":2,"B":4,"C":8,"D":10,"E":12,"F":12,"MYSECONDSTRUCT":{"A1":50,"A2":12,"MYTHIRDSTRUCT":{"B2":65,"B1":12}}},"key":"E"}]

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljz1vwjAQhuf4V7zyEpAisbfKEFGKMrSpmqqV2NxgqIU%2FqiQuA%2BK%2F95IYUMLmOz93z3vCKiN0gxQnsGhZfOEBJxZFr0VerujNjXM8oUaZb%2Fpai3ovOYvO1HzL11PcKXsY8UZulTdhYJl93O2X7jgaaCiP7nh2fmSLBcofdwS1IIao7Mmb3xm0%2BJY65dntgyf4E3UaKsz76WdltwFA5WwrlFV2T6D2Em6HeMgXsx2BL%2F07G%2BgUZVv7qu02fHb47CJKrlcFSR%2Bxlo3XbQNlMd01jvweQLJPDTfBxcDn4ay7fKT%2BB3b7hww%3D" target="_blank">Run Example</a>

```java
animals = { 
	COW : {
		NOISE : "moo",
		SIZE : "large"
	},
	PIG : {
		NOISE : "oink",
		SIZE : "medium"
	},
	CAT : {
		NOISE : "meow",
		SIZE : "small"
	}
};
// Show all animals
Dump( label="All animals", var=animals );
// Find animal containing value of 'medium'
findMediumAnimal = StructFindValue( animals, "medium" );
// Show results in findMediumAnimal
Dump( label="Results of StructFindValue(animals, ""medium"")", var=findMediumAnimal );

```



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
