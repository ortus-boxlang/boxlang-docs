[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DataNavigate`

Constructs a fluent data navigator based on different types of data.

<p>
 Available Input Types:
 <ul>
 <li>String: A JSON string</li>
 <li>File Path: A path to a JSON file as a string</li>
 <li>File Path: A path to a JSON file as a Java Path</li>
 <li>Struct: A structure</li>
 <li>Map: A Java map</li>
 </ul>

## Method Signature

```
DataNavigate(data=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `data` | `any` | `true` |  |  |

## Examples

### Navigate into a data structure using a path

```java
data = { user: { name: "Luis", address: { city: "NYC" } } };
result = dataNavigate( data, "user.address.city" );
writeOutput( result );

```

Result: NYC

### Navigate with array indices

```java
data = { users: [ { name: "Alice" }, { name: "Bob" } ] };
result = dataNavigate( data, "users[2].name" );
writeOutput( result );

```

Result: Bob

## Related

  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)
