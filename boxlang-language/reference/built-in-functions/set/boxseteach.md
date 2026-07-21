[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetEach`

Invoke a callback for every element of a Set.

The callback receives the element value, its 1-based ordinal
 position, and the Set itself; single-argument callbacks receive only the value. Iteration follows the natural
 order of the underlying variant. Use setMap() if you need a transformed result.

## Method Signature

```
BoxSetEach(set=[set], callback=[function:Consumer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The set to iterate. |  |
| `callback` | `function:Consumer` | `true` | Invoked for each element. Receives {@code (value, ordinal, set)}; single-argument callbacks<br>                    receive only the value. |  |

## Examples

### Iterate over every element in a Set

The callback receives each value in turn.

```java
s = setNew( type="linked", values=[ "a", "b", "c" ] );
s.each( ( Any value ) => {
	writeOutput( value & " " );
} );

```

Result: a b c

### Accumulate with each

```java
s = [ 1, 2, 3, 4, 5 ].toSet();
counter = [ 0 ];
s.each( ( Any v ) => {
	counter[ 1 ] += v;
} );
writeOutput( counter[ 1 ] );

```

Result: 15

## Related

  * [BoxSetAdd](./BoxSetAdd.md)
  * [BoxSetAddAll](./BoxSetAddAll.md)
  * [BoxSetClear](./BoxSetClear.md)
  * [BoxSetContains](./BoxSetContains.md)
  * [BoxSetContainsAll](./BoxSetContainsAll.md)
  * [BoxSetDifference](./BoxSetDifference.md)
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
  * [StructKeySet](./StructKeySet.md)
  * [StructValueSet](./StructValueSet.md)
  * [ToSet](./ToSet.md)
