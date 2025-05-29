
# Component: `Timer`

Times a block of code and outputs the result in a specified format.

## Component Signature

```
<bx:Timer type=[string]
label=[string]
unit=[string]
variable=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of output to generate. One of `debug`, `comment`, `inline`, or `outline` or `dump`. |  |
| `label` | `string` | `false` | The label to use for the output. |  |
| `unit` | `string` | `false` | The unit of time to use for the output. One of `nano`, `micro`, `milli`, or `second`. | `milli` |
| `variable` | `string` | `false` | The name of the variable to store the result in. |  |

## Examples

### Tag version




```java
<bx:timer label="Nap time" type="inline">
Begin some long running process ...
<bx:set sleep( 2000 ) >
done.
</bx:timer>
```

Result: The time elapsed while executing the code inside the <bx:timer> block should be displayed inline.

### Script version



<a href="https://try.boxlang.io/?code=eJxVjEEKwjAQRdfNKT6zqpsQXCrdeADv0OpQAulkSCaoiHc3dufq8x6PvzxPFjcuSPPCaaLrrPgJgr2UJ8rNUpSObzc8SjTuQpuNoAuvUVDzxkhZVpQmEvtqyTeuFd57EA5nN9TErCOOIYSd%2F3%2FuWdjv4cd9AXLfLXM%3D" target="_blank">Run Example</a>

```java
bx:timer label="Nap time" type="outline" {
	writeoutput( "Begin some long running process ... " );
	sleep( 2000 );
	writeoutput( "done." );
}

```

Result: The time elapsed while executing the code inside the bx:timer block should be displayed in the output with an outline around any output generated within the bx:timer call..

