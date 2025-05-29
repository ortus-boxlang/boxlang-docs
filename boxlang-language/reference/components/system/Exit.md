
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

### Simple bx:exit example

Here the loop over the 5 number. When it's meet the condition as true then the block of code get exit.


```java
<bx:output>
<bx:loop from="1" to="5" index="i">
<bx:if i == 3 >
	<bx:exit>
<bx:else>
	#i#
</bx:if>
</bx:loop>
</bx:output>
```

Result: 1 2

