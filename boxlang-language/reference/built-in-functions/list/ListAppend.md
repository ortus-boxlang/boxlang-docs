[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ListAppend`

Appends an element to a list

## Method Signature

```
ListAppend(list=[string], value=[string], delimiter=[string], includeEmptyFields=[boolean], multiCharacterDelimiter=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `list` | `string` | `true` | string list to filter entries from |  |
| `value` | `string` | `true` | The value to append |  |
| `delimiter` | `string` | `false` | string the list delimiter | `,` |
| `includeEmptyFields` | `boolean` | `false` | boolean whether to include empty fields in the returned result | `false` |
| `multiCharacterDelimiter` | `boolean` | `false` | boolean whether the delimiter is multi-character | `true` |

## Examples

### Simple listAppend Example

Add 'foo' to the end of this list

<a href="https://try.boxlang.io/?code=eJzLz0nxySwuUbBVUEpKLNIBYiMla6681HKoaA6QciwoSM1L0VDIh6jVUVBKy89XUtC05iovyixJ9S8tKSgtgUsrqCko6eraKQFpmDFAlQDxyCCh" target="_blank">Run Example</a>

```java
oldList = "bar,bar2";
newList = listAppend( oldList, "foo" );
writeOutput( oldList & "-->" & newList );

```

Result: bar,bar2,foo

### Simple listAppend Example with Delimiter

Add 'foo' to the end of this list using a custom delimiter

<a href="https://try.boxlang.io/?code=eJzLz0nxySwuUbBVUEpKLNIBYiMla6681HKoaA6QciwoSM1L0VDIh6jVUVBKy89XAlI1Sgqa1lzlRZklqf6lJQWlJXA1CmoKSrq6dkpAGmYWUCUAhFMhrQ%3D%3D" target="_blank">Run Example</a>

```java
oldList = "bar,bar2";
newList = listAppend( oldList, "foo", "|" );
writeOutput( oldList & "-->" & newList );

```

Result: bar,bar2|foo

### Simple listAppend Example with Empty Fields On

CF2018+ Add 'foo,,' to the end of this list using includeEmptyFields as true

<a href="https://try.boxlang.io/?code=eJzLz0nxySwuUbBVUEpKLNIBYiMla6681HKoaA6QciwoSM1L0VDIh6jVUVBKy8%2FX0VECMkBESVFpqoKmNVd5UWZJqn9pSUFpCVytgpqCkq6unRKQhpkJVAkAiv8jwQ%3D%3D" target="_blank">Run Example</a>

```java
oldList = "bar,bar2";
newList = listAppend( oldList, "foo,,", ",", true );
writeOutput( oldList & "-->" & newList );

```

Result: bar,bar2,foo,,

### Simple listAppend Example with Empty Fields Off

CF2018+ Add 'foo' to the end of this list using includeEmptyFields as false

<a href="https://try.boxlang.io/?code=eJzLz0nxySwuUbBVUEpKLNIBYiMla6681HKoaA6QciwoSM1L0VDIh6jVUVBKy8%2FX0VECMkBEWmJOcaqCpjVXeVFmSap%2FaUlBaQlcsYKagpKurp0SkIYZClQJAK6NJAw%3D" target="_blank">Run Example</a>

```java
oldList = "bar,bar2";
newList = listAppend( oldList, "foo,,", ",", false );
writeOutput( oldList & "-->" & newList );

```

Result: bar,bar2,foo

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVjr0KAjEQhPs8xZBGheD1HhaCjc29QzCrFzA%2FJBvivb254IFWC%2FPN7IxbXjYzzpDBk%2BIaFM%2BJSI7CLZ7qF67nEiN5s4frCQX5CCVJHEYxDJgCE3jW%2FGPFPZFmytBonzo44sYwgbLfMUo0uqcI9G7Q%2Bmc3nURNlulaXNza1pY%2FcZvW9A%2BFhkMn" target="_blank">Run Example</a>

```java
mylist = "one,two,three";
mynewlist = listAppend( mylist, "four" );
// Note that listAppend creates a new list. It doesn't update the existing list:
writeDump( mylist );
writeDump( mynewlist );

```


<a href="https://try.boxlang.io/?code=eJzLrczJLC5RsFVQSsvPV7Lmyq3MSy2HCoEox4KC1LwUDYVcsDodBaWkxCIlIFWjpKBpzVVelFmS6lKaWwBSANMIFAcA50scNg%3D%3D" target="_blank">Run Example</a>

```java
mylist = "foo";
mynewlist = listAppend( mylist, "bar", "|" );
writeDump( mynewlist );

```



## Related

  * [GetToken](./GetToken.md)
  * [ListAvg](./ListAvg.md)
  * [ListChangeDelims](./ListChangeDelims.md)
  * [ListCompact](./ListCompact.md)
  * [ListContains](./ListContains.md)
  * [ListContainsNoCase](./ListContainsNoCase.md)
  * [ListDeleteAt](./ListDeleteAt.md)
  * [ListEach](./ListEach.md)
  * [ListEvery](./ListEvery.md)
  * [ListFilter](./ListFilter.md)
  * [ListFind](./ListFind.md)
  * [ListFindNoCase](./ListFindNoCase.md)
  * [ListFirst](./ListFirst.md)
  * [ListGetAt](./ListGetAt.md)
  * [ListIndexExists](./ListIndexExists.md)
  * [ListInsertAt](./ListInsertAt.md)
  * [ListItemTrim](./ListItemTrim.md)
  * [ListLast](./ListLast.md)
  * [ListLen](./ListLen.md)
  * [ListMap](./ListMap.md)
  * [ListNone](./ListNone.md)
  * [ListPrepend](./ListPrepend.md)
  * [ListQualify](./ListQualify.md)
  * [ListReduceRight](./ListReduceRight.md)
  * [ListRemoveDuplicates](./ListRemoveDuplicates.md)
  * [ListRest](./ListRest.md)
  * [ListSetAt](./ListSetAt.md)
  * [ListSome](./ListSome.md)
  * [ListSort](./ListSort.md)
  * [ListToArray](./ListToArray.md)
  * [ListTrim](./ListTrim.md)
  * [ListValueCount](./ListValueCount.md)
  * [ListValueCountNoCase](./ListValueCountNoCase.md)
