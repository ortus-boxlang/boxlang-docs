[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetFind`

Return the first element of a Set for which the predicate returns true, or null if no element matches.

Iteration follows the natural order of the underlying variant and stops at the first match. The predicate
 receives the element value, its 1-based ordinal position, and the Set itself.

## Method Signature

```
BoxSetFind(set=[set], callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The set to search. |  |
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives {@code (value, ordinal, set)}.<br>                    Iteration stops at the first element for which this returns {@code true}. |  |

## Examples

### Find the first element that satisfies a predicate

Returns the matching element, or `null` when nothing matches.

```java
s = [ 1, 2, 3, 4, 5 ].toSet();
found = s.find( ( Any v ) => v > 3 );
writeOutput( found >= 4 ? "yes" : "no" );

```

Result: yes

### Returns null when no element matches

```java
s = setOf( 1, 2, 3 );
found = s.find( ( Any v ) => v > 100 );
writeOutput( isNull( found ) ? "null" : found );

```

Result: null

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
  * [StructKeySet](./StructKeySet.md)
  * [StructValueSet](./StructValueSet.md)
  * [ToSet](./ToSet.md)
