[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxSetReduce`

Left-fold a Set with an accumulator function, reducing it to a single value.

The callback receives the
 current accumulator, the element value, its 1-based ordinal position, and the Set itself, and returns the
 new accumulator. Iteration follows the natural order of the underlying variant.

## Method Signature

```
BoxSetReduce(set=[set], callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `set` | `set` | `true` | The set to reduce. |  |
| `callback` | `function:BiFunction` | `true` | Receives {@code (accumulator, value, ordinal, set)} and returns the new accumulator. |  |
| `initialValue` | `any` | `false` | The starting accumulator value. If omitted, the first element is used as the initial value. |  |

## Examples

### Sum all elements with reduce

The callback receives an accumulator and the current value. The third argument is the initial accumulator value.

```java
s = [ 1, 2, 3, 4, 5 ].toSet();
total = s.reduce( ( Any acc, Any v ) => acc + v, 0 );
writeOutput( total );

```

Result: 15

### Build a comma-separated string

```java
s = setNew( type="linked", values=[ "apple", "banana", "cherry" ] );
result = s.reduce( ( Any acc, Any v ) => listAppend( acc, v ), "" );
writeOutput( result );

```

Result: apple,banana,cherry

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
