
# Component: `Log`

Logs information to the specified log file

## Component Signature

```
<bx:Log text=[string]
file=[string]
log=[string]
type=[string]
application=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `text` | `string` | `false` | The text to log |  |
| `file` | `string` | `false` | (COMPAT ONLY) Do not use anymore, use log instead. If defined, we will use this instead of log. |  |
| `log` | `string` | `false` | The destination logger to use. If not passed, we use the default logger (application.log).<br>                If the logger is a file appender and it doesn't exist it will create it for you.<br>                If the value is an absolue path, it will create a file appender for you at that location. |  |
| `type` | `string` | `false` | The log level of the entry. One of "Information", "Warning", "Error", "Debug", "Trace" | `info` |
| `application` | `boolean` | `false` |  | `true` |

## Examples

### Write an informational log entry

```java
<bx:log text="Application started successfully" type="Information">

```

### Write a warning to the log

```java
<bx:log text="Cache miss rate exceeding threshold" type="Warning">

```

### Write an error log entry

```java
<bx:log text="Database connection failed" type="Error">

```

### Log to a custom logger/file

```java
<bx:log text="Payment processed" log="payments" type="Information">

```

### Log with application name disabled

```java
<bx:log text="Debug trace" application="false" type="Debug">

```
