[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetMap`

Apply a transform function to every element of a Set and collect the deduplicated results into a new Set
 of the same variant.

The source Set is not modified. The callback receives the element value, its 1-based
 ordinal position, and the original Set.

## Method Signature

```
BoxSetMap(set=[set], callback=[function:Function])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The source set to transform. |  |
| `callback` | `function:Function` | `true` | Receives {@code (value, ordinal, set)} and returns the transformed value. |  |

## Examples

### Transform each element and return a new Set

The callback receives each value and must return the replacement value.

```java
s = [ 1, 2, 3, 4, 5 ].toSet();
doubled = s.map( ( Any v ) => v * 2 );
writeOutput( doubled.size() );

```

Result: 5

### Map strings to uppercase

```java
s = setOf( "apple", "banana", "cherry" );
upper = s.map( ( Any v ) => uCase( v ) );
writeOutput( upper.contains( "APPLE" ) );

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
  * [BoxSetIsSubsetOf](./BoxSetIsSubsetOf.md)
  * [BoxSetIsSupersetOf](./BoxSetIsSupersetOf.md)
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
