
# Component: `Transaction`

Demarcate or manage a JDBC transaction.

## Component Signature

```
<bx:Transaction action=[string]
isolation=[string]
savepoint=[string]
datasource=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `false` | When used inside a transaction block, perform some action upon an existing transaction. One of: `begin`, `commit`, `rollback`, or `setsavepoint`. | `begin` |
| `isolation` | `string` | `false` | The isolation level to use for the transaction. Can only be set upon transaction begin. One of: `read_uncommitted`, `read_committed`, `repeatable_read`, or `serializable`. |  |
| `savepoint` | `string` | `false` | The name of the savepoint to set or rollback to. Used with `savepoint` or `rollback` actions. |  |
| `datasource` | `string` | `false` | The name of the datasource to use for the transaction. If not provided, the first query execution inside the transaction will set the datasource. |  |

## Examples

### Simple Transaction

A "simple" transaction might look like this:

```js
transaction{
    queryExecute( "UPDATE users SET name=:name WHERE id=:id", { id: variables.id, name: variables.name } );
    queryExecute(
        "INSERT INTO userLog( action, id, changes ) VALUES ( 'UPDATE', :id, :change)",
        { id: variables.id, change: "changed name to #variables.name#" }
    );
}
```

Note that you can specify a custom isolation level using the `isolation` attribute on the component:

```js
transaction isolation="serializable"{
    // ...
}
```


### Nested Transaction

BoxLang supports nested transactions, using savepoints to control transaction state between the parent and child transactions.

```js
transaction{
    queryExecute( "UPDATE users SET name=:name WHERE id=:id", { id: variables.id, name: variables.name } );

    transaction{
        try{
            queryExecute(
                "INSERT INTO userLog( action, id, changes ) VALUES ( 'UPDATE', :id, :change)",
                { id: variables.id, change: "changed name to #variables.name#" }
            );
        } catch( any e ){
            // user log errored; rollback!
            transactionRollback();
            // log error here
        }
    }
}
```

Here, we have a nested transaction that may (or may not) error; if this happens we want to roll back the logging query but NOT roll back the user query. This functions the same as if we were rolling back to a named savepoint created just after the `UPDATE users` query.
### Script Syntax



<a href="https://try.boxlang.io/?code=eJxLqrAqKUrMK05MLsnMz1Oo5uIsKaoEUZz6%2BgrJ%2BSmpCiX5CkWleUCBJFSlEMpWKTk%2FNzezRMmai7NWITmxJDlDQSMxr1IhVRNsCg5NRfk5OUmJydlgbVy1XADL1Cvw" target="_blank">Run Example</a>

```java
bx:transaction {
	try {
		// code to run
		bx:transaction action="commit";
	} catch (any e) {
		bx:transaction action="rollback";
	}
}

```


### Tag Syntax




```java
<bx:transaction> 
 <bx:try> 
 <!--- code to run ---> 
   <bx:transaction action="commit"/> 
  
 <bx:catch type="any"> 
 <bx:transaction action="rollback"/> 
 </bx:catch></bx:try> 
 </bx:transaction>
```


