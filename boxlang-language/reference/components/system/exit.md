[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Exit`

This component aborts processing of the currently executing custom tag, exits the page within the currently executing custom tag, or re-executes a section of code within the currently executing custom tag.

## Component Signature

```
<bx:Exit method=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `method` | `string` | `false` | The method to use for exiting (exitTag, exitTemplate, loop) | `exitTag` |

## Examples

```
<bx:Exit method=[string] />
```
