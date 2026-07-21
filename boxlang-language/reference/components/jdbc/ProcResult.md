
# Component: `ProcResult`

Register a result set variable for a stored procedure.

## Component Signature

```
<bx:ProcResult name=[string]
resultSet=[integer]
maxRows=[integer] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The variable name to place the result set in. |  |
| `resultSet` | `integer` | `false` | The index of the resultset to access. Required if there is more than one ProcResult component. |  |
| `maxRows` | `integer` | `false` | The maximum number of rows to fetch per resultset. | `-1` |

## Examples

### Capture a stored procedure result set

Registers a variable to hold the result set returned by a stored procedure.

```java
<bx:storedproc procedure="getUsers" datasource="myDS">
    <bx:procResult name="users">
    <bx:dump var="#users#">
</bx:storedproc>

```

### Capture multiple result sets

When a stored procedure returns multiple result sets, use `resultSet` to specify which one.

```java
<bx:storedproc procedure="getReportData" datasource="myDS">
    <bx:procResult name="summary" resultSet="1">
    <bx:procResult name="details" resultSet="2">
</bx:storedproc>

```

### Limit rows in a result set

```java
<bx:storedproc procedure="getLargeDataset" datasource="myDS">
    <bx:procResult name="top100" maxRows="100">
</bx:storedproc>

```
