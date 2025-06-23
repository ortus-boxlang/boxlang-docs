[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsLocalHost`

Determine whether a given string value represents a loopback IP address, like `localhost`, `127.0.0.1` or `::1`.

## Method Signature

```
IsLocalHost(ip=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `ip` | `string` | `true` | String representing the IP address to test. |  |

## Examples

### Is 127.0.0.1 localhost



<a href="https://try.boxlang.io/?code=eJzLLPbJT07M8cgvLtFQUDI0MtczAEJDJQVNay4AfssHNQ%3D%3D" target="_blank">Run Example</a>

```java
isLocalHost( "127.0.0.1" );

```

Result: true

### Is ::1 localhost

Test the IPv6 Loopback address. IPv6 only has one loopback address.

<a href="https://try.boxlang.io/?code=eJzLLPbJT07M8cgvLtFQULKyMlRS0LTmAgBVSwYl" target="_blank">Run Example</a>

```java
isLocalHost( "::1" );

```

Result: true

### Is 127.8.8.8 localhost

IPv4 network standards reserve the entire 127.0.0.0/8 address block for loopback networking purposes however they are not usually mapped to `localhost` by default.

<a href="https://try.boxlang.io/?code=eJzLLPbJT07M8cgvLtFQUDI0MtezAEElBU1rLgB%2FhQdM" target="_blank">Run Example</a>

```java
isLocalHost( "127.8.8.8" );

```

Result: true

### Is 8.8.8.8 localhost

Not a localhost IP.

<a href="https://try.boxlang.io/?code=eJzLLPbJT07M8cgvLtFQULLQA0MlBU1rLgBwuQbq" target="_blank">Run Example</a>

```java
isLocalHost( "8.8.8.8" );

```

Result: false

### Additional Examples


```java
ip = "127.0.0.1";
writeDump( islocalhost( ip ) ); // true
writeDump( islocalhost( GetLocalHostIP() ) );
 // true

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
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
  * [IsNull](./IsNull.md)
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
  * [IsSimpleValue](./IsSimpleValue.md)
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
