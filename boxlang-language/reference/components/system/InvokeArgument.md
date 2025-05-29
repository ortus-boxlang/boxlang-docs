
# Component: `InvokeArgument`

Passes the name and value of an argument to a method.

## Component Signature

```
<bx:InvokeArgument name=[string]
value=[any] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the argument |  |
| `value` | `any` | `false` | The value of the argument |  |

## Examples

### Invoke a SOAP webservice and passing arguments using bx:invokeargument

Calls a remote web service to perform an addition, uses bx:invokeargument to pass the arguments to the method.


```java
<bx:invoke webservice="http://soaptest.parasoft.com/calculator.wsdl" method="add" returnvariable="answer">
    <bx:invokeargument name="x" value="2">
    <bx:invokeargument name="y" value="3">
</bx:invoke>
<bx:output>#answer#</bx:output>
```

Result: 5.0

