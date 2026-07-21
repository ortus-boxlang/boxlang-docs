[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsBoolean`

Determine whether a given object is a boolean

## Method Signature

```
IsBoolean(object=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | The value to test for boolean-ness. |  |

## Examples

### Yes

`Yes` is considered a boolean that is `true`

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUFCqTC1WUtC05gIAST8GCA%3D%3D" target="_blank">Run Example</a>

```java
isBoolean( "yes" );

```

Result: true

### No

`No` is considered a boolean that is `false`

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUFDKy1dS0LTmAgBBlwWU" target="_blank">Run Example</a>

```java
isBoolean( "no" );

```

Result: true

### Maybe

`Maybe` is not considered a boolean

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUFDKTaxMSlVS0LTmAgBYjwbF" target="_blank">Run Example</a>

```java
isBoolean( "maybe" );

```

Result: false

### True

`true` is a boolean

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUCgpKk1V0LTmAgBFtgYz" target="_blank">Run Example</a>

```java
isBoolean( true );

```

Result: true

### False

`false` is a boolean

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUEhLzClOVdC05gIATGMGfg%3D%3D" target="_blank">Run Example</a>

```java
isBoolean( false );

```

Result: true

### Zero

`0` is considered a boolean that is `false`

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUDBQ0LTmAgAvggSj" target="_blank">Run Example</a>

```java
isBoolean( 0 );

```

Result: true

### Non Zero Integer

`23` is considered a boolean that is `true`

<a href="https://try.boxlang.io/?code=eJzLLHbKz89JTczTUDAyVtC05gIANKIE2A%3D%3D" target="_blank">Run Example</a>

```java
isBoolean( 23 );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUPAsdsrPz0lNzNNQKCkqTVXQVNC05irHKp%2BWmFOMV4EBPkldQwM9E3wKjPXM8EkrVaYWK%2BFVkJePXx7kP%2FwqwD7Er8QAvzTYl%2FiVAP0JVQAApTZ2vw%3D%3D" target="_blank">Run Example</a>

```java
writeDump( IsBoolean( true ) );
writeDump( IsBoolean( false ) );
writeDump( IsBoolean( 0 ) );
writeDump( IsBoolean( -10.4 ) );
writeDump( IsBoolean( 3.6 ) );
writeDump( IsBoolean( "yes" ) );
writeDump( IsBoolean( "no" ) );
writeDump( IsBoolean( "true" ) );
writeDump( IsBoolean( "false" ) );
writeDump( IsBoolean( "0" ) );
writeDump( IsBoolean( "-10.4" ) );
writeDump( IsBoolean( "3.6" ) );

```


<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUPAsdsrPz0lNzNNQ8Msv19BUAEJrrnKsCqpr8clGx%2BKTDSxNLar0Sy3XUFBSUsBrC0Qep2yiQnFJUWZeOlQVALVWPsM%3D" target="_blank">Run Example</a>

```java
writeDump( IsBoolean( Now() ) );
writeDump( IsBoolean( {} ) );
writeDump( IsBoolean( [] ) );
writeDump( IsBoolean( QueryNew( "" ) ) );
writeDump( IsBoolean( "" ) );
writeDump( IsBoolean( "a string" ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
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
