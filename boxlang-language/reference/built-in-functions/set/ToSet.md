[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToSet`

Convert a collection into a Set, deduplicating automatically.

Accepts an Array, a list-delimited String,
 an existing Set, a QueryColumn, an XML node, a bounded Range, or any value castable to a Set. When the
 value is already of the requested variant it is returned as-is; otherwise a new Set of the specified
 variant is created and populated.

## Method Signature

```
ToSet(value=[any], type=[string], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to convert. Accepts Array, Set, list-delimited String, QueryColumn, XML, Range, etc. |  |
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet),<br>                or "sorted" / "tree" (TreeSet). Defaults to "default". | `default` |
| `delimiter` | `string` | `false` | When {@code value} is a String, the list delimiter to split on. Defaults to {@code ","}. | `,` |

## Examples

### Convert an array to a Set

Deduplicates the array elements and returns a BoxSet.

```java
s = [ 1, 2, 2, 3 ].toSet();
writeOutput( s.size() );

```

Result: 3

### Convert to a linked (insertion-ordered) Set

```java
s = [ "c", "a", "b", "a" ].toSet( "linked" );
writeOutput( s.toArray().toString() );

```

Result: [c, a, b]

### Convert to a sorted Set

```java
s = [ 9, 1, 5, 3 ].toSet( "sorted" );
writeOutput( s.toArray().toString() );

```

Result: [1, 3, 5, 9]

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
  * [StructKeySet](./StructKeySet.md)
  * [StructValueSet](./StructValueSet.md)
