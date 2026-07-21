[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Attempt`

Create an Attempt object with or without a given value so you can do fluent operations on the
 registered attempt value.

## Method Signature

```
Attempt(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | The value to store as the attempt. This can be a value, or a closure/lambda that will be executed to get the value. |  |

## Examples

### Create an Attempt with a value

Wraps a value in an Attempt object for fluent error-safe operations.

```java
attempt = attempt( 42 );
writeOutput( attempt.get() );

```

Result: 42

### Create an Attempt with a closure

The closure is executed and its result (or exception) is captured.

```java
attempt = attempt( () => 10 / 2 );
writeOutput( attempt.get() );

```

Result: 5

### Attempt that catches an exception

When the closure throws, the Attempt captures the failure instead of crashing.

```java
attempt = attempt( () => 10 / 0 );
writeOutput( attempt.hasError() );

```

Result: true

### Fluent chaining with Attempt

```java
result = attempt( () => "hello".len() )
    .map( (x) => x * 2 )
    .getOrDefault( 0 );
writeOutput( result );

```

Result: 10

### Attempt with no value

Creates an empty Attempt object for later use.

```java
attempt = attempt();
writeOutput( attempt.isEmpty() );

```

Result: true

## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsBoxSet](./IsBoxSet.md)
  * [IsClosure](./IsClosure.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsDate](./IsDate.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsDefined](./IsDefined.md)
  * [IsEmpty](./IsEmpty.md)
  * [IsFileObject](./IsFileObject.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsJSON](./IsJSON.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsNull](./IsNull.md)
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
  * [IsRange](./IsRange.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStringBuilder](./IsStringBuilder.md)
  * [IsStruct](./IsStruct.md)
  * [IsValid](./IsValid.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)
