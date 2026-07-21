
# Component: `Trace`

Traces messages into the tracing facilites so they can be display by the running runtime either in console, or debug
 output or whatever the runtime is configured to do.

## Component Signature

```
<bx:Trace abort=[boolean]
category=[String]
text=[string]
type=[string]
extrainfo=[any] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `abort` | `boolean` | `false` | If true, the current request will be aborted after the trace call. Default is false. | `false` |
| `category` | `String` | `false` | The category of the trace message. Default is an empty string. |  |
| `text` | `string` | `true` | The text of the trace message. Required. |  |
| `type` | `string` | `true` | The type of the trace message. Default is "Information". | `Information` |
| `extrainfo` | `any` | `false` | Any extra information to be logged with the trace message. This can be simple or a complex object. We will convert it to string for logging. |  |

## Examples

### Add a trace message

Records debugging information visible in the runtime's trace output.

```java
<bx:trace text="Entering processOrder function" type="Information">

```

### Trace with a category

```java
<bx:trace text="Query executed in 45ms" category="database" type="Information">

```

### Trace with extra info

```java
<bx:trace
    text="User login attempt"
    category="auth"
    type="Warning"
    extrainfo="#{ username: 'john', ip: '192.168.1.1' }#"
>

```

### Trace and abort the request

```java
<bx:trace text="Fatal error encountered" type="Error" abort="true">

```

### Trace different severity levels

```java
<bx:trace text="Step 1 complete" type="Information">
<bx:trace text="Unexpected value detected" type="Warning">
<bx:trace text="Operation failed" type="Error">

```
