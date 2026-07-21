[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `StructKeySet`

Build a Set containing the keys of a Struct.

Key names are extracted as plain Strings via Key.getName(),
 so the resulting Set always holds String values. The backing variant can be configured; use "linked" to
 preserve the Struct's iteration order.

## Method Signature

```
StructKeySet(struct=[struct], type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct` | `struct` | `true` | The struct whose keys should populate the set. |  |
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet,<br>                preserves Struct iteration order), or "sorted" / "tree" (TreeSet, alphabetical order). | `default` |

## Examples

### Get the keys of a struct as a Set

Returns a BoxSet containing all keys of the struct.

```java
s = { name: "Luis", age: 42, email: "x@y.z" }.keySet();
writeOutput( s.size() );

```

Result: 3

### Using the standalone function form

```java
s = structKeySet( { a: 1, b: 2, c: 3 } );
writeOutput( s.size() );

```

Result: 3

### Case sensitivity mirrors the source struct

A case-sensitive struct produces a case-sensitive key Set.

```java
cs = structNew( "casesensitive" );
cs[ "Name" ] = "Luis";
cs[ "name" ] = "Brad";
keys = cs.keySet();
writeOutput( keys.isCaseSensitive() & "," & keys.size() );

```

Result: true,2

## Related

  * [BoxSetAdd](./BoxSetAdd.md)
  * [BoxSetAddAll](./BoxSetAddAll.md)
  * [BoxSetClear](./BoxSetClear.md)
  * [BoxSetContains](./BoxSetContains.md)
  * [BoxSetContainsAll](./BoxSetContainsAll.md)
  * [BoxSetDifference](./BoxSetDifference.md)
  * [BoxSetEach](./BoxSetEach.md)
  * [BoxSetEquals](./BoxSetEquals.md)
  * [BoxSetEvery](./BoxSetEvery.md)
  * [BoxSetFilter](./BoxSetFilter.md)
  * [BoxSetFind](./BoxSetFind.md)
  * [BoxSetIntersection](./BoxSetIntersection.md)
  * [BoxSetIsDisjointFrom](./BoxSetIsDisjointFrom.md)
  * [BoxSetIsEmpty](./BoxSetIsEmpty.md)
  * [BoxSetIsSubsetOf](./BoxSetIsSubsetOf.md)
  * [BoxSetIsSupersetOf](./BoxSetIsSupersetOf.md)
  * [BoxSetMap](./BoxSetMap.md)
  * [BoxSetNone](./BoxSetNone.md)
  * [BoxSetReduce](./BoxSetReduce.md)
  * [BoxSetReject](./BoxSetReject.md)
  * [BoxSetRemove](./BoxSetRemove.md)
  * [BoxSetRemoveAll](./BoxSetRemoveAll.md)
  * [BoxSetRetainAll](./BoxSetRetainAll.md)
  * [BoxSetSome](./BoxSetSome.md)
  * [BoxSetSymmetricDifference](./BoxSetSymmetricDifference.md)
  * [BoxSetToArray](./BoxSetToArray.md)
  * [BoxSetToList](./BoxSetToList.md)
  * [BoxSetUnion](./BoxSetUnion.md)
  * [ObjectToSet](./ObjectToSet.md)
  * [SetNew](./SetNew.md)
  * [SetOf](./SetOf.md)
  * [StructValueSet](./StructValueSet.md)
  * [ToSet](./ToSet.md)
