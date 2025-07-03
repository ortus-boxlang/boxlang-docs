# IsEmpty

Determine whether a given value is empty.

We check for emptiness of\
anything that can be casted to: Array, Struct, Query, or String.

## Method Signature

```
IsEmpty(value=[any])
```

### Arguments

| Argument | Type  | Required | Description                              | Default |
| -------- | ----- | -------- | ---------------------------------------- | ------- |
| `value`  | `any` | `true`   | The value/object to check for emptiness. |         |

## Examples

### Test to see if a struct is empty

[Run Example](https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVaiuteYqL8osSfUvLSkoLdFQKAbLeBa75haUVGoo5MKUaipoWnMBAGaYFCQ%3D)

```java
myStruct = {};
writeOutput( structIsEmpty( myStruct ) );

```

Result: true

### Test to see if a struct contains something

[Run Example](https://try.boxlang.io/?code=eJzLrQwuKSpNLgnPLMkIycjMSy9WsFWoVuDiVMrPS1VSsFJQSsvPV9IB8kvK88H8pMQiJa5aa67yosySVP%2FSkoLSEg2FYrAhnsWuuQUllRoKuZimaipoWnMBAK9QI8s%3D)

```java
myStructWithThings = { 
	"one" : "foo",
	"two" : "bar"
};
writeOutput( structIsEmpty( myStructWithThings ) );

```

Result: false

### Using Member Function

[Run Example](https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVaiuteYqL8osSfUvLSkoLdFQyIXK6XkWu%2BYWlFRqaCpoWnMBANb3EW0%3D)

```java
myStruct = {};
writeOutput( myStruct.IsEmpty() );

```

Result: true

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJzT11fwy89TSM0tKKlUKC4pKk0u4UrMy8xNzClWsFWo5uJ09g9XsFJQys3PV9Lh4gzwdAfx8jPzspW4aq259PUVXJG1piUW5YL0QaSCwYKexWAlGlBjNblSkzPyNRSUbArsHKE2QXQrZBZDHAK0QUENTbcCzFWaQCklG%2F0COyUFTSy2gFyAbIUbyEXEmA92OqrhAMfTWKE%3D)

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

* [ArrayIsEmpty](ArrayIsEmpty.md)
* [arrayIsEmpty](arrayIsEmpty.md)
* [Attempt](Attempt.md)
* [IsArray](IsArray.md)
* [IsBinary](IsBinary.md)
* [IsBoolean](IsBoolean.md)
* [IsClosure](IsClosure.md)
* [IsCustomFunction](IsCustomFunction.md)
* [IsDate](IsDate.md)
* [IsDateObject](IsDateObject.md)
* [IsDebugMode](IsDebugMode.md)
* [IsDefined](IsDefined.md)
* [IsFileObject](IsFileObject.md)
* [IsIPv6](IsIPv6.md)
* [IsJSON](IsJSON.md)
* [IsLeapYear](IsLeapYear.md)
* [IsLocalHost](IsLocalHost.md)
* [IsNull](IsNull.md)
* [IsNumeric](IsNumeric.md)
* [IsNumericDate](IsNumericDate.md)
* [IsObject](IsObject.md)
* [IsQuery](IsQuery.md)
* [IsSimpleValue](IsSimpleValue.md)
* [IsStruct](IsStruct.md)
* [IsValid](IsValid.md)
* [IsXML](IsXML.md)
* [IsXmlAttribute](IsXmlAttribute.md)
* [IsXMLDoc](IsXMLDoc.md)
* [IsXMLElem](IsXMLElem.md)
* [IsXMLNode](IsXMLNode.md)
* [IsXMLRoot](IsXMLRoot.md)
* [LSIsNumeric](LSIsNumeric.md)
* [structIsEmpty](structIsEmpty.md)
