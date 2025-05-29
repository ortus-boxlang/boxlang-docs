
# Component: `Component`

Invokes a custom tag.

## Component Signature

```
<bx:Component template=[string]
name=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `template` | `string` | `false` | Mutually exclusive with the name attribute. A path to the template that implements the tag. |  |
| `name` | `string` | `false` | Mutually exclusive with the template attribute. A custom tag name, in the form "Name.Name.Name..." Identifies subdirectory, under<br>                 the tag root directory, that contains custom tag template. |  |

## Examples

### Script Syntax

```java
component displayname="Script Widget" output="false" { 
 // functions and properties here 
}
```
