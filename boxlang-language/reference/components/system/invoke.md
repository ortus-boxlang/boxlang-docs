[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Invoke`

Invokes a method from within a template or class.

## Component Signature
```
<bx:Invoke class=[any]
method=[string]
returnVariable=[string]
argumentCollection=[any] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `class` | `any` | `false` | The Box Class instance or the name of the Box Class to instantiate. |  |
| `method` | `string` | `true` | The name of the method to invoke. |  |
| `returnVariable` | `string` | `false` | The variable to store the result of the method invocation. |  |
| `argumentCollection` | `any` | `false` | An array or struct of arguments to pass to the method. |  |

## Examples

```
<bx:Invoke class=[any]
method=[string]
returnVariable=[string]
argumentCollection=[any] />
```
