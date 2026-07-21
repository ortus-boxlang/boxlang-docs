[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsXML`

Determines whether a string is well-formed XML text.

## Method Signature

```
IsXML(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | A string containing the XML document text. |  |

## Examples

### isXML Example

Returns true if the string is well-formed XML.

<a href="https://try.boxlang.io/?code=eJxLrUjMLchJVbBVULJJzs9JSSstzszPS81Lz8xLLbbjUrCBMIEsBZu8xNxUO8eU%2FKRUBWegUjewUht9sDBQpT5cKYYmn9Lk1FSiVAYlZubkE6XSvyA1T8EppzTVpSgxHas7bPQxfaRkzVVelFmS6l9aUlBaoqGQWRyRm6OhkAoNBk0FTWsuAPAfWi0%3D" target="_blank">Run Example</a>

```java
example = "<boxlangengines>
 <engine>
  <name>Adobe ColdFusion</name>
 </engine>
 <engine>
  <name>Boxlang</name>
 </engine>
 <engine>
  <name>Railo</name>
 </engine>
 <engine>
  <name>Open BlueDragon</name>
 </engine>
</boxlangengines>";
writeOutput( isXml( example ) );

```

Result: true

### isXML Example for Invalid XML

Returns false if the string is not well-formed XML.

<a href="https://try.boxlang.io/?code=eJxLrUjMLchJNVSwVVCySc7PSUkrLc7Mz0vNS8%2FMSy2241KwgTCBLAWbvMTcVDvHlPykVAVnoFI3sFIbfbAwUKU%2BXCmGJp%2FS5NRUqEola67yosySVP%2FSkoLSEg2FzOKI3BwNhVSYSzQVNK25ADTpMcQ%3D" target="_blank">Run Example</a>

```java
example1 = "<boxlangengines>
 <engine>
  <name>Adobe ColdFusion</name>
 </engine>
 <engine>
  <name>Boxlang</name>";
writeOutput( isXml( example1 ) );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLz8lPSswJSyxSsFVQsnFNLCrJsONSsClKLSzNLEpNAbIVbPISc1PtQopSU4tt9MFsoAJ9JBVYVIcnlqQWEa3aMb0oM7k0p6S0KJVoPR6luYl5mSWVWDXY6EN8omTNVV6UWZLqX1pSUFqioZBZHJGbo6GQDve0poKmNRcAVs9U%2FA%3D%3D" target="_blank">Run Example</a>

```java
globalVar = "<Earth>
 <required>
  <name>Trees</name>
 </required>
 <required>
  <name>Water</name>
 </required>
 <required>
  <name>Agriculture</name>
 </required>
 <required>
  <name>Humanity</name>
 </required>
</Earth>";
writeOutput( isXml( globalVar ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
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
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)
