[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsEmpty`

Determine whether a given value is empty.

We check for emptiness of
 anything that can be casted to: Array, Struct, Query, or String.

## Method Signature

```
IsEmpty(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value/object to check for emptiness. |  |

## Examples

### Test to see if a struct is empty



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVaiuteYqL8osSfUvLSkoLdFQKAbLeBa75haUVGoo5MKUaipoWnMBAGaYFCQ%3D" target="_blank">Run Example</a>

```java
myStruct = {};
writeOutput( structIsEmpty( myStruct ) );

```

Result: true

### Test to see if a struct contains something



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLgnPLMkIycjMSy9WsFWoVuDiVMrPS1VSsFJQSsvPV9IB8kvK88H8pMQiJa5aa67yosySVP%2FSkoLSEg2FYrAhnsWuuQUllRoKuZimaipoWnMBAK9QI8s%3D" target="_blank">Run Example</a>

```java
myStructWithThings = { 
	"one" : "foo",
	"two" : "bar"
};
writeOutput( structIsEmpty( myStructWithThings ) );

```

Result: false

### Using Member Function



<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVaiuteYqL8osSfUvLSkoLdFQyIXK6XkWu%2BYWlFRqaCpoWnMBANb3EW0%3D" target="_blank">Run Example</a>

```java
myStruct = {};
writeOutput( myStruct.IsEmpty() );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzT11fwy89TSM0tKKlUKC4pKk0u4UrMy8xNzClWsFWo5uJ09g9XsFJQys3PV9Lh4gzwdAfx8jPzspW4aq259PUVXJG1piUW5YL0QaSCwYKexWAlGlBjNblSkzPyNRSUbArsHKE2QXQrZBZDHAK0QUENTbcCzFWaQCklG%2F0COyUFTSy2gFyAbIUbyEXEmA92OqrhAMfTWKE%3D" target="_blank">Run Example</a>

```java
// Non empty struct
animals = {
	COW : "moo",
	PIG : "oink"
};
// Empty struct
farm = {};
// StructIsEmpty(animals)
echo( "<p>Animals struct is empty: " & StructIsEmpty( animals ) & "</p>" );
// StructIsEmpty(farm)
echo( "<p>Farm struct is empty: " & StructIsEmpty( farm ) & "</p>" );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsBinary](./IsBinary.md)
  * [IsDate](./IsDate.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsDefined](./IsDefined.md)
  * [structIsEmpty](./structIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsObject](./IsObject.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsValid](./IsValid.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsQuery](./IsQuery.md)
  * [IsArray](./IsArray.md)
  * [IsJSON](./IsJSON.md)
  * [IsXML](./IsXML.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsNull](./IsNull.md)
  * [IsClosure](./IsClosure.md)
  * [IsNumeric](./IsNumeric.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStruct](./IsStruct.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsFileObject](./IsFileObject.md)
