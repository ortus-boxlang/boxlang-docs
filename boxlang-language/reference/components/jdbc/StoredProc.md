
# Component: `StoredProc`

Execute a stored procedure.

## Component Signature

```
<bx:StoredProc procedure=[string]
datasource=[string]
blockfactor=[integer]
debug=[boolean]
returnCode=[boolean]
result=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `procedure` | `string` | `true` | The name of the procedure to execute. |  |
| `datasource` | `string` | `false` | The name of the datasource where the stored procedure is registered. |  |
| `blockfactor` | `integer` | `false` | The fetch size to use for batching rows and reducing network round trips when reading results. |  |
| `debug` | `boolean` | `false` | If enabled, list debugging info on each statement. | `false` |
| `returnCode` | `boolean` | `false` | If enabled, populates `bxstoredproc.statusCode` with status code returned by stored procedure. | `false` |
| `result` | `string` | `false` | The name of the variable to store the result set in. |  |

## Examples

### Tag Syntax

Basic example of calling a stored procedure, passing a parameter, and getting a result set.


```java
<bx:storedproc procedure="spu_my_storedproc" datasource="myDSN">
	<bx:procparam sqltype="integer" value="#myParameterValue#">
	<bx:procresult name="qResults">
</bx:storedproc>
```


### Script Syntax

Call stored procedure and get back multiple result sets.


```java
bx:storedproc procedure="spu_my_storedproc" datasource="myDSN" {
	bx:procparam sqltype="date" value=myDateParam;
	bx:procresult name="qSummary" resultset=1;
	bx:procresult name="qDetails" resultset=2;
}

```


### Scripted Tag Syntax

Call stored procedure and get back multiple result sets.


```java
bx:storedproc procedure="spu_my_storedproc" datasource="myDSN" {
	procparam( sqltype="date", value=myDateParam );
	procresult( name="qSummary", resultset=1 );
	procresult( name="qDetails", resultset=2 );
}

```


