# Serialization & Marshalling Events

These events fire during binary object serialization/deserialization via the `ObjectMarshaller` (used internally for session persistence and object storage), and during JSON serialization of BoxLang queries. They are announced on the **global interceptor pool**.

> **Scope:** The four `ObjectMarshall*` events relate to **Java binary serialization** (`ObjectOutputStream` / `ObjectInputStream`), not JSON. This is used internally by BoxLang for session persistence, object caching, and any operation that needs to store or transfer object state as bytes. The object being serialized must implement `java.io.Serializable`.

| Event Name                          | Cancellable | Description                                                                              |
| ----------------------------------- | :---------: | ---------------------------------------------------------------------------------------- |
| `beforeObjectMarshallSerialize`     |     No      | Fired before an object is serialized to binary (Java serialization).                     |
| `afterObjectMarshallSerialize`      |     No      | Fired after an object has been serialized. Provides the raw binary output.               |
| `beforeObjectMarshallDeserialize`   |     No      | Fired before binary data is deserialized back into an object.                            |
| `afterObjectMarshallDeserialize`    |     No      | Fired after binary data has been deserialized. Provides the reconstructed object.        |
| `onJSONQuerySerialize`              |     No      | Fired once per query during JSON serialization, after the output structure is built.     |

* [`beforeObjectMarshallSerialize`](object-marshalling-events.md#beforeobjectmarshallserialize)
* [`afterObjectMarshallSerialize`](object-marshalling-events.md#afterobjectmarshallserialize)
* [`beforeObjectMarshallDeserialize`](object-marshalling-events.md#beforeobjectmarshalldeserialize)
* [`afterObjectMarshallDeserialize`](object-marshalling-events.md#afterobjectmarshalldeserialize)
* [`onJSONQuerySerialize`](object-marshalling-events.md#onjsonqueryserialize)

## beforeObjectMarshallSerialize

Fired before an object is serialized to binary format. Use this to audit, validate, or log objects before they are stored or transmitted as binary data.

### Data Structure

| Data Key | Type     | Description                        |
| -------- | -------- | ---------------------------------- |
| `object` | `Object` | The object about to be serialized. |

### Example

```groovy
class myListener{
	function beforeObjectMarshallSerialize( struct data ){
		// Audit or validate the object before binary serialization
		var object = data.object;
	}
}
```

## afterObjectMarshallSerialize

Fired after an object has been successfully serialized to a byte array. Provides the raw binary output for inspection, logging, or metrics.

### Data Structure

| Data Key | Type     | Description                                         |
| -------- | -------- | --------------------------------------------------- |
| `binary` | `byte[]` | The serialized binary representation of the object. |

### Example

```groovy
class myListener{
	function afterObjectMarshallSerialize( struct data ){
		// Log size, checksum, audit binary output, etc.
		var binary = data.binary;
	}
}
```

## beforeObjectMarshallDeserialize

Fired before binary data is deserialized back into an object. Use this to inspect, validate, or log the raw bytes before deserialization.

### Data Structure

| Data Key | Type     | Description                                   |
| -------- | -------- | --------------------------------------------- |
| `binary` | `byte[]` | The raw binary data about to be deserialized. |

### Example

```groovy
class myListener{
	function beforeObjectMarshallDeserialize( struct data ){
		// Inspect or audit the binary payload before deserialization
		var binary = data.binary;
	}
}
```

## afterObjectMarshallDeserialize

Fired after binary data has been deserialized back into an object. If the deserialized object is a `BoxClassState` (a serialized BoxLang class), the runtime will have already reconstructed a live `IClassRunnable` from it before this event fires.

### Data Structure

| Data Key | Type     | Description                                                                                |
| -------- | -------- | ------------------------------------------------------------------------------------------ |
| `object` | `Object` | The reconstructed object. May be an `IClassRunnable` if the original was a BoxLang class.  |

### Example

```groovy
class myListener{
	function afterObjectMarshallDeserialize( struct data ){
		// Inspect or post-process the reconstructed object
		var object = data.object;
	}
}
```

## onJSONQuerySerialize

Fired once per query during JSON serialization, after the query data has been converted into its intermediate representation but before it is written to the JSON output stream. This fires for each of the three supported query formats: `row`, `column`, and `struct`.

The format of the `data` key varies by `queryFormat`:

| `queryFormat`     | `data` structure                                                                  |
| ----------------- | --------------------------------------------------------------------------------- |
| `row` / `false`   | `Struct` with `columns` (`String[]`) and `data` (`Object[][]`)                   |
| `column` / `true` | `Struct` with `rowCount` (`int`), `columns` (`String[]`), and `data` (`Struct`)  |
| `struct`          | `Array` of `Struct` — one struct per row                                          |

### Data Structure

| Data Key | Type     | Description                                                              |
| -------- | -------- | ------------------------------------------------------------------------ |
| `data`   | `Object` | The intermediate structure built from the query, ready for JSON writing. |

### Example

```groovy
class myListener{
	function onJSONQuerySerialize( struct data ){
		// Inspect or audit the query structure being serialized to JSON
		var queryData = data.data;
	}
}
```
