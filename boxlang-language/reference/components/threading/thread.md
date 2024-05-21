[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Thread`

The thread component enables multithreaded programming in BoxLang.

## Component Signature
```
<bx:Thread name=[string]
action=[string]
duration=[integer]
priority=[string]
timeout=[integer] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | The name of the thread. |  |
| `action` | `string` | `false` | The action to perform. The default value is "run". The following are the possible values: "join", "run", "sleep", "terminate". | `run` |
| `duration` | `integer` | `false` | The number of milliseconds to pause the thread. This attribute is required if the action attribute is set to "sleep". | `0` |
| `priority` | `string` | `false` | The priority of the thread. The default value is "normal". The following are the possible values: "high", "low", "normal". | `normal` |
| `timeout` | `integer` | `false` | The number of milliseconds to wait for the thread to finish. If the thread does not finish within the specified time, the thread<br>                    is terminated. If the timeout attribute is not specified, the thread runs until it finishes. |  |

## Examples

```
<bx:Thread name=[string]
action=[string]
duration=[integer]
priority=[string]
timeout=[integer] />
```
