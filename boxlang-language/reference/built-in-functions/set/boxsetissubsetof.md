[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetIsSubsetOf`

Test whether every element of set A is also contained in set B, i.e.

A \u2286 B. An empty set is always a
 subset of any set. Returns true if A is a subset of B, false otherwise.

## Method Signature

```
BoxSetIsSubsetOf(set=[set], otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The candidate subset (A). |  |
| `otherSet` | `any` | `true` | The candidate superset (B). Accepts any value castable to a Set. |  |

## Examples

### Check that every element of this Set is contained in another

```java
a = setOf( 1, 2 );
b = setOf( 1, 2, 3 );
writeOutput( a.isSubsetOf( b ) );

```

Result: true

### Returns false when the Set has elements not in the other

```java
a = setOf( 1, 2, 4 );
b = setOf( 1, 2, 3 );
writeOutput( a.isSubsetOf( b ) );

```

Result: false

### A Set is a subset of itself

```java
a = setOf( 1, 2, 3 );
writeOutput( a.isSubsetOf( a ) );

```

Result: true

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
  * [StructKeySet](./StructKeySet.md)
  * [StructValueSet](./StructValueSet.md)
  * [ToSet](./ToSet.md)
