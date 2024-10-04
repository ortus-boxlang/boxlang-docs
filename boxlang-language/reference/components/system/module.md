[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Module`

Invokes a custom tag.

## Component Signature

```
<bx:Module template=[string]
name=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `template` | `string` | `false` | Mutually exclusive with the name attribute. A path to the template that implements the tag. |  |
| `name` | `string` | `false` | Mutually exclusive with the template attribute. A custom tag name, in the form "Name.Name.Name..." Identifies subdirectory, under<br>                 the tag root directory, that contains custom tag template. |  |

## Examples

```
<bx:Module template=[string]
name=[string] />
```
