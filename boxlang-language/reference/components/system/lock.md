[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Lock`

Ensures the integrity of shared data.

## Component Signature

```
<bx:Lock name=[string]
scope=[string]
type=[string]
timeout=[Integer]
throwOnTimeout=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | Lock name. Mutually exclusive with the scope attribute. Only one request can execute the code within a lock component with a given<br>                 name<br>                 at a time. Cannot be an empty string. |  |
| `scope` | `string` | `false` | Lock scope. Mutually exclusive with the name attribut Lock name. Only one request in the specified scope can execute the code<br>                  within this component (or within any other lock component with the same lock scope scope) at a time. |  |
| `type` | `string` | `false` | readOnly: lets more than one request read shared data. exclusive: lets one request read or write shared data. | `exclusive` |
| `timeout` | `Integer` | `true` | Maximum length of time, in seconds, to wait to obtain a lock. If lock is obtained, tag execution continues. Otherwise, behavior<br>                    depends on throwOnTimeout attribute value. A value of 0 will wait forever. |  |
| `throwOnTimeout` | `boolean` | `false` | True: if lock is not obtained within the timeout period, a runtime exception is thrown. False: if lock is not obtained,<br>                           the body of the component is skipped and execution continues without running the statements in the component. | `true` |

## Examples

```
<bx:Lock name=[string]
scope=[string]
type=[string]
timeout=[Integer]
throwOnTimeout=[boolean] />
```
