[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsArray`

Determine whether a value is an array

## Method Signature

```
IsArray(value=[any], number=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to test for array-ness. |  |
| `number` | `numeric` | `false` | If passed, the array dimension to test. |  |

## Examples

### simple isArray example


<a href="https://try.boxlang.io/?code=eJxLzs%2FJL3IsKkqsVLBViFbg4lSqTM3JyS9X0gEy04tSU%2FPArKLUFCWuWGuu8qLMklT%2F0pKC0hINhcxisEYNhWSEIZoKmtZcAGG2GiQ%3D" target="_blank">Run Example</a>

```java
colorArray = [ 
	"yellow",
	"green",
	"red"
];
writeOutput( isArray( colorArray ) );

```

Result: yes

### simple isArray example


<a href="https://try.boxlang.io/?code=eJxLzs%2FJL3IsKkqsVLBViFbg4lSqTM3JyS9X0gEy04tSU%2FPArKLUFCWuWGuu8qLMklT%2F0pKC0hINhcxisEYNhWSEIZoKmtZcAGG2GiQ%3D" target="_blank">Run Example</a>

```java
colorArray = [ 
	"yellow",
	"green",
	"red"
];
writeOutput( isArray( colorArray ) );

```

Result: true

### isArray example with number


<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI01OHiNAJiY65Ya67yosySVP%2FSkoLSEg2FzGKwOg2FPIQmHQVDBU0FTWsuABqtFVc%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	1,
	2,
	3
];
writeOutput( isArray( numberArray, 1 ) );

```

Result: yes

### isArray example with number


<a href="https://try.boxlang.io/?code=eJzLK81NSi1yLCpKrFSwVYhW4OI01OHiNAJiY65Ya67yosySVP%2FSkoLSEg2FzGKwOg2FPIQmHQVDBU0FTWsuABqtFVc%3D" target="_blank">Run Example</a>

```java
numberArray = [ 
	1,
	2,
	3
];
writeOutput( isArray( numberArray, 1 ) );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMhJTErNsVVyzS0oqVRwLCpKrFTSUShLLLLNLAbzNBSiYxU0FTStucoxNIEV%2BKWWo%2BtIhIprKBiCtOLXrFCQX5xZkpmfZ4zbGGMFTR0Qgd0kp%2Fz8nNTEPKDmnNJUdENKikpTcWkMLinKzEvHrk8JbLsSRCsAyt1jGg%3D%3D" target="_blank">Run Example</a>

```java
writeDump( label="Empty Array", var=isArray( [] ) );
writeDump( label="ArrayNew", var=isArray( arrayNew( 1 ) ) );
writeDump( label="ArrayNew position3", var=isArray( arrayNew( 3 ), 3 ) );
writeDump( label="Boolean value", var=isArray( true ) );
writeDump( label="String value", var=isArray( "array" ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsBinary](./IsBinary.md)
  * [IsDate](./IsDate.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsDefined](./IsDefined.md)
  * [IsEmpty](./IsEmpty.md)
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
