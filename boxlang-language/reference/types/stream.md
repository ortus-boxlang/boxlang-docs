
# Type: `Stream`

In BoxLang, the `stream` type is represented by the native Java class `java.util.stream.Stream`. The member functions below are provided by the BoxLang runtime and can be called directly on the value, in addition to the methods of the underlying Java class.

A sequence of elements supporting sequential and parallel aggregate
 operations.

## Stream Methods

<details>
<summary><code>toBXArray()</code></summary>

Collect a Java stream into a BoxLang Array

### Method Signature

```
toBXArray()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toBXList(delimiter=[string])</code></summary>

Collect a Java stream into a BoxLang delimited list.

Each item in the stream will cast
 to a string and then be joined with the delimiter.

### Method Signature

```
toBXList(delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | The delimiter to use. | `,` |
</details>
<details>
<summary><code>toBXQuery(query=[query])</code></summary>

Collect a Java stream into a BoxLang Query.

Provide a template query to match the columns and types of the stream.
 Once the stream collects, it will return a Query object that can be used in BoxLang.

 <h2>Usage</h2>

 <pre>
 // Create a query template
 templateQuery = queryNew( "id,name,age" );
 // Create a stream from an array of structs
 stream = [ {id:1, name:"John", age:30}, {id:2, name:"Jane", age:25} ].toStream();
 // Convert the stream to a query
 result = stream.toBXQuery( templateQuery );
 </pre>

### Method Signature

```
toBXQuery(query=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query template that defines the structure of the resulting Query. |  |
</details>
<details>
<summary><code>toBXStruct(type=[string])</code></summary>

Collect a Java stream into a BoxLang Struct.

Must be a stream of Map.Entry instances.

### Method Signature

```
toBXStruct(type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of struct to create. | `default` |
</details>


## Java Methods

> **Use at your own risk:** These are the public methods of the native Java class `java.util.stream.Stream`, documented from the JDK 21 javadocs. They are not part of the BoxLang API, are not tested or supported by BoxLang, and may change between Java versions.

<details>
<summary><code>boolean allMatch(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns whether all elements of this stream match the provided predicate.
 May not evaluate the predicate on all elements if not necessary for
 determining the result.  If the stream is empty then <code>true</code> is
 returned and the predicate is not evaluated.

 <p>This is a short-circuiting
 terminal operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to elements of this stream

**Returns:** <code>true</code> if either all elements of the stream match the
 provided predicate or the stream is empty, otherwise <code>false</code>

</details>
<details>
<summary><code>boolean anyMatch(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns whether any elements of this stream match the provided
 predicate.  May not evaluate the predicate on all elements if not
 necessary for determining the result.  If the stream is empty then
 <code>false</code> is returned and the predicate is not evaluated.

 <p>This is a short-circuiting
 terminal operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to elements of this stream

**Returns:** <code>true</code> if any elements of the stream match the provided
 predicate, otherwise <code>false</code>

</details>
<details>
<summary><code>static &lt;T&gt; Builder&lt;T&gt; builder()</code></summary>

Returns a builder for a <code>Stream</code>.

**Returns:** a stream builder

</details>
<details>
<summary><code>&lt;R, A&gt; R collect(Collector&lt;? super T, A, R&gt; collector)</code></summary>

Performs a mutable
 reduction operation on the elements of this stream using a
 <code>Collector</code>.  A <code>Collector</code>
 encapsulates the functions used as arguments to
 <code>BiConsumer, BiConsumer)</code>, allowing for reuse of
 collection strategies and composition of collect operations such as
 multiple-level grouping or partitioning.

 <p>If the stream is parallel, and the <code>Collector</code>
 is <code>concurrent</code>, and
 either the stream is unordered or the collector is
 <code>unordered</code>,
 then a concurrent reduction will be performed (see <code>Collector</code> for
 details on concurrent reduction.)

 <p>This is a terminal
 operation.

 <p>When executed in parallel, multiple intermediate results may be
 instantiated, populated, and merged so as to maintain isolation of
 mutable data structures.  Therefore, even when executed in parallel
 with non-thread-safe data structures (such as <code>ArrayList</code>), no
 additional synchronization is needed for a parallel reduction.

**Parameters:**

* `collector` - the <code>Collector</code> describing the reduction

**Returns:** the result of the reduction

</details>
<details>
<summary><code>&lt;R&gt; R collect(Supplier&lt;R&gt; supplier, BiConsumer&lt;R, ? super T&gt; accumulator, BiConsumer&lt;R, R&gt; combiner)</code></summary>

Performs a mutable
 reduction operation on the elements of this stream.  A mutable
 reduction is one in which the reduced value is a mutable result container,
 such as an <code>ArrayList</code>, and elements are incorporated by updating
 the state of the result rather than by replacing the result.  This
 produces a result equivalent to:
 <pre><code>R result = supplier.get();
     for (T element : this stream)
         accumulator.accept(result, element);
     return result;</code></pre>

 <p>Like <code>BinaryOperator)</code>, <code>collect</code> operations
 can be parallelized without requiring additional synchronization.

 <p>This is a terminal
 operation.

**Parameters:**

* `supplier` - a function that creates a new mutable result container.
                 For a parallel execution, this function may be called
                 multiple times and must return a fresh value each time.
* `accumulator` - an associative,
                    non-interfering,
                    stateless
                    function that must fold an element into a result
                    container.
* `combiner` - an associative,
                    non-interfering,
                    stateless
                    function that accepts two partial result containers
                    and merges them, which must be compatible with the
                    accumulator function.  The combiner function must fold
                    the elements from the second result container into the
                    first result container.

**Returns:** the result of the reduction

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; concat(Stream&lt;? extends T&gt; a, Stream&lt;? extends T&gt; b)</code></summary>

Creates a lazily concatenated stream whose elements are all the
 elements of the first stream followed by all the elements of the
 second stream.  The resulting stream is ordered if both
 of the input streams are ordered, and parallel if either of the input
 streams is parallel.  When the resulting stream is closed, the close
 handlers for both input streams are invoked.

 <p>This method operates on the two input streams and binds each stream
 to its source.  As a result subsequent modifications to an input stream
 source may not be reflected in the concatenated stream result.

**Parameters:**

* `a` - the first stream
* `b` - the second stream

**Returns:** the concatenation of the two input streams

</details>
<details>
<summary><code>long count()</code></summary>

Returns the count of elements in this stream.  This is a special case of
 a reduction and is
 equivalent to:
 <pre><code>return mapToLong(e -&gt; 1L).sum();</code></pre>

 <p>This is a terminal operation.

**Returns:** the count of elements in this stream

</details>
<details>
<summary><code>Stream&lt;T&gt; distinct()</code></summary>

Returns a stream consisting of the distinct elements (according to
 <code>Object#equals(Object)</code>) of this stream.

 <p>For ordered streams, the selection of distinct elements is stable
 (for duplicated elements, the element appearing first in the encounter
 order is preserved.)  For unordered streams, no stability guarantees
 are made.

 <p>This is a stateful
 intermediate operation.

**Returns:** the new stream

</details>
<details>
<summary><code>Stream&lt;T&gt; dropWhile(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns, if this stream is ordered, a stream consisting of the remaining
 elements of this stream after dropping the longest prefix of elements
 that match the given predicate.  Otherwise returns, if this stream is
 unordered, a stream consisting of the remaining elements of this stream
 after dropping a subset of elements that match the given predicate.

 <p>If this stream is ordered then the longest prefix is a contiguous
 sequence of elements of this stream that match the given predicate.  The
 first element of the sequence is the first element of this stream, and
 the element immediately following the last element of the sequence does
 not match the given predicate.

 <p>If this stream is unordered, and some (but not all) elements of this
 stream match the given predicate, then the behavior of this operation is
 nondeterministic; it is free to drop any subset of matching elements
 (which includes the empty set).

 <p>Independent of whether this stream is ordered or unordered if all
 elements of this stream match the given predicate then this operation
 drops all elements (the result is an empty stream), or if no elements of
 the stream match the given predicate then no elements are dropped (the
 result is the same as the input).

 <p>This is a stateful
 intermediate operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to elements to determine the longest
                  prefix of elements.

**Returns:** the new stream

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; empty()</code></summary>

Returns an empty sequential <code>Stream</code>.

**Returns:** an empty sequential stream

</details>
<details>
<summary><code>Stream&lt;T&gt; filter(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns a stream consisting of the elements of this stream that match
 the given predicate.

 <p>This is an intermediate
 operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to each element to determine if it
                  should be included

**Returns:** the new stream

</details>
<details>
<summary><code>Optional&lt;T&gt; findAny()</code></summary>

Returns an <code>Optional</code> describing some element of the stream, or an
 empty <code>Optional</code> if the stream is empty.

 <p>This is a short-circuiting
 terminal operation.

 <p>The behavior of this operation is explicitly nondeterministic; it is
 free to select any element in the stream.  This is to allow for maximal
 performance in parallel operations; the cost is that multiple invocations
 on the same source may not return the same result.  (If a stable result
 is desired, use <code>#findFirst()</code> instead.)

**Returns:** an <code>Optional</code> describing some element of this stream, or an
 empty <code>Optional</code> if the stream is empty

</details>
<details>
<summary><code>Optional&lt;T&gt; findFirst()</code></summary>

Returns an <code>Optional</code> describing the first element of this stream,
 or an empty <code>Optional</code> if the stream is empty.  If the stream has
 no encounter order, then any element may be returned.

 <p>This is a short-circuiting
 terminal operation.

**Returns:** an <code>Optional</code> describing the first element of this stream,
 or an empty <code>Optional</code> if the stream is empty

</details>
<details>
<summary><code>&lt;R&gt; Stream&lt;R&gt; flatMap(Function&lt;? super T, ? extends Stream&lt;? extends R&gt;&gt; mapper)</code></summary>

Returns a stream consisting of the results of replacing each element of
 this stream with the contents of a mapped stream produced by applying
 the provided mapping function to each element.  Each mapped stream is
 <code>closed</code> after its contents
 have been placed into this stream.  (If a mapped stream is <code>null</code>
 an empty stream is used, instead.)

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element which produces a stream
               of new values

**Returns:** the new stream

</details>
<details>
<summary><code>DoubleStream flatMapToDouble(Function&lt;? super T, ? extends DoubleStream&gt; mapper)</code></summary>

Returns an <code>DoubleStream</code> consisting of the results of replacing
 each element of this stream with the contents of a mapped stream produced
 by applying the provided mapping function to each element.  Each mapped
 stream is <code>closed</code> after its
 contents have placed been into this stream.  (If a mapped stream is
 <code>null</code> an empty stream is used, instead.)

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element which produces a stream
               of new values

**Returns:** the new stream

</details>
<details>
<summary><code>IntStream flatMapToInt(Function&lt;? super T, ? extends IntStream&gt; mapper)</code></summary>

Returns an <code>IntStream</code> consisting of the results of replacing each
 element of this stream with the contents of a mapped stream produced by
 applying the provided mapping function to each element.  Each mapped
 stream is <code>closed</code> after its
 contents have been placed into this stream.  (If a mapped stream is
 <code>null</code> an empty stream is used, instead.)

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element which produces a stream
               of new values

**Returns:** the new stream

</details>
<details>
<summary><code>LongStream flatMapToLong(Function&lt;? super T, ? extends LongStream&gt; mapper)</code></summary>

Returns an <code>LongStream</code> consisting of the results of replacing each
 element of this stream with the contents of a mapped stream produced by
 applying the provided mapping function to each element.  Each mapped
 stream is <code>closed</code> after its
 contents have been placed into this stream.  (If a mapped stream is
 <code>null</code> an empty stream is used, instead.)

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element which produces a stream
               of new values

**Returns:** the new stream

</details>
<details>
<summary><code>void forEach(Consumer&lt;? super T&gt; action)</code></summary>

Performs an action for each element of this stream.

 <p>This is a terminal
 operation.

 <p>The behavior of this operation is explicitly nondeterministic.
 For parallel stream pipelines, this operation does <em>not</em>
 guarantee to respect the encounter order of the stream, as doing so
 would sacrifice the benefit of parallelism.  For any given element, the
 action may be performed at whatever time and in whatever thread the
 library chooses.  If the action accesses shared state, it is
 responsible for providing the required synchronization.

**Parameters:**

* `action` - a 
               non-interfering action to perform on the elements

</details>
<details>
<summary><code>void forEachOrdered(Consumer&lt;? super T&gt; action)</code></summary>

Performs an action for each element of this stream, in the encounter
 order of the stream if the stream has a defined encounter order.

 <p>This is a terminal
 operation.

 <p>This operation processes the elements one at a time, in encounter
 order if one exists.  Performing the action for one element
 <i>happens-before</i>
 performing the action for subsequent elements, but for any given element,
 the action may be performed in whatever thread the library chooses.

**Parameters:**

* `action` - a 
               non-interfering action to perform on the elements

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; generate(Supplier&lt;? extends T&gt; s)</code></summary>

Returns an infinite sequential unordered stream where each element is
 generated by the provided <code>Supplier</code>.  This is suitable for
 generating constant streams, streams of random elements, etc.

**Parameters:**

* `s` - the <code>Supplier</code> of generated elements

**Returns:** a new infinite sequential unordered <code>Stream</code>

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; iterate(T seed, Predicate&lt;? super T&gt; hasNext, UnaryOperator&lt;T&gt; next)</code></summary>

Returns a sequential ordered <code>Stream</code> produced by iterative
 application of the given <code>next</code> function to an initial element,
 conditioned on satisfying the given <code>hasNext</code> predicate.  The
 stream terminates as soon as the <code>hasNext</code> predicate returns false.

 <p><code>Stream.iterate</code> should produce the same sequence of elements as
 produced by the corresponding for-loop:
 <pre><code>for (T index=seed; hasNext.test(index); index = next.apply(index)) {
         ...</code>
 }</pre>

 <p>The resulting sequence may be empty if the <code>hasNext</code> predicate
 does not hold on the seed value.  Otherwise the first element will be the
 supplied <code>seed</code> value, the next element (if present) will be the
 result of applying the <code>next</code> function to the <code>seed</code> value,
 and so on iteratively until the <code>hasNext</code> predicate indicates that
 the stream should terminate.

 <p>The action of applying the <code>hasNext</code> predicate to an element
 <i>happens-before</i>
 the action of applying the <code>next</code> function to that element.  The
 action of applying the <code>next</code> function for one element
 <i>happens-before</i> the action of applying the <code>hasNext</code>
 predicate for subsequent elements.  For any given element an action may
 be performed in whatever thread the library chooses.

**Parameters:**

* `seed` - the initial element
* `hasNext` - a predicate to apply to elements to determine when the
                stream must terminate.
* `next` - a function to be applied to the previous element to produce
             a new element

**Returns:** a new sequential <code>Stream</code>

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; iterate(T seed, UnaryOperator&lt;T&gt; f)</code></summary>

Returns an infinite sequential ordered <code>Stream</code> produced by iterative
 application of a function <code>f</code> to an initial element <code>seed</code>,
 producing a <code>Stream</code> consisting of <code>seed</code>, <code>f(seed)</code>,
 <code>f(f(seed))</code>, etc.

 <p>The first element (position <code>0</code>) in the <code>Stream</code> will be
 the provided <code>seed</code>.  For <code>n &gt; 0</code>, the element at position
 <code>n</code>, will be the result of applying the function <code>f</code> to the
 element at position <code>n - 1</code>.

 <p>The action of applying <code>f</code> for one element
 <i>happens-before</i>
 the action of applying <code>f</code> for subsequent elements.  For any given
 element the action may be performed in whatever thread the library
 chooses.

**Parameters:**

* `seed` - the initial element
* `f` - a function to be applied to the previous element to produce
          a new element

**Returns:** a new sequential <code>Stream</code>

</details>
<details>
<summary><code>Stream&lt;T&gt; limit(long maxSize)</code></summary>

Returns a stream consisting of the elements of this stream, truncated
 to be no longer than <code>maxSize</code> in length.

 <p>This is a short-circuiting
 stateful intermediate operation.

**Parameters:**

* `maxSize` - the number of elements the stream should be limited to

**Returns:** the new stream

</details>
<details>
<summary><code>&lt;R&gt; Stream&lt;R&gt; map(Function&lt;? super T, ? extends R&gt; mapper)</code></summary>

Returns a stream consisting of the results of applying the given
 function to the elements of this stream.

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element

**Returns:** the new stream

</details>
<details>
<summary><code>&lt;R&gt; Stream&lt;R&gt; mapMulti(BiConsumer&lt;? super T, ? super Consumer&lt;R&gt;&gt; mapper)</code></summary>

Returns a stream consisting of the results of replacing each element of
 this stream with multiple elements, specifically zero or more elements.
 Replacement is performed by applying the provided mapping function to each
 element in conjunction with a <code>consumer</code> argument
 that accepts replacement elements. The mapping function calls the consumer
 zero or more times to provide the replacement elements.

 <p>This is an intermediate
 operation.

 <p>If the <code>consumer</code> argument is used outside the scope of
 its application to the mapping function, the results are undefined.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function that generates replacement elements

**Returns:** the new stream

</details>
<details>
<summary><code>DoubleStream mapMultiToDouble(BiConsumer&lt;? super T, ? super DoubleConsumer&gt; mapper)</code></summary>

Returns a <code>DoubleStream</code> consisting of the results of replacing each
 element of this stream with multiple elements, specifically zero or more
 elements.
 Replacement is performed by applying the provided mapping function to each
 element in conjunction with a <code>consumer</code> argument
 that accepts replacement elements. The mapping function calls the consumer
 zero or more times to provide the replacement elements.

 <p>This is an intermediate
 operation.

 <p>If the <code>consumer</code> argument is used outside the scope of
 its application to the mapping function, the results are undefined.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function that generates replacement elements

**Returns:** the new stream

</details>
<details>
<summary><code>IntStream mapMultiToInt(BiConsumer&lt;? super T, ? super IntConsumer&gt; mapper)</code></summary>

Returns an <code>IntStream</code> consisting of the results of replacing each
 element of this stream with multiple elements, specifically zero or more
 elements.
 Replacement is performed by applying the provided mapping function to each
 element in conjunction with a <code>consumer</code> argument
 that accepts replacement elements. The mapping function calls the consumer
 zero or more times to provide the replacement elements.

 <p>This is an intermediate
 operation.

 <p>If the <code>consumer</code> argument is used outside the scope of
 its application to the mapping function, the results are undefined.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function that generates replacement elements

**Returns:** the new stream

</details>
<details>
<summary><code>LongStream mapMultiToLong(BiConsumer&lt;? super T, ? super LongConsumer&gt; mapper)</code></summary>

Returns a <code>LongStream</code> consisting of the results of replacing each
 element of this stream with multiple elements, specifically zero or more
 elements.
 Replacement is performed by applying the provided mapping function to each
 element in conjunction with a <code>consumer</code> argument
 that accepts replacement elements. The mapping function calls the consumer
 zero or more times to provide the replacement elements.

 <p>This is an intermediate
 operation.

 <p>If the <code>consumer</code> argument is used outside the scope of
 its application to the mapping function, the results are undefined.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function that generates replacement elements

**Returns:** the new stream

</details>
<details>
<summary><code>DoubleStream mapToDouble(ToDoubleFunction&lt;? super T&gt; mapper)</code></summary>

Returns a <code>DoubleStream</code> consisting of the results of applying the
 given function to the elements of this stream.

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element

**Returns:** the new stream

</details>
<details>
<summary><code>IntStream mapToInt(ToIntFunction&lt;? super T&gt; mapper)</code></summary>

Returns an <code>IntStream</code> consisting of the results of applying the
 given function to the elements of this stream.

 <p>This is an 
     intermediate operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element

**Returns:** the new stream

</details>
<details>
<summary><code>LongStream mapToLong(ToLongFunction&lt;? super T&gt; mapper)</code></summary>

Returns a <code>LongStream</code> consisting of the results of applying the
 given function to the elements of this stream.

 <p>This is an intermediate
 operation.

**Parameters:**

* `mapper` - a non-interfering,
               stateless
               function to apply to each element

**Returns:** the new stream

</details>
<details>
<summary><code>Optional&lt;T&gt; max(Comparator&lt;? super T&gt; comparator)</code></summary>

Returns the maximum element of this stream according to the provided
 <code>Comparator</code>.  This is a special case of a
 reduction.

 <p>This is a terminal
 operation.

**Parameters:**

* `comparator` - a non-interfering,
                   stateless
                   <code>Comparator</code> to compare elements of this stream

**Returns:** an <code>Optional</code> describing the maximum element of this stream,
 or an empty <code>Optional</code> if the stream is empty

</details>
<details>
<summary><code>Optional&lt;T&gt; min(Comparator&lt;? super T&gt; comparator)</code></summary>

Returns the minimum element of this stream according to the provided
 <code>Comparator</code>.  This is a special case of a
 reduction.

 <p>This is a terminal operation.

**Parameters:**

* `comparator` - a non-interfering,
                   stateless
                   <code>Comparator</code> to compare elements of this stream

**Returns:** an <code>Optional</code> describing the minimum element of this stream,
 or an empty <code>Optional</code> if the stream is empty

</details>
<details>
<summary><code>boolean noneMatch(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns whether no elements of this stream match the provided predicate.
 May not evaluate the predicate on all elements if not necessary for
 determining the result.  If the stream is empty then <code>true</code> is
 returned and the predicate is not evaluated.

 <p>This is a short-circuiting
 terminal operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to elements of this stream

**Returns:** <code>true</code> if either no elements of the stream match the
 provided predicate or the stream is empty, otherwise <code>false</code>

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; of(T t)</code></summary>

Returns a sequential <code>Stream</code> containing a single element.

**Parameters:**

* `t` - the single element

**Returns:** a singleton sequential stream

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; of(T[] values)</code></summary>

Returns a sequential ordered stream whose elements are the specified values.

**Parameters:**

* `values` - the elements of the new stream

**Returns:** the new stream

</details>
<details>
<summary><code>static &lt;T&gt; Stream&lt;T&gt; ofNullable(T t)</code></summary>

Returns a sequential <code>Stream</code> containing a single element, if
 non-null, otherwise returns an empty <code>Stream</code>.

**Parameters:**

* `t` - the single element

**Returns:** a stream with a single element if the specified element
         is non-null, otherwise an empty stream

</details>
<details>
<summary><code>Stream&lt;T&gt; peek(Consumer&lt;? super T&gt; action)</code></summary>

Returns a stream consisting of the elements of this stream, additionally
 performing the provided action on each element as elements are consumed
 from the resulting stream.

 <p>This is an intermediate
 operation.

 <p>For parallel stream pipelines, the action may be called at
 whatever time and in whatever thread the element is made available by the
 upstream operation.  If the action modifies shared state,
 it is responsible for providing the required synchronization.

**Parameters:**

* `action` - a 
                 non-interfering action to perform on the elements as
                 they are consumed from the stream

**Returns:** the new stream

</details>
<details>
<summary><code>&lt;U&gt; U reduce(U identity, BiFunction&lt;U, ? super T, U&gt; accumulator, BinaryOperator&lt;U&gt; combiner)</code></summary>

Performs a reduction on the
 elements of this stream, using the provided identity, accumulation and
 combining functions.  This is equivalent to:
 <pre><code>U result = identity;
     for (T element : this stream)
         result = accumulator.apply(result, element)
     return result;</code></pre>

 but is not constrained to execute sequentially.

 <p>The <code>identity</code> value must be an identity for the combiner
 function.  This means that for all <code>u</code>, <code>combiner(identity, u)</code>
 is equal to <code>u</code>.  Additionally, the <code>combiner</code> function
 must be compatible with the <code>accumulator</code> function; for all
 <code>u</code> and <code>t</code>, the following must hold:
 <pre><code>combiner.apply(u, accumulator.apply(identity, t)) == accumulator.apply(u, t)</code></pre>

 <p>This is a terminal
 operation.

**Parameters:**

* `identity` - the identity value for the combiner function
* `accumulator` - an associative,
                    non-interfering,
                    stateless
                    function for incorporating an additional element into a result
* `combiner` - an associative,
                    non-interfering,
                    stateless
                    function for combining two values, which must be
                    compatible with the accumulator function

**Returns:** the result of the reduction

</details>
<details>
<summary><code>Optional&lt;T&gt; reduce(BinaryOperator&lt;T&gt; accumulator)</code></summary>

Performs a reduction on the
 elements of this stream, using an
 associative accumulation
 function, and returns an <code>Optional</code> describing the reduced value,
 if any. This is equivalent to:
 <pre><code>boolean foundAny = false;
     T result = null;
     for (T element : this stream) {
         if (!foundAny) {
             foundAny = true;
             result = element;</code>
         else
             result = accumulator.apply(result, element);
     }
     return foundAny ? Optional.of(result) : Optional.empty();
 }</pre>

 but is not constrained to execute sequentially.

 <p>The <code>accumulator</code> function must be an
 associative function.

 <p>This is a terminal
 operation.

**Parameters:**

* `accumulator` - an associative,
                    non-interfering,
                    stateless
                    function for combining two values

**Returns:** an <code>Optional</code> describing the result of the reduction

</details>
<details>
<summary><code>T reduce(T identity, BinaryOperator&lt;T&gt; accumulator)</code></summary>

Performs a reduction on the
 elements of this stream, using the provided identity value and an
 associative
 accumulation function, and returns the reduced value.  This is equivalent
 to:
 <pre><code>T result = identity;
     for (T element : this stream)
         result = accumulator.apply(result, element)
     return result;</code></pre>

 but is not constrained to execute sequentially.

 <p>The <code>identity</code> value must be an identity for the accumulator
 function. This means that for all <code>t</code>,
 <code>accumulator.apply(identity, t)</code> is equal to <code>t</code>.
 The <code>accumulator</code> function must be an
 associative function.

 <p>This is a terminal
 operation.

**Parameters:**

* `identity` - the identity value for the accumulating function
* `accumulator` - an associative,
                    non-interfering,
                    stateless
                    function for combining two values

**Returns:** the result of the reduction

</details>
<details>
<summary><code>Stream&lt;T&gt; skip(long n)</code></summary>

Returns a stream consisting of the remaining elements of this stream
 after discarding the first <code>n</code> elements of the stream.
 If this stream contains fewer than <code>n</code> elements then an
 empty stream will be returned.

 <p>This is a stateful
 intermediate operation.

**Parameters:**

* `n` - the number of leading elements to skip

**Returns:** the new stream

</details>
<details>
<summary><code>Stream&lt;T&gt; sorted()</code></summary>

Returns a stream consisting of the elements of this stream, sorted
 according to natural order.  If the elements of this stream are not
 <code>Comparable</code>, a <code>java.lang.ClassCastException</code> may be thrown
 when the terminal operation is executed.

 <p>For ordered streams, the sort is stable.  For unordered streams, no
 stability guarantees are made.

 <p>This is a stateful
 intermediate operation.

**Returns:** the new stream

</details>
<details>
<summary><code>Stream&lt;T&gt; sorted(Comparator&lt;? super T&gt; comparator)</code></summary>

Returns a stream consisting of the elements of this stream, sorted
 according to the provided <code>Comparator</code>.

 <p>For ordered streams, the sort is stable.  For unordered streams, no
 stability guarantees are made.

 <p>This is a stateful
 intermediate operation.

**Parameters:**

* `comparator` - a non-interfering,
                   stateless
                   <code>Comparator</code> to be used to compare stream elements

**Returns:** the new stream

</details>
<details>
<summary><code>Stream&lt;T&gt; takeWhile(Predicate&lt;? super T&gt; predicate)</code></summary>

Returns, if this stream is ordered, a stream consisting of the longest
 prefix of elements taken from this stream that match the given predicate.
 Otherwise returns, if this stream is unordered, a stream consisting of a
 subset of elements taken from this stream that match the given predicate.

 <p>If this stream is ordered then the longest prefix is a contiguous
 sequence of elements of this stream that match the given predicate.  The
 first element of the sequence is the first element of this stream, and
 the element immediately following the last element of the sequence does
 not match the given predicate.

 <p>If this stream is unordered, and some (but not all) elements of this
 stream match the given predicate, then the behavior of this operation is
 nondeterministic; it is free to take any subset of matching elements
 (which includes the empty set).

 <p>Independent of whether this stream is ordered or unordered if all
 elements of this stream match the given predicate then this operation
 takes all elements (the result is the same as the input), or if no
 elements of the stream match the given predicate then no elements are
 taken (the result is an empty stream).

 <p>This is a short-circuiting
 stateful intermediate operation.

**Parameters:**

* `predicate` - a non-interfering,
                  stateless
                  predicate to apply to elements to determine the longest
                  prefix of elements.

**Returns:** the new stream

</details>
<details>
<summary><code>&lt;A&gt; A[] toArray(IntFunction&lt;A[]&gt; generator)</code></summary>

Returns an array containing the elements of this stream, using the
 provided <code>generator</code> function to allocate the returned array, as
 well as any additional arrays that might be required for a partitioned
 execution or for resizing.

 <p>This is a terminal
 operation.

**Parameters:**

* `generator` - a function which produces a new array of the desired
                  type and the provided length

**Returns:** an array containing the elements in this stream

</details>
<details>
<summary><code>Object[] toArray()</code></summary>

Returns an array containing the elements of this stream.

 <p>This is a terminal
 operation.

**Returns:** an array, whose <code>runtime component
 type</code> is <code>Object</code>, containing the elements of this stream

</details>
<details>
<summary><code>List&lt;T&gt; toList()</code></summary>

Accumulates the elements of this stream into a <code>List</code>. The elements in
 the list will be in this stream's encounter order, if one exists. The returned List
 is unmodifiable; calls to any mutator method will always cause
 <code>UnsupportedOperationException</code> to be thrown. There are no
 guarantees on the implementation type or serializability of the returned List.

 <p>The returned instance may be value-based.
 Callers should make no assumptions about the identity of the returned instances.
 Identity-sensitive operations on these instances (reference equality (<code>==</code>),
 identity hash code, and synchronization) are unreliable and should be avoided.

 <p>This is a terminal operation.

**Returns:** a List containing the stream elements

</details>


## Examples


