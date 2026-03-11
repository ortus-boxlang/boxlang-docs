
# Component: `Invoke`

Invokes a method from within a template or class or a web service dynamically.

## Component Signature

```
<bx:Invoke class=[any]
webservice=[string]
method=[string]
returnVariable=[string]
argumentCollection=[any]
username=[string]
password=[string]
timeout=[numeric] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `class` | `any` | `false` | The Box Class instance or the name of the Box Class to instantiate. |  |
| `webservice` | `string` | `false` | The WSDL URL of a web service to invoke. Mutually exclusive with class attribute. |  |
| `method` | `string` | `true` | The name of the method to invoke on the class or web service. |  |
| `returnVariable` | `string` | `false` | The variable to store the result of the method invocation. |  |
| `argumentCollection` | `any` | `false` | An array or struct of arguments to pass to the method being invoked. |  |
| `username` | `string` | `false` | The username for basic authentication when invoking web services. |  |
| `password` | `string` | `false` | The password for basic authentication when invoking web services. |  |
| `timeout` | `numeric` | `false` | The timeout in seconds for web service requests. |  |

## Examples


