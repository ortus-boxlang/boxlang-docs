[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetSome`

Test whether at least one element of a Set satisfies a predicate.

Iteration short-circuits on the first
 element for which the predicate returns true. Returns false for an empty Set. The predicate receives the
 element value, its 1-based ordinal position, and the Set itself.

## Method Signature

```
BoxSetSome(set=[set], callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The set to test. |  |
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives {@code (value, ordinal, set)}.<br>                    Short-circuits on the first {@code true} result. |  |

## Examples

### Test that at least one element satisfies a predicate

Returns `true` on the first match.

```java
s = [ 1, 2, 3, 4 ].toSet();
writeOutput( s.some( ( Any v ) => v > 3 ) );

```

Result: true

### Returns false when nothing matches

```java
s = setOf( 1, 2, 3 );
writeOutput( s.some( ( Any v ) => v > 100 ) );

```

Result: false

### Using the any alias

`any` is an alias for `some`.

```java
s = setOf( "apple", "banana", "cherry" );
writeOutput( s.any( ( Any v ) => len( v ) > 5 ) );

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
  * [BoxSetMap](./BoxSetMap.md)
  * [BoxSetNone](./BoxSetNone.md)
  * [BoxSetReduce](./BoxSetReduce.md)
  * [BoxSetReject](./BoxSetReject.md)
  * [BoxSetRemove](./BoxSetRemove.md)
  * [BoxSetRemoveAll](./BoxSetRemoveAll.md)
  * [BoxSetRetainAll](./BoxSetRetainAll.md)
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
