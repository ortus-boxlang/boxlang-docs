[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsClosure`

Determine whether a given object is a closure

## Method Signature

```
IsClosure(object=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | The value to test for closure-ness. |  |

## Examples

### Returns true if the object is a closure



<a href="https://try.boxlang.io/?code=eJwrLixNLEpVsFXQUHDMq1SoUNBUsLVTqObiLEotKS3KAwpoKVRYc9Vac5UXZZakupTmFmgoZBY75%2BQXlxalaigUQ%2FRrKmhacwEAeU4XPA%3D%3D" target="_blank">Run Example</a>

```java
square = ( Any x ) => {
	return x * x;
};
writeDump( isClosure( square ) );

```

Result: TRUE

### Returns false if the object is not a closure



<a href="https://try.boxlang.io/?code=eJwrLixNLEpVsFXQUHDMq1SoUNBUsLVTqObiLEotKS3KAwpoKVRYc9VacxWDVaYAlUJYGgqmCprWXOVFmSWpLqW5BRoKmcXOOfnFpSApmGJNkBIA%2BtYerg%3D%3D" target="_blank">Run Example</a>

```java
square = ( Any x ) => {
	return x * x;
};
squared = square( 5 );
writeDump( isClosure( squared ) );

```

Result: FALSE

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxtjkEKAjEQBM%2FOK5o9JSDkASFeFH%2FgA9ZkFgIxK5PMXsS%2FKyoiuMeG6u5yDrHMTYUpIsBYhB1utBHuKhVdlD3dPZFz0MaCxFOunDBpjT3PFeZ0OFr6Rn1O%2FPUp6eVqsIwSctu%2F%2Fwwi7BZlPHMJw0digPXrsP7AqyKv6gNk50I%2B" target="_blank">Run Example</a>

```java
// closure
c = () => {
	return true;
};

// user defined function (UDF)
function u() {
	return true;
}
dump( var=isClosure( c ), label="closure" );
dump( var=isClosure( u ), label="user defined function" );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
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
