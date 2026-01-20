
# Component: `ProcParam`

Provide a paramater to a stored procudure.

## Component Signature

```
<bx:ProcParam type=[string]
value=[any]
variable=[string]
sqltype=[string]
maxLength=[integer]
scale=[integer]
null=[boolean]
DBVarName=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of stored procedure paramter. One of in | out | inout | `in` |
| `value` | `any` | `false` | The value to pass |  |
| `variable` | `string` | `false` |  |  |
| `sqltype` | `string` | `false` | The sql type the value | `string` |
| `maxLength` | `integer` | `false` |  |  |
| `scale` | `integer` | `false` |  |  |
| `null` | `boolean` | `false` | If the value should be counted as null |  |
| `DBVarName` | `string` | `false` |  |  |

## Examples

### Basic Example




```java
<bx:storedproc procedure="foo_proc" dataSource="MY_SYBASE_TEST" username="sa" password="mygoodpw" dbServer="scup" dbName="pubs2" returnCode="Yes" debug="Yes">
    <bx:procresult name="RS1"> 
    <bx:procresult name="RS3" resultSet="3"> 
    <bx:procparam type="IN" sqltype="INTEGER" value="1" dbVarName="@param1"> 
    <bx:procparam type="OUT" sqltype="DATE" variable="FOO" dbVarName="@param2">
</bx:storedproc>
```


