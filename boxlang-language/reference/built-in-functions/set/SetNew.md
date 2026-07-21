[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SetNew`

Create a new empty Set, optionally pre-seeded from an existing collection.

The backing variant (hash,
 linked, or sorted) and case-sensitivity can be configured. When no seed is provided, an empty Set of the
 requested variant is returned.

## Method Signature

```
SetNew(type=[string], values=[any], caseSensitive=[boolean], isSynchronized=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet,<br>                preserves insertion order), or "sorted" / "tree" (TreeSet, natural ordering). | `default` |
| `values` | `any` | `false` | An optional seed collection (Array, Set, or anything castable to a Set). Its elements are<br>                  deduplicated into the new set. A single non-collection value seeds a one-element set. |  |
| `caseSensitive` | `boolean` | `false` | Whether string element comparisons are case-sensitive. Defaults to false. | `false` |
| `isSynchronized` | `boolean` | `false` | Whether the set should be thread-safe (synchronized). Default is true. | `true` |

## Examples

### Create an empty default Set

Creates a new empty hash-based Set (no ordering, fastest lookup).

```java
s = setNew();
writeOutput( s.size() );

```

Result: 0

### Create a linked (insertion-ordered) Set seeded with values

Duplicate values are automatically removed.

```java
s = setNew( type="linked", values=[ "c", "a", "b", "a" ] );
writeOutput( s.toArray().toString() );

```

Result: [c, a, b]

### Create a sorted Set

Elements are kept in natural ascending order at all times.

```java
s = setNew( type="sorted", values=[ 9, 1, 5, 3 ] );
writeOutput( s.toArray().toString() );

```

Result: [1, 3, 5, 9]

### Create a case-sensitive Set

By default Sets are case-insensitive. Pass `caseSensitive=true` to treat different cases as distinct elements.

```java
s = setNew( values=[ "Hello", "hello", "HELLO" ], caseSensitive=true );
writeOutput( s.size() );

```

Result: 3

### Default behavior is case-insensitive

```java
s = setNew( values=[ "Hello", "hello", "HELLO" ] );
writeOutput( s.size() );

```

Result: 1

### Create an unsynchronized (non-thread-safe) Set

Pass `isSynchronized=false` for a faster single-threaded set that skips locking overhead.

```java
s = setNew( isSynchronized=false, values=[ 1, 2, 3 ] );
writeOutput( s.size() );

```

Result: 3

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
  * [SetOf](./SetOf.md)
  * [StructKeySet](./StructKeySet.md)
  * [StructValueSet](./StructValueSet.md)
  * [ToSet](./ToSet.md)
